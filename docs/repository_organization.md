# 存储库组织

该存储库包含两个独立的组件：
1. **dnacalib C++ 库** - 用于操作 DNA 文件
2. **dna_viewer python 代码** - 用于在 Autodesk Maya 中可视化 DNA

# 文件夹结构

- [dnacalib](/dnacalib) - DNACalib 源代码
- [dna_viewer](/dna_viewer) - dna_viewer 的源代码
- [examples](/examples) - 几个 Python 脚本，展示 dna_viewer 的基本用法以及对 DNACalib 的 Python 封装
- [lib](/lib) - DNACalib、PyDNACalib 和 PyDNA 的预编译二进制文件
- [data](/data) - 必要的 DNA 和 Maya 场景
- [docs](/docs) - 文档


## DNACalib
文档位于[此处](dnacalib.md)

## DNAViewer
文档位于[此处](dna_viewer.md)

## 示例
要运行[DNAViewer 示例](/docs/dna_viewer.md#examples)，您必须安装 Maya 2022。
要运行[DNACalib 示例](/docs/dnacalib.md#python)，您需要 Python3。

## Lib

[Lib 文件夹](/lib) 包含 Windows 和 Linux 的 DNACalib 库的预编译二进制文件。此外，还提供了一个用于 RL4 的 Maya 插件。

### Linux 位置
您需要复制或创建所有 **.so** 文件的符号链接在 [lib](lib/Maya2022/linux) 中：

```shell
sudo ln -s ~/MetaHuman-DNA-Calibration/lib/Maya2022/linux/_py3dna.so /usr/lib/_py3dna.so

sudo ln -s ~/MetaHuman-DNA-Calibration/lib/Maya2022/linux/libdnacalib.so /usr/lib/libdnacalib.so

sudo ln -s ~/MetaHuman-DNA-Calibration/lib/Maya2022/linux/libdnacalib.so.6 /usr/lib/libdnacalib.so.6

sudo ln -s ~/MetaHuman-DNA-Calibration/lib/Maya2022/linux/libembeddedRL4.so /usr/lib/embeddedRL4.mll

sudo ln -s ~/MetaHuman-DNA-Calibration/lib/Maya2022/linux/MayaUERBFPlugin.mll /usr/lib/MayaUERBFPlugin.mll
```

注意：将路径 `~/MetaHuman-DNA-Calibration` 更改为 `MetaHuman-DNA-Calibration` 所在的位置。

## 数据

[`data 文件夹`](/data) 包含示例 DNA 文件。我们提供了两个 MetaHuman DNA 文件（Ada 和 Taro，我们的第一个预设）。

| Ada | Taro |
|---|---|
|![image](img/metahuman_008.png)| ![image](img/metahuman_010.png) |

此外，我们还添加了[`gui`](/data/gui.ma) 和[`analog_gui`](/data/analog_gui.ma) Maya 场景，这些场景在 Maya 场景组装过程中使用。
此外，[`additional_assemble_script.py`](/data/additional_assemble_script.py) 用于组织场景中的对象并连接控件。理想的设置如下所示：

![image](img/aas.png)

2023 年春季发布的 MHC 引入了刚性定义的更改（关节数量增加以及表达式数量增加）。
为了适应这些变化，我们在存储库的 `/data/mh4` 文件夹中添加了几个文件：新的[ gui 场景](/data/mh4/gui.ma)、更新的[ 组装脚本](/data/mh4/additional_assemble_script.py) 以及 Ada 的[ DNA 文件](data/mh4/dna_files/Ada.dna) 的示例。
此外，在 lib 文件夹中，我们添加了用于控制颈部表达式的 Maya RBF 插件。颈部设置最近已经得到改进，并且通过添加 RBF 插件以及使用它的新 gui 场景，我们获得了更好的颈部变形。
