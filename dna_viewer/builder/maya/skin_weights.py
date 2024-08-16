import logging
from typing import List, Tuple, Union

from maya import cmds, mel
from maya.api.OpenMaya import MFnMesh, MGlobal
from maya.api.OpenMayaAnim import MFnSkinCluster

from ...builder.maya.util import Maya
from ...common import DNAViewerError


class MayaSkinWeights:
    """
    A class used for reading and storing skin weight related data needed for adding skin clusters
    一个用于读取和存储皮肤权重相关数据的类，用于添加皮肤集。
    """

    no_of_influences: int
    skinning_method: int
    joints: List[str]
    vertices_info: List[List[Union[int, float]]]

    def __init__(self, skin_cluster: MFnSkinCluster, mesh_name: str) -> None:
        self.no_of_influences = cmds.skinCluster(skin_cluster.name(), q=True, mi=True)

        self.skinning_method = cmds.skinCluster(skin_cluster.name(), q=True, sm=True)

        self.joints = self.get_skin_cluster_influence(skin_cluster)

        self.vertices_info = self.get_skin_weights_for_mesh_name(
            skin_cluster, mesh_name
        )

    def get_skin_cluster_influence(self, skin_cluster: MFnSkinCluster) -> List[str]:
        """
        Gets a list of joint names that are influences to the skin cluster.

        @type skin_cluster: MFnSkinCluster
        @param skin_cluster: The functionalities of a maya skin cluster object

        @rtype: List[str]
        @returns: The list if names of the joints that influence the skin cluster

        获取对皮肤集群有影响的关节名称列表。

        @type skin_cluster：MFnSkinCluster
        @param skin_cluster：一个Maya皮肤集群对象的功能
        
        @rtype：List[str]
        @returns：影响皮肤集群的关节名称列表
        """

        influences: List[str] = cmds.skinCluster(skin_cluster.name(), q=True, inf=True)
        if influences and not isinstance(influences[0], str):
            influences = [obj.name() for obj in influences]
        return influences

    def get_skin_weights_for_mesh_name(
        self,
        skin_cluster: MFnSkinCluster,
        mesh_name: str,
    ) -> List[List[Union[int, float]]]:
        """
        Gets the skin weights concerning the given mesh.

        @type skin_cluster: MFnSkinCluster
        @param skin_cluster: The functionalities of a maya skin cluster object

        @type mesh_name: str
        @param mesh_name: The name of the mesh

        @rtype: List[List[Union[int, float]]]
        @returns: A list of list of weight indices and the weight values

        获取与给定网格相关的皮肤权重。

        @type skin_cluster: MFnSkinCluster
        @param skin_cluster: Maya皮肤集群对象的功能
        
        @type mesh_name: str
        @param mesh_name: 网格的名称
        
        @rtype: List[List[Union[int, float]]]
        @returns: 权重索引和权重值的列表列表
        """

        mesh = Maya.get_element(mesh_name)
        components = MGlobal.getSelectionListByName(f"{mesh_name}.vtx[*]").getComponent(
            0
        )[1]
        weights_data, chunk = skin_cluster.getWeights(mesh, components)
        iterator = [
            weights_data[i : i + chunk] for i in range(0, len(weights_data), chunk)
        ]

        vertices_info = []
        for weights in iterator:
            vertex_weights: List[float] = []
            vertices_info.append(vertex_weights)

            for i, weight in enumerate(weights):
                if weight:
                    vertex_weights.append(i)
                    vertex_weights.append(weight)
        return vertices_info


def get_skin_weights_data(mesh_name: str) -> Tuple[MFnMesh, MFnSkinCluster]:
    """
    Gets the maya objects that manipulate the mesh node and the skin cluster for a given mesh name.

    @type mesh_name: str
    @param mesh_name: The name of the mesh

    @rtype: Tuple[MFnMesh, MFnSkinCluster]
    @returns: The maya object that manipulate the mesh node and the skin cluster for a given mesh name.

    获取操纵给定网格名称的网格节点和皮肤集群的Maya对象。
    
    @type mesh_name: str
    @param mesh_name: 网格的名称
    
    @rtype: Tuple[MFnMesh, MFnSkinCluster]
    @returns: 获取操纵给定网格名称的网格节点和皮肤集群的Maya对象。
    """

    skin_cluster_name = mel.eval(f"findRelatedSkinCluster {mesh_name}")
    if skin_cluster_name:
        skin_cluster = MFnSkinCluster(Maya.get_element(skin_cluster_name))
        mesh_node = MFnMesh(Maya.get_element(mesh_name))
        return mesh_node, skin_cluster
    raise DNAViewerError(f"Unable to find skin for given mesh: {mesh_name}")


