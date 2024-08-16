import logging
from dataclasses import dataclass, field
from typing import List, Tuple

from maya import cmds
from maya.api.OpenMaya import MDagModifier, MFnDagNode, MFnMesh, MObject, MPoint

from ...builder.maya.util import Maya
from ...common import SKIN_WEIGHT_PRINT_RANGE
from ...dnalib.dnalib import DNA
from ...model import Point3


@dataclass
class Mesh:
    """
    为在网格构建过程中需要的数据创建一个模型类
    
    属性
    ----------
    @type dna_vertex_positions: List[Point3]
    @param dna_vertex_positions: 表示顶点位置的数据
    
    @type dna_vertex_layout_positions: List[int]
    @param dna_vertex_layout_positions: 表示顶点布局位置索引的数据
    
    @type polygon_faces: List[int]
    @param polygon_faces: 顶点布局索引长度的列表
    
    @type polygon_connects: List[int]
    @param polygon_connects: 顶点布局位置索引的列表
    
    @type derived_mesh_names: List[str]
    @param derived_mesh_names: 网格名称的列表
    
    """

    dna_vertex_positions: List[Point3] = field(default_factory=list)
    dna_vertex_layout_positions: List[int] = field(default_factory=list)
    polygon_faces: List[int] = field(default_factory=list)
    polygon_connects: List[int] = field(default_factory=list)
    derived_mesh_names: List[str] = field(default_factory=list)


