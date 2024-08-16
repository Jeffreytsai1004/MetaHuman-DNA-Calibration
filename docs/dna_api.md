# DNA API概览

这里是用于读取和写入DNA文件的主要方法概述。  
以下文档适用于C++。目前没有Python文档。  

如[此处](/docs/dna.md#api-overview)所述，有用于从流中读取DNA或向其写入的类。它们是：  
- [BinaryStreamReader](/dnacalib/DNACalib/include/dna/BinaryStreamReader.h)
- [BinaryStreamWriter](/dnacalib/DNACalib/include/dna/BinaryStreamWriter.h)
- [JSONStreamReader](/dnacalib/DNACalib/include/dna/JSONStreamReader.h)
- [JSONStreamWriter](/dnacalib/DNACalib/include/dna/JSONStreamWriter.h)

创建阅读器后，可以用它来查询DNA中包含的不同信息。  
创建编写器后，可以用它来在DNA中设置新值。  

这是通过此页面上列出的方法完成的。它们根据DNA文件中的[层](/docs/dna.md#layers)进行分组。  

**注意**：此页面上未列出所有可用方法。有关此处列出的方法的更多详细信息以及所有可用方法的列表，请参考适当的阅读器和/或编写器[此处](/dnacalib/DNACalib/include/dna/layers)。

## BinaryStreamReader
包含用于创建和销毁[BinaryStreamReader](/dnacalib/DNACalib/include/dna/BinaryStreamReader.h)的方法。  
创建BinaryStreamReader时，用户可以通过指定要加载的LOD来过滤DNA文件中的数据。正如[此处](/docs/dna.md#reader)所解释的，还可以通过指定要加载的数据层来进行过滤。  

- `create(stream, layer = DataLayer::All, maxLOD = 0u, memRes = nullptr)`  
    用于创建BinaryStreamReader的工厂方法。  
    参数：  
        `stream` - 要从中读取数据的源流。  
        `layer` - 指定需要加载数据的层。  
        `maxLOD` - 要加载的最大细节级别。值为零表示加载所有LOD。  
        `memRes` - 用于分配的内存资源。如果未提供内存资源，则将使用默认分配机制。用户负责通过调用destroy释放返回的指针。

- `create(stream, layer, maxLOD, minLOD, memRes = nullptr)`  
    用于创建BinaryStreamReader的工厂方法。  
    参数：  
        `stream` - 要从中读取数据的源流。  
        `layer` - 指定需要加载数据的层。  
        `maxLOD` - 要加载的最大细节级别。  
        `minLOD` - 要加载的最小细节级别。对于maxLOD / minLOD，范围为[0，LOD计数-1]分别表示加载所有LOD。  
        `memRes` - 用于分配的内存资源。如果未提供内存资源，则将使用默认分配机制。用户负责通过调用destroy释放返回的指针。

- `create(stream, layer, lods, lodCount, memRes = nullptr)`  
    用于创建BinaryStreamReader的工厂方法。  
    参数：  
        `stream` - 要从中读取数据的源流。  
        `layer` - 指定需要加载数据的层。  
        `lods` - 指定要加载的确切LOD的数组。  
        `lodCount` - lods数组中的元素数。  
        `memRes` - 用于分配的内存资源。如果未提供内存资源，则将使用默认分配机制。用户负责通过调用destroy释放返回的指针。

- `destroy(instance)`  
    释放BinaryStreamReader实例的方法。  
    参数：  
       `instance` - 要释放的BinaryStreamReader实例。

## BinaryStreamWriter
- `create(stream, memRes = nullptr)`  
    用于创建BinaryStreamWriter的工厂方法。  
    参数：  
        `stream` - 要写入数据的流。
        `memRes` - 用于分配的内存资源。如果未提供内存资源，则将使用默认分配机制。用户负责通过调用destroy释放返回的指针。

- `destroy(BinaryStreamWriter* instance)`  
    释放BinaryStreamWriter实例的方法。  
    参数：  
        `instance` - 要释放的BinaryStreamWriter实例。

## JSONStreamReader
- `create(stream, memRes = nullptr)`  
    用于创建JSONStreamReader的工厂方法。  
        参数：  
            `stream` - 从中读取数据的源流。  
            `memRes` - 用于分配的内存资源。如果没有提供内存资源，则将使用默认的分配机制。用户负责通过调用 destroy 释放返回的指针。  

- `destroy(instance)`  
    用于释放 JSONStreamReader 实例的方法。  
        参数：  
            `instance` - 要释放的 JSONStreamReader 实例。  

## JSONStreamWriter
- `create(stream, indentWidth = 4u, memRes = nullptr)`  
    用于创建 JSONStreamWriter 的工厂方法。  
    参数：  
        `stream` - 要写入数据的流。  
        `indentWidth` - 用于缩进的空格数。  
        `memRes` - 用于分配的内存资源。如果没有提供内存资源，则将使用默认的分配机制。用户负责通过调用 destroy 释放返回的指针。  

- `destroy(instance)`  
    用于释放 JSONStreamWriter 实例的方法。  
    参数：  
        `instance` - 要释放的 JSONStreamWriter 实例。  

## setFrom() 方法
除了用于创建 writer 的方法之外，BinaryStreamReader 和 JSONStreamReader 还具有一个 setFrom() 方法，继承自[Writer](/dnacalib/DNACalib/include/dna/Writer.h)，用于使用读取器中的数据初始化写入器。  
使用此方法，用于初始化写入器的数据可以通过数据层进行过滤。  
- `setFrom(source, layer = DataLayer::All, memRes = nullptr)`  
    从给定的 Reader 初始化 Writer。  
    此函数通过调用 Reader 的每个 getter 函数，并将返回值传递给 Writer 中匹配的 setter 函数，将给定 Reader 中的所有数据复制到 Writer 实例中。  
    参数：  
        `source` - 需要复制数据的源 DNA Reader。  
        `layer` - 指定应从给定源读取器中接管哪些层。  
        `memRes` - 用于在复制过程中临时分配的可选内存资源。  

## Reader 方法
### DescriptorReader
包含有关角色和机构的各种元数据的只读访问器。  

- `getName()`
    角色名称。
- `getArchetype()`
    角色原型。
- `getGender()`
    角色性别。
- `getAge()`
    角色年龄。
- `getTranslationUnit()`
    使用的翻译单位（厘米或米）。
- `getRotationUnit()`
    使用的旋转单位（度或弧度）。
- `getCoordinateSystem()`
    使用的坐标系（x、y 和 z 轴的方向）。
- `getLODCount()`
    可用的细节级别（例如 6 表示可用以下级别：[0,1,2,3,4,5]，其中 0 是具有最高细节的 LOD，5 是具有最低细节的 LOD）。
- `getDBMaxLOD()`
    存储在此角色的 DNA 数据中的最大细节级别。该值相对于数据库中的 LOD-0。
- `getDBComplexity()`
    用于驱动此角色机构的输入控制界面的名称。此参数表示角色的输入控制复杂性。
- `getDBName()`
    该角色所属数据库的名称。来自同一数据库的所有角色必须具有相同的 Definition，但可以具有不同的复杂性或 LOD。

### DefinitionReader
包含用于表示机构静态数据的 DNA 属性的只读访问器。  

- `getGUIControlCount()`
    GUI 控件数量。
- `getGUIControlName(index)`
    请求的 GUI 控件名称。
- `getRawControlCount()`
    原始控件数量。
- `getRawControlName(index)`
    请求的原始控件名称。
- `getJointCount()`
    关节数量。
- `getJointName(index)`
    请求的关节名称。
- `getJointIndicesForLOD(lod)`
    指定 LOD 的关节索引列表。
- `getJointParentIndex(index)`
    请求的关节的父级索引。  
    可以使用此函数遍历和重建关节层次结构。示例：  
    关节名称：[A, B, C, D, E, F, G, H, I]  
    层次结构：[0, 0, 0, 1, 1, 4, 2, 6, 2]  
    描述以下层次结构：
    ```
    A
    ├── B
    │   ├── D
    │   └── E
    │       └── F
    └── C
        ├── G
        │   └── H
        └  ── 我
    ```
    请求关节5的父级索引（关节名称：F）将返回4（关节名称：E）。
    请求根关节的父级索引：0（关节名称：A）将返回相同的索引0。
- `getBlendShapeChannelCount()`
    混合形状通道数量。
- `getBlendShapeChannelName(index)`
    请求的混合形状通道的名称。
- `getBlendShapeChannelIndicesForLOD(lod)`
    指定LOD的混合形状通道索引列表。
- `getAnimatedMapCount()`
    动画地图数量。
- `getAnimatedMapName(index)`
    请求的动画地图的名称。
- `getAnimatedMapIndicesForLOD(lod)`
    指定LOD的动画地图索引列表。
- `getMeshCount()`
    网格数量。
- `getMeshName(index)`
    请求的网格的名称。
- `getMeshIndicesForLOD(lod)`
    指定LOD的网格索引列表。
- `getMeshBlendShapeChannelMappingCount()`
    网格-混合形状通道映射项数量。
- `getMeshBlendShapeChannelMapping(index)`
    包含指定映射索引的网格索引和关联的混合形状通道索引的结构。
- `getMeshBlendShapeChannelMappingIndicesForLOD(lod)`
    指定LOD的网格-混合形状通道映射索引列表。
- `getNeutralJointTranslation(index)`
    关节在绑定姿势中的平移（x，y，z）。
- `getNeutralJointTranslationXs()`
    绑定姿势中所有关节的所有平移X值列表。
- `getNeutralJointTranslationYs()`
    绑定姿势中所有关节的所有平移Y值列表。
- `getNeutralJointTranslationZs()`
    绑定姿势中所有关节的所有平移Z值列表。
- `getNeutralJointRotation(index)`
    关节在绑定姿势中的旋转（x，y，z）。
- `getNeutralJointRotationXs()`
    绑定姿势中所有关节的所有旋转X值列表。
- `getNeutralJointRotationYs()`
    绑定姿势中所有关节的所有旋转Y值列表。
- `getNeutralJointRotationZs()`
    绑定姿势中所有关节的所有旋转Z值列表。

### BehaviorReader
包含用于定义角色评估的DNA属性的只读访问器。

- `getGUIToRawInputIndices()`
    用于将GUI映射到原始控件的输入索引。
- `getGUIToRawOutputIndices()`
    用于将GUI映射到原始控件的输出索引。
- `getGUIToRawFromValues()`
    用于在GUI到原始控件映射期间决定是否评估特定条目的过滤值（下界）。
- `getGUIToRawToValues()`
    用于在GUI到原始控件映射期间决定是否评估特定条目的过滤值（上界）。
- `getGUIToRawSlopeValues()`
    用于在GUI到原始控件映射期间计算输出值的计算值（斜率/梯度）。
- `getGUIToRawCutValues()`
    用于在GUI到原始控件映射期间计算输出值的计算值（垂直截距）。
- `getPSDCount()`
    不同PSD表达式的数量。
- `getPSDRowIndices()`
    PSD（输入）索引。
- `getPSDColumnIndices()`
    控件（输入）索引。
- `getPSDValues()`
    与每个PSD行和列对相关联的权重。
- `getJointRowCount()`
    整个未压缩关节矩阵中的行数。
- `getJointColumnCount()`
    整个未压缩关节矩阵中的列数。
- `getJointVariableAttributeIndices(lod)`
    请求的LOD的关节属性索引（输出索引）。
- `getJointGroupCount()`
    整个关节矩阵中存在的关节组数量。
- `getJointGroupLODs(jointGroupIndex)`
    请求的关节组每个细节级别的行数。
    每个元素的位置代表级别本身，值表示属于该级别的关节组中的行数。例如：
    ```
    [12, 9, 3]
     │   │  └── LOD-2 包含前3行
     │   └── LOD-1 包含前9行
     └── LOD-0 包含前12行
    ```
- `getJointGroupInputIndices(jointGroupIndex)`
    请求的关节组包含的列索引。列索引指向整个未压缩关节矩阵。
- `getJointGroupOutputIndices(jointGroupIndex)`
    请求的关节组包含的行索引。行索引指向整个未压缩关节矩阵。
- `获取`jointGroupIndex`的联合组值。
- `getJointGroupJointIndices(jointGroupIndex)`
    获取请求的联合组包含的关节索引。
- `getBlendShapeChannelLODs()`
    每个融合形状通道不同细节级别的输入索引数。 
    每个元素的位置代表级别本身（例如[0,1,2,3,4,5] 值0是最高细节级别的LOD，值5是最低细节级别的LOD），而该值表示属于该级别的输入索引数。
- `getBlendShapeChannelInputIndices()`
    用于索引输入向量的输入索引。
- `getBlendShapeChannelOutputIndices()`
    输出索引指定融合形状通道输出值的位置。
- `getAnimatedMapLODs()`
    每个动画贴图不同细节级别的行数。 
    每个元素的位置代表级别本身（例如[0,1,2,3,4,5] 值0是最高细节级别的LOD，值5是最低细节级别的LOD），而该值表示该级别所属的行数（在条件表内）。
- `getAnimatedMapInputIndices()`
    用于索引输入值数组的输入索引。
- `getAnimatedMapOutputIndices()`
    指定计算输出值位置的输出索引。
- `getAnimatedMapFromValues()`
    用于决定是否应评估特定条目的过滤值（下限）。
- `getAnimatedMapToValues()`
    用于决定是否应评估特定条目的过滤值（上限）。
- `getAnimatedMapSlopeValues()`
    用于计算输出值的计算值（斜率/梯度）。
- `getAnimatedMapCutValues()`
    用于计算输出值的计算值（垂直截距）。

### GeometryReader
包含对与骨骼关联的几何数据的只读访问器。

- `getVertexPositionCount(meshIndex)`
    整个网格中顶点位置的数量。
- `getVertexPosition(meshIndex, vertexIndex)`
    指定网格中指定顶点的位置。 顶点按顶点ID排序。
- `getVertexPositionXs(meshIndex)`
    用于参考网格的所有顶点位置X值的列表。
- `getVertexPositionYs(meshIndex)`
    用于参考网格的所有顶点位置Y值的列表。
- `getVertexPositionZs(meshIndex)`
    用于参考网格的所有顶点位置Z值的列表。
- `getVertexTextureCoordinateCount(meshIndex)`
    整个网格中纹理坐标的数量。
- `getVertexTextureCoordinate(meshIndex, textureCoordinateIndex)`
    指定网格中指定索引的纹理坐标。
- `getVertexTextureCoordinateUs(meshIndex)`
    用于参考网格的所有纹理坐标U值的列表。
- `getVertexTextureCoordinateVs(meshIndex)`
    用于参考网格的所有纹理坐标V值的列表。
- `getVertexNormalCount(meshIndex)`
    整个网格中顶点法线的数量。
- `getVertexNormal(meshIndex, normalIndex)`
    指定网格中指定索引的顶点法线。
- `getVertexNormalXs(meshIndex)`
    用于参考网格的所有法线X值的列表。
- `getVertexNormalYs(meshIndex)`
    用于参考网格的所有法线Y值的列表。
- `getVertexNormalZs(meshIndex)`
    用于参考网格的所有法线Z值的列表。
- `getVertexLayoutCount(meshIndex)`
    整个网格中顶点布局的数量。 顶点布局是顶点属性的集合。
- `getVertexLayout(meshIndex, layoutIndex)`
    顶点布局仅包含可用于查询与顶点关联的实际属性（如位置、纹理坐标和法线）的属性索引。 布局中的索引可与上面定义的API一起使用。
- `getVertexLayoutPositionIndices(meshIndex)`
    参考网格每个顶点的位置索引。
- `getVertexLayoutTextureCoordinateIndices(meshIndex)`
    参考网格每个顶点的纹理坐标索引。
- `getVertexLayoutNormalIndices(meshIndex)`
    参考网格每个顶点的法线索引。
- `getFaceCount(meshIndex)`
    属于指定网格的面数。
- `getFaceVertexLayoutIndices(meshIndex, faceIndex)`
    属于指定网格上面的顶点布局索引列表。
- `getMaximumInfluencePerVertex(meshIndex)`
    可影响任何单个顶点的最大关节数。
- `getSkinWeightsCount(meshIndex)`
    与指定网格关联的皮肤权重数。
- `getSkinWeightsValues(meshIndex, vertexIndex)`
    影响请求的顶点的皮肤权重列表。
- `getSkinWeightsJointIndices(meshIndex, vertexIndex)`
    关联的关节索引列表。为指定顶点的每个皮肤权重。关节索引按与它们关联的权重相同的顺序存储。
- `getBlendShapeTargetCount(meshIndex)`
    属于指定网格的变形目标数量。
- `getBlendShapeChannelIndex(meshIndex, blendShapeTargetIndex)`
    请求的变形目标的匹配变形通道索引。
- `getBlendShapeTargetDeltaCount(meshIndex, blendShapeTargetIndex)`
    属于指定变形的增量数量。
- `getBlendShapeTargetDelta(meshIndex, blendShapeTargetIndex, deltaIndex)`
    每个受影响顶点的增量列表。
- `getBlendShapeTargetDeltaXs(meshIndex, blendShapeTargetIndex)`
    引用的变形目标的所有增量X值列表。
- `getBlendShapeTargetDeltaYs(meshIndex, blendShapeTargetIndex)`
    引用的变形目标的所有增量Y值列表。
- `getBlendShapeTargetDeltaZs(meshIndex, blendShapeTargetIndex)`
    引用的变形目标的所有增量Z值列表。
- `getBlendShapeTargetVertexIndices(meshIndex, blendShapeTargetIndex)`
    受引用变形目标影响的顶点位置索引。顶点位置索引按与它们关联的增量相同的顺序存储。这些索引可用于通过getVertexPosition查询关联的顶点本身。

## 写入方法

### DescriptorWriter
包含对角色和骨骼的各种元数据的只写访问器。

- `setName(name)`
    设置角色名称。
- `setArchetype(archetype)`
    设置角色原型。
- `setGender(gender)`
    设置角色性别。
- `setAge(age)`
    设置角色年龄。
- `setTranslationUnit(unit)`
    设置平移单位（厘米或米）。
- `setRotationUnit(unit)`
    设置旋转单位（度或弧度）。
- `setCoordinateSystem(system)`
    设置坐标系统（轴的方向）。
- `setLODCount(lodCount)`
    设置可用的细节级别（例如6表示以下级别可用：[0,1,2,3,4,5]，其中0是具有最高细节的LOD，5是具有最低细节的LOD）。
- `setDBMaxLOD(lod)`
    设置存储在此角色的DNA数据中的最大细节级别。
- `setDBComplexity(name)`
    设置用于驱动此角色骨骼的输入控制界面的名称。
- `setDBName(name)`
    设置角色来源的数据库名称。

### DefinitionWriter
包含用于表示骨骼静态数据的DNA属性的只写访问器。
- `clearGUIControlNames()`
    删除所有存储的GUI控件名称。
- `setGUIControlName(index, name)`
    设置指定GUI控件的名称。
- `clearRawControlNames()`
    删除所有存储的原始控件名称。
- `setRawControlName(index, name)`
    设置指定原始控制的名称。
- `clearJointNames()`
    删除所有存储的关节名称。
- `setJointName(index, name)`
    设置指定关节的名称。
- `clearJointIndices()`
    删除所有存储的关节索引。
- `setJointIndices(index, jointIndices, count)`
    将关节索引列表存储到指定索引上。索引表示整个关节索引列表的位置，而不是它的单个元素的位置，即关节索引的2D矩阵中的行索引。
- `clearLODJointMappings()`
    删除所有存储的LOD到关节列表索引映射条目。
- `setLODJointMapping(lod, index)`
    设置哪些关节属于哪个细节级别。
- `clearBlendShapeChannelNames()`
    删除所有存储的变形通道名称。
- `setBlendShapeChannelName(index, name)`
    设置指定变形通道的名称。
- `clearBlendShapeChannelIndices()`
    删除所有存储的变形通道索引。
- `setBlendShapeChannelIndices(index, blendShapeChannelIndices, count)`
    将变形通道名称索引列表存储到指定索引上。索引表示整个变形通道索引列表的位置，而不是它的单个元素的位置，即变形通道索引的2D矩阵中的行索引。
- `clearLODBlendShapeChannelMappings()`
    删除所有存储的LOD到变形通道列表索引映射条目。
- `setLODBlendShapeChannelMapping(lod, index)`
    设置哪些变形通道属于哪个细节级别。
- `clearAnimatedMapNames()`
    删除所有存储的动画映射名称。
- `setAnimatedMapName(index, name)`
    设置指定动画映射的名称。
- `clearAnimatedMapIndices()`
    删除所有存储的动画映射索引。
- `setAnimatedMapIndices(index, animatedMap索引、计数）
    将动画地图名称索引列表存储到指定索引上。索引表示整个动画地图索引列表的位置，而不是其各个元素的位置，即在二维动画地图索引矩阵中的行索引。
- `clearLODAnimatedMapMappings()`
    删除所有存储的LOD到动画地图列表索引映射条目。
- `setLODAnimatedMapMapping(lod, index)`
    设置哪些动画地图属于哪个细节级别。
- `clearMeshNames()`
    删除所有存储的网格名称。
- `setMeshName(index, name)`
    设置指定网格的名称。
- `clearMeshIndices()`
    删除所有存储的网格索引。
- `setMeshIndices(index, meshIndices, count)`
    将网格名称索引列表存储到指定索引上。索引表示整个网格索引列表的位置，而不是其各个元素的位置，即在二维网格索引矩阵中的行索引。
- `clearLODMeshMappings()`
    删除所有存储的LOD到网格列表索引映射条目。
- `setLODMeshMapping(lod, index)`
    设置哪些网格属于哪个细节级别。
- `clearMeshBlendShapeChannelMappings()`
    删除所有存储的网格到混合形状通道映射条目。
- `setMeshBlendShapeChannelMapping(index, meshIndex, blendShapeChannelIndex)`
    将混合形状通道与其网格关联。
- `setJointHierarchy(jointIndices, count)`
    设置描述关节之间父子关系的简单数组。  
    例如：  
    关节名称：[A, B, C, D, E, F, G, H]  
    层次结构：[0, 0, 0, 1, 1, 4, 2, 2]  
    描述了以下层次结构：  
    ```
    A
    ├── B
    │   ├── D
    │   └── E
    │       └── F
    └── C
        ├── G
        └── H
    ```
- `setNeutralJointTranslations(translations, count)`
    设置绑定姿势中关节的平移。
- `setNeutralJointRotations(rotations, count)`
    设置绑定姿势中关节的旋转。

### BehaviorWriter
包含仅写访问器，用于定义机构评估的DNA属性。
- `setGUIToRawInputIndices(inputIndices, count)`
    设置用于将GUI映射到原始控件的输入索引。
- `setGUIToRawOutputIndices(outputIndices, count)`
    设置用于将GUI映射到原始控件的输出索引。
- `setGUIToRawFromValues(fromValues, count)`
    设置用于决定在GUI到原始控件映射期间是否应该评估特定条目的过滤值（下限）。
- `setGUIToRawToValues(toValues, count)`
    设置用于决定在GUI到原始控件映射期间是否应该评估特定条目的过滤值（上限）。
- `setGUIToRawSlopeValues(slopeValues, count)`
    设置用于在计算GUI到原始控件映射期间计算输出值的计算值（斜率/梯度）。
- `setGUIToRawCutValues(cutValues, count)`
    设置用于在计算GUI到原始控件映射期间计算输出值的计算值（垂直截距）。
- `setPSDCount(count)`
    设置不同PSD表达式的数量。
- `setPSDRowIndices(rowIndices, count)`
    设置将成为PSD矩阵行的PSD（输入）索引。
- `setPSDColumnIndices(columnIndices, count)`
    设置将成为PSD矩阵列的控制（输入）索引。
- `setPSDValues(weights, count)`
    设置与每个PSD行和列对相关联的权重。
- `setJointRowCount(rowCount)`
    设置整个未压缩关节矩阵中的行数。
- `setJointColumnCount(columnCount)`
    设置整个未压缩关节矩阵中的列数。
- `clearJointGroups()`
    删除所有关节组。
- `deleteJointGroup(jointGroupIndex)`
    删除指定的关节组。
- `setJointGroupLODs(jointGroupIndex, lods, count)`
    设置指定关节组每个细节级别的行数。  
    每个元素的位置代表级别本身，而值表示属于该级别的关节组内的行数。例如：  
    ```
    [12, 9, 3]
     │   │  └── LOD-2 包含前3行
     │   └── LOD-1 包含前9行
     └── LOD-0 包含前12行
    ```
- `setJointGroupInputIndices(jointGroupIndex, inputIndices, count)`
    设置列出指定联合组包含的列索引。列索引指向整个未压缩的联合矩阵。
- `setJointGroupOutputIndices(jointGroupIndex, outputIndices, count)`
    设置指定联合组包含的行索引。行索引指向整个未压缩的联合矩阵。
- `setJointGroupValues(jointGroupIndex, values, count)`
    设置指定联合组包含的值。
- `setJointGroupJointIndices(jointGroupIndex, jointIndices, count)`
    设置指定联合组包含的联合索引。
- `setBlendShapeChannelLODs(lods, count)`
    为混合形状设置每个细节级别的输入索引计数。  
    每个元素的位置表示级别本身（例如[0,1,2,3,4,5]值0是具有最高细节的LOD，值5是具有最低细节的LOD），而值表示属于该级别的输入索引数。
- `setBlendShapeChannelInputIndices(inputIndices, count)`
    设置用于索引输入向量的输入索引。
- `setBlendShapeChannelOutputIndices(outputIndices, count)`
    设置输出索引，指定混合形状输出值的位置。
- `setAnimatedMapLODs(lods, count)`
    为动画地图设置每个细节级别的行数。  
    每个元素的位置表示级别本身（例如[0,1,2,3,4,5]值0是具有最高细节的LOD，值5是具有最低细节的LOD），而值表示属于该级别的行数（在条件表中）。
- `setAnimatedMapInputIndices(inputIndices, count)`
    设置用于索引输入值数组的输入索引。
- `setAnimatedMapOutputIndices(outputIndices, count)`
    设置输出索引，指定计算输出值位置。
- `setAnimatedMapFromValues(fromValues, count)`
    设置用于决定是否评估特定条目的过滤值（下限）。
- `setAnimatedMapToValues(toValues, count)`
    设置用于决定是否评估特定条目的过滤值（上限）。
- `setAnimatedMapSlopeValues(slopeValues, count)`
    设置用于计算输出值的计算值（斜率/梯度）。
- `setAnimatedMapCutValues(cutValues, count)`
    设置用于计算输出值的计算值（垂直截距）。

### GeometryWriter
包含与一个姿势相关的几何数据的只写访问器。

- `clearMeshes()`
    删除所有网格。
- `deleteMesh(meshIndex)`
    删除指定的网格。
- `setVertexPositions(meshIndex, positions, count)`
    设置顶点位置。
- `setVertexTextureCoordinates(meshIndex, textureCoordinates, count)`
    设置顶点纹理坐标。
- `setVertexNormals(meshIndex, normals, count)`
    设置顶点法线。
- `setVertexLayouts(meshIndex, layouts, count)`
    设置属于指定网格的顶点布局。
- `clearFaceVertexLayoutIndices(meshIndex)`
    删除指定网格的所有顶点布局索引列表。
- `setFaceVertexLayoutIndices(meshIndex, faceIndex, layoutIndices, count)`
    设置属于指定面的顶点布局索引。布局索引指向通过setVertexLayouts()设置的数组。
- `setMaximumInfluencePerVertex(meshIndex, maxInfluenceCount)`
    设置可能影响任一顶点的最大关节数。
- `clearSkinWeights(meshIndex)`
    删除指定网格的所有皮肤权重。
- `setSkinWeightsValues(meshIndex, vertexIndex, weights, count)`
    设置影响引用顶点的皮肤权重。权重总和必须为1。
- `setSkinWeightsJointIndices(meshIndex, vertexIndex, jointIndices, count)`
    设置指定顶点的每个皮肤权重关联的联合索引。联合索引必须按与其关联的权重相同的顺序存储。
- `clearBlendShapeTargets(meshIndex)`
    删除指定网格的所有混合形状目标。
- `setBlendShapeChannelIndex(meshIndex, blendShapeTargetIndex, blendShapeChannelIndex)`
    设置指定混合形状目标的匹配混合形状通道索引。将网格本地混合形状目标索引与在Definition层中找到的绝对混合形状通道索引相关联。
- `setBlendShapeTargetDeltas(meshIndex, blendShapeTargetIndex, deltas, count)`
    设置每个受影响顶点的增量。
- `setBlendShapeTargetVertexIndices(meshIndex, blendShapeTargetIndex, vertexIndices, count)`
    设置由指定混合形状目标影响的顶点位置索引。顶点位置索引必须按与其关联的增量相同的顺序存储。
