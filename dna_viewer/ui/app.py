import logging
import os
import webbrowser
from typing import Callable, List

from maya import cmds
from maya.cmds import confirmDialog
from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import (
    QApplication,
    QCheckBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QTabWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
    QVBoxLayout,
    QWidget,
)

from .. import DNA, build_rig
from ..builder.config import RigConfig
from ..dnalib.layer import Layer
from ..version import __version__
from .widgets import FileChooser, QHLine


def show() -> None:
    DnaViewerWindow.show_window()


WINDOW_OBJECT = "dnaviewer"
WINDOW_TITLE = "DNA Viewer"
HELP_URL = "https://epicgames.github.io/MetaHuman-DNA-Calibration/"
SPACING = 6
WINDOW_SIZE_WIDTH_MIN = 800
WINDOW_SIZE_WIDTH_MAX = 1200
WINDOW_SIZE_HEIGHT_MIN = 800
WINDOW_SIZE_HEIGHT_MAX = 1000
MARGIN_LEFT = 8
MARGIN_TOP = 8
MARGIN_RIGHT = 8
MARGIN_BOTTOM = 8
MARGIN_HEADER_LEFT = 0
MARGIN_HEADER_TOP = 0
MARGIN_HEADER_RIGHT = 0
MARGIN_HEADER_BOTTOM = 0
MARGIN_BODY_LEFT = 0
MARGIN_BODY_TOP = 0
MARGIN_BODY_RIGHT = 0


