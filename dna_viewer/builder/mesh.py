import logging
from typing import List

from ..builder.maya.mesh import MayaMesh
from ..dnalib.dnalib import DNA
from .config import Config


class Mesh:
    """
    一个用于向场景中添加关节的构建器类
    
    属性
    ----------
    @type dna: DNA
    @param dna: DNA文件的位置
    
    @type mesh_index: int
    @param mesh_index: 我们正在使用的网格索引
    
    @type joint_ids: List[int]
    @param joint_ids: 用于添加皮肤的关节索引
    
    @type joint_names: List[str]
    @param joint_names: 用于添加皮肤的关节名称
    
    @type config: Config
    @param config: 创建网格时将应用的构建选项
    
    @type mesh: MayaMesh
    @param mesh: 用于创建网格的构建器类对象
    
    @type dna: DNA
    @param dna: 加载的DNA对象
    """

    def __init__(
        self,
        config: Config,
        dna: DNA,
        mesh_index: int,
    ) -> None:
        self.mesh_index: int = mesh_index
        self.joint_ids: List[int] = []
        self.joint_names: List[str] = []
        self.config = config
        self.dna = dna
        self.mesh = MayaMesh(
            self.mesh_index,
            self.dna,
            blend_shape_group_prefix=self.config.blend_shape_group_prefix,
            blend_shape_name_postfix=self.config.blend_shape_name_postfix,
            skin_cluster_suffix=self.config.skin_cluster_suffix,
        )

    def build(self) -> None:
        """开始构建过程，创建中性网格，然后添加法线，混合形状并根据需要添加皮肤"""

        self.create_neutral_mesh()
        self.add_blend_shapes()
        self.add_skin_cluster()

    def create_neutral_mesh(self) -> None:
        """创建中性网格"""

        self.mesh.create_neutral_mesh()

    def add_blend_shapes(self) -> None:
        """读取混合形状，然后根据构建选项将它们添加到网格中"""

        if self.config.add_blend_shapes:
            logging.info("adding blend shapes...")
            self.mesh.add_blend_shapes(
                self.config.add_mesh_name_to_blend_shape_channel_name
            )

    def add_skin_cluster(self) -> None:
        """如果在构建选项中设置了，将皮肤集群添加到网格中"""

        if self.config.add_skin_cluster and self.config.add_joints:
            self.prepare_joints()
            if self.joint_names:
                self.mesh.add_skin_cluster(self.joint_names, self.joint_ids)

    def prepare_joints(self) -> None:
        """
        获取给定网格所需的关节索引和名称。
        """

        self.prepare_joint_ids()

        joints = self.dna.read_all_neutral_joints()
        self.joint_names = []
        for joint_id in self.joint_ids:
            self.joint_names.append(joints[joint_id].name)

    def prepare_joint_ids(self) -> None:
        joints_temp: List[int] = []
        joint_indices = self.dna.get_all_skin_weights_joint_indices_for_mesh(
            self.mesh_index
        )
        self.joint_ids = []
        if any(joint_indices):
            for row in joint_indices:
                for column in row:
                    joints_temp.append(column)

            self.joint_ids = list(set(joints_temp))
            self.joint_ids.sort()
        else:
            lod = self.dna.get_lowest_lod_containing_meshes([self.mesh_index])
            if lod:
                self.joint_ids = self.dna.get_joint_indices_for_lod(lod)
