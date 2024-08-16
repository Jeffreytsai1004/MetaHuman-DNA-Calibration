# API概览
DNA修改是通过可用命令完成的。每个命令实现`run(DNACalibDNAReader* output)`方法，该方法通过其参数修改指定的DNA。要配置在`run()`中发生的修改，可以通过构造函数或特定的setter方法传递参数。
以下文档适用于C++。目前没有Python文档。

所有可用命令列表：

## 删除DNA的特定部分的命令：

- [`RemoveJointAnimationCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RemoveJointAnimationCommand.h) 从DNA中删除具有给定索引的关节动画。

- [`RemoveJointCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RemoveJointCommand.h) 从DNA中删除具有给定索引的关节。

- [`RemoveMeshCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RemoveMeshCommand.h) 从DNA中删除具有给定索引的网格。

- [`ClearBlendShapesCommand`](/dnacalib/DNACalib/include/dnacalib/commands/ClearBlendShapesCommand.h) 从DNA中清除所有混合形状数据。

## 重命名DNA的特定部分的命令：

- [`RenameAnimatedMapCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RenameAnimatedMapCommand.h) 重命名具有给定索引或先前名称的动画映射。

- [`RenameBlendShapeCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RenameBlendShapeCommand.h) 重命名具有给定索引或先前名称的混合形状。

- [`RenameJointCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RenameJointCommand.h) 重命名具有给定索引或先前名称的关节。

- [`RenameMeshCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RenameMeshCommand.h) 重命名具有给定索引或先前名称的网格。

## 转换DNA的命令：

- [`RotateCommand`](/dnacalib/DNACalib/include/dnacalib/commands/RotateCommand.h) 围绕给定原点旋转中性关节和顶点位置。

- [`ScaleCommand`](/dnacalib/DNACalib/include/dnacalib/commands/ScaleCommand.h) 通过因子缩放中性关节、顶点位置和关节和混合形状增量。对于中性关节和关节增量，仅缩放平移属性。

- [`TranslateCommand`](/dnacalib/DNACalib/include/dnacalib/commands/TranslateCommand.h) 将中性关节和顶点位置平移。

## 修改混合形状的命令：

- [`SetBlendShapeTargetDeltasCommand`](/dnacalib/DNACalib/include/dnacalib/commands/SetBlendShapeTargetDeltasCommand.h) 更改混合形状目标增量。

- [`PruneBlendShapeTargetsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/PruneBlendShapeTargetsCommand.h) 修剪低于或等于指定阈值的混合形状目标增量。

## 更改绑定姿势的命令：

- [`SetNeutralJointRotationsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/SetNeutralJointRotationsCommand.h) 为中性关节设置新的旋转值。

- [`SetNeutralJointTranslationsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/SetNeutralJointTranslationsCommand.h) 为中性关节设置新的平移值。

- [`SetVertexPositionsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/SetVertexPositionsCommand.h) 更改顶点位置的值。

## 执行有用计算或提供附加功能的命令：

- [`SetLODsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/SetLODsCommand.h) 过滤DNA，使其仅包含指定LOD的数据。

- [`CalculateMeshLowerLODsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/CalculateMeshLowerLODsCommand.h) 重新计算指定网格的较低LOD网格的顶点位置。

- [`CommandSequence`](/dnacalib/DNACalib/include/dnacalib/commands/CommandSequence.h) 在指定的DNA上运行一系列命令。


可以在[`DNACalib/include/dnacalib/commands`](/dnacalib/DNACalib/include/dnacalib/commands)中找到每个可用命令及其方法的更详细描述。
