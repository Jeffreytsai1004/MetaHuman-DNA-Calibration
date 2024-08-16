"""
这个例子演示了以二进制格式读取DNA文件并将其写入人类可读的JSON格式。
重要提示：在运行此示例之前，您必须设置环境。请参考README.md中的“环境设置”部分。

- 在命令行中的使用方法：
    python dna_binary_to_json_demo.py
    mayapy dna_binary_to_json_demo.py
- 在Maya中的使用方法：
    1. 将此文件的整个内容复制到Maya脚本编辑器中
    2. 将ROOT_DIR的值更改为dna_calibration的绝对路径，例如在Windows中为`c:/dna_calibration`或在`/home/user/dna_calibration`。重要提示：
    使用`/`（正斜杠），因为Maya在路径中使用正斜杠。

- 自定义：
    - 将CHARACTER_NAME更改为Taro，或将其更改为放置在/data/dna_files中的自定义DNA文件的名称

预期结果：脚本将从原始的Ada.dna在OUTPUT_DIR中生成Ada_output.json。
注意：如果OUTPUT_DIR不存在，它将被创建。
"""

from os import makedirs
from os import path as ospath

# If you use Maya, use absolute path
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
OUTPUT_DIR = f"{ROOT_DIR}/output"

CHARACTER_NAME = "Ada"

DATA_DIR = f"{ROOT_DIR}/data"
CHARACTER_DNA = f"{DATA_DIR}/dna_files/{CHARACTER_NAME}.dna"
OUTPUT_DNA = f"{OUTPUT_DIR}/{CHARACTER_NAME}_output.json"

from dna import DataLayer_All, FileStream, Status, BinaryStreamReader, JSONStreamWriter


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
    writer = JSONStreamWriter(stream)
    # Create a writer based on the reader using all data layers (if no argument is passed, DataLayer_All is the default value)
    writer.setFrom(reader)
    # Alternatively, a writer can be created using only a subset of layers,
    # e.g. to write only Behavior layer (Descriptor and Definition included with it), use:
    # writer.setFrom(reader, DataLayer_Behavior)
    #
    # Available layer options and their approximate sizes for this example (Ada.dna, JSON format):
    # DataLayer_Descriptor - ~ 3 KB
    # DataLayer_Definition - includes Descriptor, ~ 131 KB
    # DataLayer_Behavior - includes Descriptor and Definition, ~ 10 MB
    # DataLayer_Geometry - includes Descriptor and Definition, ~ 191 MB
    # DataLayer_GeometryWithoutBlendShapes - includes Descriptor and Definition, ~ 22 MB
    # DataLayer_AllWithoutBlendShapes - includes everything except blend shapes from Geometry, ~ 32 MB
    # DataLayer_All - ~ 201 MB
    #
    # If using one of the other layer options, be sure to add it to the import list.
    #
    # Beside specifying layers when creating a writer, layers to use can be specified when
    # creating a reader as well.
    writer.write()

    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error saving DNA: {status.message}")


def create_json_dna(input_path, output_path):
    dna_reader = load_dna(input_path)
    save_dna(dna_reader, output_path)
    print('Done.')


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)
    create_json_dna(CHARACTER_DNA, OUTPUT_DNA)
