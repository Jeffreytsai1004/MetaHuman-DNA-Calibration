"""
这个例子演示了如何重命名一个关节。
重要提示：在运行这个例子之前，你必须设置好环境。请参考 README.md 中的“环境设置”部分。

- 在命令行中的使用方法：
    python rename_joint_demo.py
    mayapy rename_joint_demo.py

    预期结果：脚本将在 OUTPUT_DIR 中生成 Ada_output.dna 文件。
- 在 Maya 中的使用方法：
    1. 将这个文件的全部内容复制到 Maya 脚本编辑器中
    2. 将 ROOT_DIR 的值更改为 dna_calibration 的绝对路径，例如在 Windows 中为 `c:/dna_calibration`，在 Unix 系统中为 `/home/user/dna_calibration`。重要提示：
    使用 `/`（正斜杠），因为 Maya 在路径中使用正斜杠。

- 定制：
    - 将 CHARACTER_NAME 更改为 Taro，或者将其更改为放置在 /data/dna_files 中的自定义 DNA 文件的名称

预期结果：脚本将从原始的 Ada.dna 文件生成 Ada_output.dna 文件，并放在 OUTPUT_DIR 中。
注意：如果 OUTPUT_DIR 不存在，脚本会创建它。
"""

from os import makedirs
from os import path as ospath

# if you use Maya, use absolute path
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
OUTPUT_DIR = f"{ROOT_DIR}/output"

CHARACTER_NAME = "Ada"

DATA_DIR = f"{ROOT_DIR}/data"
CHARACTER_DNA = f"{DATA_DIR}/dna_files/{CHARACTER_NAME}.dna"
OUTPUT_DNA = f"{OUTPUT_DIR}/{CHARACTER_NAME}_output.dna"

from dna import DataLayer_All, FileStream, Status, BinaryStreamReader, BinaryStreamWriter
from dnacalib import DNACalibDNAReader, RenameJointCommand


def load_dna(path):
    stream = FileStream(path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
    reader = BinaryStreamReader(stream, DataLayer_All)
    reader.read()
    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error loading DNA: {status.message}")
    return reader


def save_dna(reader, path):
    stream = FileStream(path, FileStream.AccessMode_Write, FileStream.OpenMode_Binary)
    writer = BinaryStreamWriter(stream)
    writer.setFrom(reader)
    writer.write()

    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error saving DNA: {status.message}")


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)

    dna_reader = load_dna(CHARACTER_DNA)
    calibrated = DNACalibDNAReader(dna_reader)
    # Prints current joint name
    print(calibrated.getJointName(10))
    # Creates rename command
    rename = RenameJointCommand(10, "NewJointA")
    # Executes command
    rename.run(calibrated)
    # Prints the new joint name
    print(calibrated.getJointName(10))
    save_dna(calibrated, OUTPUT_DNA)
    print('Done.')
