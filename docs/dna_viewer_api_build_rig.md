＃构建机器人（[`build_rig`](../dna_viewer/api.py#L9))

构建机器人API用于从给定的DNA文件路径在Maya场景中轻松组装字符机器人。

## 创建RigConfig实例（[`RigConfig`](../dna_viewer/builder/config.py#35))
创建一个将在网格构建过程中使用的配置对象。

```
from dna_viewer import RigConfig
```

这些只是`RigConfig`类的一些属性：
- `gui_path: str` - GUI文件路径。
- `analog_gui_path: str` - 模拟GUI文件路径。
- `aas_path: str` - 附加装配脚本路径。
- `aas_method: str` - 应该从附加组装脚本中调用的方法名称。
- `add_ctrl_attributes_on_root_joint: bool` - 一个代表是否应该在根关节上添加属性的标志，默认为`True`。
- `add_key_frames: bool` - 一个代表是否应该添加关键帧的标志，默认为`True`。

## 示例

**重要**：在运行此示例之前需要执行上面提供的[环境设置](dna_viewer_api.md#environment-setup)。

```
from dna_viewer import DNA, RigConfig, build_rig

# 如果您使用Maya，请使用绝对路径
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")

# 设置将使用的值
DNA_PATH_ADA = f"{ROOT_DIR}/data/dna_files/Ada.dna"
dna_ada = DNA(DNA_PATH_ADA)

config = RigConfig(
    gui_path=f"{ROOT_DIR}/data/gui.ma",
    analog_gui_path=f"{ROOT_DIR}/data/analog_gui.ma",
    aas_path=f"{ROOT_DIR}/data/additional_assemble_script.py",
)

# 创建机器人
build_rig(dna=dna_ada, config=config)
```
