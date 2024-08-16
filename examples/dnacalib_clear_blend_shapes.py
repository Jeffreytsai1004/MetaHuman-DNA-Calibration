"""
此示例演示如何从DNA中删除所有混合形状数据。
重要提示：在运行此示例之前，您必须设置环境。请参考README.md中的“环境设置”部分。

- 命令行中的用法：
    python dnacalib_clear_blend_shapes.py
    mayapy dnacalib_clear_blend_shapes.py
- Maya中的用法：
    1. 将此文件的整个内容复制到Maya脚本编辑器中
    2. 将ROOT_DIR的值更改为dna_calibration的绝对路径，例如在Windows中为`c:/dna_calibration`或在`/home/user/dna_calibration`。重要提示：
    使用`/`（正斜杠），因为Maya在路径中使用正斜杠。

- 自定义：
    - 将CHARACTER_NAME更改为Taro，或者是放置在/data/dna_files中的自定义DNA文件的名称

预期结果：脚本将从原始的Ada.dna生成Ada_output.dna到OUTPUT_DIR中。
注意：如果OUTPUT_DIR不存在，将会被创建。
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
    ClearBlendShapesCommand
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


def validate_geometry(dna):
    mesh_count = dna.getMeshCount()
    for mesh_index in range(mesh_count):
        bs_tgt_count = dna.getBlendShapeTargetCount(mesh_index)
        for bs_tgt_index in range(bs_tgt_count):
            bs_tgt_delta_count = dna.getBlendShapeTargetDeltaCount(mesh_index, bs_tgt_index)
            if bs_tgt_delta_count != 0:
                raise RuntimeError("Blend shape target deltas not removed properly!")


def validate_animation_data(dna):
    bs_channel_lods = dna.getBlendShapeChannelLODs()
    bs_channel_input_indices = dna.getBlendShapeChannelInputIndices()
    bs_channel_output_indices = dna.getBlendShapeChannelOutputIndices()

    if len(bs_channel_lods) != dna.getLODCount():
        raise RuntimeError("Blend shape animation data not removed properly! Number of blend shape LODs does not match LOD count!")

    for lod in bs_channel_lods:
        if lod != 0:
            raise RuntimeError("Blend shape animation data not removed properly!")

    if (len(bs_channel_input_indices) != 0) or (len(bs_channel_output_indices) != 0):
        raise RuntimeError("Blend shape animation data not removed properly!")


def calibrate_dna(input_path, output_path):
    dna = load_dna(input_path)

    # Copies DNA contents and will serve as input/output parameter to commands
    calibrated = DNACalibDNAReader(dna)

    mesh_count = calibrated.getMeshCount()
    print(f"Number of meshes: {mesh_count}")

    for mesh_index in range(mesh_count):
        bs_tgt_count = calibrated.getBlendShapeTargetCount(mesh_index)
        print(f"Number of blendshape targets for mesh {calibrated.getMeshName(mesh_index)}({mesh_index}): {bs_tgt_count}")
        for bs_tgt_index in range(bs_tgt_count):
            bs_tgt_delta_count = calibrated.getBlendShapeTargetDeltaCount(mesh_index, bs_tgt_index)
            print(f"Number of blendshape target deltas for mesh {calibrated.getMeshName(mesh_index)}({mesh_index}), blend shape target {bs_tgt_index}: {bs_tgt_delta_count}")

    print(f"Blend shape channel LODs: {calibrated.getBlendShapeChannelLODs()}")
    print(f"Blend shape channel input indices: {calibrated.getBlendShapeChannelInputIndices()}")
    print(f"Blend shape channel output indices: {calibrated.getBlendShapeChannelOutputIndices()}")

    # Clears all blend shapes
    command = ClearBlendShapesCommand()

    print("\n\nClearing blend shape data...\n\n")
    # Modifies calibrated DNA in-place
    command.run(calibrated)

    validate_geometry(calibrated)
    validate_animation_data(calibrated)

    print(f"Number of meshes: {mesh_count}")

    for mesh_index in range(mesh_count):
        bs_tgt_count = calibrated.getBlendShapeTargetCount(mesh_index)
        print(f"Number of blendshape targets for mesh {calibrated.getMeshName(mesh_index)}({mesh_index}): {bs_tgt_count}")
        for bs_tgt_index in range(bs_tgt_count):
            bs_tgt_delta_count = calibrated.getBlendShapeTargetDeltaCount(mesh_index, bs_tgt_index)
            print(f"Number of blendshape target deltas for mesh {calibrated.getMeshName(mesh_index)}({mesh_index}), blend shape target {bs_tgt_index}: {bs_tgt_delta_count}")

    bs_channel_lods = dna.getBlendShapeChannelLODs()
    bs_channel_input_indices = dna.getBlendShapeChannelInputIndices()
    bs_channel_output_indices = dna.getBlendShapeChannelOutputIndices()

    print(f"Blend shape channel LODs: {bs_channel_lods}")
    print(f"Blend shape channel input indices: {bs_channel_input_indices}")
    print(f"Blend shape channel output indices: {bs_channel_output_indices}")

    print("\n\nSuccessfully cleared blend shape data.")

    print("Saving DNA...")
    save_dna(calibrated, output_path)
    print("Done.")


if __name__ == "__main__":
    makedirs(OUTPUT_DIR, exist_ok=True)
    calibrate_dna(CHARACTER_DNA, OUTPUT_DNA)
