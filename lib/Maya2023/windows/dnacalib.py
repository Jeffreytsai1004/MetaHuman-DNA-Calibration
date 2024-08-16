# 该文件是由 SWIG (https://www.swig.org) 自动生成的。
# 版本 4.1.1
#
# 除非您知道自己在做什么，请不要对此文件进行更改 - 请修改 SWIG 接口文件。


import os
if hasattr(os, 'add_dll_directory'):
    for path in os.environ.get('PATH', '').split(';'):
        try:
            if path:
                os.add_dll_directory(path)
        except Exception:
            pass



from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _py3dnacalib
else:
    import _py3dnacalib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def with_metaclass(meta, *bases):
    class metaclass(type):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

        @classmethod
        def __prepare__(cls, name, this_bases):
            return meta.__prepare__(name, bases)
    return type.__new__(metaclass, 'temporary_class', (), {})

import dna
class VersionInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def getMajorVersion():
        return _py3dnacalib.VersionInfo_getMajorVersion()

    @staticmethod
    def getMinorVersion():
        return _py3dnacalib.VersionInfo_getMinorVersion()

    @staticmethod
    def getPatchVersion():
        return _py3dnacalib.VersionInfo_getPatchVersion()

    @staticmethod
    def getVersionString():
        return _py3dnacalib.VersionInfo_getVersionString()

    def __init__(self):
        _py3dnacalib.VersionInfo_swiginit(self, _py3dnacalib.new_VersionInfo())
    __swig_destroy__ = _py3dnacalib.delete_VersionInfo

# Register VersionInfo in _py3dnacalib:
_py3dnacalib.VersionInfo_swigregister(VersionInfo)
class DNACalibDNAReader(dna.Reader):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(*args):
        return _py3dnacalib.DNACalibDNAReader_create(*args)

    @staticmethod
    def destroy(instance):
        return _py3dnacalib.DNACalibDNAReader_destroy(instance)

# Register DNACalibDNAReader in _py3dnacalib:
_py3dnacalib.DNACalibDNAReader_swigregister(DNACalibDNAReader)

DNACalibDNAReaderImpl = DNACalibDNAReader

class DNACalibDNAReaderImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(DNACalibDNAReaderImpl, name)

    def __dir__(cls):
        return [name for name in dir(DNACalibDNAReaderImpl) if name not in ("create","destroy")]

