from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class LinearUnit(Enum):
    """
    An enum used to represent the unit used for linear representation.

    Attributes
    ----------
    @cm: using cm as unit
    @m: using m as unit

    用于表示线性表示所使用的单位的枚举。

    属性
    @cm：使用cm作为单位
    @m：使用m作为单位
    """

    cm = 0
    m = 1


class AngleUnit(Enum):
    """
    An enum used to represent the unit used for angle representation.

    Attributes
    ----------
    @degree: using degree as unit
    @radian: using radian as unit

    用于表示角度单位的枚举。
    
    属性
    @degree：使用度作为单位
    @radian：使用弧度作为单位
    """

    degree = 0
    radian = 1


@dataclass
class Config:
    """
    A class used to represent the config for @Builder

    Attributes
    ----------
    @type mesh_filter: List[str]
    @param mesh_filter: List of mesh names that should be filtered. Mash names can be just substrings. ["head"] will find all meshes that contins string "head" in its mash name.


    @type lod_filter: List[int]
    @param lod_filter: List of lods that should be filtered.

    @type group_by_lod: bool
    @param group_by_lod: A flag representing whether the character should be parented to a character transform node in the scene hierarchy

    @type group_by_lod: bool
    @param group_by_lod: A flag representing whether the character should be parented to a character transform node in rig hierarchy

    @type top_level_group: str
    @param top_level_group: Value that is going to be used when creating root group

    @type geometry_group: str
    @param geometry_group: Value that is going to be used when creating group that contains geometry

    @type facial_root_joint_name: str
    @param facial_root_joint_name: The name of the facial root joint

    @type blend_shape_group_prefix: str
    @param blend_shape_group_prefix: prefix string for blend shape group

    @type blend_shape_name_postfix: str
    @param blend_shape_name_postfix: postfix string for blend shape name

    @type skin_cluster_suffix: str
    @param skin_cluster_suffix: postfix string for skin cluster name

    @type animated_map_attribute_multipliers_name: str
    @param animated_map_attribute_multipliers_name: string for frame animated map attribute name

    @type create_display_layers: bool
    @param create_display_layers: A flag representing whether the created meshes should be assigned to a display layer

    @type add_joints: bool
    @param add_joints: A flag representing whether joints should be added

    @type add_blend_shapes: bool
    @param add_blend_shapes: A flag representing whether blend shapes should be added

    @type add_skin_cluster: bool
    @param add_skin_cluster: A flag representing whether skin should be added

    @type add_ctrl_attributes_on_root_joint: bool
    @param add_ctrl_attributes_on_root_joint: A flag representing whether control attributes should be added to the root joint

    @type add_animated_map_attributes_on_root_joint: bool
    @param add_animated_map_attributes_on_root_joint: A flag representing whether animated map attributes should be added to the root joint

    @type add_key_frames: bool
    @param add_key_frames: A flag representing whether key frames should be added

    @type add_mesh_name_to_blend_shape_channel_name: bool
    @param add_mesh_name_to_blend_shape_channel_name: A flag representing whether mesh name of blend shape channel is added to name when creating it

    用于表示@Builder配置的类
    
    属性
    ----------
    @type mesh_filter: List[str]
    @param mesh_filter: 应该被过滤的网格名称列表。网格名称可以是子字符串。["head"] 将找到所有包含字符串 "head" 的网格。
    
    @type lod_filter: List[int]
    @param lod_filter: 应该被过滤的LOD列表。
    
    @type group_by_lod: bool
    @param group_by_lod: 一个表示角色是否应该被父节点到场景层次结构中的角色变换节点的标志。
    
    @type group_by_lod: bool
    @param group_by_lod: 一个表示角色是否应该被父节点到rig层次结构中的角色变换节点的标志。
    
    @type top_level_group: str
    @param top_level_group: 在创建根组时将要使用的值
    
    @type geometry_group: str
    @param geometry_group: 在创建包含几何图形的组时将要使用的值
    
    @type facial_root_joint_name: str
    @param facial_root_joint_name: 面部根关节的名称
    
    @type blend_shape_group_prefix: str
    @param blend_shape_group_prefix: 混合形状组的前缀字符串
    
    @type blend_shape_name_postfix: str
    @param blend_shape_name_postfix: 混合形状名称的后缀字符串
    
    @type skin_cluster_suffix: str
    @param skin_cluster_suffix: 皮肤集名称的后缀字符串
    
    @type animated_map_attribute_multipliers_name: str
    @param animated_map_attribute_multipliers_name: 帧动画映射属性名称的字符串
    
    @type create_display_layers: bool
    @param create_display_layers: 一个表示创建的网格是否应该分配给一个显示层的标志
    
    @type add_joints: bool
    @param add_joints: 一个表示是否应该添加关节的标志
    
    @type add_blend_shapes: bool
    @param add_blend_shapes: 一个表示是否应该添加混合形状的标志
    
    @type add_skin_cluster: bool
    @param add_skin_cluster: 一个表示是否应该添加皮肤的标志
    
    @type add_ctrl_attributes_on_root_joint: bool
    @param add_ctrl_attributes_on_root_joint: 一个表示是否应该将控制属性添加到根关节的标志
    
    @type add_animated_map_attributes_on_root_joint: bool
    @param add_animated_map_attributes_on_root_joint: 一个表示是否应该将动画映射属性添加到根关节的标志
    
    @type add_key_frames: bool
    @param add_key_frames: 一个表示是否应该添加关键帧的标志
    
    @type add_mesh_name_to_blend_shape_channel_name: bool
    @param add_mesh_name_to_blend_shape_channel_name: 一个表示在创建时是否要将混合形状通道的网格名称添加到名称中的标志
    """

    meshes: List[int] = field(default_factory=list)
    mesh_filter: List[str] = field(default_factory=list)
    lod_filter: List[int] = field(default_factory=list)

    group_by_lod: bool = field(default=True)
    top_level_group: str = "head"
    geometry_group: str = "geometry"

    facial_root_joint_name: str = "FACIAL_C_FacialRoot"

    blend_shape_group_prefix: str = "BlendshapeGroup_"
    blend_shape_name_postfix: str = "_blendShapes"
    skin_cluster_suffix: str = "skinCluster"

    animated_map_attribute_multipliers_name = "FRM_WMmultipliers"

    create_display_layers: bool = field(default=True)

    add_joints: bool = field(default=True)
    add_blend_shapes: bool = field(default=True)
    add_skin_cluster: bool = field(default=True)
    add_ctrl_attributes_on_root_joint: bool = field(default=True)
    add_animated_map_attributes_on_root_joint: bool = field(default=True)
    add_key_frames: bool = field(default=True)
    add_mesh_name_to_blend_shape_channel_name: bool = field(default=True)

    def get_top_level_group(self) -> str:
        return f"{self.top_level_group}_grp"

    def get_geometry_group(self) -> str:
        return f"{self.geometry_group}_grp"

    def get_rig_group(self) -> str:
        return f"{self.top_level_group}Rig_grp"