class MeshTreeList(QWidget):
    """
    一个自定义小部件，其中列出了带有复选框的网格，这样这些网格就可以被选择以进行处理。这些网格按LOD分组。
    
    @type mesh_tree: QWidget
    @param mesh_tree: 包含要在树列表中选择的网格的小部件
    """

    def __init__(self, main_window: "DnaViewerWindow") -> None:
        super().__init__()
        self.main_window = main_window

        label = QLabel("Meshes:")
        self.mesh_tree = self.create_mesh_tree()

        layout = QGridLayout()
        layout.addWidget(self.mesh_tree, 0, 0, 4, 1)
        layout.setContentsMargins(
            MARGIN_BODY_LEFT,
            MARGIN_BODY_TOP,
            MARGIN_BODY_RIGHT,
            MARGIN_BOTTOM,
        )

        layout_holder = QVBoxLayout()
        layout_holder.addWidget(label)
        layout_holder.addLayout(layout)
        layout_holder.setContentsMargins(
            MARGIN_BODY_LEFT,
            MARGIN_BODY_TOP,
            MARGIN_BODY_RIGHT,
            MARGIN_BOTTOM,
        )

        self.btn_select_all = QPushButton("Select all meshes")
        self.btn_select_all.setEnabled(False)
        self.btn_select_all.clicked.connect(self.select_all)
        layout_holder.addWidget(self.btn_select_all)

        self.btn_deselect_all = QPushButton("Deselect all meshes")
        self.btn_deselect_all.setEnabled(False)
        self.btn_deselect_all.clicked.connect(self.deselect_all)
        layout_holder.addWidget(self.btn_deselect_all)

        self.setLayout(layout_holder)

    def create_mesh_tree(self) -> QWidget:
        """
        创建网格树列表小部件
        
        @rtype: QWidget
        @returns: 创建的小部件
        """

        mesh_tree = QTreeWidget()
        mesh_tree.setHeaderHidden(True)
        mesh_tree.itemChanged.connect(self.tree_item_changed)
        mesh_tree.setStyleSheet("background-color: #505050")
        mesh_tree.setToolTip("Select mesh or meshes to add to rig")
        return mesh_tree

    def fill_mesh_list(
        self, lod_count: int, names: List[str], indices_names: List[List[int]]
    ) -> None:
        """
        用网格填充网格列表，并根据LOD对它们进行分组
        
        @type lod_count: int
        @param lod_count: LOD计数
        
        @type names: List[str]
        @param names: 所有网格的名称和索引
        
        @type indices_names: List[List[int]
        @param indices_names: 所有网格的名称和索引
        """

        self.mesh_tree.clear()

        for i in range(lod_count):
            parent = QTreeWidgetItem(self.mesh_tree)
            parent.setText(0, f"LOD {i}")
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

            meshes_in_lod = indices_names[i]

            for mesh_index in meshes_in_lod:
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, f"{names[mesh_index]}")
                child.setCheckState(0, Qt.Unchecked)

            self.mesh_tree.setItemExpanded(parent, True)

    def get_selected_meshes(self) -> List[int]:
        """
        从树部件中获取所选的网格
        
        @rtype: List[int]
        @returns: 所选网格的索引列表
        """

        meshes = []

        iterator = QTreeWidgetItemIterator(
            self.mesh_tree, QTreeWidgetItemIterator.Checked
        )
        while iterator.value():
            item = iterator.value()
            mesh_name = item.text(0)
            mesh_index = self.main_window.dna.get_mesh_id_from_mesh_name(mesh_name)
            if mesh_index is not None:
                meshes.append(mesh_index)

            iterator += 1

        return meshes

    def select_all(self) -> None:
        """
        选择树部件中的所有网格
        """
        self.iterate_over_items(Qt.Checked)

    def deselect_all(self) -> None:
        """
        取消树部件中的所有网格选择
        """

        self.iterate_over_items(Qt.Unchecked)

    def iterate_over_items(self, state: Qt.CheckState) -> None:
        """
        反选树部件中的所有网格
        """

        item = self.mesh_tree.invisibleRootItem()
        for index in range(item.childCount()):
            child = item.child(index)
            child.setCheckState(0, state)

    def tree_item_changed(self) -> None:
        """当树形项目的值更改时调用的方法"""

        meshes = self.get_selected_meshes()

        if meshes:
            self.main_window.skin_cb.setEnabled(self.main_window.joints_cb.checkState())
            self.main_window.blend_shapes_cb.setEnabled(True)
            self.main_window.process_btn.setEnabled(True)
            self.main_window.rig_logic_cb.setEnabled(False)

            if len(meshes) == self.main_window.dna.get_mesh_count():
                self.main_window.rig_logic_cb.setEnabled(
                    self.main_window.joints_cb.checkState()
                    and self.main_window.blend_shapes_cb.checkState()
                    and self.main_window.skin_cb.checkState()
                    and self.main_window.select_gui_path.get_file_path() is not None
                    and self.main_window.select_analog_gui_path.get_file_path()
                    is not None
                    and self.main_window.select_aas_path.get_file_path() is not None
                )
        else:
            self.main_window.skin_cb.setEnabled(False)
            self.main_window.blend_shapes_cb.setEnabled(False)
            self.main_window.process_btn.setEnabled(
                self.main_window.joints_cb.checkState()
            )


