# DNAViewer
[`dna_viewer`](/dna_viewer)包含从DNA文件中读取并在Maya中创建功能性骨骼所需的所有类。
它以一种允许每个选项可配置的方式进行组织，因此您可以轻松地获得您想要的确切结果。

## 示例
- [生成骨骼](/examples/dna_viewer_build_rig.py)
- [每个LOD导出FBX](/examples/dna_viewer_export_fbx.py)
- [从Maya场景传播更改到DNA](/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py)
- [简单UI](/examples/dna_viewer_run_in_maya.py)


## 代码中的用法
有两个[APIs](dna_viewer_api.md):
  - [build_meshes](dna_viewer_api_build_meshes.md)
  - [build_rig](dna_viewer_api_build_rig.md)

## 在Maya中的用法
Maya中的用法在[这里](/docs/dna_viewer_maya.md)


## 文件夹结构

- [builder](/dna_viewer/builder) - 包含用于轻松添加配置选项和构建场景、配置、网格等的构建类。
- [dnalib](/dna_viewer/dnalib) - 包含用于更好地访问DNA文件的类。
- [ui](/dna_viewer/ui) - 包含用于Maya UI所需的类。

## 工作原理

一般流程如下：

![image](img/flow_general.png)

场景构建过程的流程如下：

![image](img/flow_scene_build.png)

骨骼构建过程的流程如下：

![image](img/flow_character_build.png)

图例：
- <span style="color:blue">蓝色：与构建相关</span>。
- <span style="color:green">绿色：与配置相关</span>。
- <span style="color:brown">棕色：与模型相关</span>。
- <span style="color:purple">紫色：与读取相关</span>。
