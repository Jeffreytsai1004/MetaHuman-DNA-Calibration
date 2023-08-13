# MetaHuman DNA 校准
MetaHuman DNA Calibration 是一组用于处理 MetaHuman DNA 文件的工具，捆绑在一个软件包中。
[`DNA`](/docs/dna.md#meta human-dna) 是 [MetaHuman](https://www.unrealengine.com/en-US/metahuman) 身份的一个组成部分。
DNA 文件是使用 [MetaHuman Creator](https://meta human.unrealengine.com/) 创建并使用
UE5 中的 [Quixel Bridge](https://docs.meta human.unrealengine.com/en-US/downloading-metahumans-with-quixel-bridge/) 和 Bifrost。

MetaHuman DNA Calibration 是一组用于处理 MetaHuman DNA 文件的工具，捆绑在一个软件包中。 
我们希望分享此代码来帮助用户自定义 DNA 文件，以便他们可以更好地将他们创建的角色融入到他们的游戏和体验中。
位于此地址的 GitHub 存储库中提供了 MetaHuman DNA 校准工具。

＃ 概述
有关如何组织存储库的说明，请[单击此处](docs/repository_organization.md)。

MetaHuman DNA 校准存储库包含两个不同的工具：
- [DNACalib](docs/dnacalib.md)（及其依赖项）
- [DNAViewer](docs/dna_viewer.md)

## 所需知识
要使用这些工具，您应该熟悉：
- Rigging in Maya
- Python

## 可选知识
- C++（对于 [DNACalib](docs/dnacalib.md) 及其 [API](docs/dnacalib_api.md)）


## DNA 校准
[DNACalib](docs/dnacalib.md) 及其 [API](docs/dnacalib_api.md) 用于检查和修改 DNA 文件。 使用 [DNACalib](docs/dnacalib.md)，您可以在 DNA 文件中进行以下更改：
- 重命名关节、网格、混合形状和/或动画贴图。
- 删除关节、网格和/或关节动画。
- 旋转、缩放和平移装备。
- 删除 LOD。
- 更改中性关节位置、中性网格位置和混合形状增量值。
- 修剪混合形状。
- 删除所有混合形状数据。

有关 MetaHuman DNA 文件格式的概述，请参阅[`此处`](/docs/dna.md)。

**注意**：DNACalib 库允许删除和重命名任何关节。 但是，以下关节用于连接头部和身体，不应删除或重命名：neck_01、neck_02、FACIAL_C_FacialRoot。

## 外部软件依赖项
DNACalib 的 Python 包装器是针对 Python 3.7 和 3.9 编译的。 适用于 Windows 和 Linux（均为 64 位）的预编译二进制文件是存储库的一部分。
如果您使用不同版本的Python，则必须重新编译它。 任何 Python 3 版本都应该没问题。
如果用户有不同的平台或体系结构，则必须编译库及其依赖项。

**重要的**
DNA 文件存储为 [LFS（大文件存储）](https://git-lfs.github.com/) 文件。 如果满足以下条件，它们将与其余代码一起下载
git-lfs 已安装并配置为使用。 如果您不使用 git-lfs，则必须手动下载 DNA 文件。

其他信息可以在[此处](docs/faq.md#fix--runtimeerror--error-loading-dna--dna-signature-mismatched-expected-dna-got-ver-)找到

**警告：**
不支持 Python 2。

DNACalib 可以作为 C++ 库在 C++ 项目中使用。

DNACalib Python 包装器可在 Python 3.7 和 3.9 中使用，“mayapy”（随 Maya 附带的 Python 解释器）随 Maya 附带。
支持的 Maya 版本为 2022 和 2023。

注意：Maya 2022 与 Python 3.7 捆绑在一起，Maya 2023 与 Python 3.9 捆绑在一起。 

## 环境设置

为了在您的脚本中使用 MetaHuman DNA 校准，您需要：
- 已安装Python3，请参阅[注意](README.md#external-software-dependencies)，
- 将 MetaHuman DNA 校准位置添加到“MAYA_MODULE_PATH”系统变量（如果您想在 Maya 中使用 MetaHuman DNA 校准）


如果您打算从命令行运行脚本：

- 如果使用 Maya 的解释器 (mayapy)，您必须使用以下命令初始化 Maya：

```python
import maya.standalone 
maya.standalone.initialize()
```

- in case of python interpreter you will have to add the following on top of your script: 
```python
from os import path as ospath
from sys import path as syspath
from sys import platform

ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
MAYA_VERSION = "2022"  # or 2023
ROOT_LIB_DIR = f"{ROOT_DIR}/lib/Maya{MAYA_VERSION}"
if platform == "win32":
    LIB_DIR = f"{ROOT_LIB_DIR}/windows"
elif platform == "linux":
    LIB_DIR = f"{ROOT_LIB_DIR}/linux"
else:
    raise OSError(
        "OS not supported, please compile dependencies and add value to LIB_DIR"
    )

# Adds directories to path
syspath.insert(0, ROOT_DIR)
syspath.insert(0, LIB_DIR)
```

注意：
如果在 Linux 上运行，请确保在运行示例之前将 LD_LIBRARY_PATH 附加到 `lib/Maya2022/linux` 或 `lib/Maya2023/linux` 目录的绝对路径：
  - `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<lib-linux-dir 路径>`

## DNA查看器
使用 DNAViewer，您可以：
- 为 Maya 创建功能装备。
- 导出 FBX 文件。
- 读取 DNA 文件的内部部分。

DNAViewer 可以在“mayapy”（Maya 附带的 Python 解释器）或 Maya 2022 中使用，但 [将更改从 Maya 场景传播到 dna](/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py) 除外，它只能在 Maya 中使用。

＃ 例子
提供了几个 Python 示例供参考，可以在 **examples'** 文件夹中找到：
- [展示一些命令](/examples/dnacalib_demo.py)
- [重命名关节](/examples/dnacalib_rename_joint_demo.py)
- [从头开始创建一个小 DNA](/examples/dna_demo.py)
- [读取二进制 DNA 并以人类可读的格式写入](/examples/dna_binary_to_json_demo.py)
- [通过提取特定 LOD 从现有 DNA 中创建新 DNA](/examples/dnacalib_lod_demo.py)
- [删除关节](/examples/dnacalib_remove_joint.py)
- [清除混合形状数据](/examples/dnacalib_clear_blend_shapes.py)
- [从中性网格中减去值](/examples/dnacalib_neutral_mesh_subtract.py)
- [Maya 中的简单 UI](examples/dna_viewer_run_in_maya.py) 和一些 [文档](docs/dna_viewer.md#usage-in-maya)
- [生成装备](/examples/dna_viewer_build_rig.py)
- [导出每个 LOD 的 FBX](/examples/dna_viewer_export_fbx.py)
- [将更改从 Maya 场景传播到 dna](/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py)
注意：示例分为三组：DNA、DNACalib 和 DNAViewer。 这些名称作为前缀嵌入：dna_、dnacalib_ 和 dna_viewer_。

## DNA 文件示例
提供了[两个演示 DNA 文件](data/dna_files)，以便更轻松地测试该工具。 使用 [MetaHumanCreator](https://www.unrealengine.com/en-US/metahuman) 生成的任何 DNA
应该管用。

MHC 2023 春季版本对装备定义进行了更改（增加了关节数量以及表情数量）。
为了适应这些更改，我们在`/data/mh4`文件夹中的存储库中添加了几个文件：新的[gui场景](/data/mh4/gui.ma)，更新的[汇编脚本](/data/mh4/ extra_assemble_script.py）和 Ada 的 [DNA 文件] 示例（data/mh4/dna_files/Ada.dna）。
如果用户想要切换并使用这个新的装备版本，则需要更新其脚本中的路径：
```python
GUI = f"{DATA_DIR}/mh4/gui.ma"
ADDITIONAL_ASSEMBLE_SCRIPT = f"{DATA_DIR}/mh4/additional_assemble_script.py"
```

如果角色DNA是从[Quixel Bridge](https://quixel.com/bridge)下载的，并且我们不确定使用哪个装备定义，可以使用以下代码进行检查：
```python
from dna import (
    BinaryStreamReader,
    DataLayer_All,
    FileStream,
    Status,
)

def load_dna_reader(dna_file):
    stream = FileStream(
        dna_file, FileStream.AccessMode_Read, FileStream.OpenMode_Binary
    )
    reader = BinaryStreamReader(stream, DataLayer_All)
    reader.read()
    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error loading DNA: {status.message}")
    return reader

character_dna = "path_to/character.dna"
reader = load_dna_reader(character_dna)
if reader.getDBName() == "MH.4":
  print("Use mh4 folder")
elif reader.getDBName() == "DHI":
  print("Use data folder")
else:
  print("Unsupported rig definition!")
```

# 注释
如果用户在 Maya 2022 中运行示例，则应更改“ROOT_DIR”的值并且必须使用绝对路径，
例如 Windows 中的“c:/MetaHuman-DNA-Calibration”或 Linux 中的“/home/user/MetaHuman-DNA-Calibration”。 重要提示：使用“/”（正斜杠），Maya 在路径中使用正斜杠。

有关其他规范，请参阅[常见问题解答指南](docs/faq.md)。

＃ 执照
MetaHuman DNA Calibration 已获得[许可证](LICENSE) 发布。