class MayaMesh:
    """
    一个用于向场景添加连接件的建造者类
    
    属性
    ----------
    @type mesh_index: int
    @param mesh_index: 网格的索引
    
    @type dna: DNA
    @param dna: DNA的实例
    
    @type blend_shape_group_prefix: str
    @param blend_shape_group_prefix: 用于混合形状组的前缀字符串
    
    @type blend_shape_name_postfix: str
    @param blend_shape_name_postfix: 用于混合形状名称的后缀字符串
    
    @type skin_cluster_suffix: str
    @param skin_cluster_suffix: 用于皮肤集群名称的后缀字符串
    
    @type data: Mesh
    @param data: 在网格创建过程中使用的网格数据
    
    @type fn_mesh: om.MFnMesh
    @param fn_mesh: 用于创建网格的OpenMaya类
    
    @type mesh_object: om.MObject
    @param mesh_object: 代表网格的对象
    
    @type dag_modifier: om.MDagModifier
    @param dag_modifier: 用于命名网格的OpenMaya类
    """

    def __init__(
        self,
        mesh_index: int,
        dna: DNA,
        blend_shape_group_prefix: str,
        blend_shape_name_postfix: str,
        skin_cluster_suffix: str,
    ) -> None:
        self.mesh_index = mesh_index
        self.data: Mesh = Mesh()
        self.fn_mesh = MFnMesh()
        self.mesh_object: MObject = None
        self.dag_modifier: MDagModifier = None
        self.dna = dna
        self.blend_shape_group_prefix = blend_shape_group_prefix
        self.blend_shape_name_postfix = blend_shape_name_postfix
        self.skin_cluster_suffix = skin_cluster_suffix

    def create_neutral_mesh(self) -> MObject:
        """
        使用提供给此构建器类对象的配置创建中性网格
        
        @rtype：om.MObject
        @returns：创建的网格对象的实例
        """
        self.prepare_mesh()
        self.mesh_object = self.create_mesh_object()
        self.dag_modifier = self.rename_mesh()
        self.add_texture_coordinates()
        return self.mesh_object

    def create_mesh_object(self) -> MObject:
        """
        获取表示顶点位置的点列表。
        
        @rtype：MObject
        @returns：表示Maya网格函数和创建的Maya网格对象的Maya对象。
        """

        mesh_object = self.fn_mesh.create(
            self.get_vertex_positions_from_dna_vertex_positions(),
            self.data.polygon_faces,
            self.data.polygon_connects,
        )

        return mesh_object

    def get_vertex_positions_from_dna_vertex_positions(self) -> List[MPoint]:
        """
        获取代表顶点位置的点列表。
        
        @rtype: List[MPoint]
        @returns: Maya点对象的列表。
        """

        vertex_positions = []
        for position in self.data.dna_vertex_positions:
            vertex_positions.append(
                MPoint(
                    position.x,
                    position.y,
                    position.z,
                )
            )
        return vertex_positions

    def rename_mesh(self) -> MDagModifier:
        """
        将创建的初始网格对象重命名为来自配置的名称。
        
        @rtype：元组[MDagModifier]
        @returns：表示dag修改器的Maya对象。
        """

        mesh_name = self.dna.get_mesh_name(self.mesh_index)
        dag_modifier = MDagModifier()
        dag_modifier.renameNode(self.mesh_object, mesh_name)
        dag_modifier.doIt()
        return dag_modifier

    def prepare_mesh(self) -> None:
        """
        获取一个表示顶点位置的点列表。
        """

        logging.info("==============================")
        mesh_name = self.dna.get_mesh_name(self.mesh_index)
        logging.info(f"adding mesh: {mesh_name}")
        self.data.dna_vertex_positions = self.dna.get_vertex_positions_for_mesh_index(
            self.mesh_index
        )
        self.data.dna_vertex_layout_positions = (
            self.dna.get_vertex_layout_positions_for_mesh_index(self.mesh_index)
        )

        (
            self.data.polygon_faces,
            self.data.polygon_connects,
        ) = self.dna.get_polygon_faces_and_connects(self.mesh_index)

    def add_texture_coordinates(self) -> None:
        """
        添加纹理坐标的方法。

        """

        logging.info("adding texture coordinates...")

        (
            texture_coordinate_us,
            texture_coordinate_vs,
            texture_coordinate_indices,
        ) = self.get_texture_data()

        self.fn_mesh.setUVs(texture_coordinate_us, texture_coordinate_vs)
        self.fn_mesh.assignUVs(self.data.polygon_faces, texture_coordinate_indices)

        mesh_name = self.dna.get_mesh_name(self.mesh_index)

        cmds.select(mesh_name, replace=True)
        cmds.polyMergeUV(mesh_name, distance=0.01, constructionHistory=False)

    def get_texture_data(self) -> Tuple[List[float], List[float], List[int]]:
        """
        获取创建纹理所需的数据。
        
        @rtype：元组[列表[float]，列表[float]，列表[int]] @returns：包含纹理坐标U列表，纹理坐标V列表和纹理坐标索引列表的元组。
        """

        texture_coordinates = self.dna.get_vertex_texture_coordinates_for_mesh(
            self.mesh_index
        )
        dna_faces = self.dna.get_faces(self.mesh_index)

        coordinate_indices = []
        for layout_id in range(
            len(self.dna.get_layouts_for_mesh_index(self.mesh_index))
        ):
            coordinate_indices.append(
                self.dna.get_texture_coordinate_index(self.mesh_index, layout_id)
            )

        texture_coordinate_us = []
        texture_coordinate_vs = []
        texture_coordinate_indices = []

        index_counter = 0

        for vertices_layout_index_array in dna_faces:
            for vertex_layout_index_array in vertices_layout_index_array:
                texture_coordinate = texture_coordinates[
                    coordinate_indices[vertex_layout_index_array]
                ]
                texture_coordinate_us.append(texture_coordinate.u)
                texture_coordinate_vs.append(texture_coordinate.v)
                texture_coordinate_indices.append(index_counter)
                index_counter += 1

        return texture_coordinate_us, texture_coordinate_vs, texture_coordinate_indices

    def add_blend_shapes(self, add_mesh_name_to_blend_shape_channel_name: bool) -> None:
        """Adds blend shapes to the mesh"""
        if self.dna.has_blend_shapes(self.mesh_index):
            self.create_blend_shapes(add_mesh_name_to_blend_shape_channel_name)
            self.create_blend_shape_node()

    def create_blend_shape_node(self) -> None:
        """
        创建混合形状节点。
        """
        mesh_name = self.dna.get_mesh_name(self.mesh_index)

        nodes = []
        for derived_mesh_name in self.data.derived_mesh_names:
            nodes.append(derived_mesh_name)

        cmds.select(nodes, replace=True)

        cmds.select(mesh_name, add=True)
        cmds.blendShape(name=f"{mesh_name}{self.blend_shape_name_postfix}")
        cmds.delete(f"{self.blend_shape_group_prefix}{mesh_name}")

    def create_blend_shapes(
        self, add_mesh_name_to_blend_shape_channel_name: bool
    ) -> None:
        """
        使用提供的网格和DNA的混合形状数据构建所有派生网格。
        
        @type add_mesh_name_to_blend_shape_channel_name: bool
        @param add_mesh_name_to_blend_shape_channel_name: 一个表示在创建时是否将混合形状通道的网格名称添加到名称的标志
        """

        logging.info("adding derived meshes...")

        group: str = cmds.group(
            empty=True,
            name=f"{self.blend_shape_group_prefix}{self.dna.get_mesh_name(self.mesh_index)}",
        )

        self.data.derived_mesh_names = []
        blend_shapes = self.dna.get_blend_shapes(self.mesh_index)
        for blend_shape_target_index, blend_shape in enumerate(blend_shapes):

            self.create_blend_shape(
                blend_shape_target_index,
                blend_shape.channel,
                group,
                add_mesh_name_to_blend_shape_channel_name,
            )
        cmds.setAttr(f"{group}.visibility", 0)

    def create_blend_shape(
        self,
        blend_shape_target_index: int,
        blend_shape_channel: int,
        group: str,
        add_mesh_name_to_blend_shape_channel_name: bool,
    ) -> None:
        """
        使用提供的网格和DNA的混合形状数据构建一个单一的派生网格。

        @type blend_shape_target_index: int
        @param blend_shape_target_index: 用于获取表示有关混合形状的值更改的增量值。
        
        @type blend_shape_channel: int
        @param blend_shape_channel: 用于从DNA中获取混合形状名称。
        
        @type group: str
        @param group: 新网格将添加到的变换。
        
        @type add_mesh_name_to_blend_shape_channel_name: bool
        @param add_mesh_name_to_blend_shape_channel_name: 一个表示在创建时是否将混合形状通道的网格名称添加到名称的标志。
        
        """

        new_vert_layout = self.get_vertex_positions_from_dna_vertex_positions()

        zipped_deltas = self.dna.get_blend_shape_target_deltas_with_vertex_id(
            self.mesh_index, blend_shape_target_index
        )
        for zipped_delta in zipped_deltas:
            delta: Point3 = zipped_delta[1]
            new_vert_layout[zipped_delta[0]] += MPoint(
                delta.x,
                delta.y,
                delta.z,
            )

        new_mesh = self.fn_mesh.create(
            new_vert_layout, self.data.polygon_faces, self.data.polygon_connects
        )
        derived_name = self.dna.get_blend_shape_channel_name(blend_shape_channel)
        name = (
            f"{self.dna.geometry_meshes[self.mesh_index].name}__{derived_name}"
            if add_mesh_name_to_blend_shape_channel_name
            else derived_name
        )
        self.dag_modifier.renameNode(new_mesh, name)
        self.dag_modifier.doIt()

        dag = MFnDagNode(Maya.get_element(group))
        dag.addChild(new_mesh)

        self.data.derived_mesh_names.append(name)

    def add_skin_cluster(self, joint_names: List[str], joint_ids: List[int]) -> None:
        """
        向网格添加皮肤集

        @type joint_names: List[str]
        @param joint_names: 添加皮肤集所需的关节名称
        
        @type joint_ids: List[int]
        @param joint_ids: 设置皮肤权重所需的关节索引
        """

        mesh_name = self.dna.get_mesh_name(self.mesh_index)

        self._add_skin_cluster(mesh_name, joint_names)
        self.set_skin_weights(mesh_name, joint_ids)

    def _add_skin_cluster(self, mesh_name: str, joint_names: List[str]) -> None:
        """
        创建一个skin cluster对象。
        
        @type mesh_name: str
        @param mesh_name: 用于皮肤集群命名的网格名称。
        
        @type joints: List[Joint]
        @param joints: 用于添加皮肤集群的关节列表。
        """

        logging.info("adding skin cluster...")
        maximum_influences = self.dna.get_maximum_influence_per_vertex(self.mesh_index)

        cmds.select(joint_names[0], replace=True)

        cmds.select(mesh_name, add=True)
        skin_cluster = cmds.skinCluster(
            toSelectedBones=True,
            name=f"{mesh_name}_{self.skin_cluster_suffix}",
            maximumInfluences=maximum_influences,
            skinMethod=0,
            obeyMaxInfluences=True,
        )
        cmds.skinCluster(
            skin_cluster, edit=True, addInfluence=joint_names[1:], weight=0
        )

    def set_skin_weights(self, mesh_name: str, joint_ids: List[int]) -> None:
        """
        设置皮肤权重属性。

        @type mesh_name: str
        @param mesh_name: 用于获取皮肤集群名称的网格名称。
        
        @type joint_ids: List[int]
        @param joint_ids: 用于设置皮肤权重属性的关节索引列表。
        """

        logging.info("adding skin weights...")
        skin_weights = self.dna.get_skin_weight_matrix_for_mesh(self.mesh_index)

        # import skin weights
        temp_str = f"{mesh_name}_{self.skin_cluster_suffix}.wl["
        for vertex_id, skin_weight in enumerate(skin_weights):
            if not (vertex_id + 1) % SKIN_WEIGHT_PRINT_RANGE:
                logging.info(f"\t{vertex_id + 1} / {len(skin_weights)}")
            vertex_infos = skin_weight

            # set all skin weights to zero
            vertex_string = f"{temp_str}{str(vertex_id)}].w["
            cmds.setAttr(f"{vertex_string}0]", 0.0)

            # import skin weights
            for vertex_info in vertex_infos:
                cmds.setAttr(
                    f"{vertex_string}{str(joint_ids.index(vertex_info[0]))}]",
                    float(vertex_info[1]),
                )
        if len(skin_weights) % SKIN_WEIGHT_PRINT_RANGE != 0:
            logging.info(f"\t{len(skin_weights)} / {len(skin_weights)}")
