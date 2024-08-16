"""
这个例子演示了一些 DNACalib 的命令。
重要提示：在运行这个例子之前，您必须设置好环境。请参考 README.md 中的“环境设置”部分。

- 命令行中的用法：
    python dnacalib_remove_joint.py
    mayapy dnacalib_remove_joint.py
- 在 Maya 中的用法：
    1. 将此文件的整个内容复制到 Maya 脚本编辑器中
    2. 将 ROOT_DIR 的值更改为 dna_calibration 的绝对路径，例如在 Windows 中为 `c:/dna_calibration` 或在 `/home/user/dna_calibration`。重要提示：
    使用 `/`（正斜杠），因为 Maya 在路径中使用正斜杠。

- 自定义：
    - 将 CHARACTER_NAME 更改为 Taro，或者在 /data/dna_files 中放置的自定义 DNA 文件的名称

预期结果：脚本将从原始 Ada.dna 生成 OUTPUT_DIR 中的 Ada_output.dna。
注意：如果 OUTPUT_DIR 不存在，将会创建它。
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
from dnacalib import (
    DNACalibDNAReader,
    RemoveJointCommand,
)


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


def get_joints(dna):
    joints = []
    for jointIndex in range(dna.getJointCount()):
        joints.append(dna.getJointName(jointIndex))
    return joints


def calibrate_dna(input_path, output_path):
    dna = load_dna(input_path)

    # Copies DNA contents and will serve as input/output parameter to command
    calibrated = DNACalibDNAReader(dna)

    original_joints = get_joints(calibrated)

    # An example joint to remove
    joint_index = 314
    joint_name = calibrated.getJointName(joint_index)

    # Removes joint with specified index
    command = RemoveJointCommand(joint_index)

    # Modifies calibrated DNA in-place
    command.run(calibrated)

    modified_joints = get_joints(calibrated)

    if (len(modified_joints) != (len(original_joints) - 1)) or (joint_name in modified_joints):
        raise RuntimeError("Joint not removed properly!")

    print(f"Successfully removed joint `{joint_name}`.")

    print("Saving DNA...")
    save_dna(calibrated, output_path)

    print("Done.")


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)
    calibrate_dna(CHARACTER_DNA, OUTPUT_DNA)
