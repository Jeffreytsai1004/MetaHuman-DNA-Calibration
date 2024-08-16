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
    """A utility class used for interfacing with maya transforms"""

    @staticmethod
    def get_element(name: str) -> Union[MDagPath, MFnDagNode]:
        """
        gets the Union[MDagPath, MFnDagNode] object of the element with the given name

        @type name: str
        @param name: The name of the element to be retrieved

        @rtype: Union[MDagPath, MFnDagNode]
        @returns: A OpenMaya object representing the given element

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
        gets the transform of the element with the given name

        @type element: str
        @param element: The element name that we want the transform of

        @rtype: MFnTransform
        @returns: A MFnTransform object representing the given elements transform

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
        gets the translation of the element with the given name

        @type element: str
        @param element: The element name that we want the translation of

        @type space: str
        @param space: A string value representing the translation space (default is "world")

        @rtype: MVector
        @returns: A MVector object representing the given elements translation

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
        sets the translation of the element with the given name

        @type element: str
        @param element: The element name that we want to set the translation of

        @type translation: MVector
        @param translation: The new translation value

        @type space: str
        @param space: A string value representing the translation space (default is "object")

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
