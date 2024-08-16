import logging
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from maya import cmds, mel

from ..builder.maya.util import Maya
from ..common import DNAViewerError
from ..dnalib.dnalib import DNA
from ..model import Joint as JointModel
from .config import AngleUnit, Config, LinearUnit
from .joint import Joint as JointBuilder
from .mesh import Mesh


@dataclass
class BuildResult:
    """
    用于在构建过程完成后返回数据的类

    属性
    ----------
    @type meshes_per_lod: Dict[int, List[str]]
    @param meshes_per_lod: 按LOD号分组创建的网格名称列表
    """

    meshes_per_lod: Dict[int, List[str]] = field(default_factory=dict)

    def get_all_meshes(self) -> List[str]:
        """
        将网格展平为单个列表。
        
        @rtype: List[str]
        @returns: 所有网格名称的列表。
        """

        all_meshes = []
        for meshes_per_lod in self.meshes_per_lod.values():
            all_meshes.extend(meshes_per_lod)
        return all_meshes


class Builder:
    """
    一个用于构建角色的生成器类
    
    属性
    ----------
    @type config: Config
    @param config: 用于构建角色的配置选项
    
    @type dna: DNA
    @param dna: 从DNA文件中读取的DNA对象
    
    @type meshes: Dict[int, List[str]]
    @param meshes: 按LOD分组创建的网格列表

    """

    def __init__(self, dna: DNA, config: Optional[Config] = None) -> None:
        self.config = config or Config()
        self.dna = dna
        self.meshes: Dict[int, List[str]] = {}
        self.all_loaded_meshes: List[int] = []

    def _build(self) -> bool:
        self.new_scene()
        self.set_filtered_meshes()
        if not self.all_loaded_meshes:
            logging.error("No mashes has been loaded.")
            return False

        self.create_groups()

        self.set_units()
        self.add_joints()
        self.build_meshes()
        self.add_ctrl_attributes_on_root_joint()
        self.add_animated_map_attributes_on_root_joint()
        self.add_key_frames()
        return True

    def build(self) -> BuildResult:
        """构建角色"""
        self.meshes = {}
        try:
            filename = Path(self.dna.path).stem
            logging.info("******************************")
            logging.info(f"{filename} started building")
            logging.info(f"{filename} 开始构建")
            logging.info("******************************")

            self._build()

            logging.info(f"{filename} built successfully!")
            logging.info(f"{filename} 构建成功!")

        except DNAViewerError as e:
            traceback.print_exc()
            raise e
        except Exception as e:
            traceback.print_exc()
            logging.error(f"Unhandled exception, {e}")
            raise DNAViewerError(f"Scene creation failed! Reason: {e}") from e
        return BuildResult(meshes_per_lod=self.meshes)

    def new_scene(self) -> None:
        cmds.file(new=True, force=True)

    def add_mesh_to_display_layer(self, mesh_name: str, lod: int) -> None:
        """
        将具有给定名称的网格添加到已创建的显示层。
        
        @type mesh_name: str
        @param mesh_name: 应添加到显示层的网格的名称。
        
        @type lod: int
        @param lod: lod 值，这是确定应将网格添加到的显示层名称所需的值。
        """
        if self.config.create_display_layers:
            cmds.editDisplayLayerMembers(
                f"{self.config.top_level_group}_lod{lod}_layer", mesh_name
            )

    def _add_joints(self) -> List[JointModel]:
        """
        读取并将关节添加到场景中，还返回一个关节模型对象列表，其中包含已添加的关节。
        
        @rtype：List[JointModel]
        @returns：包含表示已添加到场景中的关节的模型对象列表。
        """

        joints: List[JointModel] = self.dna.read_all_neutral_joints()
        builder = JointBuilder(
            joints,
        )
        builder.process()
        return joints

    def add_joints(self) -> None:
        """
        开始添加角色的关节，如果角色配置选项中的add_joints设置为False，则会跳过这一步。
        """

        if self.config.add_joints:
            logging.info("adding joints to character...")
            joints = self._add_joints()

            if self.config.group_by_lod and joints:
                cmds.parent(joints[0].name, self.config.get_top_level_group())

    def create_groups(self) -> None:
        """
        创建一个Maya变换，用于容纳角色，如果角色配置选项中的create_character_node设置为False，则将跳过此步骤。
        """

        if self.config.group_by_lod:
            logging.info("building character node...")
            cmds.group(world=True, empty=True, name=self.config.get_top_level_group())
            cmds.group(
                parent=self.config.get_top_level_group(),
                empty=True,
                name=self.config.get_geometry_group(),
            )
            cmds.group(
                parent=self.config.get_top_level_group(),
                empty=True,
                name=self.config.get_rig_group(),
            )
        for lod in self.get_display_layers():
            name = f"{self.config.top_level_group}_lod{lod}_layer"
            if not cmds.objExists(name):
                if self.config.group_by_lod:
                    cmds.group(
                        parent=self.config.get_geometry_group(),
                        empty=True,
                        name=f"{self.config.top_level_group}_lod{lod}_grp",
                    )
                    cmds.select(
                        f"{self.config.top_level_group}_lod{lod}_grp",
                        replace=True,
                    )
                if self.config.create_display_layers:
                    cmds.createDisplayLayer(name=name, noRecurse=True)

    def attach_mesh_to_lod(self, mesh_name: str, lod: int) -> None:
        """
        将名为mesh_name的网格附加到给定的lod。
        
        @type mesh_name: str
        @param mesh_name:需要附加到lod持有者对象的网格。
        
        @type lod: str
        @param lod:应该添加到显示层的网格的名称。
        """
        if self.config.group_by_lod:
            parent_node = f"{self.config.get_top_level_group()}|{self.config.get_geometry_group()}|{self.config.top_level_group}_lod{lod}_grp"
            cmds.parent(
                self.get_mesh_node_fullpath_on_root(mesh_name=mesh_name), parent_node
            )

    def get_mesh_node_fullpath_on_root(self, mesh_name: str) -> str:
        """
        获取场景中网格的完整路径。
        
        @type mesh_name: str
        @param mesh_name: 需要路径的网格。
        
        @rtype: str
        @returns: 场景中网格对象的完整路径
        """

        return str(Maya.get_element(f"|{mesh_name}").fullPathName())

    def add_ctrl_attributes_on_root_joint(self) -> None:
        """
        在根关节上添加和设置原始GUI控件属性。
        """

        if self.config.add_ctrl_attributes_on_root_joint and self.config.add_joints:
            gui_control_names = self.dna.get_raw_control_names()
            for name in gui_control_names:
                ctrl_and_attr_names = name.split(".")
                self.add_attribute(
                    control_name=self.config.facial_root_joint_name,
                    long_name=ctrl_and_attr_names[1],
                )

    def add_animated_map_attributes_on_root_joint(self) -> None:
        """
        在根关节上添加并设置动画地图属性。
        """

        if (
            self.config.add_animated_map_attributes_on_root_joint
            and self.config.add_joints
        ):
            names = self.dna.get_animated_map_names()
            for name in names:
                long_name = name.replace(".", "_")
                self.add_attribute(
                    control_name=self.config.facial_root_joint_name, long_name=long_name
                )

    def add_attribute(self, control_name: str, long_name: str) -> None:
        """
        为内部使用添加属性包装器。
        """
        cmds.addAttr(
            control_name,
            longName=long_name,
            keyable=True,
            attributeType="float",
            minValue=0.0,
            maxValue=1.0,
        )

    def add_key_frames(self) -> None:
        """
        如果添加了关节并且设置了add_key_frames选项为True，则在面部根关节上添加一个起始关键帧。
        """

        if self.config.add_key_frames and self.config.add_joints:
            logging.info("setting keyframe on the root joint...")
            cmds.currentTime(0)
            if cmds.objExists(self.config.facial_root_joint_name):
                cmds.select(self.config.facial_root_joint_name, replace=True)
                cmds.setKeyframe(inTangentType="linear", outTangentType="linear")

    def set_filtered_meshes(self) -> None:
        self.all_loaded_meshes = self.get_filtered_meshes()

    def get_mesh_indices_filter(self) -> List[int]:
        indices = []
        for index in range(self.dna.get_mesh_count()):
            mesh_name = self.dna.get_mesh_name(index)
            for cur_filter in self.config.mesh_filter:
                if cur_filter in mesh_name:
                    indices.append(index)
        return indices

    def get_filtered_meshes(self) -> List[int]:
        if not self.config.mesh_filter and not self.config.lod_filter:
            if self.config.meshes:
                return self.config.meshes
            return list(range(self.dna.get_mesh_count()))

        meshes: List[int] = []
        meshes_by_lod = self.dna.get_all_meshes_grouped_by_lod()
        all_meshes = [mesh_index for meshes in meshes_by_lod for mesh_index in meshes]
        mesh_indices_filter = self.get_mesh_indices_filter()

        if self.config.lod_filter:
            for lod in self.config.lod_filter:
                if 0 <= lod < len(meshes_by_lod):
                    meshes.extend(meshes_by_lod[lod])
            if mesh_indices_filter:
                return list(set(meshes) & set(mesh_indices_filter))
            return meshes
        if self.config.mesh_filter:
            return list(set(all_meshes) & set(mesh_indices_filter))
        return all_meshes

    def build_meshes(self) -> None:
        """
        构建网格。如果在配置中指定，它们将被添加到创建的角色节点变换下，否则网格将被放置在场景的根级别。
        """

        logging.info("adding character meshes...")
        self.meshes = {}
        for lod, meshes_per_lod in enumerate(
            self.dna.get_meshes_by_lods(self.all_loaded_meshes)
        ):
            self.meshes[lod] = self.build_meshes_by_lod(
                lod=lod, meshes_per_lod=meshes_per_lod
            )

    def build_meshes_by_lod(self, lod: int, meshes_per_lod: List[int]) -> List[str]:
        """
        从提供的网格ID构建网格，然后将它们附加到角色配置中指定的LOD（如果有）。
        
        @type lod: int
        @param lod: 表示网格显示层的LOD编号。
        
        @type meshes_per_lod: List[int]
        @param meshes_per_lod: 正在构建的网格索引列表。
        
        @rtype: List[MObject]
        @returns: 表示添加到场景中的网格的Maya对象列表。
        """

        meshes: List[str] = []
        for mesh_index in meshes_per_lod:
            builder = Mesh(
                config=self.config,
                dna=self.dna,
                mesh_index=mesh_index,
            )
            builder.build()

            mesh_name = self.dna.get_mesh_name(index=mesh_index)
            meshes.append(mesh_name)

            self.add_mesh_to_display_layer(mesh_name, lod)
            self.attach_mesh_to_lod(mesh_name, lod)
            self.default_lambert_shader(mesh_name)
        return meshes

    def default_lambert_shader(self, mesh_name: str) -> None:
        try:
            if self.config.group_by_lod:
                names = cmds.ls(f"*|{mesh_name}", l=True)
                for item in names:
                    if item.startswith(f"|{self.config.get_top_level_group()}"):
                        cmds.select(item, r=True)
                        break
            else:
                cmds.select(mesh_name, r=True)

            mel.eval("sets -e -forceElement initialShadingGroup")

        except Exception as e:
            logging.error(
                f"Couldn't set lambert shader for mesh {mesh_name}. Reason: {e}"
            )
            raise DNAViewerError(e) from e

    def set_units(self) -> None:
        """Sets the translation and rotation units of the scene from @config"""

        linear_unit = self.get_linear_unit()
        angle_unit = self.get_angle_unit()

        cmds.currentUnit(linear=linear_unit.name, angle=angle_unit.name)

    def get_linear_unit(self) -> LinearUnit:
        return self.get_linear_unit_from_int(self.dna.get_translation_unit())

    def get_angle_unit(self) -> AngleUnit:
        return self.get_angle_unit_from_int(self.dna.get_rotation_unit())

    def get_linear_unit_from_int(self, value: int) -> LinearUnit:
        """
        从提供的网格ID构建网格，然后将它们附加到角色配置中指定的LOD（如果有）。
        
        @type lod: int
        @param lod: 表示网格显示层的LOD编号。
        
        @type meshes_per_lod: List[int]
        @param meshes_per_lod: 正在构建的网格索引列表。
        
        @rtype: List[MObject]
        @returns: 表示添加到场景中的网格的Maya对象列表。
        """

        if value == 0:
            return LinearUnit.cm
        if value == 1:
            return LinearUnit.m
        raise DNAViewerError(f"Unknown linear unit set in DNA file! value {value}")

    def get_angle_unit_from_int(self, value: int) -> AngleUnit:
        """
        从整数值返回一个枚举。
        0 -> degree
        1 -> radian
        
        @type value: int
        @param value: 枚举映射的值。
        
        @rtype: AngleUnit
        @returns: AngleUnit.degree 或 AngleUnit.radian
        """

        if value == 0:
            return AngleUnit.degree
        if value == 1:
            return AngleUnit.radian
        raise DNAViewerError(f"Unknown angle unit set in DNA file! value {value}")

    def get_display_layers(self) -> List[int]:
        """获取需要为@config中的网格创建的LOD ID列表。"""
        meshes: List[int] = []
        for idx, meshes_per_lod in enumerate(
            self.dna.get_meshes_by_lods(self.all_loaded_meshes)
        ):
            if meshes_per_lod:
                meshes.append(idx)
        return list(set(meshes))
