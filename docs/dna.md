## DNA 库

DNA 库作为DNACalib的一个依赖项捆绑在此代码库中。它提供了读取和写入MetaHuman DNA文件的核心功能，可以让用户查询和更改其中包含的信息。

DNACalib提供了一套用于编辑MetaHuman DNA文件的有用命令。在底层，它利用了DNA库。一些命令只是封装了对DNA库的调用，而其他命令则包含了额外的逻辑。虽然用户也可以纯粹使用DNA库来做到这一切，这些命令旨在让他们的操作更轻松。

## MetaHuman DNA

MetaHuman DNA是一种文件格式，旨在存储3D对象的完整绑定和几何描述。仅依靠MetaHuman DNA文件，就可以重建对象的完整网格，并使其完全绑定，准备好进行动画处理。实际上，MetaHuman DNA文件主要用于存储人类角色的面部。

### 层

MetaHuman DNA文件中的数据被分成几个逻辑层。层之间形成一个松散的层级结构，MetaHuman DNA文件中的每个后续层依赖于其上方层中存储的数据。

![MetaHuman DNA Layers](img/layers.svg "MetaHuman DNA Layers")

可以选择性地加载MetaHuman DNA直至指定层。如图中所示的层组织，行为层和几何层彼此不依赖。这种独立性对于只需要MetaHuman DNA文件来驱动绑定（使用行为层进行运行时评估），而无需访问几何数据的使用场景至关重要。

#### 描述符

描述符层包含了有关绑定的基本元数据，例如：

- 角色名称
- 年龄
- 面部原型
- 任意字符串元数据，以键/值对的形式
- 根据需要提供的兼容性参数（与更高层次系统相关，例如用于混合MetaHuman DNA文件）

#### 定义

定义层包含绑定的静态数据，例如：

- 控件、关节、混合形状、动画地图和网格的名称
- 把关节、混合形状、动画地图和网格映射到单个LOD
- 关节层级
- 绑定姿势（如T型姿势）中的关节变换

此层包含基于选择的LOD对后续层进行过滤所需的信息。

#### 行为

行为层包含绑定的动态数据，用于：

- 将GUI控件映射到原始控件值
- 计算校正表达式
- 计算关节变换
- 计算混合形状通道权重
- 计算动画地图权重

#### 几何

几何层包含重建角色网格所需的所有数据，以及其皮肤权重和混合形状目标增量。网格信息本身的结构类似于OBJ格式。

### API概览

在处理MetaHuman DNA文件时，主要使用两个接口：
- [`BinaryStreamReader`](/dnacalib/DNACalib/include/dna/BinaryStreamReader.h)
- [`BinaryStreamWriter`](/dnacalib/DNACalib/include/dna/BinaryStreamWriter.h)

它们用于从二进制流中读取数据或将数据写入二进制流。例如，当处理文件时，会使用[`FileStream`](/dnacalib/DNACalib/include/trio/streams/FileStream.h)。

在此，我们将展示一些库的基本用法代码片段。有关DNA库的一般API概览，请参见[这里](/docs/dna_api.md)。

与DNACalib类似，DNA库是用C++编写的，但它有一个Python包装器，因此可以从C++和Python中使用。

#### 创建阅读器/写入器

##### 阅读器

一个从文件中读取二进制DNA的函数示例：

```python
def load_dna(path):
    stream = FileStream(path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
    reader = BinaryStreamReader(stream, DataLayer_All)
    reader.read()
    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error loading DNA: {status.message}")
    return reader
```

在创建阅读器时，除了流参数，还可以指定要加载的数据层。在此示例中，将加载所有层，因为使用了```DataLayer_All```，但你可以指定以下任何一项：

```python
DataLayer_Descriptor
DataLayer_Definition - 包含描述符和定义
DataLayer_Behavior - 包含描述符、定义和行为
DataLayer_Geometry - 包含描述符、定义和几何
DataLayer_GeometryWithoutBlendShapes - 包含描述符、定义和没有混合形状的几何
DataLayer_AllWithoutBlendShapes - 包含除几何中混合形状之外的所有内容
DataLayer_All
```

例如，如果你只想加载行为层（包括定义和描述符），使用：

```python
stream = FileStream(path, FileStream.AccessMode_Read, FileStream.OpenMode_Binary)
reader = BinaryStreamReader(stream, DataLayer_Behavior)
reader.read()
if not Status.isOk():
    status = Status.get()
    raise RuntimeError(f"Error loading DNA: {status.message}")
```

##### 写入器

一个从文件中写入二进制DNA的函数示例：

```python
def save_dna(reader, path):
    stream = FileStream(path, FileStream.AccessMode_Write, FileStream.OpenMode_Binary)
    writer = BinaryStreamWriter(stream)
    # 使用所有数据层基于reader创建一个writer（如果没有参数传递给setFrom()，DataLayer_All是默认值）
    writer.setFrom(reader)
    # 例如，要创建只有几何层（包括定义和描述符）的writer，使用：
    # writer.setFrom(reader, DataLayer_Geometry)

    writer.write()

    if not Status.isOk():
        status = Status.get()
        raise RuntimeError(f"Error saving DNA: {status.message}")
```

除了在创建阅读器时指定层外，也可以在创建写入器时指定要使用的层（作为`setFrom()`方法的参数）。

