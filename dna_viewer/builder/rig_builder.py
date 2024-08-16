import logging
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path
from types import ModuleType
from typing import Optional

from maya import cmds, mel
from maya.api.OpenMaya import MSpace, MVector

from ..builder.maya.util import Maya
from ..common import ANALOG_GUI_HOLDER, GUI_HOLDER, RIG_LOGIC_PREFIX, DNAViewerError
from ..dnalib.dnalib import DNA
from .builder import Builder
from .config import RigConfig


class RigBuilder(Builder):
    """
    一个用于构建网格的构建器类
    """

    def __init__(self, dna: DNA, config: Optional[RigConfig] = None) -> None:
        super().__init__(dna=dna, config=config)
        self.config: Optional[RigConfig]
        self.eye_l_pos: MVector
        self.eye_r_pos: MVector

    def _build(self) -> None:
        if super()._build():
            self.add_gui()
            self.add_analog_gui()
            self.add_rig_logic()
            self.run_additional_assemble_script()

    def run_additional_assemble_script(self) -> None:
        """
        如果在角色配置中指定，则运行额外的组装脚本。
        """

        if self.config.aas_path:
            logging.info("running additional assemble script...")
            try:
                module_name = Path(self.config.aas_path).stem
                script = self.source_py_file(module_name, self.config.aas_path)
                script_method = getattr(script, self.config.aas_method)
                script_method(
                    self.config.get_top_level_group(),
                    self.config.get_rig_group(),
                    self.config.aas_parameter,
                )
            except Exception as e:
                raise DNAViewerError(f"Can't run aas script. Reason: {e}") from e

    def add_rig_logic(self) -> None:
        """
        创建并添加在角色配置中指定的骨骼逻辑节点。
        """

        if (
            self.config.add_rig_logic
            and self.config.add_joints
            and self.config.add_skin_cluster
            and self.config.add_blend_shapes
            and self.config.aas_path
            and self.config.analog_gui_path
            and self.config.gui_path
        ):
            logging.info("adding rig logic...")
            try:
                cmds.loadPlugin("embeddedRL4.mll")
                self.config.rig_logic_name = f"{RIG_LOGIC_PREFIX}{self.dna.name}"
                dna = self.dna.path.replace("\\", "/")

                mel_command = self.config.rig_logic_command
                mel_command += f' -n "{self.config.rig_logic_name}"'
                mel_command += f' -dfp "{dna}"'
                mel_command += f' -cn "{self.config.control_naming}"'
                mel_command += f' -jn "{self.config.joint_naming}"'
                mel_command += f' -bsn "{self.config.blend_shape_naming}"'
                mel_command += f' -amn "{self.config.animated_map_naming}"; '

                logging.info(f"mel command: {mel_command}")
                mel.eval(mel_command)
            except Exception as e:
                logging.error(
                    "The procedure needed for assembling the rig logic was not found, the plugin needed for this might not be loaded."
                    "Rig logic 所需的程序未找到，可能未加载此插件。"
                )
                raise DNAViewerError(
                    f"Something went wrong, skipping adding the rig logic... Reason: {e}"
                ) from e

    def add_gui(self) -> None:
        """
        根据指定的GUI选项添加GUI。如果未指定任何选项，则不会添加GUI。
        """

        if self.config.gui_path:
            logging.info("adding gui...")

            self.import_gui(
                gui_path=self.config.gui_path,
                group_name=GUI_HOLDER,
            )
            self.position_gui(GUI_HOLDER)

            self.add_ctrl_attributes()
            self.add_animated_map_attributes()

    def add_ctrl_attributes(self) -> None:
        """
        添加并设置原始 GUI 控件属性。
        """

        gui_control_names = self.dna.get_raw_control_names()
        for name in gui_control_names:
            ctrl_and_attr_names = name.split(".")
            self.add_attribute(
                control_name=ctrl_and_attr_names[0],
                long_name=ctrl_and_attr_names[1],
            )

    def add_animated_map_attributes(self) -> None:
        """
        添加并设置Anim Map属性。
        """

        names = self.dna.get_animated_map_names()
        for name in names:
            long_name = name.replace(".", "_")
            if self.config.gui_path:
                self.add_attribute(
                    control_name=self.config.animated_map_attribute_multipliers_name,
                    long_name=long_name,
                )

    def position_gui(self, group_name: str) -> None:
        """将 GUI 位置设置为与角色的眼睛对齐"""

        if not cmds.objExists(self.config.eye_gui_name) or not cmds.objExists(
            self.config.left_eye_joint_name
        ):
            logging.warning(
                "could not find joints needed for positioning the gui, leaving it at its default position... 开始将所有提供的关节添加到场景中..."
            )
            return

        gui_y = (
            Maya.get_transform(self.config.eye_gui_name).translation(MSpace.kObject).y
        )
        eyes_y = (
            Maya.get_transform(self.config.left_eye_joint_name)
            .translation(MSpace.kObject)
            .y
        )
        delta_y = eyes_y - gui_y

        if isinstance(self.config.gui_translate_x, str):
            try:
                logging.warning(
                    "gui_translate_x should be a float, trying to cast the value to float..."
                )
                self.config.gui_translate_x = float(self.config.gui_translate_x)
            except ValueError:
                logging.error("could not cast string value to float")
                return

        Maya.get_transform(group_name).translateBy(
            MVector(self.config.gui_translate_x, delta_y, 0), MSpace.kObject
        )

    def add_analog_gui(self) -> None:
        """
        根据指定的模拟 GUI 选项添加模拟 GUI。如果未指定，将不添加模拟 GUI。
        """

        if self.config.analog_gui_path and self.config.add_joints:
            logging.info("adding analog gui...")
            self.import_gui(
                gui_path=self.config.analog_gui_path,
                group_name=ANALOG_GUI_HOLDER,
            )
            if self.dna.joints.names:
                self.add_eyes()
                self.add_eye_locators()

    def add_eyes(self) -> None:
        """将眼睛添加到模拟界面。"""

        self.eye_l_pos = Maya.get_translation(self.config.left_eye_joint_name)
        self.eye_r_pos = Maya.get_translation(self.config.right_eye_joint_name)

        Maya.set_translation(
            self.config.central_driver_name,
            Maya.get_translation(self.config.facial_root_joint_name),
        )

        delta_l = Maya.get_translation(
            self.config.left_eye_aim_up_name
        ) - Maya.get_translation(self.config.left_eye_driver_name)
        delta_r = Maya.get_translation(
            self.config.right_eye_aim_up_name
        ) - Maya.get_translation(self.config.right_eye_driver_name)

        Maya.set_translation(self.config.left_eye_driver_name, self.eye_l_pos)
        Maya.set_translation(
            self.config.right_eye_driver_name,
            self.eye_r_pos,
        )
        Maya.set_translation(
            self.config.left_eye_aim_up_name,
            MVector(
                self.eye_l_pos[0] + delta_l[0],
                self.eye_l_pos[1] + delta_l[1],
                self.eye_l_pos[2] + delta_l[2],
            ),
        )
        Maya.set_translation(
            self.config.right_eye_aim_up_name,
            MVector(
                self.eye_r_pos[0] + delta_r[0],
                self.eye_r_pos[1] + delta_r[1],
                self.eye_r_pos[2] + delta_r[2],
            ),
        )

    def add_eye_locators(self) -> None:
        """将眼睛定位器添加到模拟界面。"""

        eye_l_locator_pos = Maya.get_translation(self.config.le_aim)
        eye_r_locator_pos = Maya.get_translation(self.config.re_aim)
        central_aim_pos = Maya.get_translation(self.config.central_aim)

        eye_middle_delta = (self.eye_l_pos - self.eye_r_pos) / 2

        eye_middle = self.eye_r_pos + eye_middle_delta

        Maya.set_translation(
            self.config.central_aim,
            MVector(eye_middle[0], eye_middle[1], central_aim_pos[2]),
        )
        Maya.set_translation(
            self.config.le_aim,
            MVector(self.eye_l_pos[0], self.eye_l_pos[1], eye_l_locator_pos[2]),
        )
        Maya.set_translation(
            self.config.re_aim,
            MVector(self.eye_r_pos[0], self.eye_r_pos[1], eye_r_locator_pos[2]),
        )

    def source_py_file(self, name: str, path: str) -> Optional[ModuleType]:
        """
        用于加载一个Python文件，用于额外的组装脚本。
        
        @type name: str
        @param name: 模块的名称。
        
        @type path: str
        @param path: Python文件的路径。
        
        @rtype: Optional[ModuleType]
        @returns: 加载的模块。
        """

        path_obj = Path(path.strip())
        if (
            path
            and path_obj.exists()
            and path_obj.is_file()
            and path_obj.suffix == ".py"
        ):
            spec = spec_from_loader(name, SourceFileLoader(name, path))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        raise DNAViewerError(f"File {path} is not found!")

    def import_gui(self, gui_path: str, group_name: str) -> None:
        """
        使用提供的参数导入一个GUI。
        
        @type gui_path: str
        @param gui_path: 需要导入的GUI文件的路径。
        
        @type group_name: str
        @param group_name: 持有导入资产的变换的名称。
        """

        cmds.file(gui_path, i=True, groupReference=True, groupName=group_name)
