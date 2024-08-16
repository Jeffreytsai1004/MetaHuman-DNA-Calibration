from typing import Union

from maya.api.OpenMaya import (
    MDagPath,
    MFnDagNode,
    MFnTransform,
    MGlobal,
    MSpace,
    MVector,
)

from ...common import DNAViewerError


class Maya:
    """用于与maya变换接口的实用程序类"""

    @staticmethod
    def get_element(name: str) -> Union[MDagPath, MFnDagNode]:
        """
        获取具有给定名称的元素的 Union[MDagPath, MFnDagNode] 对象

        @type name: str
        @param name: 要检索的元素的名称
        
        @rtype: Union[MDagPath, MFnDagNode]
        @returns: 表示给定元素的 OpenMaya 对象
        """
        try:
            sellist = MGlobal.getSelectionListByName(name)
        except Exception as exception:
            raise DNAViewerError(f"Element with name:{name} not found!") from exception

        try:
            return sellist.getDagPath(0)
        except Exception:
            return sellist.getDependNode(0)

    @staticmethod
    def get_transform(name: str) -> MFnTransform:
        """
        获取具有给定名称的元素的变换
        
        @type element: str
        @param element: 我们要获取变换的元素名称
        
        @rtype: MFnTransform
        @returns: 代表给定元素变换的 MFnTransform 对象
        """
        return MFnTransform(Maya.get_element(name))

    @staticmethod
    def get_translation(element: str, space: int = MSpace.kObject) -> MVector:
        """
        获取具有给定名称的元素的翻译
        
        @type element: str
        @param element: 我们想要翻译的元素名称
        
        @type space: str
        @param space: 代表翻译空间的字符串值（默认为"world"）
        
        @rtype: MVector
        @returns: 代表给定元素翻译的MVector对象
        """
        return MFnTransform(Maya.get_element(element)).translation(space)

    @staticmethod
    def set_translation(
        element: str, translation: MVector, space: int = MSpace.kObject
    ) -> None:
        """
        设置具有给定名称的元素的翻译

        @type元素：str
        @param元素：我们要设置翻译的元素名称
        
        @type翻译：MVector
        @param翻译：新的翻译值
        
        @type空间：str
        @param空间：表示翻译空间的字符串值（默认为“object”）
        """
        element_obj = Maya.get_transform(element)
        element_obj.setTranslation(translation, space)
