# 网格实用工具

以下方法的目的是提供：
- 从给定的 DNA 文件路径构建网格的简单机制
- 返回并打印关于 DNA 文件中包含的网格的信息

## 导入

```
from dna_viewer import DNA, Config, build_meshes
```

```
DNA_PATH_ADA = f"{ROOT_DIR}/data/dna_files/Ada.dna"
DNA_PATH_TARO = f"{ROOT_DIR}/data/dna_files/Taro.dna"
```

## 创建配置实例([`Config`](../dna_viewer/builder/config.py#35))
创建一个配置对象，将在网格构建过程中使用。

```
config = Config(
    add_joints=True,
    add_blend_shapes=True,
    add_skin_cluster=True,
    add_ctrl_attributes_on_root_joint=True,
    add_animated_map_attributes_on_root_joint=True,
    lod_filter=[0, 1],
    mesh_filter=["head"],
)
```

这些只是 `Config` 类的一些属性：
- `add_joints: bool` - 一个表示是否应添加关节的标志，默认为 `True`。
- `add_blend_shapes: bool` - 一个表示是否应添加混合形状的标志，默认为 `True`。
- `add_skin_cluster: bool` - 一个表示是否应添加皮肤集群的标志，默认为 `True`。
- `add_ctrl_attributes_on_root_joint: bool` - 一个表示是否应将控制属性作为属性添加到根关节中， 默认为 `False`。它们在引擎中用作 Rig Logic 输入的动画曲线。
- `add_animated_map_attributes_on_root_joint: bool` - 一个表示是否应将动画地图属性作为属性添加到根关节中， 默认为 `True`。它们在引擎中用作动画地图的动画曲线。

**重要**: 某些标志值的组合可能导致无法使用的 rig 或禁用某些功能！



## 构建网格 ([`build_meshes`](../dna_viewer/api.py#L26))

用于构建不带 Rig Logic 的 rig 元素（关节、网格、混合形状和皮肤集群）。
它返回已添加到场景中的网格的长名称。

```
config = Config(
    add_joints=True,
    add_blend_shapes=True,
    add_skin_cluster=True,
    add_ctrl_attributes_on_root_joint=True,
    add_animated_map_attributes_on_root_joint=True,
    lod_filter=[0, 1],
    mesh_filter=["head"],
)
mesh_names = build_meshes(
    dna=dna_ada,
    config=config
)
```


这使用以下参数：
- `dna: DNA` - 通过 `DNA` 获取的 DNA 实例。
- `config: Config` - 配置实例。

```
mesh_names = build_meshes(dna=dna_ada)
```

它默认添加 DNA 文件中的所有网格。



### 示例

**重要**: 需要先执行上面提供的[环境设置](dna_viewer_api.md#environment-setup)，然后再运行此示例。

```
from dna_viewer import DNA, Config, build_meshes

# 如果使用 Maya，请使用绝对路径
ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\", "/")
# 设置 DNA 文件路径
DNA_PATH_ADA = f"{ROOT_DIR}/data/dna_files/Ada.dna"
dna_ada = DNA(DNA_PATH_ADA)

# 开始使用默认值启动网格构建过程
build_meshes(dna=dna_ada)

# 创建要传递给 `build_meshes` 的选项
config = Config(
    add_joints=True,
    add_blend_shapes=True,
    add_skin_cluster=True,
    add_ctrl_attributes_on_root_joint=True,
    add_animated_map_attributes_on_root_joint=True,
    lod_filter=[0, 1],
    mesh_filter=["head"],
)

# 使用提供的参数开始网格构建过程
# 在本例中，将创建包含在 LODs 0 和 1 中，名称中包含 'head' 的每个网格，
build_meshes(
    dna=dna_ada,
    config=config,
)
```
