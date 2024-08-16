"""
这个示例演示了在Maya场景中生成功能性的骨骼系统，并根据每个LOD导出FBX文件。

重要提示：在运行此示例之前，您必须设置好环境。请参考README.md中的“环境设置”部分。

- 命令行中的用法：
    python dna_viewer_build_rig.py
    mayapy dna_viewer_build_rig.py
    注意：脚本不能用Python调用，必须用mayapy调用。

- 在Maya中的用法：
    1. 将此文件的整个内容复制到Maya脚本编辑器中
    2. 将ROOT_DIR的值更改为dna_calibration的绝对路径，例如在Windows中为`c:/dna_calibration`或`/home/user/dna_calibration`。重要提示：
    使用`/`（正斜杠），因为Maya在路径中使用正斜杠。

- 自定义：
    - 将CHARACTER_NAME更改为Taro，或者放置在/data/dna_files中的自定义DNA文件的名称
期望结果：
    - 脚本将在OUTPUT_DIR中生成Maya场景Ada.mb
    - 脚本将在OUTPUT_DIR中生成workspace.mel
    - 脚本将原始的Ada.dna文件复制到OUTPUT_DIR

期望结果：脚本将生成<新DNA文件的路径>。
注意：如果OUTPUT_DIR不存在，将会创建它。
"""


from os import makedirs
from os import path as ospath
from shutil import copyfile

# if you use Maya, use absolute path
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
OUTPUT_DIR = f"{ROOT_DIR}/output"
EXAMPLES_DIR = f"{ROOT_DIR}/examples"
ROOT_LIB_DIR = f"{ROOT_DIR}/lib"

CHARACTER_NAME = "Ada"

DATA_DIR = f"{ROOT_DIR}/data"
CHARACTER_DNA = f"{DATA_DIR}/dna_files/{CHARACTER_NAME}.dna"
ANALOG_GUI = f"{DATA_DIR}/analog_gui.ma"
GUI = f"{DATA_DIR}/gui.ma"
ADDITIONAL_ASSEMBLE_SCRIPT = f"{DATA_DIR}/additional_assemble_script.py"


from maya import cmds, mel

from dna_viewer import DNA, RigConfig, build_rig


if __name__ == "__main__":
    dna = DNA(CHARACTER_DNA)

    makedirs(OUTPUT_DIR, exist_ok=True)

    # This fixes warning when calling this script with headless maya Warning: line 1: Unknown object type: HIKCharacterNode
    mel.eval(f"HIKCharacterControlsTool;")

    # Generate workspace.mel
    mel.eval(f'setProject "{OUTPUT_DIR}";')

    config = RigConfig(
        gui_path=GUI,
        analog_gui_path=ANALOG_GUI,
        aas_path=ADDITIONAL_ASSEMBLE_SCRIPT,
    )

    # Creates the rig
    build_rig(dna=dna, config=config)
    # Renames and saves the scene
    cmds.file(rename=f"{OUTPUT_DIR}/{CHARACTER_NAME}.mb")
    cmds.file(save=True)
    # Copy dna file and workspace file alongside generated scene
    copyfile(CHARACTER_DNA, f"{OUTPUT_DIR}/{CHARACTER_NAME}.dna")