@dataclass
class RigConfig(Config):
    """
    A class used to represent the config for @RigBuilder


    @type add_rig_logic: bool
    @param add_rig_logic: A flag representing whether normals should be added

    @type rig_logic_command: str
    @param rig_logic_command: The command used to start creating the rig logic using the plugin

    @type rig_logic_name: str
    @param rig_logic_name: The name of the rig logic node

    @type control_naming: str
    @param control_naming: The naming pattern of controls

    @type joint_naming: str
    @param joint_naming: The naming pattern of joints

    @type blend_shape_naming: str
    @param blend_shape_naming: The naming pattern of blend shapes

    @type animated_map_naming: str
    @param animated_map_naming: The naming pattern of animated maps

    @type gui_path: str
    @param gui_path: The location of the gui file

    @type left_eye_joint_name: str
    @param left_eye_joint_name: The name of the left eye joint

    @type eye_gui_name: str
    @param eye_gui_name: The name of the control in the gui

    @type gui_translate_x: float
    @param gui_translate_x: Represents the value that the gui should be additionally translated on the X axis

    @type analog_gui_path: str
    @param analog_gui_path: The location of the analog gui file

    @type left_eye_joint_name: str
    @param left_eye_joint_name: The name of the left eye joint

    @type right_eye_joint_name: str
    @param right_eye_joint_name: The name of the right eye joint

    @type central_driver_name: str
    @param central_driver_name: The name of the central driver

    @type left_eye_driver_name: str
    @param left_eye_driver_name: The name of the left eye driver

    @type right_eye_driver_name: str
    @param right_eye_driver_name: The name of the right eye driver

    @type central_aim: str
    @param central_aim: The name of the central aim

    @type le_aim: str
    @param le_aim: The name of the left eye aim

    @type re_aim: str
    @param re_aim: The name of the right eye aim

    @type aas_path: Optional[str]
    @param aas_path: The location of the script file

    @type aas_method: str
    @param aas_method: The method that should be called

    @type aas_parameter: Dict[Any, Any]
    @param aas_parameter: The parameters that will be passed as the method arguments

    用于表示@RigBuilder配置的类
    
    @type add_rig_logic: bool
    @param add_rig_logic: 一个表示是否应添加法线的标志
    
    @type rig_logic_command: str
    @param rig_logic_command: 用于启动使用插件创建骨骼逻辑的命令
    
    @type rig_logic_name: str
    @param rig_logic_name: 骨骼逻辑节点的名称
    
    @type control_naming: str
    @param control_naming: 控件命名模式
    
    @type joint_naming: str
    @param joint_naming: 骨骼命名模式
    
    @type blend_shape_naming: str
    @param blend_shape_naming: 形变命名模式
    
    @type animated_map_naming: str
    @param animated_map_naming: 动画地图命名模式
    
    @type gui_path: str
    @param gui_path: GUI文件的位置
    
    @type left_eye_joint_name: str
    @param left_eye_joint_name: 左眼骨骼的名称
    
    @type eye_gui_name: str
    @param eye_gui_name: GUI中控件的名称
    
    @type gui_translate_x: float
    @param gui_translate_x: 表示GUI应在X轴上额外平移的值
    
    @type analog_gui_path: str
    @param analog_gui_path: 模拟GUI文件的位置
    
    @type left_eye_joint_name: str
    @param left_eye_joint_name: 左眼骨骼的名称
    
    @type right_eye_joint_name: str
    @param right_eye_joint_name: 右眼骨骼的名称
    
    @type central_driver_name: str
    @param central_driver_name: 中心驱动器的名称
    
    @type left_eye_driver_name: str
    @param left_eye_driver_name: 左眼驱动器的名称
    
    @type right_eye_driver_name: str
    @param right_eye_driver_name: 右眼驱动器的名称
    
    @type central_aim: str
    @param central_aim: 中心瞄准的名称
    
    @type le_aim: str
    @param le_aim: 左眼瞄准的名称
    
    @type re_aim: str
    @param re_aim: 右眼瞄准的名称
    
    @type aas_path: Optional[str]
    @param aas_path: 脚本文件的位置
    
    @type aas_method: str
    @param aas_method: 应该调用的方法
    
    @type aas_parameter: Dict[Any, Any]
    @param aas_parameter: 作为方法参数传递的参数

    """

    add_rig_logic: bool = field(default=True)
    rig_logic_command: str = field(default="createEmbeddedNodeRL4")
    rig_logic_name: str = field(default="")
    control_naming: str = field(default="<objName>.<attrName>")
    joint_naming: str = field(default="<objName>.<attrName>")
    blend_shape_naming: str = field(default="")
    animated_map_naming: str = field(default="")
    gui_path: str = field(default=None)

    eye_gui_name: str = "CTRL_C_eye"
    gui_translate_x: float = 10

    analog_gui_path: str = field(default=None)

    left_eye_joint_name: str = "FACIAL_L_Eye"
    right_eye_joint_name: str = "FACIAL_R_Eye"

    central_driver_name: str = "LOC_C_eyeDriver"
    left_eye_driver_name: str = "LOC_L_eyeDriver"
    right_eye_driver_name: str = "LOC_R_eyeDriver"

    left_eye_aim_up_name: str = "LOC_L_eyeAimUp"
    right_eye_aim_up_name: str = "LOC_R_eyeAimUp"
    central_aim: str = "GRP_C_eyesAim"

    le_aim: str = "GRP_L_eyeAim"
    re_aim: str = "GRP_R_eyeAim"

    aas_path: Optional[str] = field(default=None)
    aas_method: str = "run_after_assemble"
    aas_parameter: Dict[Any, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.add_mesh_name_to_blend_shape_channel_name:
            self.blend_shape_naming = (
                f"<objName>{self.blend_shape_name_postfix}.<objName>__<attrName>"
            )
        else:
            self.blend_shape_naming = (
                f"<objName>{self.blend_shape_name_postfix}.<attrName>"
            )

        self.animated_map_naming = (
            f"{self.animated_map_attribute_multipliers_name}.<objName>_<attrName>"
        )
