from typing import Optional

from .builder.builder import Builder, BuildResult
from .builder.config import Config, RigConfig
from .builder.rig_builder import RigBuilder
from .dnalib.dnalib import DNA


def build_rig(dna: DNA, config: RigConfig) -> BuildResult:
    """
    用于使用提供的配置组装机架。
    
    @type config: DNA
    @param config: DNA实例
    
    @type config: Config
    @param config: 配置实例
    
    @rtype: BuildResult
    @returns: 代表构建结果的对象
    """

    return RigBuilder(dna, config).build()


def build_meshes(dna: DNA, config: Optional[Config] = None) -> BuildResult:
    """
    使用提供的配置开始网格构建过程。
    
    @type config: DNA
    @param config: DNA实例
    
    @type config: Config
    @param config: 配置实例
    
    @rtype: BuildResult
    @returns: 代表构建结果的对象
    """
    if config is None:
        config = Config()

    return Builder(dna, config).build()
