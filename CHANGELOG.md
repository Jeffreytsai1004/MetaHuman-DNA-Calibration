# 更改日志

此项目的所有重要更改将记录在此文件中。该项目遵循[语义化版本](http://semver.org/)。


## [1.3.0] - 2024-08-15

### 新增
- 支持 Maya 2024
- 支持 Python 3.11
- 在Python包装器中添加源代码注释

### 修复
- 重写了 `CalculateMeshLowerLODsCommand` 以解决发现的睫毛边缘情况，并处理一些常见的无效UV数据情况。
- `RotateCommand` 现在也旋转混合形状目标增量。
- `SetBlendShapeTargetDeltasCommand` 现在允许设置顶点索引。
- Swig 生成的类现在被包装，而不是被猴子补丁，以调用构造函数和析构函数（这允许使用更新的 Swig 版本 - 4.0.x 和 4.1.x 进行构建）。

### 更改
- 修改了 CMake 文件以添加执行示例脚本的测试用例，并允许使用 CPack 生成捆绑归档。
- 嵌入式RL4插件的二进制文件为 .so 文件。


## [1.2.0] - 2023-06-30

### 新增
- 支持 MHC 2.x.x 版本（UE 5.2 和 5.3）的资产（gui.ma、Ada.dna、additional_assemble_script.py）


## [1.1.0] - 2023-04-20

### 新增
- 支持 Maya 2023
- 支持 Python 3.9
- `RenameAnimatedMapCommand` 类到 DNACalib API。用于删除动画贴图的命令。
- `RemoveBlendShapeCommand` 类到 DNACalib API。用于删除混合形状的命令。
- `DNA` 类到 DNAViewer API。此类用于访问 DNA 文件中的数据。
- `rig_build` 方法到 DNAViewer API。用于使用功能性骨骼创建 Maya 场景的方法。替换方法 `assemble_rig`。
- `Config` 类到 DNAViewer API。用于 `build_meshes` 的配置类。
- `RigConfig` 类到 DNAViewer API。用于 `rig_build` 的配置类。
- DNA库的文档。

### 修复
- `ClearBlendShapesCommand` 混合形状通道 LOD 设置不正确。
- `RotateCommand` 现在也旋转混合形状目标增量。
- `SetBlendShapeTargetDeltasCommand` 现在允许设置顶点索引。

### 更改
- 更改了 `build_meshes` 的签名。用于创建带有网格的 Maya 场景的方法。
- 简化了额外的组装脚本。
- 传递要在删除命令中移除的索引列表的选项。

### 删除
- 从 DNAViewer API 中删除了方法 `assemble_rig`。
