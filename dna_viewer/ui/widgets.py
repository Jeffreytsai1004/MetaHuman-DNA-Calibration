from pathlib import Path
from typing import Callable, Optional

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class QLine(QFrame):
    """用于创建水平线的小部件"""

    def __init__(self, line: QFrame.Shape) -> None:
        super().__init__()
        self.setFrameShape(line)
        self.setFrameShadow(QFrame.Sunken)


class QHLine(QLine):
    """一个用于创建水平线的小部件"""

    def __init__(self) -> None:
        super().__init__(QFrame.HLine)


class FileChooser(QWidget):
    """
    一个用于使用 FileDialog 和输入字段选择文件路径的自定义小部件
    """

    def __init__(
        self,
        label_text: str,
        hint: str,
        parent: Optional[QWidget] = None,
        placeholder: str = "",
        dialog_caption: str = "Select a file",
        dialog_filter: str = "All files (*.*)",
        button_text: str = "...",
        dir_selector: bool = False,
        on_changed: Callable[[int], None] = None,
    ) -> None:
        super().__init__(parent=parent)

        self._dialog_caption = dialog_caption
        self._dialog_filter = dialog_filter
        self._dir_selector = dir_selector

        layout = QHBoxLayout()
        layout.setMargin(0)

        fc_label = QLabel(label_text)
        fc_label.setMinimumHeight(32)
        fc_label.setToolTip(hint)

        self.fc_text_field = QLineEdit()
        self.fc_text_field.setAlignment(Qt.AlignLeft)
        self.fc_text_field.setPlaceholderText(placeholder)
        self.fc_text_field.textChanged.connect(on_changed)
        self.fc_text_field.setToolTip(hint)

        fc_btn = QPushButton(button_text)
        fc_btn.setToolTip(hint)

        layout.addWidget(fc_label)
        layout.addWidget(self.fc_text_field)
        layout.addWidget(fc_btn)

        fc_btn.clicked.connect(
            self.open_dialog,
        )

        self.setLayout(layout)

    def get_file_path(self) -> str:
        """
        从文本字段获取文件路径
        
        @rtype: str
        @returns: 文本字段中包含的文件路径
        """

        path = str(self.fc_text_field.text())
        if path and Path(path.strip()).exists():
            return path
        return None

    def open_dialog(self) -> None:
        """打开一个文件对话框，当选择了一个路径后，文本字段将被填充为该路径的值。"""

        if self._dir_selector:
            file_name, _ = QFileDialog.getExistingDirectory(
                self,
                self._dialog_caption,
                "",
                QFileDialog.Option.ShowDirsOnly,
            )
            if file_name:
                self.fc_text_field.setText(file_name)
        else:
            file_name, _ = QFileDialog.getOpenFileName(
                self, self._dialog_caption, "", self._dialog_filter
            )
            if file_name:
                self.fc_text_field.setText(file_name)
