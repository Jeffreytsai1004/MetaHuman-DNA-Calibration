"""
这个示例演示了一些 DNACalib 的命令。
重要提示：在运行此示例之前，您必须设置好环境。请参考 README.md 中的'环境设置'部分。

- 在命令行中的用法：
    python dnacalib_demo.py
    mayapy dnacalib_demo.py

- 在 Maya 中的用法：
    1. 将此文件的整个内容复制到 Maya 脚本编辑器中
    2. 将 ROOT_DIR 的值更改为 dna_calibration 的绝对路径，例如在 Windows 中为 `c:/dna_calibration` 或在 `/home/user/dna_calibration`。重要提示：
    使用 `/`（正斜杠），因为 Maya 在路径中使用正斜杠。

- 自定义：
    - 将 CHARACTER_NAME 更改为 Taro，或放置在 /data/dna_files 中的自定义 DNA 文件的名称


预期结果：脚本将从原始的 Ada.dna 生成 Ada_output.dna 到 OUTPUT_DIR 中。
注意：如果 OUTPUT_DIR 不存在，将会被创建。
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
    CommandSequence,
    DNACalibDNAReader,
    RenameJointCommand,
    ScaleCommand,
    SetBlendShapeTargetDeltasCommand,
    SetVertexPositionsCommand,
    VectorOperation_Add,
    VectorOperation_Interpolate,
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


def build_command_list():
    # Abstraction to collect all commands into a sequence, and run them with only one invocation
    commands = CommandSequence()

    print("Creating a sequence of commands...")
    # Instantiate command with parameters: scale-factor = 2 , origin-xyz = (0, 120, 0)
    scale_by_two = ScaleCommand(2.0, [0.0, 120.0, 0.0])
    # Alternatively a command can be instantiated empty, and populated with parameters later, e.g.:
    # scale_by_two = ScaleCommand()
    # scale_by_two.setScale(2.0)
    # scale_by_two.setOrigin([0.0, 120.0, 0.0])
    commands.add(scale_by_two)

    print("Added command to scale dna")
    # Rename by joint index (faster)
    commands.add(RenameJointCommand(10, "NewJointA"))

    # Rename by matching joint name (slower)
    commands.add(RenameJointCommand("OldJointB", "NewJointB"))

    print("Added command to rename joint")
    # Interpolate blend shape target deltas between original DNA and below specified deltas
    # ¯\_(ツ)_/¯
    # Deltas in [[x, y, z], [x, y, z], [x, y, z]] format
    blend_shape_target_deltas = [[0.0, 0.0, 2.0], [0.0, -1.0, 4.0], [3.0, -3.0, 8.0]]
    vertex_indices = [0, 1, 2]
    # Weights for interpolation between original deltas and above defined deltas
    # 1.0 == take the new value completely, 0.0 means keep the old value
    # Format: [Delta-0-Mask, Delta-1-Mask, Delta-2-Mask]
    masks = [1.0, 0.0, 0.5]
    set_blend_shapes_m0_b0 = SetBlendShapeTargetDeltasCommand(
        0,  # mesh index
        0,  # blend shape target index
        blend_shape_target_deltas,
        vertex_indices,
        masks,
        VectorOperation_Interpolate,
    )
    commands.add(set_blend_shapes_m0_b0)
    print("Added command to change blend shape target deltas")

    # Add vertex position deltas onto existing vertex positions
    # Note the alternative data format, instead of using nested lists, separate all X, Y, Z
    # components into distinct lists (might also be faster)
    position_xs = [1.0, -4.5, 7.2]
    position_ys = [2.0, -5.5, -8.3]
    position_zs = [3.0, -6.5, 9.7]
    # Weights to be multiplied with the above specified delta positions, before adding
    # them onto the original data
    # Format: [Delta-0-Weight, Delta-1-Weight, Delta-2-Weight]
    masks = [1.0, 0.2, 0.4]
    set_vertices_m0 = SetVertexPositionsCommand(
        0,  # mesh index
        position_xs,
        position_ys,
        position_zs,
        masks,
        VectorOperation_Add,
    )
    commands.add(set_vertices_m0)
    print("Added command to change vertex positions")

    return commands


def calibrate_dna(input_path, output_path):
    dna = load_dna(input_path)

    # Copies DNA contents and will serve as input/output parameter to commands
    calibrated = DNACalibDNAReader(dna)

    commands = build_command_list()

    print("Running command sequence...")
    # Modifies calibrated DNA in-place
    commands.run(calibrated)

    print("Saving DNA...")
    save_dna(calibrated, output_path)

    print("Done.")


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)
    calibrate_dna(CHARACTER_DNA, OUTPUT_DNA)