```load_dna```和```save_dna```函数在大多数[`示例`](/examples/)中使用。

**注意**：还有[`JSONStreamReader`](/dnacalib/DNACalib/include/dna/JSONStreamReader.h)和[`JSONStreamWriter`](/dnacalib/DNACalib/include/dna/JSONStreamWriter.h)，用于当MetaHuman DNA文件以JSON格式而不是二进制格式编写时使用。然而应注意，JSON变体仅打算用作例如调试工具。与二进制阅读器和写入器不同，它们的JSON对等体无法执行过滤，且通常产生的文件要大得多。
存储DNA文件的推荐格式是二进制。

**已知问题**：当前读取JSON MetaHuman DNA文件会失败。这个问题将在未来的版本中解决。

#### 示例

以下是一些使用该库的示例代码片段。

##### 示例1：读取指定网格的中性顶点位置

```python
dna = load_dna(input_path)

if dna.getMeshCount() == 0:
    print("No meshes found in DNA.")
    return

mesh_index = 0
xs = dna.getVertexPositionXs(mesh_index)
ys = dna.getVertexPositionYs(mesh_index)
zs = dna.getVertexPositionZs(mesh_index)
```

##### 示例2：读取中性关节坐标和关节朝向值

```python
dna = load_dna(input_path)

# 读取关节坐标
neutral_joint_translation_xs = dna.getNeutralJointTranslationXs()
neutral_joint_translation_ys = dna.getNeutralJointTranslationYs()
neutral_joint_translation_zs = dna.getNeutralJointTranslationZs()

# 读取关节方向
neutral_joint_orient_xs = dna.getNeutralJointRotationXs()
neutral_joint_orient_ys = dna.getNeutralJointRotationYs()
neutral_joint_orient_zs = dna.getNeutralJointRotationZs()
```

##### 示例3：读取表达式的混合形状目标增量并更改它们

```python
def read_blend_shape_target_deltas(reader, mesh_index, blend_shape_target_index):
    """
    读取混合形状目标增量和对应的顶点索引。
    """

    vertex_indices = reader.getBlendShapeTargetVertexIndices(
        mesh_index, blend_shape_target_index
    )
    blend_shape_target_delta_count = reader.getBlendShapeTargetDeltaCount(
        mesh_index, blend_shape_target_index
    )
    deltas = []
    for delta_index in range(blend_shape_target_delta_count):
        x, y, z = reader.getBlendShapeTargetDelta(
            mesh_index, blend_shape_target_index, delta_index
        )
        deltas.append([x, y, z])
    return vertex_indices, deltas

# 读取并更改表达式"jaw_open"，网格"head_lod0_mesh"的混合形状目标增量
input_dna = load_dna(input_path)

mesh_name = "head_lod0_mesh"
mesh_count = input_dna.getMeshCount()
head_mesh_index = 0
for mesh_index in range(mesh_count):
    if input_dna.getMeshName(mesh_index) == mesh_name:
        head_mesh_index = mesh_index
        break

bs_target_count = input_dna.getBlendShapeTargetCount(head_mesh_index)
expr_name = "jaw_open"

# 获取指定表达式的混合形状目标索引
for i in range(bs_target_count):
    bs_channel_index = input_dna.getBlendShapeChannelIndex(head_mesh_index, i)
    bs_name = input_dna.getBlendShapeChannelName(bs_channel_index)
    if bs_name == expr_name:
        bs_target_index = i
        break

vertex_indices, deltas = read_blend_shape_target_deltas(input_dna, head_mesh_index, bs_target_index)

# 修改增量（在此示例中，仅为每个增量加1.0）
for i in range(len(deltas)):
    deltas[i][0] += 1.0
    deltas[i][1] += 1.0
    deltas[i][2] += 1.0

# 从输入DNA创建一个writer DNA
output_stream = dna.FileStream(outputPath, dna.FileStream.AccessMode_Write, dna.FileStream.OpenMode_Binary)

# 在此示例中，为了调试目的，以JSON格式写入DNA，以快速查看混合形状增量是否已更改
output_dna = dna.JSONStreamWriter(output_stream)
output_dna.setFrom(input_dna)

# 为表达式写入新的混合形状增量值
output_dna.setBlendShapeTargetDeltas(mesh_index, bs_target_index, deltas)

# 如果您以某种方式替换增量，例如移除或添加了部分，
# 那么您还需要设置与新增量对应的新顶点索引：
# output_dna.setBlendShapeTargetVertexIndices(mesh_index, bs_target_index, new_vertex_indices)

# 写入具有修改值的DNA
output_dna.write()

if not dna.Status.isOk():
    status = dna.Status.get()
    raise RuntimeError("Error saving DNA: {}".format(status.message))
```

### 用法

这些简短的[`示例`](/examples)涵盖了用户在处理MetaHuman DNA时可能遇到的一些情况。其中一些是：
- [`将MetaHuman DNA文件的内容写入JSON格式以供检查`](/examples/dna_binary_to_json_demo.py)
- [`从DNA中清除所有混合形状数据`](/examples/dnacalib_clear_blend_shapes.py)
- [`从DNA中移除某些LOD`](/examples/dnacalib_lod_demo.py)
