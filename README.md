# Metahuman DNA Calibration
MetaHuman DNA校准是一套用于处理MetaHuman DNA文件的工具集，打包成一个单独的软件包。
[`DNA`](/docs/dna.md#metahuman-dna)是[MetaHuman](https://www.unrealengine.com/en-US/metahuman)身份的一个组成部分。
DNA文件是使用[MetaHuman Creator](https://metahuman.unrealengine.com/)创建的，并通过[Quixel Bridge](https://docs.metahuman.unrealengine.com/en-US/downloading-metahumans-with-quixel-bridge/)和UE5中的Bifrost进行下载。

MetaHuman DNA校准是一套用于处理MetaHuman DNA文件的工具集，打包成一个单独的软件包。我们希望分享此代码，以帮助用户自定义DNA文件，从而更好地将他们创建的角色整合到他们的游戏和体验中。
MetaHuman DNA校准工具位于GitHub存储库的以下地址。

# 概述
有关存储库组织方式的解释，请[点击这里](docs/repository_organization.md)。

MetaHuman DNA校准存储库包含两个不同的工具：
- [DNACalib](docs/dnacalib.md)（及其依赖项）
- [DNAViewer](docs/dna_viewer.md)

## 需要的知识
要使用这些工具，您应该熟悉：
- Maya中的绑定
- Python

## 可选知识
- C++（用于[DNACalib](docs/dnacalib.md)及其[API](docs/dnacalib_api.md)）

## DNACalib
[DNACalib](docs/dnacalib.md)及其[API](docs/dnacalib_api.md)用于检查和修改DNA文件。使用[DNACalib](docs/dnacalib.md)，您可以对DNA文件进行以下更改：
- 重命名关节、网格、混合形状和/或动画贴图。
- 删除关节、网格和/或关节动画。
- 旋转、缩放和平移骨骼。
- 删除LOD。
- 更改中性关节位置、中性网格位置和混合形状增量值。
- 精简混合形状。
- 删除所有混合形状数据。

MetaHuman DNA文件格式的概述可以在[`这里`](/docs/dna.md)找到。

**注意**：DNACalib库允许删除和重命名任何关节。但是，以下关节用于连接头部和身体，不应删除或重命名：neck_01、neck_02、FACIAL_C_FacialRoot。

## 外部软件依赖
DNACalib的Python包装器是针对Python 3.7和3.9进行编译的。Windows和Linux（64位）的预编译二进制文件包含在存储库中。
如果您使用不同版本的Python，则必须重新编译它。任何Python 3版本都可以。
如果用户使用不同的平台或架构，则必须编译该库及其依赖项。

**重要**
DNA文件以[LFS（大文件存储）](https://git-lfs.github.com/)文件的形式存储。如果安装并配置了git-lfs，则它们将与代码的其余部分一起下载。
如果您不使用git-lfs，则必须手动下载DNA文件。

可以在[此处](docs/faq.md#fix--runtimeerror--error-loading-dna--dna-signature-mismatched-expected-dna-got-ver-)找到额外信息。

**警告**：
不支持Python 2。

DNACalib可以作为C++库在C++项目中使用。

DNACalib Python包装器可以在Python 3.7和3.9以及与Maya一起提供的`mayapy`（随Maya一起提供的Python解释器）中使用。
支持的Maya版本是2022和2023。

注意：Maya 2022捆绑了Python 3.7，Maya 2023捆绑了Python 3.9。

## 环境设置

为了在您的脚本中使用MetaHuman DNA校准，您需要：
- 安装Python3，请参见[备注](README.md#external-software-dependencies)
- 将MetaHuman DNA校准位置添加到`MAYA_MODULE_PATH`系统变量中（如果要在Maya中使用MetaHuman DNA校准）

如果您计划从命令行运行脚本：

- 在Maya的解释器（mayapy）中，您将不得不初始化Maya：

```python
import maya.standalone 
maya.standalone.initialize()
```

- 在Python解释器中，您将不得不在脚本顶部添加以下内容：
```python
from os import path as ospath
from sys import path as syspath
from sys import platform

ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
MAYA_VERSION = "2022"# 或2023
ROOT_LIB_DIR = f"{ROOT_DIR}/lib/Maya{MAYA_VERSION}"
if platform == "win32":
    LIB_DIR = f"{ROOT_LIB_DIR}/windows"
elif platform == "linux":
    LIB_DIR = f"{ROOT_LIB_DIR}/linux"
else:
    raise OSError(
        "不支持的操作系统，请编译依赖项并将值添加到LIB_DIR中"
    )

# 将目录添加到路径
syspath.insert(0, ROOT_DIR)
syspath.insert(0, LIB_DIR)
```

注意：
如果在Linux上运行，请确保在运行示例之前将LD_LIBRARY_PATH附加到`lib/Maya2022/linux`或`lib/Maya2023/linux`目录的绝对路径:
 - `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<path-to-lib-linux-dir>`

## DNAViewer
使用DNAViewer，您可以：
- 为Maya创建功能性的骨骼。
- 导出FBX文件。
- 读取DNA文件的内部部分。

DNAViewer可以在`mayapy`（与Maya一起提供的Python解释器）或Maya 2022中使用，除了[从Maya场景传播更改到dna](/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py)这个示例只能在Maya中使用。

# 示例
提供了几个Python示例用于参考，可以在**examples**文件夹中找到：
- [展示几个命令](/examples/dnacalib_demo.py)
- [重命名关节](/examples/dnacalib_rename_joint_demo.py)
- [从头开始创建一个小的DNA](/examples/dna_demo.py)
- [读取二进制DNA并将其写成人类可读的格式](/examples/dna_binary_to_json_demo.py)
- [从现有DNA中提取特定LOD创建新的DNA](/examples/dnacalib_lod_demo.py)
- [移除关节](/examples/dnacalib_remove_joint.py)
- [清除混合形状数据](/examples/dnacalib_clear_blend_shapes.py)
- [从中性网格中减去值](/examples/dnacalib_neutral_mesh_subtract.py)
- [Maya中的简单UI](examples/dna_viewer_run_in_maya.py)和一些[文档](docs/dna_viewer.md#usage-in-maya) 
- [生成骨骼](/examples/dna_viewer_build_rig.py)
- [每个LOD导出FBX](/examples/dna_viewer_export_fbx.py)
- [从Maya场景传播更改到dna](/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py)

注意：示例分为三组：DNA、DNACalib和DNAViewer。这些名称作为前缀嵌入在示例中：dna_、dnacalib_和dna_viewer_。

## 示例DNA文件
提供了两个演示DNA文件，用于更轻松地测试此工具。任何使用[MetaHumanCreator](https://www.unrealengine.com/en-US/metahuman)生成的DNA都应该可以使用。

MHC 2023年春季发布引入了对骨骼定义的更改（关节数量增加以及表情数量增加）。
为了适应这些更改，我们在存储库中的`/data/mh4`文件夹中添加了几个文件：新的[GUI场景](/data/mh4/gui.ma)、更新的[组装脚本](/data/mh4/additional_assemble_script.py)以及Ada的示例[DNA文件](data/mh4/dna_files/Ada.dna)。
如果用户想要切换并使用这个新的骨骼版本，则需要在其脚本中更新路径：
```python
GUI = f"{DATA_DIR}/mh4/gui.ma"
ADDITIONAL_ASSEMBLE_SCRIPT = f"{DATA_DIR}/mh4/additional_assemble_script.py"
```

如果从[Quixel Bridge](https://quixel.com/bridge)下载角色DNA并且我们不确定使用哪个骨骼定义，可以使用以下代码进行检查：
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
        raise RuntimeError(f"加载DNA时出错: {status.message}")
    return reader

character_dna = "path_to/character.dna"
reader = load_dna_reader(character_dna)
if reader.getDBName() == "MH.4":
  print("使用mh4文件夹")
elif reader.getDBName() == "DHI":
  print("使用data文件夹")
else:
  print("不支持的骨骼定义！")
```Maya 2022，`ROOT_DIR` 的值应该被更改为绝对路径，例如在 Windows 中使用 `c:/MetaHuman-DNA-Calibration` 或在 Linux 中使用 `/home/user/MetaHuman-DNA-Calibration`。重要提示：使用 `/`（正斜杠），Maya 在路径中使用正斜杠。

请查看[常见问题解答指南](docs/faq.md)获取额外的规范信息。

# 许可证
MetaHuman DNA Calibration 是根据[许可证](LICENSE)发布的。
