from typing import Dict, List, Optional, Tuple

from dna import BinaryStreamReader as DNAReader

from ..dnalib.layer import Layer


class Descriptor:
    """
    用于读取和访问DNA文件描述器部分的类
    
    属性
    ----------
    
    @type name: str
    @param name: 人物的名称
    
    @type archetype: int
    @param archetype: 代表人物原型的值
    
    @type gender: int
    @param gender: 代表人物性别的值
    
    @type age: int
    @param age: 人物的年龄
    
    @type metadata: Dict[str, str]
    @param metadata: 存储在人物上的元数据
    
    @type translation_unit: int
    @param translation_unit: 用于创建人物的翻译单位
    
    @type rotation_unit: int
    @param rotation_unit: 用于创建人物的旋转单位
    
    @type coordinate_system: Tuple[int, int, int]
    @param coordinate_system: 代表坐标系的元组
    
    @type lod_count: int
    @param lod_count: 人物的LOD数
    
    @type db_max_lod:int
    @param db_max_lod: 代表我们希望生成的最大LOD的LOD约束（即如果值为n，则潜在的LOD为0, 1, .. n-1）
    
    @type db_complexity: str
    @param db_complexity: 将来会使用
    
    @type db_name: str
    @param db_name: 数据库标识符
    """

    def __init__(self, reader: DNAReader, layers: Optional[List[Layer]]) -> None:
        self.reader = reader
        self.layers = layers
        self.name: Optional[str] = None
        self.archetype: Optional[int] = None
        self.gender: Optional[int] = None
        self.age: Optional[int] = None
        self.metadata: Dict[str, str] = {}

        self.translation_unit: Optional[int] = None
        self.rotation_unit: Optional[int] = None

        self.coordinate_system: Optional[Tuple[int, int, int]] = None

        self.lod_count: Optional[int] = None
        self.db_max_lod: Optional[int] = None
        self.db_complexity: Optional[str] = None
        self.db_name: Optional[str] = None
        self.descriptor_read = False

    def start_read(self) -> None:
        self.descriptor_read = False

    def is_read(self) -> bool:
        return self.descriptor_read

    def layer_enabled(self, layer: Layer) -> bool:
        return layer in self.layers or Layer.all in self.layers

    def read(self) -> None:
        """
        开始阅读 DNA 描述部分
        
        @rtype: DescriptorModel
        @returns: 创建的描述模型的实例
        """

        if not self.descriptor_read and self.layer_enabled(Layer.descriptor):
            self.descriptor_read = True
            self.add_basic_data()
            self.add_metadata()
            self.add_geometry_data()
            self.add_db_data()

    def add_basic_data(self) -> None:
        """读入角色名称、原型、性别和年龄"""

        self.name = self.reader.getName()
        self.archetype = self.reader.getArchetype()
        self.gender = self.reader.getGender()
        self.age = self.reader.getAge()

    def add_metadata(self) -> None:
        """读取DNA文件提供的元数据"""

        for i in range(self.reader.getMetaDataCount()):
            key = self.reader.getMetaDataKey(i)
            self.metadata[key] = self.reader.getMetaDataValue(key)

    def add_geometry_data(self) -> None:
        """从DNA文件设置翻译单位、旋转单位和坐标系统"""

        self.translation_unit = self.reader.getTranslationUnit()
        self.rotation_unit = self.reader.getRotationUnit()
        coordinate_system = self.reader.getCoordinateSystem()
        self.coordinate_system = (
            coordinate_system.xAxis,
            coordinate_system.yAxis,
            coordinate_system.zAxis,
        )

    def add_db_data(self) -> None:
        """从 DNA 文件中读取数据库数据"""

        self.lod_count = self.reader.getLODCount()
        self.db_max_lod = self.reader.getDBMaxLOD()
        self.db_complexity = self.reader.getDBComplexity()
        self.db_name = self.reader.getDBName()