def get_skin_weights_from_scene(mesh_name: str) -> MayaSkinWeights:
    """
    Gets the instance of this class filled with data from the scene for a given mesh name.

    @type mesh_name: str
    @param mesh_name: The mesh name

    @rtype: MayaSkinWeights
    @returns: An instance of this class with the data from the scene

    获取此类的实例，其中包含给定网格名称的场景数据。

    @type mesh_name: str
    @param mesh_name: 网格名称
    
    @rtype: MayaSkinWeights
    @returns: 具有来自场景数据的此类的实例
    """

    _, skin_cluster = get_skin_weights_data(mesh_name)

    return MayaSkinWeights(skin_cluster, mesh_name)


def get_file_joint_mappings(
    skin_weights: MayaSkinWeights, skin_cluster: MFnSkinCluster
) -> List[int]:
    """
    Returns a list of object indices representing the influences concerning the joint names specified in the skin weight model.

    @type skin_weights: MayaSkinWeights
    @param skin_weights: The instance of the model storing data about skin weights

    @type skin_cluster: MFnSkinCluster
    @param skin_cluster: An object for working with functions concerning a skin cluster in maya

    @rtype: List[int]
    @returns: a list of indices representing the influences concerning the given joints

    返回一个对象索引列表，表示在皮肤权重模型中指定的关节名称的影响。
    
    @type skin_weights: MayaSkinWeights
    @param skin_weights: 存储有关皮肤权重数据的模型实例
    
    @type skin_cluster: MFnSkinCluster
    @param skin_cluster: 一个用于处理Maya中皮肤集群相关功能的对象
    
    @rtype: List[int]
    @returns: 一个表示关于给定关节的影响的索引列表
    """

    file_joint_mapping: List[int] = []
    for joint_name in skin_weights.joints:
        file_joint_mapping.append(
            skin_cluster.indexForInfluenceObject(Maya.get_element(joint_name))
        )
    return file_joint_mapping


def set_skin_weights_to_scene(mesh_name: str, skin_weights: MayaSkinWeights) -> None:
    """
    Sets the skin weights to the scene.

    @type mesh_name: str
    @param mesh_name: The mesh name

    @type skin_weights: MayaSkinWeights
    @param skin_weights: The object containing data that need to be set to the scene.

    将皮肤权重设置到场景中。
    
    @type mesh_name: str
    @param mesh_name: 网格名称
    
    @type skin_weights: MayaSkinWeights
    @param skin_weights: 包含需要设置到场景中的数据的对象。
    """

    mesh_node, skin_cluster = get_skin_weights_data(mesh_name)

    file_joint_mapping = get_file_joint_mappings(skin_weights, skin_cluster)

    import_skin_weights(skin_cluster, mesh_node, skin_weights, file_joint_mapping)

    logging.info("Set skin weights ended.")


def import_skin_weights(
    skin_cluster: MFnSkinCluster,
    mesh_node: MFnMesh,
    skin_weights: MayaSkinWeights,
    file_joint_mapping: List[int],
) -> None:
    """
    Imports the skin weights to the scene using the joint mapping and the data provided in the model containing the weights.

    @type skin_cluster: MFnSkinCluster
    @param skin_cluster: An object for working with functions concerning a skin cluster in maya

    @type mesh_node: MFnMesh
    @param mesh_node: An object for working with functions concerning meshes in maya

    @type skin_weights: MayaSkinWeights
    @param skin_weights: The instance of the model storing data about skin weights

    @type file_joint_mapping: List[int]
    @param file_joint_mapping: a list of indices representing the influences concerning joints

    将皮肤权重导入场景，使用关节映射和模型中包含的权重数据。

    @type skin_cluster：MFnSkinCluster
    @param skin_cluster：用于处理Maya中皮肤集群的函数的对象
    
    @type mesh_node：MFnMesh
    @param mesh_node：用于处理Maya中网格的函数的对象
    
    @type skin_weights：MayaSkinWeights
    @param skin_weights：存储有关皮肤权重数据的模型实例
    
    @type file_joint_mapping：List[int]
    @param file_joint_mapping：表示与关节有关的影响的索引列表
    """

    temp_str = f"{skin_cluster.name()}.wl["
    for vtx_id in range(cmds.polyEvaluate(mesh_node.name(), vertex=True)):
        vtx_info = skin_weights.vertices_info[vtx_id]

        vtx_str = f"{temp_str}{str(vtx_id)}].w["

        cmds.setAttr(f"{vtx_str}0]", 0.0)

        for i in range(0, len(vtx_info), 2):
            cmds.setAttr(
                f"{vtx_str}{str(file_joint_mapping[int(vtx_info[i])])}]",
                vtx_info[i + 1],
            )
