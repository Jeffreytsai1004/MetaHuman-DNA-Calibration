"""
这个示例演示了如何从一个中性网格中减去值，并将这些改变传递到其较低的LOD网格中。
重要提示：在运行此示例之前，您必须设置环境。请参考 README.md 中的“环境设置”部分。

- 命令行中的用法：
    python dnacalib_neutral_mesh_subtract.py
    mayapy dnacalib_neutral_mesh_subtract.py
- 在Maya中的用法：
    1. 将此文件的全部内容复制到Maya脚本编辑器中
    2. 将ROOT_DIR的值更改为dna_calibration的绝对路径，例如在Windows中为`c:/dna_calibration`或在`/home/user/dna_calibration`。重要提示：
    使用“/”（正斜杠），因为Maya在路径中使用正斜杠。

- 自定义：
    - 将CHARACTER_NAME更改为Taro，或放置在/data/dna_files中的自定义DNA文件的名称

预期结果：脚本将从原始的Ada.dna 生成 OUTPUT_DIR 中的Ada_output.dna。
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
    DNACalibDNAReader,
    SetVertexPositionsCommand,
    VectorOperation_Subtract,
    CalculateMeshLowerLODsCommand
)
from math import isclose


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


def calibrate_dna(input_path, output_path):
    dna = load_dna(input_path)

    # Copies DNA contents and will serve as input/output parameter to commands
    calibrated = DNACalibDNAReader(dna)

    if calibrated.getMeshCount() == 0:
        print("No meshes found in DNA.")
        return

    mesh_index = 0
    vtx_count_mesh0 = calibrated.getVertexPositionCount(mesh_index)
    xs = calibrated.getVertexPositionXs(mesh_index)
    ys = calibrated.getVertexPositionYs(mesh_index)
    zs = calibrated.getVertexPositionZs(mesh_index)

    # Example values to subtract from original vertex positions for mesh with index 0
    ones = [1.0] * vtx_count_mesh0

    # Command used to subtract example values from a specified neutral mesh
    subtract_command = SetVertexPositionsCommand()
    subtract_command.setMeshIndex(mesh_index)
    subtract_command.setOperation(VectorOperation_Subtract)
    subtract_command.setPositions(ones, ones, ones)

    # Alternatively, if you wanted to do the opposite, to subtract neutral mesh values
    # from example values, you could do the following:
    # xs_2 = [x * 2 for x in xs]
    # ys_2 = [y * 2 for y in ys]
    # zs_2 = [z * 2 for z in zs]
    # subtract_command.setPositions(xs_2, ys_2, zs_2)
    # # After running the command, the calibrated DNA will contain -xs, -ys, -zs
    # subtract_command.run(calibrated)
    #
    # # Add the example values, which will result in:
    # # ones - xs
    # # ones - ys
    # # ones - zs
    # add_command = SetVertexPositionsCommand()
    # add_command.setMeshIndex(mesh_index)
    # add_command.setOperation(VectorOperation_Add) # remember to add VectorOperation_Add to the list of imports
    # add_command.setPositions(ones, ones, ones)
    # add_command.run(calibrated)

    print(f"Subtracting values from neutral mesh \'{calibrated.getMeshName(mesh_index)}\'...")
    # Modifies calibrated DNA in-place
    subtract_command.run(calibrated)

    # Command used to recalculate vertex positions of lower LOD neutral meshes of the specified neutral mesh
    calculate_lower_lods_command = CalculateMeshLowerLODsCommand()
    calculate_lower_lods_command.setMeshIndex(mesh_index)

    print("Recalculating values for lower LOD meshes...")
    # Modifies calibrated DNA in-place
    calculate_lower_lods_command.run(calibrated)

    new_xs = calibrated.getVertexPositionXs(mesh_index)
    new_ys = calibrated.getVertexPositionYs(mesh_index)
    new_zs = calibrated.getVertexPositionZs(mesh_index)

    for i in range(vtx_count_mesh0):
        if (not isclose(xs[i] - 1, new_xs[i], rel_tol=1e-7) or
                not isclose(ys[i] - 1, new_ys[i], rel_tol=1e-7) or
                not isclose(zs[i] - 1, new_zs[i], rel_tol=1e-7)):
            raise RuntimeError("Vertex positions were not changed successfully!")

    print("\nSuccessfully changed vertex positions.")

    print("Saving DNA...")
    save_dna(calibrated, output_path)
    print("Done.")


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)
    calibrate_dna(CHARACTER_DNA, OUTPUT_DNA)
