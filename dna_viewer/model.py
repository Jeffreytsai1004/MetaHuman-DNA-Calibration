from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Point3:
    """
    为表示三维点的模型类
    
    属性
    ----------
    @type x: float
    @param x: x的值
    
    @type y: float
    @param y: y的值
    
    @type z: float
    @param z: z的值
    """

    x: float = field(default=0.0)
    y: float = field(default=0.0)
    z: float = field(default=0.0)


@dataclass
class UV:
    """
    一个用于保存有关UV数据的模型类
    
    属性
    ----------
    @type u: 浮点数
    @param u: u的值
    
    @type v: 浮点数
    @param v: v的值
    """

    u: float = field(default=0.0)
    v: float = field(default=0.0)


@dataclass
class Layout:
    """
    为保存有关单个布局数据的模型类
    
    属性
    ----------
    @type position_index：int
    @param position_index：表示位置的索引
    
    @type texture_coordinate_index：int
    @param texture_coordinate_index：表示纹理坐标索引
    """

    position_index: int = field(default=0)
    texture_coordinate_index: int = field(default=0)


@dataclass
class Topology:
    """
    一个用于保存拓扑数据的模型类
    
    属性
    ----------
    @type positions: List[Point3]
    @param positions: 空间中位置的点列表
    
    @type texture_coordinates: List[UV]
    @param texture_coordinates: 代表位置的UV列表
    
    @type layouts: List[Layout]
    @param layouts: 布局映射的列表
    
    @type face_vertex_layouts: List[List[int]]
    @param face_vertex_layouts: 按面索引分类的面顶点布局索引列表
    """

    positions: List[Point3] = field(default_factory=list)
    texture_coordinates: List[UV] = field(default_factory=list)
    layouts: List[Layout] = field(default_factory=list)
    face_vertex_layouts: List[List[int]] = field(default_factory=list)


@dataclass
class BlendShape:
    """
    用于保存混合形状数据的模型类
    
    属性
    ----------
    @type channel: int
    @param channel: 指向混合形状名称的索引
    
    @type deltas: Dict[int, Point3]
    @param deltas: 将混合形状索引映射到混合形状产生的坐标差异的映射
    """

    channel: int = field(default=None)
    deltas: Dict[int, Point3] = field(default_factory=dict)


@dataclass
class SkinWeightsData:
    """
    一个用于保存有关皮肤权重数据的模型类
    
    属性
    ----------
    
    @type values: List[List[float]]
    @param values: 每个顶点索引的皮肤权重值
    
    @type joint_indices: List[List[int]]
    @param joint_indices: 每个顶点索引的关节索引
    """

    values: List[List[float]] = field(default_factory=list)
    joint_indices: List[List[int]] = field(default_factory=list)


@dataclass
class Mesh:
    """
    用于保存网格数据的模型类
    
    属性
    ----------
    @type name: str
    @param name: 网格的名称
    
    @type topology: Topology
    @param topology: 包含网格拓扑的数据
    
    @type skin_weights: SkinWeightsData
    @param skin_weights: 表示皮肤权重的数据
    
    @type blend_shapes: List[BlendShape]
    @param blend_shapes: 网格的混合形状列表
    """

    name: str = field(default=None)
    topology: Topology = field(default_factory=Topology)
    skin_weights: SkinWeightsData = field(default_factory=SkinWeightsData)
    blend_shapes: List[BlendShape] = field(default_factory=list)


@dataclass
class Joint:
    """
    一个用于保存单个关节数据的模型类
    
    属性
    ----------
    @type name: str
    @param name: 关节的名称
    
    @type translation: Point3
    @param translation: 代表关节平移的三维空间中的点
    
    @type orientation: Point3
    @param orientation: 代表关节方向的三维空间中的点
    
    @type parent_name: str
    @param parent_name: 父关节的名称
    """

    name: str = field(default=None)
    translation: Point3 = field(default_factory=Point3)
    orientation: Point3 = field(default_factory=Point3)
    parent_name: str = field(default=None)
