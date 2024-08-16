# 环境设置

为了能够从dna_viewer导入，需要设置环境。这是通过将以下代码添加到下面提到的任何示例的开头来实现的：

```
from sys import path as syspath, platform
from os import environ, path as ospath

ROOT_DIR = fr"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/") # 如果您使用Maya，请改用绝对路径
ROOT_LIB_DIR = fr"{ROOT_DIR}/lib"
if platform == "win32":
    LIB_DIR = f"{ROOT_LIB_DIR}/windows"
elif platform == "linux":
    LIB_DIR = f"{ROOT_LIB_DIR}/linux"
else:
    raise OSError("不支持的操作系统，请编译依赖项并将值添加到LIB_DIR")

if "MAYA_PLUG_IN_PATH" in environ:
    separator = ":" if platform == "linux" else ";"
    environ["MAYA_PLUG_IN_PATH"] = separator.join([environ["MAYA_PLUG_IN_PATH"], LIB_DIR])    
else:
    environ["MAYA_PLUG_IN_PATH"] = LIB_DIR

syspath.append(ROOT_DIR)
syspath.append(LIB_DIR)
```

在从Maya运行时，`ROOT_DIR` 应设置为存储库根目录的绝对路径。

# DNA

## 加载DNA

加载DNA并返回一个[`DNA`](../dna_viewer/dnalib/dnalib.py#L13) 对象。

```
from dna_viewer import DNA

dna_ada = DNA(DNA_PATH_ADA)
dna_taro = DNA(DNA_PATH_TARO)
```

这使用以下参数：
- `dna_path: str` - 应使用的DNA文件的路径。
- `layers: Optional[List[Layer]]` - 要加载的DNA部分列表。如果未传递任何内容，则将加载整个DNA。与传递 Layer.all 相同。

## 构建网格

构建网格的API解释位于[这里](/docs/dna_viewer_api_build_meshes.md)。

## 构建Rig

构建Rig的API解释位于[这里](/docs/dna_viewer_api_build_rig.md)。