class DNACalibDNAReader(with_metaclass(DNACalibDNAReaderImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = DNACalibDNAReaderImpl.create(*args, **kwargs)

    def __del__(self):
        DNACalibDNAReaderImpl.destroy(self._instance)

    def _in_slots(self, attr):
        for cls in type(self).__mro__:
            if attr in getattr(cls, '__slots__', []):
                return True
        return False

    def __getattr__(self, attr):
        if self._in_slots(attr):
            return object.__getattr__(self, attr)
        return getattr(self._instance, attr)

    def __setattr__(self, attr, value):
        if self._in_slots(attr):
            object.__setattr__(self, attr, value)
        else:
            setattr(self._instance, attr, value)

    def __dir__(self):
        return [name for name in self._instance.__dir__() if name not in ("create","destroy")]

class Command(object):
    r"""    Command is an abstract class whose implementations are expected to modify the DNA provided in the run() method in some way."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_Command

    def run(self, output):
        return _py3dnacalib.Command_run(self, output)

# Register Command in _py3dnacalib:
_py3dnacalib.Command_swigregister(Command)
VectorOperation_Interpolate = _py3dnacalib.VectorOperation_Interpolate
VectorOperation_Add = _py3dnacalib.VectorOperation_Add
VectorOperation_Subtract = _py3dnacalib.VectorOperation_Subtract
VectorOperation_Multiply = _py3dnacalib.VectorOperation_Multiply
class CommandSequence(Command):
    r"""
    CommandSequence is used to run a sequence of commands on the same DNA.
    Notes: 
        Commands will be run in the order in which they were added to the sequence.

        CommandSequence holds pointers to commands, but does not own them.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_CommandSequence

    def __init__(self, *args):
        _py3dnacalib.CommandSequence_swiginit(self, _py3dnacalib.new_CommandSequence(*args))

    def run(self, output):
        return _py3dnacalib.CommandSequence_run(self, output)

    def add(self, command):
        r"""
        Method for adding a command to a sequence of commands to run.
        :type command: :py:class:`Command`
        :param command:
                The command to add.
        """
        return _py3dnacalib.CommandSequence_add(self, command)

    def remove(self, command):
        r"""
        Method for removing a command from the sequence of commands to run.
        :type command: :py:class:`Command`
        :param command:
                The command to remove.
        """
        return _py3dnacalib.CommandSequence_remove(self, command)

    def contains(self, command):
        r"""
        Method for checking if the provided command is part of the command sequence.
        :type command: :py:class:`Command`
        :param command:
                The command to check.
        """
        return _py3dnacalib.CommandSequence_contains(self, command)

    def size(self):
        r"""            Number of commands in command sequence."""
        return _py3dnacalib.CommandSequence_size(self)

# Register CommandSequence in _py3dnacalib:
_py3dnacalib.CommandSequence_swigregister(CommandSequence)

def command_sequence_init(_init):
    def wrapper(self, *args, **kwargs):
        self._commands = []
        _init(self, *args, **kwargs)
    return wrapper

def command_sequence_add(_add):
    def wrapper(self, command):
        self._commands.append(command)
        _add(self, command)
    return wrapper

def command_sequence_remove(_remove):
    def wrapper(self, command):
        self._commands.remove(command)
        _remove(self, command)
    return wrapper

CommandSequence.__init__ = command_sequence_init(CommandSequence.__init__)
CommandSequence.add = command_sequence_add(CommandSequence.add)
CommandSequence.remove = command_sequence_remove(CommandSequence.remove)

class CalculateMeshLowerLODsCommand(Command):
    r"""
    CalculateMeshLowerLODsCommand is used to recalculate vertex positions for lower LOD meshes of the specified mesh.
    Notes: 
        The calculation is done based on vertex positions of the specified mesh and vertex texture coordinates of its lower LOD meshes.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_CalculateMeshLowerLODsCommand

    def __init__(self, *args):
        _py3dnacalib.CalculateMeshLowerLODsCommand_swiginit(self, _py3dnacalib.new_CalculateMeshLowerLODsCommand(*args))

    def setMeshIndex(self, meshIndex):
        r"""
        Method for setting the index of the mesh to calculate lower LOD meshes from.
        :type meshIndex: int
        :param meshIndex:
                The index of the mesh.
        """
        return _py3dnacalib.CalculateMeshLowerLODsCommand_setMeshIndex(self, meshIndex)

    def run(self, output):
        return _py3dnacalib.CalculateMeshLowerLODsCommand_run(self, output)

# Register CalculateMeshLowerLODsCommand in _py3dnacalib:
_py3dnacalib.CalculateMeshLowerLODsCommand_swigregister(CalculateMeshLowerLODsCommand)
class ClearBlendShapesCommand(Command):
    r"""
    ClearBlendShapesCommand is used to clear all blend shapes data from a DNA.
    Notes: This command clears blend shape target deltas and blend shape animation data. By doing so, it transforms the DNA to be "joints only".
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_ClearBlendShapesCommand

    def __init__(self, *args):
        _py3dnacalib.ClearBlendShapesCommand_swiginit(self, _py3dnacalib.new_ClearBlendShapesCommand(*args))

    def run(self, output):
        return _py3dnacalib.ClearBlendShapesCommand_run(self, output)

# Register ClearBlendShapesCommand in _py3dnacalib:
_py3dnacalib.ClearBlendShapesCommand_swigregister(ClearBlendShapesCommand)
class PruneBlendShapeTargetsCommand(Command):
    r"""    PruneBlendShapeTargetsCommand is used to prune blend shape target deltas whose absolute magnitude is less than or equal to the specified threshold."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_PruneBlendShapeTargetsCommand

    def __init__(self, *args):
        _py3dnacalib.PruneBlendShapeTargetsCommand_swiginit(self, _py3dnacalib.new_PruneBlendShapeTargetsCommand(*args))

    def setThreshold(self, threshold):
        r"""
        Method for setting the threshold for pruning blend shape target deltas.
        :type threshold: float
        :param threshold:
                The threshold to use.
        """
        return _py3dnacalib.PruneBlendShapeTargetsCommand_setThreshold(self, threshold)

    def run(self, output):
        return _py3dnacalib.PruneBlendShapeTargetsCommand_run(self, output)

# Register PruneBlendShapeTargetsCommand in _py3dnacalib:
_py3dnacalib.PruneBlendShapeTargetsCommand_swigregister(PruneBlendShapeTargetsCommand)
class RemoveAnimatedMapCommand(Command):
    r"""    RemoveAnimatedMapCommand is used to remove animated maps."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveAnimatedMapCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveAnimatedMapCommand_swiginit(self, _py3dnacalib.new_RemoveAnimatedMapCommand(*args))

    def setAnimatedMapIndex(self, animatedMapIndex):
        r"""
        Method for setting the index of the animated map to remove.
        :type animatedMapIndex: int
        :param animatedMapIndex:
                The index of the animated map.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set animated map(s) will be removed.
        """
        return _py3dnacalib.RemoveAnimatedMapCommand_setAnimatedMapIndex(self, animatedMapIndex)

    def setAnimatedMapIndices(self, animatedMapIndices):
        r"""
        Method for setting the indices of animated maps to remove.
        :type animatedMapIndices: dnac::ConstArrayView< std::uint16_t >
        :param animatedMapIndices:
                The animated map indices.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set animated map(s) will be removed.
        """
        return _py3dnacalib.RemoveAnimatedMapCommand_setAnimatedMapIndices(self, animatedMapIndices)

    def run(self, output):
        return _py3dnacalib.RemoveAnimatedMapCommand_run(self, output)

# Register RemoveAnimatedMapCommand in _py3dnacalib:
_py3dnacalib.RemoveAnimatedMapCommand_swigregister(RemoveAnimatedMapCommand)
class RemoveBlendShapeCommand(Command):
    r"""    RemoveBlendShapeCommand is used to remove blend shapes."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveBlendShapeCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveBlendShapeCommand_swiginit(self, _py3dnacalib.new_RemoveBlendShapeCommand(*args))

    def setBlendShapeIndex(self, blendShapeIndex):
        r"""
        Method for setting the index of the blend shape to remove.
        :type blendShapeIndex: int
        :param blendShapeIndex:
                The index of the blend shape.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set blend shape(s) will be removed.
        """
        return _py3dnacalib.RemoveBlendShapeCommand_setBlendShapeIndex(self, blendShapeIndex)

    def setBlendShapeIndices(self, blendShapeIndices):
        r"""
        Method for setting the indices of blend shapes to remove.
        :type blendShapeIndices: dnac::ConstArrayView< std::uint16_t >
        :param blendShapeIndices:
                The blend shape indices.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set blend shape(s) will be removed.
        """
        return _py3dnacalib.RemoveBlendShapeCommand_setBlendShapeIndices(self, blendShapeIndices)

    def run(self, output):
        return _py3dnacalib.RemoveBlendShapeCommand_run(self, output)

# Register RemoveBlendShapeCommand in _py3dnacalib:
_py3dnacalib.RemoveBlendShapeCommand_swigregister(RemoveBlendShapeCommand)
class RemoveJointAnimationCommand(Command):
    r"""    RemoveJointAnimationCommand is used to remove joint animation data."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveJointAnimationCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveJointAnimationCommand_swiginit(self, _py3dnacalib.new_RemoveJointAnimationCommand(*args))

    def setJointIndex(self, jointIndex):
        r"""
        Method for setting the index of a joint whose animation data to remove.
        :type jointIndex: int
        :param jointIndex:
                The index of the joint.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set joint animation(s) will be removed.
        """
        return _py3dnacalib.RemoveJointAnimationCommand_setJointIndex(self, jointIndex)

    def setJointIndices(self, jointIndices):
        r"""
        Method for setting the indices of joints whose animation data to remove.
        :type jointIndices: dnac::ConstArrayView< std::uint16_t >
        :param jointIndices:
                The joint indices.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set joint animation(s) will be removed.
        """
        return _py3dnacalib.RemoveJointAnimationCommand_setJointIndices(self, jointIndices)

    def run(self, output):
        return _py3dnacalib.RemoveJointAnimationCommand_run(self, output)

# Register RemoveJointAnimationCommand in _py3dnacalib:
_py3dnacalib.RemoveJointAnimationCommand_swigregister(RemoveJointAnimationCommand)
class RemoveJointCommand(Command):
    r"""    RemoveJointCommand is used to remove joints."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveJointCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveJointCommand_swiginit(self, _py3dnacalib.new_RemoveJointCommand(*args))

    def setJointIndex(self, jointIndex):
        r"""
        Method for setting the index of the joint to remove.
        :type jointIndex: int
        :param jointIndex:
                The index of the joint.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set joint(s) will be removed.
        """
        return _py3dnacalib.RemoveJointCommand_setJointIndex(self, jointIndex)

    def setJointIndices(self, jointIndices):
        r"""
        Method for setting the indices of joints to remove.
        :type jointIndices: dnac::ConstArrayView< std::uint16_t >
        :param jointIndices:
                The joint indices.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set joint(s) will be removed.
        """
        return _py3dnacalib.RemoveJointCommand_setJointIndices(self, jointIndices)

    def run(self, output):
        return _py3dnacalib.RemoveJointCommand_run(self, output)

# Register RemoveJointCommand in _py3dnacalib:
_py3dnacalib.RemoveJointCommand_swigregister(RemoveJointCommand)
class RemoveMeshCommand(Command):
    r"""    RemoveMeshCommand is used to remove meshes."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveMeshCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveMeshCommand_swiginit(self, _py3dnacalib.new_RemoveMeshCommand(*args))

    def setMeshIndex(self, meshIndex):
        r"""
        Method for setting the index of the mesh to remove.
        :type meshIndex: int
        :param meshIndex:
                The index of the mesh.
        """
        return _py3dnacalib.RemoveMeshCommand_setMeshIndex(self, meshIndex)

    def setMeshIndices(self, meshIndices):
        r"""
        Method for setting the indices of meshes to remove.
        :type meshIndices: dnac::ConstArrayView< std::uint16_t >
        :param meshIndices:
                The mesh indices.
        Notes: Call to either setter overwrites previous setter calls. When running the command, the last set mesh(es) will be removed.
        """
        return _py3dnacalib.RemoveMeshCommand_setMeshIndices(self, meshIndices)

    def run(self, output):
        return _py3dnacalib.RemoveMeshCommand_run(self, output)

# Register RemoveMeshCommand in _py3dnacalib:
_py3dnacalib.RemoveMeshCommand_swigregister(RemoveMeshCommand)
class RenameAnimatedMapCommand(Command):
    r"""    RenameAnimatedMapCommand is used to rename an animated map."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameAnimatedMapCommand

    def __init__(self, *args):
        _py3dnacalib.RenameAnimatedMapCommand_swiginit(self, _py3dnacalib.new_RenameAnimatedMapCommand(*args))

    def setName(self, *args):
        r"""
        *Overload 1:*

        Method for setting a new name for animated map with given index.
        :type animatedMapIndex: int
        :param animatedMapIndex:
                The index of the animated map whose name to change.
        :type newName: string
        :param newName:
                The new name for the animated map.

        |

        *Overload 2:*

        Method for setting a new name for animated map with given name.
        Notes: 
            The renaming will not happen if there is no animated map with given current name.
        :type oldName: string
        :param oldName:
                The current name of the animated map whose name to change.
        :type newName: string
        :param newName:
                The new name for the animated map.
        """
        return _py3dnacalib.RenameAnimatedMapCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameAnimatedMapCommand_run(self, output)

# Register RenameAnimatedMapCommand in _py3dnacalib:
_py3dnacalib.RenameAnimatedMapCommand_swigregister(RenameAnimatedMapCommand)
class RenameBlendShapeCommand(Command):
    r"""    RenameBlendShapeCommand is used to rename a blend shape channel."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameBlendShapeCommand

    def __init__(self, *args):
        _py3dnacalib.RenameBlendShapeCommand_swiginit(self, _py3dnacalib.new_RenameBlendShapeCommand(*args))

    def setName(self, *args):
        r"""
        *Overload 1:*

        Method for setting a new name for blend shape channel with given index.
        :type blendShapeIndex: int
        :param blendShapeIndex:
                The index of the blend shape channel whose name to change.
        :type newName: string
        :param newName:
                The new name for the blend shape channel.

        |

        *Overload 2:*

        Method for setting a new name for blend shape channel with given name.
        Notes: 
            The renaming will not happen if there is no blend shape channel with given current name.
        :type oldName: string
        :param oldName:
                The current name of the blend shape channel whose name to change.
        :type newName: string
        :param newName:
                The new name for the blend shape channel.
        """
        return _py3dnacalib.RenameBlendShapeCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameBlendShapeCommand_run(self, output)

# Register RenameBlendShapeCommand in _py3dnacalib:
_py3dnacalib.RenameBlendShapeCommand_swigregister(RenameBlendShapeCommand)
class RenameJointCommand(Command):
    r"""    RenameJointCommand is used to rename a joint."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameJointCommand

    def __init__(self, *args):
        _py3dnacalib.RenameJointCommand_swiginit(self, _py3dnacalib.new_RenameJointCommand(*args))

    def setName(self, *args):
        r"""
        *Overload 1:*

        Method for setting a new name for joint with given index.
        :type jointIndex: int
        :param jointIndex:
                The index of the joint whose name to change.
        :type newName: string
        :param newName:
                The new name for the joint.

        |

        *Overload 2:*

        Method for setting a new name for joint with given name.
        Notes: 
            The renaming will not happen if there is no joint with given current name.
        :type oldName: string
        :param oldName:
                The current name of the joint whose name to change.
        :type newName: string
        :param newName:
                The new name for the joint.
        """
        return _py3dnacalib.RenameJointCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameJointCommand_run(self, output)

# Register RenameJointCommand in _py3dnacalib:
_py3dnacalib.RenameJointCommand_swigregister(RenameJointCommand)
class RenameMeshCommand(Command):
    r"""    RenameMeshCommand is used to rename a mesh."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameMeshCommand

    def __init__(self, *args):
        _py3dnacalib.RenameMeshCommand_swiginit(self, _py3dnacalib.new_RenameMeshCommand(*args))

    def setName(self, *args):
        r"""
        *Overload 1:*

        Method for setting a new name for mesh with given index.
        :type meshIndex: int
        :param meshIndex:
                The index of the mesh whose name to change.
        :type newName: string
        :param newName:
                The new name for the mesh.

        |

        *Overload 2:*

        Method for setting a new name for mesh with given name.
        Notes: 
            The renaming will not happen if there is no mesh with given current name.
        :type oldName: string
        :param oldName:
                The current name of the mesh whose name to change.
        :type newName: string
        :param newName:
                The new name for the mesh.
        """
        return _py3dnacalib.RenameMeshCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameMeshCommand_run(self, output)

# Register RenameMeshCommand in _py3dnacalib:
_py3dnacalib.RenameMeshCommand_swigregister(RenameMeshCommand)
class RotateCommand(Command):
    r"""
    RotateCommand is used to rotate neutral joints and vertex positions around given origin.
    Notes: 
        Joint rotations are represented in parent space, so it is enough to rotate only root joints, as that rotation will be propagated to the rest of the joints.

        If the origin is not set, the assumed origin is (0, 0, 0).
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RotateCommand

    def __init__(self, *args):
        _py3dnacalib.RotateCommand_swiginit(self, _py3dnacalib.new_RotateCommand(*args))

    def setRotation(self, degrees):
        r"""
        Method for setting the rotation angles.
        :type degrees: dnac::Vector3
        :param degrees:
                Rotation angles in degrees.
        """
        return _py3dnacalib.RotateCommand_setRotation(self, degrees)

    def setOrigin(self, origin):
        r"""
        Method for setting the rotation origin.
        :type origin: dnac::Vector3
        :param origin:
                Origin coordinates.
        """
        return _py3dnacalib.RotateCommand_setOrigin(self, origin)

    def run(self, output):
        return _py3dnacalib.RotateCommand_run(self, output)

# Register RotateCommand in _py3dnacalib:
_py3dnacalib.RotateCommand_swigregister(RotateCommand)
class ScaleCommand(Command):
    r"""
    ScaleCommand is used to scale neutral joints, vertex positions and joint and blendshape deltas by a factor.
    Notes: 
        Only translation attributes of neutral joints and joint deltas are scaled.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_ScaleCommand

    def __init__(self, *args):
        _py3dnacalib.ScaleCommand_swiginit(self, _py3dnacalib.new_ScaleCommand(*args))

    def setScale(self, scale):
        r"""
        Method for setting the scale factor to multiply with.
        :type scale: float
        :param scale:
                Scale factor.
        """
        return _py3dnacalib.ScaleCommand_setScale(self, scale)

    def setOrigin(self, origin):
        r"""
        Method for setting the origin.
        Notes: The origin is used to properly scale position values (vertex positions and neutral joint translations).
        :type origin: dnac::Vector3
        :param origin:
                Origin coordinates.
        """
        return _py3dnacalib.ScaleCommand_setOrigin(self, origin)

    def run(self, output):
        return _py3dnacalib.ScaleCommand_run(self, output)

# Register ScaleCommand in _py3dnacalib:
_py3dnacalib.ScaleCommand_swigregister(ScaleCommand)
class SetBlendShapeTargetDeltasCommand(Command):
    r"""    SetBlendShapeTargetDeltasCommand is used to change blend shape target deltas."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetBlendShapeTargetDeltasCommand

    def __init__(self, *args):
        _py3dnacalib.SetBlendShapeTargetDeltasCommand_swiginit(self, _py3dnacalib.new_SetBlendShapeTargetDeltasCommand(*args))

    def setMeshIndex(self, meshIndex):
        r"""
        Method for setting the index of the mesh whose blend shape target to change.
        :type meshIndex: int
        :param meshIndex:
                The mesh index.
        """
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setMeshIndex(self, meshIndex)

    def setBlendShapeTargetIndex(self, blendShapeTargetIndex):
        r"""
        Method for setting the index of the blend shape target to change.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                The blend shape target index.
        """
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setBlendShapeTargetIndex(self, blendShapeTargetIndex)

    def setDeltas(self, *args):
        r"""
        *Overload 1:*

        Method for setting the values used to calculate new deltas for blend shape target.
        :type deltas: dnac::ConstArrayView< dnac::Vector3 >
        :param deltas:
                The values used in calculation.

        |

        *Overload 2:*

        Method for setting the values used to calculate new deltas for blend shape target.
        :type xs: dnac::ConstArrayView< float >
        :param xs:
                The X values for each delta.
        :type ys: dnac::ConstArrayView< float >
        :param ys:
                The Y values for each delta.
        :type zs: dnac::ConstArrayView< float >
        :param zs:
                The Z values for each delta.
        """
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setDeltas(self, *args)

    def setVertexIndices(self, vertexIndices):
        r"""
        Method for setting the vertex indices that correspond to new deltas.
        :type vertexIndices: dnac::ConstArrayView< std::uint32_t >
        :param vertexIndices:
                The vertexIndices.
        """
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setVertexIndices(self, vertexIndices)

    def setMasks(self, masks):
        r"""
        Method for setting masks used to calculate new deltas for blend shape target.
        Notes: 
            If no masks are set, default weight value of 1 is used for each delta.
        :type masks: dnac::ConstArrayView< float >
        :param masks:
                The weights for each delta.
        """
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setMasks(self, masks)

    def setOperation(self, operation):
        r"""
        Method for setting the type of operation used to calculate new deltas for blend shape target.
        Notes: 
            Available operations are: Interpolate, Add, Subtract and Multiply. Each delta is calculated based on the provided operation type in the following way:

            Interpolate: = previousValue * (1 - weight) + setValue * weight:math:`\n                Add: \f$newValue = previousValue + (setValue * weight)`

            Subtract: = previousValue - (setValue * weight):math:`\n                Multiply: \f$newValue = previousValue * (setValue * weight)`


            setValue is the value from new deltas that were set, and weight is the value from masks array.
        :type operation: int
        :param operation:
                The operation to use.
        """
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setOperation(self, operation)

    def run(self, output):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_run(self, output)

# Register SetBlendShapeTargetDeltasCommand in _py3dnacalib:
_py3dnacalib.SetBlendShapeTargetDeltasCommand_swigregister(SetBlendShapeTargetDeltasCommand)
cvar = _py3dnacalib.cvar
SetBlendShapeTargetDeltasCommand.VertexIndicesOutOfBoundsError = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_VertexIndicesOutOfBoundsError
SetBlendShapeTargetDeltasCommand.NoVertexIndicesSetError = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_NoVertexIndicesSetError
SetBlendShapeTargetDeltasCommand.DeltasVertexIndicesCountMismatch = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_DeltasVertexIndicesCountMismatch
SetBlendShapeTargetDeltasCommand.DeltasMasksCountMismatch = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_DeltasMasksCountMismatch

class SetLODsCommand(Command):
    r"""    SetLODsCommand is used to specify LODs to use. Joints, blend shapes, animated maps and meshes that are not in specified LODs are removed from the DNA."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetLODsCommand

    def __init__(self, *args):
        _py3dnacalib.SetLODsCommand_swiginit(self, _py3dnacalib.new_SetLODsCommand(*args))

    def setLODs(self, lods):
        r"""
        Method for setting the LODs to keep.
        :type lods: dnac::ConstArrayView< std::uint16_t >
        :param lods:
                New LODs to be used.
        """
        return _py3dnacalib.SetLODsCommand_setLODs(self, lods)

    def run(self, output):
        return _py3dnacalib.SetLODsCommand_run(self, output)

# Register SetLODsCommand in _py3dnacalib:
_py3dnacalib.SetLODsCommand_swigregister(SetLODsCommand)
class SetNeutralJointRotationsCommand(Command):
    r"""    SetNeutralJointRotationsCommand is used to set new rotation values to neutral joints."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetNeutralJointRotationsCommand

    def __init__(self, *args):
        _py3dnacalib.SetNeutralJointRotationsCommand_swiginit(self, _py3dnacalib.new_SetNeutralJointRotationsCommand(*args))

    def setRotations(self, *args):
        r"""
        *Overload 1:*

        Method for setting the neutral joint rotations.
        :type rotations: dnac::ConstArrayView< dnac::Vector3 >
        :param rotations:
                Rotation values for each joint.

        |

        *Overload 2:*

        Method for setting the neutral joint rotations.
        :type xs: dnac::ConstArrayView< float >
        :param xs:
                The X rotation value for each joint.
        :type ys: dnac::ConstArrayView< float >
        :param ys:
                The Y rotation value for each joint.
        :type zs: dnac::ConstArrayView< float >
        :param zs:
                The Z rotation value for each joint.
        """
        return _py3dnacalib.SetNeutralJointRotationsCommand_setRotations(self, *args)

    def run(self, output):
        return _py3dnacalib.SetNeutralJointRotationsCommand_run(self, output)

# Register SetNeutralJointRotationsCommand in _py3dnacalib:
_py3dnacalib.SetNeutralJointRotationsCommand_swigregister(SetNeutralJointRotationsCommand)
class SetNeutralJointTranslationsCommand(Command):
    r"""    SetNeutralJointTranslationsCommand is used to set new translation values to neutral joints."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetNeutralJointTranslationsCommand

    def __init__(self, *args):
        _py3dnacalib.SetNeutralJointTranslationsCommand_swiginit(self, _py3dnacalib.new_SetNeutralJointTranslationsCommand(*args))

    def setTranslations(self, *args):
        r"""
        *Overload 1:*

        Method for setting the neutral joint translations.
        :type translations: dnac::ConstArrayView< dnac::Vector3 >
        :param translations:
                Translation values for each joint.

        |

        *Overload 2:*

        Method for setting the neutral joint translations.
        :type xs: dnac::ConstArrayView< float >
        :param xs:
                The X translation value for each joint.
        :type ys: dnac::ConstArrayView< float >
        :param ys:
                The Y translation value for each joint.
        :type zs: dnac::ConstArrayView< float >
        :param zs:
                The Z translation value for each joint.
        """
        return _py3dnacalib.SetNeutralJointTranslationsCommand_setTranslations(self, *args)

    def run(self, output):
        return _py3dnacalib.SetNeutralJointTranslationsCommand_run(self, output)

# Register SetNeutralJointTranslationsCommand in _py3dnacalib:
_py3dnacalib.SetNeutralJointTranslationsCommand_swigregister(SetNeutralJointTranslationsCommand)
class SetSkinWeightsCommand(Command):
    r"""    SetSkinWeightsCommand is used to set new skin weights for a vertex in a mesh."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetSkinWeightsCommand

    def __init__(self, *args):
        _py3dnacalib.SetSkinWeightsCommand_swiginit(self, _py3dnacalib.new_SetSkinWeightsCommand(*args))

    def setMeshIndex(self, meshIndex):
        r"""
        Method for setting the index of the targeted mesh.
        :type meshIndex: int
        :param meshIndex:
                The mesh index.
        """
        return _py3dnacalib.SetSkinWeightsCommand_setMeshIndex(self, meshIndex)

    def setVertexIndex(self, vertexIndex):
        r"""
        Method for setting the index of the vertex to change.
        :type vertexIndex: int
        :param vertexIndex:
                The vertex index.
        """
        return _py3dnacalib.SetSkinWeightsCommand_setVertexIndex(self, vertexIndex)

    def setWeights(self, weights):
        r"""
        Method for setting the weights with which joints influence the vertex in question.
        :type weights: dnac::ConstArrayView< float >
        :param weights:
                Weights for each joint that has an influence on the vertex.
        """
        return _py3dnacalib.SetSkinWeightsCommand_setWeights(self, weights)

    def setJointIndices(self, jointIndices):
        r"""
        Method for setting the joint indices of joints that influence the vertex in question.
        :type jointIndices: dnac::ConstArrayView< std::uint16_t >
        :param jointIndices:
                Joint indices of joints that have an influence on the vertex.
        """
        return _py3dnacalib.SetSkinWeightsCommand_setJointIndices(self, jointIndices)

    def run(self, output):
        return _py3dnacalib.SetSkinWeightsCommand_run(self, output)

# Register SetSkinWeightsCommand in _py3dnacalib:
_py3dnacalib.SetSkinWeightsCommand_swigregister(SetSkinWeightsCommand)
class SetVertexPositionsCommand(Command):
    r"""    SetVertexPositionsCommand is used to change vertex positions values."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetVertexPositionsCommand

    def __init__(self, *args):
        _py3dnacalib.SetVertexPositionsCommand_swiginit(self, _py3dnacalib.new_SetVertexPositionsCommand(*args))

    def setMeshIndex(self, meshIndex):
        r"""
        Method for setting the index of the mesh to change.
        :type meshIndex: int
        :param meshIndex:
                The mesh index.
        """
        return _py3dnacalib.SetVertexPositionsCommand_setMeshIndex(self, meshIndex)

    def setPositions(self, *args):
        r"""
        *Overload 1:*

        Method for setting the vertex positions used to calculate new values.
        :type positions: dnac::ConstArrayView< dnac::Vector3 >
        :param positions:
                The vertex positions.

        |

        *Overload 2:*

        Method for setting the vertex positions used to calculate new values.
        :type xs: dnac::ConstArrayView< float >
        :param xs:
                The X coordinates for each vertex.
        :type ys: dnac::ConstArrayView< float >
        :param ys:
                The Y coordinates for each vertex.
        :type zs: dnac::ConstArrayView< float >
        :param zs:
                The Z coordinates for each vertex.
        """
        return _py3dnacalib.SetVertexPositionsCommand_setPositions(self, *args)

    def setMasks(self, masks):
        r"""
        Method for setting vertex masks used to calculate new vertex position values.
        Notes: 
            If no masks are set, default weight value of 1 is used for each vertex.
        :type masks: dnac::ConstArrayView< float >
        :param masks:
                The weights for each vertex.
        """
        return _py3dnacalib.SetVertexPositionsCommand_setMasks(self, masks)

    def setOperation(self, operation):
        r"""
        Method for setting the type of operation used to calculate new vertex position values.
        Notes: 
            Available operations are: Interpolate, Add, Subtract and Multiply. Each position is calculated based on the provided operation type in the following way:

            Interpolate: = previousValue * (1 - weight) + setValue * weight:math:`\n                Add: \f$newValue = previousValue + (setValue * weight)`

            Subtract: = previousValue - (setValue * weight):math:`\n                Multiply: \f$newValue = previousValue * (setValue * weight)`


            setValue is the value from new positions that were set, and weight is the value from masks array.
        :type operation: int
        :param operation:
                The operation to use.
        """
        return _py3dnacalib.SetVertexPositionsCommand_setOperation(self, operation)

    def run(self, output):
        return _py3dnacalib.SetVertexPositionsCommand_run(self, output)

# Register SetVertexPositionsCommand in _py3dnacalib:
_py3dnacalib.SetVertexPositionsCommand_swigregister(SetVertexPositionsCommand)
SetVertexPositionsCommand.PositionsMasksCountMismatch = _py3dnacalib.cvar.SetVertexPositionsCommand_PositionsMasksCountMismatch

class TranslateCommand(Command):
    r"""
    TranslateCommand is used to translate neutral joints and vertex positions.
    Notes: 
        Joint translations are represented in parent space, so it is enough to translate only root joints, as that translation will be propagated to the rest of the joints.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_TranslateCommand

    def __init__(self, *args):
        _py3dnacalib.TranslateCommand_swiginit(self, _py3dnacalib.new_TranslateCommand(*args))

    def setTranslation(self, translation):
        r"""
        Method for setting the translation vector.
        :type translation: dnac::Vector3
        :param translation:
                The translation vector.
        """
        return _py3dnacalib.TranslateCommand_setTranslation(self, translation)

    def run(self, output):
        return _py3dnacalib.TranslateCommand_run(self, output)

# Register TranslateCommand in _py3dnacalib:
_py3dnacalib.TranslateCommand_swigregister(TranslateCommand)

