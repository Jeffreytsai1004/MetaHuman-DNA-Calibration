# 常见问题（FAQ）

## 如何修复“RuntimeError: Error loading DNA: DNA signature mismatched, expected DNA, got ver?”

为了解决这个问题，您应该安装[git-lfs](https://git-lfs.github.com/)，然后重新克隆存储库。这样DNA文件就会正确下载。如果您无法安装git-lfs，您可以手动下载DNA文件。


## 我如何分发Maya场景？

如果您在分发中包含以下内容，您的场景应该可以直接使用：
- 场景文件（`.mb`文件）
- DNA（`.dna`文件）
- 工作空间（`workspace.mel`文件）

所有这些文件都需要一起分发。如果这些文件没有捆绑在一起，而您在Maya中遇到一些问题，请尝试以下步骤：

### 如何分享生成的文件？
如果您想将生成的Maya场景分发给其他用户，您必须将`.dna`文件和`workspace.mel`与场景一起分发。

### 如何打开生成的场景？
在加载生成的场景之前，请按照以下步骤操作：
- 从主菜单中，转到 文件 > 设置项目。
- 选择 `workspace.mel`
- 设置包含文件夹（包含生成的Maya场景、`.dna`文件和`workspace.mel`）。

### 如何更改Maya场景中的DNA路径？
如果您想在场景中更改DNA路径：
- 在`outliner`中，取消选择**仅DAG对象**：
  - ![image](img/change_path_outliner_settings.png)
- 仍然在Outliner中，搜索`rl4`。您会看到一个文件，文件名以`rl4Embedded_`开头。单击此文件以选择它。
  - ![image](img/change_path_outliner.png)
- 在`属性编辑器`中，您可以使用`Dna File Path`更改路径：
  - ![image](img/change_path_node_path.png)