class DnaViewerWindow(QMainWindow):
    """
    UI 窗口
    
    属性
    ----------
    
    @type select_dna_path: FileChooser
    @param select_dna_path: 用于获取 DNA 路径的 FileChooser 小部件
    
    @type load_dna_btn: QPushButton
    @param load_dna_btn: 启动加载 DNA 的按钮
    
    @type mesh_tree_list: QWidget
    @param mesh_tree_list: 包含要在树列表中选择的网格的小部件
    
    @type joints_cb: QCheckBox
    @param joints_cb: 表示是否应添加关节的复选框
    
    @type blend_shapes_cb: QCheckBox
    @param blend_shapes_cb: 表示是否应添加混合形状的复选框
    
    @type skin_cb: QCheckBox
    @param skin_cb: 表示是否应添加皮肤的复选框
    
    @type rig_logic_cb: QCheckBox
    @param rig_logic_cb: 表示是否应添加骨骼逻辑的复选框
    
    @type ctrl_attributes_on_root_joint_cb: QCheckBox
    @param ctrl_attributes_on_root_joint_cb: 表示是否应在关节上添加控制属性的复选框
    
    @type animated_map_attributes_on_root_joint_cb: QCheckBox
    @param animated_map_attributes_on_root_joint_cb: 表示是否应在根关节上添加动画映射属性的复选框
    
    @type mesh_name_to_blend_shape_channel_name_cb: QCheckBox
    @param mesh_name_to_blend_shape_channel_name_cb: 表示是否应将网格名称添加为混合形状通道名称的复选框
    
    @type key_frames_cb: QCheckBox
    @param key_frames_cb: 表示是否应添加关键帧的复选框
    
    @type select_gui_path: FileChooser
    @param select_gui_path: 用于获取 GUI 路径的 FileChooser 小部件
    
    @type select_analog_gui_path: FileChooser
    @param select_analog_gui_path: 用于获取模拟 GUI 路径的 FileChooser 小部件
    
    @type select_aas_path: FileChooser
    @param select_aas_path: 用于获取额外组装脚本路径的 FileChooser 小部件
    
    @type process_btn: QPushButton
    @param process_btn: 启动创建场景和角色的按钮
    
    @type progress_bar: QProgressBar
    @param progress_bar: 显示构建进度的进度条
    """

    _instance: "DnaViewerWindow" = None
    main_widget: QWidget = None
    select_dna_path: FileChooser = None
    load_dna_btn: QPushButton = None
    mesh_tree_list: QWidget = None
    joints_cb: QCheckBox = None
    blend_shapes_cb: QCheckBox = None
    skin_cb: QCheckBox = None
    rig_logic_cb: QCheckBox = None
    ctrl_attributes_on_root_joint_cb: QCheckBox = None
    animated_map_attributes_on_root_joint_cb: QCheckBox = None
    mesh_name_to_blend_shape_channel_name_cb: QCheckBox = None
    key_frames_cb: QCheckBox = None
    select_gui_path: FileChooser = None
    select_analog_gui_path: FileChooser = None
    select_aas_path: FileChooser = None
    process_btn: QPushButton = None
    progress_bar: QProgressBar = None
    dna: DNA = None

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.body: QVBoxLayout = None
        self.header: QHBoxLayout = None
        self.build_options: QWidget = None
        self.extra_build_options: QWidget = None

        self.setup_window()
        self.create_ui()

    def setup_window(self) -> None:
        """设置窗口的方法"""

        self.setWindowFlags(
            self.windowFlags()
            | Qt.WindowTitleHint
            | Qt.WindowMaximizeButtonHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowCloseButtonHint
        )
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setObjectName(WINDOW_OBJECT)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowFlags(Qt.Window)
        self.setFocusPolicy(Qt.StrongFocus)

    def create_ui(self) -> None:
        """Fills the window with UI elements"""

        self.main_widget = self.create_main_widget()
        self.setCentralWidget(self.main_widget)
        self.set_size()
        self.setStyleSheet(self.load_css())

    def load_css(self) -> str:
        css = os.path.join(os.path.dirname(__file__), "app.css")
        with open(css, encoding="utf-8") as file:
            return file.read()

    def create_main_widget(self) -> QWidget:
        """
        创建包含 UI 元素的小部件
        
        @rtype: QtWidgets.QWidget
        @returns: 主小部件
        """

        header = self.create_header()
        body = self.create_body()

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addLayout(header)
        layout.addWidget(QHLine())
        layout.addLayout(body)
        layout.setContentsMargins(MARGIN_LEFT, MARGIN_TOP, MARGIN_RIGHT, MARGIN_BOTTOM)
        layout.setSpacing(SPACING)
        return widget

    def set_size(self) -> None:
        """设置窗口大小"""

        self.setMaximumSize(WINDOW_SIZE_WIDTH_MAX, WINDOW_SIZE_HEIGHT_MAX)
        self.setMinimumSize(WINDOW_SIZE_WIDTH_MIN, WINDOW_SIZE_HEIGHT_MIN)
        self.resize(WINDOW_SIZE_WIDTH_MIN, WINDOW_SIZE_HEIGHT_MIN)

    def show_message_dialog(self) -> bool:
        dlg = QMessageBox()
        dlg.setIcon(QMessageBox.Warning)
        dlg.setWindowTitle("Warning")
        dlg.setText(
            "Unsaved changes exists.\nSave changes and create new scene, discard changes, and create new scene or cancel procesing."
        )
        dlg.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        button = dlg.exec_()

        if button == QMessageBox.Save:
            cmds.SaveScene()
            return not cmds.file(q=True, modified=True)
        if button == QMessageBox.Cancel:
            return False

        return True

    def process(self) -> None:
        """开始从UI提供的配置开始创建场景的构建过程"""

        process = True
        if cmds.file(q=True, modified=True):
            process = self.show_message_dialog()

        if process:
            self.set_progress(text="Processing in progress...", value=0)
            config = RigConfig(
                meshes=self.mesh_tree_list.get_selected_meshes(),
                gui_path=self.select_gui_path.get_file_path(),
                analog_gui_path=self.select_analog_gui_path.get_file_path(),
                aas_path=self.select_aas_path.get_file_path(),
                add_rig_logic=self.add_rig_logic(),
                add_joints=self.add_joints(),
                add_blend_shapes=self.add_blend_shapes(),
                add_skin_cluster=self.add_skin_cluster(),
                add_ctrl_attributes_on_root_joint=self.add_ctrl_attributes_on_root_joint(),
                add_animated_map_attributes_on_root_joint=self.add_animated_map_attributes_on_root_joint(),
                add_mesh_name_to_blend_shape_channel_name=self.add_mesh_name_to_blend_shape_channel_name(),
                add_key_frames=self.add_key_frames(),
            )

            self.main_widget.setEnabled(False)

            try:
                self.set_progress(value=33)
                self.dna = DNA(self.select_dna_path.get_file_path())
                self.set_progress(value=66)
                build_rig(dna=self.dna, config=config)
                self.set_progress(text="Processing completed", value=100)
            except Exception as e:
                self.set_progress(text="Processing failed", value=100)
                logging.error(e)
                confirmDialog(message=e, button=["ok"], icon="critical")

            self.main_widget.setEnabled(True)

    def set_progress(self, text: str = None, value: int = None) -> None:
        """Setting text and/or value to progress bar"""

        if text is not None:
            self.progress_bar.setFormat(text)
        if value is not None:
            self.progress_bar.setValue(value)

    @staticmethod
    def show_window() -> None:
        if DnaViewerWindow._instance is None:
            DnaViewerWindow._instance = DnaViewerWindow(
                parent=DnaViewerWindow.maya_main_window()
            )
        DnaViewerWindow.activate_window()

    @staticmethod
    def maya_main_window() -> QWidget:
        """
        获取MayaWindow实例
        
        @throws RuntimeError
        
        @rtype: QtWidgets.QWidget
        @returns: 主窗口实例
        """

        for obj in QApplication.topLevelWidgets():
            if obj.objectName() == "MayaWindow":
                return obj
        raise RuntimeError("Could not find MayaWindow instance")

    @staticmethod
    def activate_window() -> None:
        """Shows window if minimized"""

        try:
            DnaViewerWindow._instance.show()

            if DnaViewerWindow._instance.windowState() & Qt.WindowMinimized:
                DnaViewerWindow._instance.setWindowState(Qt.WindowActive)

            DnaViewerWindow._instance.raise_()
            DnaViewerWindow._instance.activateWindow()
        except RuntimeError as e:
            logging.info(e)
            if str(e).rstrip().endswith("already deleted."):
                DnaViewerWindow._instance = None
                DnaViewerWindow.show_window()

    def add_joints(self) -> bool:
        return self.is_checked(self.joints_cb)

    def add_blend_shapes(self) -> bool:
        return self.is_checked(self.blend_shapes_cb)

    def add_skin_cluster(self) -> bool:
        return self.is_checked(self.skin_cb)

    def add_rig_logic(self) -> bool:
        return self.is_checked(self.rig_logic_cb)

    def add_ctrl_attributes_on_root_joint(self) -> bool:
        return self.is_checked(self.ctrl_attributes_on_root_joint_cb)

    def add_animated_map_attributes_on_root_joint(self) -> bool:
        return self.is_checked(self.animated_map_attributes_on_root_joint_cb)

    def add_mesh_name_to_blend_shape_channel_name(self) -> bool:
        return self.is_checked(self.mesh_name_to_blend_shape_channel_name_cb)

    def add_key_frames(self) -> bool:
        return self.is_checked(self.key_frames_cb)

    def is_checked(self, checkbox: QCheckBox) -> bool:
        """
        返回所提供复选框是否已选中并启用
        
        @type checkbox：QCheckBox
        @param checkbox：需要检查并启用其值的复选框
        
        @rtype：bool
        @returns：表示复选框是否已选中并启用的标志
        """

        return (
            checkbox is not None
            and bool(checkbox.isEnabled())
            and checkbox.checkState() == Qt.CheckState.Checked
        )

    def create_body(self) -> QVBoxLayout:
        """
        创建主体布局并添加所需的小部件
        
        @rtype：QVBoxLayout
        @returns：添加了小部件的创建的垂直框布局
        """

        self.body = QVBoxLayout()
        self.body.setContentsMargins(
            MARGIN_BODY_LEFT,
            MARGIN_BODY_TOP,
            MARGIN_BODY_RIGHT,
            MARGIN_BOTTOM,
        )
        self.body.setSpacing(SPACING)
        self.create_dna_selector()
        self.mesh_tree_list = self.create_mesh_selector()
        self.build_options = self.create_build_options()
        self.extra_build_options = self.create_extra_build_options()

        tab = QTabWidget(self)
        tab.addTab(self.build_options, "Build options")
        tab.addTab(self.extra_build_options, "Extra options")
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(tab)

        self.body.addWidget(widget)

        self.select_gui_path = self.create_gui_selector()
        self.select_analog_gui_path = self.create_analog_gui_selector()
        self.select_aas_path = self.create_aas_selector()
        self.process_btn = self.create_process_btn()
        self.progress_bar = self.create_progress_bar()

        return self.body

    def create_header(self) -> QHBoxLayout:
        """
        创建并添加到标题部件
        
        @rtype: QHBoxLayout
        @returns: 添加小部件的创建的水平框布局
        """

        self.header = QHBoxLayout()
        label = QLabel("v" + __version__)
        btn = self.create_help_btn()
        self.header.addWidget(label)
        self.header.addStretch(1)
        self.header.addWidget(btn)
        self.header.setContentsMargins(
            MARGIN_HEADER_LEFT,
            MARGIN_HEADER_TOP,
            MARGIN_HEADER_RIGHT,
            MARGIN_HEADER_BOTTOM,
        )
        self.header.setSpacing(SPACING)
        return self.header

    def create_help_btn(self) -> QWidget:
        """
        创建帮助按钮小部件
        
        @rtype: QHBoxLayout
        @returns: 添加小部件后创建的水平框布局
        """

        btn = QPushButton(self)
        btn.setText(" ? ")
        btn.setToolTip("Help")
        btn.clicked.connect(self.on_help)
        return btn

    def on_help(self) -> None:
        """当点击帮助按钮时调用的方法"""

        if HELP_URL:
            webbrowser.open(HELP_URL)
        else:
            QMessageBox.about(
                self,
                "About",
                "Sorry, this application does not have documentation yet.",
            )

    def create_dna_selector(self) -> QWidget:
        """
        创建并添加DNA选择器小部件
        
        @rtype: QWidget
        @returns: 创建的DNA选择器小部件
        """

        widget = QWidget()
        self.select_dna_path = self.create_dna_chooser()
        self.load_dna_btn = self.create_load_dna_button(self.select_dna_path)

        self.select_dna_path.fc_text_field.textChanged.connect(
            lambda: self.on_dna_selected(self.select_dna_path)
        )

        layout = QVBoxLayout()
        layout.addWidget(self.select_dna_path)
        layout.addWidget(self.load_dna_btn)
        layout.setContentsMargins(
            MARGIN_HEADER_LEFT,
            MARGIN_HEADER_TOP,
            MARGIN_HEADER_RIGHT,
            MARGIN_HEADER_BOTTOM,
        )
        widget.setLayout(layout)

        self.body.addWidget(widget)

        return widget

    def on_dna_selected(self, input: FileChooser) -> None:
        """
        当选择 DNA 文件时调用的方法
        
        @type input: FileChooser
        @param input: 对应 DNA 选择器小部件的文件选择器对象
        """

        enabled = input.get_file_path() is not None
        self.load_dna_btn.setEnabled(enabled)
        self.process_btn.setEnabled(False)

    def create_dna_chooser(self) -> FileChooser:
        """
        创建并添加 DNA 选择器小部件
        
        @rtype: 文件选择器
        @returns: DNA 选择器小部件
        """

        return self.create_file_chooser(
            "Path:",
            "DNA file to load. Required by all gui elements",
            "Select a DNA file",
            "DNA files (*.dna)",
            self.on_dna_changed,
        )

    def on_dna_changed(self, state: int) -> None:  # pylint: disable=unused-argument
        """
        当复选框更改时调用的方法
        
        @type state: int
        @param state: 复选框的更改状态
        """
        enabled = False
        if self.dna:
            if self.dna.path == self.select_dna_path.get_file_path():
                enabled = True

        self.load_dna_btn.setEnabled(enabled)
        self.mesh_tree_list.btn_select_all.setEnabled(enabled)
        self.mesh_tree_list.btn_deselect_all.setEnabled(enabled)
        self.process_btn.setEnabled(enabled)

    def create_load_dna_button(self, dna_input: FileChooser) -> QWidget:
        """
        创建并添加加载DNA按钮小部件
        
        @type input：FileChooser
        @param input：与DNA选择器小部件对应的文件选择器对象
        
        @rtype：QWidget
        @returns：创建的加载DNA按钮小部件
        """

        btn = QPushButton("Load DNA")
        btn.setEnabled(False)
        btn.clicked.connect(lambda: self.on_load_dna_clicked(dna_input))
        return btn

    def on_load_dna_clicked(self, input: FileChooser) -> None:
        """
        当选择了一个DNA文件时被调用的方法
        
        @type input: FileChooser
        @param input: 对应于DNA选择器小部件的文件选择器对象
        """

        self.main_widget.setEnabled(False)
        QCoreApplication.processEvents()
        try:
            dna_file_path = input.get_file_path()

            if dna_file_path:
                self.dna = DNA(dna_file_path, [Layer.definition])
                lod_count = self.dna.get_lod_count()
                names = self.get_mesh_names()
                indices_names = self.get_lod_indices_names()
                self.mesh_tree_list.fill_mesh_list(lod_count, names, indices_names)
                self.joints_cb.setEnabled(True)
                self.enable_additional_build_options(True)
                self.process_btn.setEnabled(False)
                self.mesh_tree_list.btn_select_all.setEnabled(True)
                self.mesh_tree_list.btn_deselect_all.setEnabled(True)
        except Exception as e:
            dlg = QMessageBox()
            dlg.setIcon(QMessageBox.Warning)
            dlg.setWindowTitle("Error")
            dlg.setText(str(e))
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.exec_()

        self.main_widget.setEnabled(True)

    def get_mesh_names(self) -> List[str]:
        """读取定义中的网格"""
        names: List[str] = []
        for index in range(self.dna.get_mesh_count()):
            names.append(self.dna.get_mesh_name(index))
        return names

    def get_lod_indices_names(self) -> List[List[int]]:
        """读取定义中的网格"""
        lod_indices: List[List[int]] = []
        for index in range(self.dna.get_lod_count()):
            lod_indices.append(self.dna.get_mesh_indices_for_lod(index))
        return lod_indices

    def create_mesh_selector(self) -> MeshTreeList:
        """
        创建并添加一个网格树列表，其中条目按LOD分组，这用于选择需要处理的网格
        
        @rtype：MeshTreeList
        @returns：创建的网格树列表小部件
        """

        widget = MeshTreeList(self)
        self.body.addWidget(widget)
        return widget

    def create_file_chooser(
        self,
        label: str,
        hint: str,
        caption: str,
        filter: str,
        on_changed: Callable[[int], None] = None,
    ) -> FileChooser:
        """
        创建一个文件选择器小部件，用于选择文件路径
        
        @type label: str
        @param label: 文件对话框中弹出的标签
        
        @type hint: str
        @param hint: 文件对话框中弹出的标签
        
        @type caption: str
        @param caption: 文件对话框中弹出的标题
        
        @type filter: str
        @param filter: 文件对话框中使用的文件过滤器
        
        @rtype: FileChooser
        @returns: 创建的文件选择器对象
        """

        widget = FileChooser(
            label,
            hint,
            self,
            dialog_caption=caption,
            dialog_filter=filter,
            on_changed=on_changed or self.on_generic_changed,
        )
        self.body.addWidget(widget)
        return widget

    def create_gui_selector(self) -> FileChooser:
        """
        创建GUI选择器小部件
        
        @rtype：FileChooser
        @returns：GUI选择器小部件
        """

        return self.create_file_chooser(
            "Gui path:",
            "GUI file to load. Required by RigLogic",
            "Select the gui file",
            "gui files (*.ma)",
        )

    def create_aas_selector(self) -> FileChooser:
        """
        创建并添加额外的组装脚本选择器小部件
        
        @rtype：FileChooser
        @returns：额外的组装脚本选择器小部件
        """

        return self.create_file_chooser(
            "Additional assemble script path:",
            "Additional assemble script to use. Required by RigLogic",
            "Select the aas file",
            "python script (*.py)",
        )

    def create_analog_gui_selector(self) -> FileChooser:
        """
        创建并添加模拟gui选择器小部件
        
        @rtype：FileChooser
        @returns：模拟gui选择器小部件
        """

        return self.create_file_chooser(
            "Analog gui path:",
            "Analog GUI file to load. Required by RigLogic",
            "Select the analog gui file",
            "analog gui files (*.ma)",
        )

    def create_build_options(self) -> QWidget:
        """创建并添加包含构建选项复选框的小部件"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(
            MARGIN_BODY_LEFT,
            MARGIN_BODY_TOP,
            MARGIN_BODY_RIGHT,
            MARGIN_BOTTOM,
        )

        self.joints_cb = self.create_checkbox(
            "joints",
            "Add joints to rig. Requires: DNA to be loaded",
            layout,
            self.on_joints_changed,
        )
        self.blend_shapes_cb = self.create_checkbox(
            "blend shapes",
            "Add blend shapes to rig. Requires: DNA to be loaded and at least one mesh to be check",
            layout,
            self.on_generic_changed,
        )
        self.skin_cb = self.create_checkbox(
            "skin cluster",
            "Add skin cluster to rig. Requires: DNA to be loaded and at least one mesh and joints to be checked",
            layout,
            self.on_generic_changed,
        )
        self.rig_logic_cb = self.create_checkbox(
            "rig logic",
            "Add RigLogic to rig. Requires: DNA to be loaded, all meshes to be checked, joints, skin, blend shapes to be checked, also gui, analog gui and additional assemble script must be set",
            layout,
        )
        layout.addStretch()

        return widget

    def create_extra_build_options(self) -> QWidget:
        """创建并添加包含额外构建选项复选框的小部件"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(
            MARGIN_BODY_LEFT,
            MARGIN_BODY_TOP,
            MARGIN_BODY_RIGHT,
            MARGIN_BOTTOM,
        )

        self.ctrl_attributes_on_root_joint_cb = self.create_checkbox(
            "ctrl attributes on root joint",
            "ctrl attributes on root joint",
            layout,
            enabled=True,
            checked=True,
        )
        self.animated_map_attributes_on_root_joint_cb = self.create_checkbox(
            "animated map attributes on root joint",
            "animated map attributes on root joint",
            layout,
            enabled=True,
            checked=True,
        )
        self.mesh_name_to_blend_shape_channel_name_cb = self.create_checkbox(
            "mesh name to blend shape channel name",
            "mesh name to blend shape channel name",
            layout,
            enabled=True,
            checked=True,
        )
        self.key_frames_cb = self.create_checkbox(
            "key frames",
            "Add keyframes to rig",
            layout,
            enabled=True,
            checked=True,
        )
        layout.addStretch()

        return widget

    def enable_additional_build_options(self, enable: bool) -> None:
        self.ctrl_attributes_on_root_joint_cb.setEnabled(enable)
        self.animated_map_attributes_on_root_joint_cb.setEnabled(enable)
        self.mesh_name_to_blend_shape_channel_name_cb.setEnabled(enable)
        self.key_frames_cb.setEnabled(enable)

    def create_checkbox(
        self,
        label: str,
        hint: str,
        layout: QHBoxLayout,
        on_changed: Callable[[int], None] = None,
        checked: bool = False,
        enabled: bool = False,
    ) -> QCheckBox:
        """
        向给定参数添加复选框，并将它们连接到on_changed方法
        
        @type label: str
        @param label: 复选框的标签
        
        @type hint: str
        @param hint: 复选框的提示
        
        @type on_changed: Callable[[int], None]
        @param on_changed: 复选框状态改变时调用的方法
        
        @type checked: bool
        @param checked: 创建后表示复选框是否已选中的值
        
        @type enabled: bool
        @param enabled: 创建后表示复选框是否已启用的值
        
        @rtype: QCheckBox
        @returns: 创建的复选框对象
        """

        checkbox = QCheckBox(label, self)
        checkbox.setChecked(checked)
        checkbox.setEnabled(enabled)
        checkbox.setToolTip(hint)
        if on_changed:
            checkbox.stateChanged.connect(on_changed)
        layout.addWidget(checkbox)
        return checkbox

    def on_joints_changed(self, state: int) -> None:
        """
        当关节复选框更改时调用的方法
        
        @type state: int
        @param state: 复选框的更改状态
        """

        if self.joints_cb.isChecked():
            self.process_btn.setEnabled(True)
            if self.mesh_tree_list.get_selected_meshes():
                self.skin_cb.setEnabled(True)
        else:
            self.skin_cb.setEnabled(False)
            if not self.mesh_tree_list.get_selected_meshes():
                self.process_btn.setEnabled(False)
        self.on_generic_changed(state)

    def create_process_btn(self) -> QPushButton:
        """
        创建并添加一个处理按钮
        
        @类型 窗口: QMainWindow
        @参数 窗口: 窗口对象的实例
        
        @类型: QPushButton
        @返回: 创建的处理按钮
        """

        btn = QPushButton("Process")
        btn.setEnabled(False)
        btn.clicked.connect(self.process)

        self.body.addWidget(btn)
        return btn

    def create_progress_bar(self) -> QProgressBar:
        """
        创建并添加进度条
        
        @类型窗口: QMainWindow
        @参数窗口: 窗口对象的实例
        
        @rtype: QProgressBar
        @returns: 创建的进度条
        """

        progress = QProgressBar(self)
        progress.setRange(0, 100)
        progress.setValue(0)
        progress.setTextVisible(True)
        progress.setFormat("")
        self.body.addWidget(progress)
        return progress

    def on_generic_changed(self, state: int) -> None:  # pylint: disable=unused-argument
        """
        当复选框更改时被调用的方法
        
        @type state: int
        @param state: 复选框的更改状态
        """

        self.set_riglogic_cb_enabled()

    def is_enabled_and_checked(self, check_box: QCheckBox) -> bool:
        """
        检查复选框是否同时启用的方法
        
        @type check_box: QCheckBox
        @param check_box: 要检查的复选框实例
        """

        return (
            check_box is not None
            and bool(check_box.isEnabled())
            and bool(check_box.isChecked())
        )

    def set_riglogic_cb_enabled(self) -> None:
        """设置riglogic复选框启用状态的方法"""

        all_total_meshes = False

        if self.dna and self.is_enabled_and_checked(self.blend_shapes_cb):
            if (
                len(self.mesh_tree_list.get_selected_meshes())
                == self.dna.get_mesh_count()
            ):
                all_total_meshes = True

        enabled = (
            self.is_enabled_and_checked(self.joints_cb)
            and self.is_enabled_and_checked(self.blend_shapes_cb)
            and all_total_meshes
            and self.is_enabled_and_checked(self.skin_cb)
            and self.select_gui_path.get_file_path() is not None
            and self.select_analog_gui_path.get_file_path() is not None
            and self.select_aas_path.get_file_path() is not None
        )
        self.rig_logic_cb.setEnabled(enabled)
