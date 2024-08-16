"""
此示例演示了如何将Maya场景中的更改传播到dna文件。
重要提示：在运行此示例之前，您必须设置环境。请参考README.md中的“环境设置”部分。

按照以下步骤操作：

1. 启动Maya
2. 打开Maya场景（执行2.1或2.2）
2.1. 使用build_meshes生成新场景，或
2.2. 启动DNA Viewer GUI（dna_viewer_run_in_maya.py）
    - 选择要加载和生成场景的DNA文件
    - 选择要更改的网格
    - 在“构建选项”中勾选关节
    - 点击“处理”
    - 在Maya场景中，将会组装骨骼系统
3. 运行此脚本到“加载数据”部分
    a. 获取所有网格的当前顶点位置

4. 在场景中对中性网格和关节进行修改（重要提示：
    如果旋转关节，请确保冻结变换，以便将其存储为方向）
5. 从“将更改传播到dna”部分到结束运行此脚本
    a. 设置新的关节平移
    b. 设置新的关节旋转
    c. 将所有网格顶点移动到新位置

执行完这些步骤后，您对Maya场景的更改将传播到dna。

- 在Maya中的使用：
    1. 将此文件的全部内容复制到Maya脚本编辑器中
    2. 将ROOT_DIR的值更改为dna_calibration的绝对路径，例如在Windows中为`c:/dna_calibration`或在`/home/user/dna_calibration`。重要提示：
    使用`/`（正斜杠），因为Maya在路径中使用正斜杠。

- 自定义：
    - 将CHARACTER_NAME更改为Taro，或放置在/data/dna_files中的自定义DNA文件的名称

期望：
    - 脚本将在OUTPUT_DIR中生成dna文件<CHARACTER_NAME>_modified.dna，例如Ada_modified.dna
    - 脚本将在OUTPUT_DIR中生成Maya场景<CHARACTER_NAME>_modified.mb，例如Ada_modified.mb
    - 脚本将在OUTPUT_DIR中生成workspace.mel

注意：如果OUTPUT_DIR不存在，将会创建它。
"""

import maya.OpenMaya as om
from maya import cmds

from os import makedirs
from os import path as ospath

CHARACTER_NAME = "Ada"

# If you use Maya, use absolute path
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
OUTPUT_DIR = f"{ROOT_DIR}/output"
ROOT_LIB_DIR = f"{ROOT_DIR}/lib"
DATA_DIR = f"{ROOT_DIR}/data"
DNA_DIR = f"{DATA_DIR}/dna_files"
CHARACTER_DNA = f"{DNA_DIR}/{CHARACTER_NAME}.dna"
ANALOG_GUI = f"{DATA_DIR}/analog_gui.ma"
GUI = f"{DATA_DIR}/gui.ma"
ADDITIONAL_ASSEMBLE_SCRIPT = f"{DATA_DIR}/additional_assemble_script.py"
ADD_MESH_NAME_TO_BLEND_SHAPE_CHANNEL_NAME = True

MODIFIED_CHARACTER_DNA = f"{OUTPUT_DIR}/{CHARACTER_NAME}_modified"

from dna import (
    BinaryStreamReader,
    BinaryStreamWriter,
    DataLayer_All,
    FileStream,
    Status,
)
from dnacalib import (
    CommandSequence,
    DNACalibDNAReader,
    SetNeutralJointRotationsCommand,
    SetNeutralJointTranslationsCommand,
    SetVertexPositionsCommand,
    VectorOperation_Add,
)

from dna_viewer import DNA, RigConfig, build_rig, build_meshes


