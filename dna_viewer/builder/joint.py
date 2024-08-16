from typing import Dict, List

from maya import cmds

from ..model import Joint as JointModel


class Joint:
    """
    用于向场景添加关节的构建器类
    
    属性
    ----------
    @type joints: List[JointModel]
    @param joints: 表示关节的数据
    
    @type joint_flags: Dict[str, bool]
    @param joint_flags: 用于设置标志的映射，以避免多次添加相同的关节
    """

    def __init__(self, joints: List[JointModel]) -> None:
        self.joints = joints
        self.joint_flags: Dict[str, bool] = {}

        for joint in self.joints:
            self.joint_flags[joint.name] = False

    def add_joint_to_scene(self, joint: JointModel) -> None:
        """
        将给定的关节添加到场景中
        
        @type joint: JointModel
        @param joint: 要添加到场景中的关节
        """

        if self.joint_flags[joint.name]:
            return

        in_parent_space = True

        if cmds.objExists(joint.parent_name):
            cmds.select(joint.parent_name)
        else:
            if joint.name != joint.parent_name:
                parent_joint = next(
                    j for j in self.joints if j.name == joint.parent_name
                )
                self.add_joint_to_scene(parent_joint)
            else:
                # this is the first node
                cmds.select(d=True)
                in_parent_space = False

        position = (
            joint.translation.x,
            joint.translation.y,
            joint.translation.z,
        )
        orientation = (
            joint.orientation.x,
            joint.orientation.y,
            joint.orientation.z,
        )
        cmds.joint(
            p=position,
            o=orientation,
            n=joint.name,
            r=in_parent_space,
            a=not in_parent_space,
            scaleCompensate=False,
        )
        self.joint_flags[joint.name] = True

    def process(self) -> None:
        """开始将所有提供的关节添加到场景中"""

        for joint in self.joints:
            self.add_joint_to_scene(joint)
