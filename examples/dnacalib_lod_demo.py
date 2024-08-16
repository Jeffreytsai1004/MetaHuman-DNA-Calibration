"""
此示例演示了通过从现有DNA中提取特定LOD来创建新的DNA。
重要提示：在运行此示例之前，您必须设置环境。请参考 README.md 中的“环境设置”部分。

- 在命令行中使用：
    python dnacalib_lod_demo.py
    mayapy dnacalib_lod_demo.py

- 在Maya中使用：
    1.将此文件的整个内容复制到Maya脚本编辑器中
    2.将ROOT_DIR的值更改为dna_calibration的绝对路径，例如在Windows中为`c:/dna_calibration`或在`/home/user/dna_calibration`。重要提示：在路径中使用`/`（正斜杠），因为Maya在路径中使用正斜杠。

- 自定义：
    -将CHARACTER_NAME更改为Taro，或将其更改为放置在/data/dna_files中的自定义DNA文件的名称
    -将LODS的值更改为需要提取的LOD列表

预期结果：脚本将从原始Ada生成Ada_with_lods_1_and_3.dna放在OUTPUT_DIR中。
注意：如果OUTPUT_DIR不存在，将会创建它。
"""


from os import makedirs
from os import path as ospath

# if you use Maya, use absolute path
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
OUTPUT_DIR = f"{ROOT_DIR}/output"

from dna import DataLayer_All, FileStream, Status, BinaryStreamReader, BinaryStreamWriter
from dnacalib import (
    DNACalibDNAReader,
    SetLODsCommand,
)

# Sets DNA file path
DNA = f"{ROOT_DIR}/data/dna_files/Ada.dna"
# Sets new DNA output file path
DNA_NEW = f"{OUTPUT_DIR}/Ada_with_lods_1_and_3.dna"
# Sets lods to extract
LODS = [1, 3]


def save_dna(reader: DNACalibDNAReader, created_dna_path: str):
    # Saves the dna
    stream = FileStream(created_dna_path, FileStream.AccessMode_Write, FileStream.OpenMode_Binary)
    writer = BinaryStreamWriter(stream)
    writer.setFrom(reader)
    writer.write()

    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error saving DNA: {status.message}")


def run_SetLODsCommand(reader):
    calibrated = DNACalibDNAReader(reader)
    command = SetLODsCommand()
    # Set a list of LODs that will be exported to the new file
    command.setLODs(LODS)
    # Runs the command that reduces LODs of the DNA
    command.run(calibrated)
    print("Setting new LODs...")

    if calibrated.getLODCount() != 2:
        raise RuntimeError("Setting new number of LODs in DNA was unsuccessful!")

    print("\nSuccessfully changed number of LODs in ")
    print("Saving ..")
    # Save the newly created DNA
    save_dna(calibrated, DNA_NEW)
    print("Done.")
    

def load_dna_calib(dna_path: str):
    # Load the DNA
    stream = FileStream(dna_path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
    reader = BinaryStreamReader(stream, DataLayer_All)
    reader.read()
    return reader


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)
    reader = load_dna_calib(DNA)
    run_SetLODsCommand(reader)