def load_dna_reader(path):
    stream = FileStream(path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
    reader = BinaryStreamReader(stream, DataLayer_All)
    reader.read()
    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error loading DNA: {status.message}")
    return reader


def save_dna(reader):
    stream = FileStream(
        f"{MODIFIED_CHARACTER_DNA}.dna",
        FileStream.AccessMode_Write,
        FileStream.OpenMode_Binary,
    )
    writer = BinaryStreamWriter(stream)
    writer.setFrom(reader)
    writer.write()

    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error saving DNA: {status.message}")


def get_mesh_vertex_positions_from_scene(meshName):
    try:
        sel = om.MSelectionList()
        sel.add(meshName)

        dag_path = om.MDagPath()
        sel.getDagPath(0, dag_path)

        mf_mesh = om.MFnMesh(dag_path)
        positions = om.MPointArray()

        mf_mesh.getPoints(positions, om.MSpace.kObject)
        return [
            [positions[i].x, positions[i].y, positions[i].z]
            for i in range(positions.length())
        ]
    except RuntimeError:
        print(f"{meshName} is missing, skipping it")
        return None


def run_joints_command(reader, calibrated):
    # Making arrays for joints' transformations and their corresponding mapping arrays
    joint_translations = []
    joint_rotations = []

    for i in range(reader.getJointCount()):
        joint_name = reader.getJointName(i)

        translation = cmds.xform(joint_name, query=True, translation=True)
        joint_translations.append(translation)

        rotation = cmds.joint(joint_name, query=True, orientation=True)
        joint_rotations.append(rotation)

    # This is step 5 sub-step a
    set_new_joints_translations = SetNeutralJointTranslationsCommand(joint_translations)
    # This is step 5 sub-step b
    set_new_joints_rotations = SetNeutralJointRotationsCommand(joint_rotations)

    # Abstraction to collect all commands into a sequence, and run them with only one invocation
    commands = CommandSequence()
    # Add vertex position deltas (NOT ABSOLUTE VALUES) onto existing vertex positions
    commands.add(set_new_joints_translations)
    commands.add(set_new_joints_rotations)

    commands.run(calibrated)
    # Verify that everything went fine
    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error run_joints_command: {status.message}")


def run_vertices_command(
    calibrated, old_vertices_positions, new_vertices_positions, mesh_index
):
    # Making deltas between old vertices positions and new one
    deltas = []
    for new_vertex, old_vertex in zip(new_vertices_positions, old_vertices_positions):
        delta = []
        for new, old in zip(new_vertex, old_vertex):
            delta.append(new - old)
        deltas.append(delta)

    # This is step 5 sub-step c
    new_neutral_mesh = SetVertexPositionsCommand(
        mesh_index, deltas, VectorOperation_Add
    )
    commands = CommandSequence()
    # Add nex vertex position deltas (NOT ABSOLUTE VALUES) onto existing vertex positions
    commands.add(new_neutral_mesh)
    commands.run(calibrated)

    # Verify that everything went fine
    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error run_vertices_command: {status.message}")


def assemble_maya_scene():
    dna = DNA(f"{MODIFIED_CHARACTER_DNA}.dna")
    config = RigConfig(
        gui_path=f"{DATA_DIR}/gui.ma",
        analog_gui_path=f"{DATA_DIR}/analog_gui.ma",
        aas_path=ADDITIONAL_ASSEMBLE_SCRIPT,
    )
    build_rig(dna=dna, config=config)

    cmds.file(rename=f"{MODIFIED_CHARACTER_DNA}.mb")
    cmds.file(save=True)


makedirs(OUTPUT_DIR, exist_ok=True)

dna = DNA(CHARACTER_DNA)
##################################
# This is step 2 sub-step 1
# use this block only if you need to assemble of scene from step 2.1
# config = RigConfig(
#     gui_path=f"{DATA_DIR}/gui.ma",
#     analog_gui_path=f"{DATA_DIR}/analog_gui.ma",
#     aas_path=ADDITIONAL_ASSEMBLE_SCRIPT,
# )
# build_meshes(dna=dna, config=config)
# This is end of step 2 sub-step 1
##################################


# This is step 3 sub-step a
current_vertices_positions = {}
mesh_indices = []
for mesh_index, name in enumerate(dna.meshes.names):
    current_vertices_positions[name] = {
        "mesh_index": mesh_index,
        "positions": get_mesh_vertex_positions_from_scene(name),
    }
# Loaded data - end of 3rd step
##################################

##################################
# Modify rig in maya, 4th step
##################################

##################################
# Propagate changes to dna, 5th step
reader = load_dna_reader(CHARACTER_DNA)
calibrated = DNACalibDNAReader(reader)

run_joints_command(reader, calibrated)

for name, item in current_vertices_positions.items():
    new_vertices_positions = get_mesh_vertex_positions_from_scene(name)
    if new_vertices_positions:
        run_vertices_command(
            calibrated, item["positions"], new_vertices_positions, item["mesh_index"]
        )
save_dna(calibrated)
assemble_maya_scene()
