＃此文件是由SWIG（http://www.swig.org）自动生成的。
＃版本4.0.2
＃
＃除非您知道自己在做什么-否则请不要对此文件进行更改-而应修改
＃SWIG接口文件。


import os
if hasattr(os, 'add_dll_directory'):
    for path in os.environ.get('PATH', '').split(';'):
        try:
            if path:
                os.add_dll_directory(path)
        except Exception:
            pass



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _py3dna
else:
    import _py3dna

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
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
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

class MemoryResource(object):
    r"""
    MemoryResource is an abstract class that allows the implementation of polymorphic allocators.
    Notes: 
        It's purpose is to allow passing arbitrary allocators through API boundaries, without requiring changes in the
        signatures and types involved.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_MemoryResource

    def allocate(self, size, alignment):
        return _py3dna.MemoryResource_allocate(self, size, alignment)

    def deallocate(self, ptr, size, alignment):
        return _py3dna.MemoryResource_deallocate(self, ptr, size, alignment)

# Register MemoryResource in _py3dna:
_py3dna.MemoryResource_swigregister(MemoryResource)

class AlignedMemoryResource(MemoryResource):
    r"""
    A MemoryResource that honors alignment requirements.
    See also: MemoryResource
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def allocate(self, size, alignment):
        return _py3dna.AlignedMemoryResource_allocate(self, size, alignment)

    def deallocate(self, ptr, size, alignment):
        return _py3dna.AlignedMemoryResource_deallocate(self, ptr, size, alignment)

    def __init__(self):
        _py3dna.AlignedMemoryResource_swiginit(self, _py3dna.new_AlignedMemoryResource())
    __swig_destroy__ = _py3dna.delete_AlignedMemoryResource

# Register AlignedMemoryResource in _py3dna:
_py3dna.AlignedMemoryResource_swigregister(AlignedMemoryResource)

class ArenaMemoryResource(MemoryResource):
    r"""
    Serves allocations from a preallocated memory region.
    See also: MemoryResource
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_ArenaMemoryResource

    def __init__(self, *args):
        _py3dna.ArenaMemoryResource_swiginit(self, _py3dna.new_ArenaMemoryResource(*args))

    def allocate(self, size, alignment):
        r"""            All allocations will be served from the currently active memory region."""
        return _py3dna.ArenaMemoryResource_allocate(self, size, alignment)

    def deallocate(self, ptr, size, alignment):
        r"""            This is a no-op, and the regions are only freed when the arena itself is destroyed."""
        return _py3dna.ArenaMemoryResource_deallocate(self, ptr, size, alignment)

    def getUpstreamMemoryResource(self):
        r"""            The upstream memory resource was passed through the constructor and is backing all arena allocations."""
        return _py3dna.ArenaMemoryResource_getUpstreamMemoryResource(self)

# Register ArenaMemoryResource in _py3dna:
_py3dna.ArenaMemoryResource_swigregister(ArenaMemoryResource)

class DefaultMemoryResource(MemoryResource):
    r"""
    A MemoryResource that delegates to malloc / free.
    See also: MemoryResource
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def allocate(self, size, alignment):
        return _py3dna.DefaultMemoryResource_allocate(self, size, alignment)

    def deallocate(self, ptr, size, alignment):
        return _py3dna.DefaultMemoryResource_deallocate(self, ptr, size, alignment)

    def __init__(self):
        _py3dna.DefaultMemoryResource_swiginit(self, _py3dna.new_DefaultMemoryResource())
    __swig_destroy__ = _py3dna.delete_DefaultMemoryResource

# Register DefaultMemoryResource in _py3dna:
_py3dna.DefaultMemoryResource_swigregister(DefaultMemoryResource)

class StatusCode(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    code = property(_py3dna.StatusCode_code_get, _py3dna.StatusCode_code_set)
    message = property(_py3dna.StatusCode_message_get, _py3dna.StatusCode_message_set)

    def __init__(self):
        _py3dna.StatusCode_swiginit(self, _py3dna.new_StatusCode())
    __swig_destroy__ = _py3dna.delete_StatusCode

# Register StatusCode in _py3dna:
_py3dna.StatusCode_swigregister(StatusCode)

class Status(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def isOk():
        return _py3dna.Status_isOk()

    @staticmethod
    def get():
        return _py3dna.Status_get()

    def __init__(self):
        _py3dna.Status_swiginit(self, _py3dna.new_Status())
    __swig_destroy__ = _py3dna.delete_Status

# Register Status in _py3dna:
_py3dna.Status_swigregister(Status)

def Status_isOk():
    return _py3dna.Status_isOk()

def Status_get():
    return _py3dna.Status_get()

class Readable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def read(self, *args):
        r"""
        *Overload 1:*

        Read bytes from stream into the given buffer.
        :type destination: string
        :param destination:
                Destination buffer into which the data is going to be read from the stream.
        :type size: std::size_t
        :param size:
                Number of bytes to read from stream.
        :rtype: std::size_t
        :return: 
                Number of bytes read.

        |

        *Overload 2:*

        Read bytes from this stream into the given stream.
        :type destination: :py:class:`Writable`
        :param destination:
                Destination stream into which the data is going to be read from this stream.
        :type size: std::size_t
        :param size:
                Number of bytes to read from stream.
        :rtype: std::size_t
        :return: 
                Number of bytes read.
        """
        return _py3dna.Readable_read(self, *args)

# Register Readable in _py3dna:
_py3dna.Readable_swigregister(Readable)

class Writable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def write(self, *args):
        r"""
        *Overload 1:*

        Writes bytes from the given buffer to the stream.
        :type source: string
        :param source:
                Source buffer from which the data is going to be written to the stream.
        :type size: std::size_t
        :param size:
                Number of bytes to write to the stream.
        :rtype: std::size_t
        :return: 
                Number of bytes written.

        |

        *Overload 2:*

        Writes bytes from the given stream to this stream.
        :type source: :py:class:`Readable`
        :param source:
                Source stream from which the data is going to be written into this stream.
        :type size: std::size_t
        :param size:
                Number of bytes to write to the stream.
        :rtype: std::size_t
        :return: 
                Number of bytes written.
        """
        return _py3dna.Writable_write(self, *args)

# Register Writable in _py3dna:
_py3dna.Writable_swigregister(Writable)

class Seekable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def tell(self):
        r"""
        Get the current position in the stream.
        :rtype: int
        :return: 
                Position in the stream relative to it's start, with 0 denoting the start position.
        """
        return _py3dna.Seekable_tell(self)

    def seek(self, position):
        r"""
        Set the current position in the stream.
        :type position: int
        :param position:
                Position in the stream relative to it's start, with 0 denoting the start position.
        """
        return _py3dna.Seekable_seek(self, position)

# Register Seekable in _py3dna:
_py3dna.Seekable_swigregister(Seekable)

class Openable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def open(self):
        r"""            Open access to the stream."""
        return _py3dna.Openable_open(self)

# Register Openable in _py3dna:
_py3dna.Openable_swigregister(Openable)

class Closeable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def close(self):
        r"""            Close access to the stream."""
        return _py3dna.Closeable_close(self)

# Register Closeable in _py3dna:
_py3dna.Closeable_swigregister(Closeable)

class Controllable(Openable, Closeable):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register Controllable in _py3dna:
_py3dna.Controllable_swigregister(Controllable)

class Bounded(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def size(self):
        r"""
        Obtain size of stream in bytes.
        :rtype: int
        :return: 
                Size in bytes.
        """
        return _py3dna.Bounded_size(self)

# Register Bounded in _py3dna:
_py3dna.Bounded_swigregister(Bounded)

class Buffered(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def flush(self):
        r"""            Flush the changes to filesystem."""
        return _py3dna.Buffered_flush(self)

# Register Buffered in _py3dna:
_py3dna.Buffered_swigregister(Buffered)

class Resizable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def resize(self, size):
        r"""            Resize file to the requested size."""
        return _py3dna.Resizable_resize(self, size)

# Register Resizable in _py3dna:
_py3dna.Resizable_swigregister(Resizable)

class BoundedIOStream(Controllable, Readable, Writable, Seekable, Bounded):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_BoundedIOStream

# Register BoundedIOStream in _py3dna:
_py3dna.BoundedIOStream_swigregister(BoundedIOStream)
cvar = _py3dna.cvar
BoundedIOStream.OpenError = _py3dna.cvar.BoundedIOStream_OpenError
BoundedIOStream.ReadError = _py3dna.cvar.BoundedIOStream_ReadError
BoundedIOStream.WriteError = _py3dna.cvar.BoundedIOStream_WriteError
BoundedIOStream.AlreadyOpenError = _py3dna.cvar.BoundedIOStream_AlreadyOpenError
BoundedIOStream.SeekError = _py3dna.cvar.BoundedIOStream_SeekError

AccessMode_Read = _py3dna.AccessMode_Read
AccessMode_Write = _py3dna.AccessMode_Write
AccessMode_ReadWrite = _py3dna.AccessMode_ReadWrite
OpenMode_Binary = _py3dna.OpenMode_Binary
OpenMode_Text = _py3dna.OpenMode_Text
class FileStream(BoundedIOStream):
    r"""    Standard file stream."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(path, accessMode, openMode, memRes=None):
        r"""
        Factory method for creation of a FileStream instance.
        :type path: string
        :param path:
                UTF-8 encoded path to file to be opened.
        :type accessMode: int
        :param accessMode:
                Control whether the file is opened for reading or writing.
        :type openMode: int
        :param openMode:
                Control whether the file is opened in binary or textual mode.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                The memory resource to be used for the allocation of the FileStream instance.
        Notes: 
            If a custom memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.FileStream_create(path, accessMode, openMode, memRes)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a FileStream instance.
        :type instance: :py:class:`FileStream`
        :param instance:
                Instance of FileStream to be freed.
        See also: create
        """
        return _py3dna.FileStream_destroy(instance)
    __swig_destroy__ = _py3dna.delete_FileStream

# Register FileStream in _py3dna:
_py3dna.FileStream_swigregister(FileStream)

def FileStream_create(path, accessMode, openMode, memRes=None):
    r"""
    Factory method for creation of a FileStream instance.
    :type path: string
    :param path:
            UTF-8 encoded path to file to be opened.
    :type accessMode: int
    :param accessMode:
            Control whether the file is opened for reading or writing.
    :type openMode: int
    :param openMode:
            Control whether the file is opened in binary or textual mode.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            The memory resource to be used for the allocation of the FileStream instance.
    Notes: 
        If a custom memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.FileStream_create(path, accessMode, openMode, memRes)

def FileStream_destroy(instance):
    r"""
    Method for freeing a FileStream instance.
    :type instance: :py:class:`FileStream`
    :param instance:
            Instance of FileStream to be freed.
    See also: create
    """
    return _py3dna.FileStream_destroy(instance)

class MemoryMappedFileStream(BoundedIOStream, Buffered, Resizable):
    r"""    Memory mapped file stream."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(path, accessMode, memRes=None):
        r"""
        Factory method for creation of a MemoryMappedFileStream instance.
        :type path: string
        :param path:
                UTF-8 encoded path to file to be opened.
        :type accessMode: int
        :param accessMode:
                Control whether the file is opened for reading or writing.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                The memory resource to be used for the allocation of the MemoryMappedFileStream instance.
        Notes: 
            If a custom memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.MemoryMappedFileStream_create(path, accessMode, memRes)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a MemoryMappedFileStream instance.
        :type instance: :py:class:`MemoryMappedFileStream`
        :param instance:
                Instance of MemoryMappedFileStream to be freed.
        See also: create
        """
        return _py3dna.MemoryMappedFileStream_destroy(instance)
    __swig_destroy__ = _py3dna.delete_MemoryMappedFileStream

# Register MemoryMappedFileStream in _py3dna:
_py3dna.MemoryMappedFileStream_swigregister(MemoryMappedFileStream)

def MemoryMappedFileStream_create(path, accessMode, memRes=None):
    r"""
    Factory method for creation of a MemoryMappedFileStream instance.
    :type path: string
    :param path:
            UTF-8 encoded path to file to be opened.
    :type accessMode: int
    :param accessMode:
            Control whether the file is opened for reading or writing.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            The memory resource to be used for the allocation of the MemoryMappedFileStream instance.
    Notes: 
        If a custom memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.MemoryMappedFileStream_create(path, accessMode, memRes)

def MemoryMappedFileStream_destroy(instance):
    r"""
    Method for freeing a MemoryMappedFileStream instance.
    :type instance: :py:class:`MemoryMappedFileStream`
    :param instance:
            Instance of MemoryMappedFileStream to be freed.
    See also: create
    """
    return _py3dna.MemoryMappedFileStream_destroy(instance)

class MemoryStream(BoundedIOStream):
    r"""    In-memory stream."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(*args):
        r"""
        *Overload 1:*

        Factory method for creation of a MemoryStream instance.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                The memory resource to be used for the allocation of the MemoryStream instance.
        Notes: 
            If a custom memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy

        |

        *Overload 2:*

        Factory method for creation of a MemoryStream instance.
        :type initialSize: std::size_t
        :param initialSize:
                Initial size of the memory stream.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                The memory resource to be used for the allocation of the MemoryStream instance.
        Notes: 
            If a custom memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy

        |

        *Overload 3:*

        Factory method for creation of a MemoryStream instance.
        :type initialSize: std::size_t
        :param initialSize:
                Initial size of the memory stream.
        :param memRes:
                The memory resource to be used for the allocation of the MemoryStream instance.
        Notes: 
            If a custom memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.MemoryStream_create(*args)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a MemoryStream instance.
        :type instance: :py:class:`MemoryStream`
        :param instance:
                Instance of MemoryStream to be freed.
        See also: create
        """
        return _py3dna.MemoryStream_destroy(instance)
    __swig_destroy__ = _py3dna.delete_MemoryStream

# Register MemoryStream in _py3dna:
_py3dna.MemoryStream_swigregister(MemoryStream)

def MemoryStream_create(*args):
    r"""
    *Overload 1:*

    Factory method for creation of a MemoryStream instance.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            The memory resource to be used for the allocation of the MemoryStream instance.
    Notes: 
        If a custom memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy

    |

    *Overload 2:*

    Factory method for creation of a MemoryStream instance.
    :type initialSize: std::size_t
    :param initialSize:
            Initial size of the memory stream.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            The memory resource to be used for the allocation of the MemoryStream instance.
    Notes: 
        If a custom memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy

    |

    *Overload 3:*

    Factory method for creation of a MemoryStream instance.
    :type initialSize: std::size_t
    :param initialSize:
            Initial size of the memory stream.
    :param memRes:
            The memory resource to be used for the allocation of the MemoryStream instance.
    Notes: 
        If a custom memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.MemoryStream_create(*args)

def MemoryStream_destroy(instance):
    r"""
    Method for freeing a MemoryStream instance.
    :type instance: :py:class:`MemoryStream`
    :param instance:
            Instance of MemoryStream to be freed.
    See also: create
    """
    return _py3dna.MemoryStream_destroy(instance)


FileStreamImpl = FileStream

class FileStreamImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(FileStreamImpl, name)

    def __dir__(cls):
        return [name for name in dir(FileStreamImpl) if name not in ("create","destroy")]

class FileStream(with_metaclass(FileStreamImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = FileStreamImpl.create(*args, **kwargs)

    def __del__(self):
        FileStreamImpl.destroy(self._instance)

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


MemoryMappedFileStreamImpl = MemoryMappedFileStream

class MemoryMappedFileStreamImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(MemoryMappedFileStreamImpl, name)

    def __dir__(cls):
        return [name for name in dir(MemoryMappedFileStreamImpl) if name not in ("create","destroy")]

class MemoryMappedFileStream(with_metaclass(MemoryMappedFileStreamImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = MemoryMappedFileStreamImpl.create(*args, **kwargs)

    def __del__(self):
        MemoryMappedFileStreamImpl.destroy(self._instance)

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


MemoryStreamImpl = MemoryStream

class MemoryStreamImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(MemoryStreamImpl, name)

    def __dir__(cls):
        return [name for name in dir(MemoryStreamImpl) if name not in ("create","destroy")]

class MemoryStream(with_metaclass(MemoryStreamImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = MemoryStreamImpl.create(*args, **kwargs)

    def __del__(self):
        MemoryStreamImpl.destroy(self._instance)

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


FileStream.AccessMode_Read = AccessMode_Read
FileStream.AccessMode_Write = AccessMode_Write
FileStream.AccessMode_ReadWrite = AccessMode_ReadWrite

FileStream.OpenMode_Binary = OpenMode_Binary
FileStream.OpenMode_Text = OpenMode_Text

MemoryMappedFileStream.AccessMode_Read = AccessMode_Read
MemoryMappedFileStream.AccessMode_Write = AccessMode_Write
MemoryMappedFileStream.AccessMode_ReadWrite = AccessMode_ReadWrite

class StringView(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def c_str(self):
        return _py3dna.StringView_c_str(self)

    def __ref__(self):
        return _py3dna.StringView___ref__(self)

    def __init__(self):
        _py3dna.StringView_swiginit(self, _py3dna.new_StringView())
    __swig_destroy__ = _py3dna.delete_StringView

# Register StringView in _py3dna:
_py3dna.StringView_swigregister(StringView)


def __add__(*args):
    return _py3dna.__add__(*args)

def __sub__(*args):
    return _py3dna.__sub__(*args)

def __mul__(*args):
    return _py3dna.__mul__(*args)

def __truediv__(*args):
    return _py3dna.__truediv__(*args)

def __eq__(lhs, rhs):
    return _py3dna.__eq__(lhs, rhs)

def __ne__(lhs, rhs):
    return _py3dna.__ne__(lhs, rhs)
DataLayer_Descriptor = _py3dna.DataLayer_Descriptor
DataLayer_Definition = _py3dna.DataLayer_Definition
DataLayer_Behavior = _py3dna.DataLayer_Behavior
DataLayer_Geometry = _py3dna.DataLayer_Geometry
DataLayer_GeometryWithoutBlendShapes = _py3dna.DataLayer_GeometryWithoutBlendShapes
DataLayer_AllWithoutBlendShapes = _py3dna.DataLayer_AllWithoutBlendShapes
DataLayer_All = _py3dna.DataLayer_All
Archetype_asian = _py3dna.Archetype_asian
Archetype_black = _py3dna.Archetype_black
Archetype_caucasian = _py3dna.Archetype_caucasian
Archetype_hispanic = _py3dna.Archetype_hispanic
Archetype_alien = _py3dna.Archetype_alien
Archetype_other = _py3dna.Archetype_other
Gender_male = _py3dna.Gender_male
Gender_female = _py3dna.Gender_female
Gender_other = _py3dna.Gender_other
TranslationUnit_cm = _py3dna.TranslationUnit_cm
TranslationUnit_m = _py3dna.TranslationUnit_m
RotationUnit_degrees = _py3dna.RotationUnit_degrees
RotationUnit_radians = _py3dna.RotationUnit_radians
Direction_left = _py3dna.Direction_left
Direction_right = _py3dna.Direction_right
Direction_up = _py3dna.Direction_up
Direction_down = _py3dna.Direction_down
Direction_front = _py3dna.Direction_front
Direction_back = _py3dna.Direction_back
class CoordinateSystem(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    xAxis = property(_py3dna.CoordinateSystem_xAxis_get, _py3dna.CoordinateSystem_xAxis_set)
    yAxis = property(_py3dna.CoordinateSystem_yAxis_get, _py3dna.CoordinateSystem_yAxis_set)
    zAxis = property(_py3dna.CoordinateSystem_zAxis_get, _py3dna.CoordinateSystem_zAxis_set)

    def __init__(self):
        _py3dna.CoordinateSystem_swiginit(self, _py3dna.new_CoordinateSystem())
    __swig_destroy__ = _py3dna.delete_CoordinateSystem

# Register CoordinateSystem in _py3dna:
_py3dna.CoordinateSystem_swigregister(CoordinateSystem)

class DescriptorReader(object):
    r"""
    Read-only accessors for various metadata about the character and the rig.
    Warning: 
        Implementors should inherit from Reader itself and not this class.
    See also: Reader
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getName(self):
        return _py3dna.DescriptorReader_getName(self)

    def getArchetype(self):
        return _py3dna.DescriptorReader_getArchetype(self)

    def getGender(self):
        return _py3dna.DescriptorReader_getGender(self)

    def getAge(self):
        return _py3dna.DescriptorReader_getAge(self)

    def getMetaDataCount(self):
        return _py3dna.DescriptorReader_getMetaDataCount(self)

    def getMetaDataKey(self, index):
        r"""
        :type index: int
        :param index:
                A position in the zero-indexed array of key-value pairs.
        Warning: 
            The index must be less than the value returned by getMetaDataCount.
        :rtype: :py:class:`StringView`
        :return: View over the key name string.
        """
        return _py3dna.DescriptorReader_getMetaDataKey(self, index)

    def getMetaDataValue(self, key):
        r"""
        Stored metadata value associated with the given key.
        Notes: 
            If no value is associated with the given key, the returned view
            will contain nullptr and will have a size of 0.
        :type key: string
        :param key:
                A unique-known key that has a value associated to it.
        Warning: 
            The key must be null-terminated.
        :rtype: :py:class:`StringView`
        :return: View over the metadata value string.
        """
        return _py3dna.DescriptorReader_getMetaDataValue(self, key)

    def getTranslationUnit(self):
        return _py3dna.DescriptorReader_getTranslationUnit(self)

    def getRotationUnit(self):
        return _py3dna.DescriptorReader_getRotationUnit(self)

    def getCoordinateSystem(self):
        return _py3dna.DescriptorReader_getCoordinateSystem(self)

    def getLODCount(self):
        r"""
        Available levels of detail (e.g. 6 which means the following levels are available:
            [0,1,2,3,4,5], where 0 is the LOD with the highest details, and 5 is the LOD with
            lowest details).
        """
        return _py3dna.DescriptorReader_getLODCount(self)

    def getDBMaxLOD(self):
        r"""
        The maximum level of detail stored in the DNA data for this character.
        Notes: 
            The value is relative to LOD-0 from the database.
        """
        return _py3dna.DescriptorReader_getDBMaxLOD(self)

    def getDBComplexity(self):
        r"""
        Name of the input control interface used to drive this character rig.
        Notes: 
            This parameter denotes the character's input control complexity.
        """
        return _py3dna.DescriptorReader_getDBComplexity(self)

    def getDBName(self):
        r"""
        Name of the database from which the character originates.
        Notes: 
            All characters from the same database must have the same Definition, but may
            have different complexity or LOD.
        """
        return _py3dna.DescriptorReader_getDBName(self)

# Register DescriptorReader in _py3dna:
_py3dna.DescriptorReader_swigregister(DescriptorReader)

class MeshBlendShapeChannelMapping(object):
    r"""    Mapping that associates a blend shape channel to it's mesh."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    meshIndex = property(_py3dna.MeshBlendShapeChannelMapping_meshIndex_get, _py3dna.MeshBlendShapeChannelMapping_meshIndex_set)
    blendShapeChannelIndex = property(_py3dna.MeshBlendShapeChannelMapping_blendShapeChannelIndex_get, _py3dna.MeshBlendShapeChannelMapping_blendShapeChannelIndex_set)

    def __init__(self):
        _py3dna.MeshBlendShapeChannelMapping_swiginit(self, _py3dna.new_MeshBlendShapeChannelMapping())
    __swig_destroy__ = _py3dna.delete_MeshBlendShapeChannelMapping

# Register MeshBlendShapeChannelMapping in _py3dna:
_py3dna.MeshBlendShapeChannelMapping_swigregister(MeshBlendShapeChannelMapping)

class DefinitionReader(DescriptorReader):
    r"""
    Read-only accessors for DNA attributes that represent the rig's static data.
    Warning: 
        Implementors should inherit from Reader itself and not this class.
    See also: Reader
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getGUIControlCount(self):
        return _py3dna.DefinitionReader_getGUIControlCount(self)

    def getGUIControlName(self, index):
        r"""
        Name of the requested GUI control.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of GUI control names.
        Warning: 
            The index must be less than the value returned by getGUIControlCount.
        :rtype: :py:class:`StringView`
        :return: View over the GUI control name string.
        """
        return _py3dna.DefinitionReader_getGUIControlName(self, index)

    def getRawControlCount(self):
        return _py3dna.DefinitionReader_getRawControlCount(self)

    def getRawControlName(self, index):
        r"""
        Name of the requested raw control.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of raw control names.
        Warning: 
            The index must be less than the value returned by getRawControlCount.
        :rtype: :py:class:`StringView`
        :return: View over the control name string.
        """
        return _py3dna.DefinitionReader_getRawControlName(self, index)

    def getJointCount(self):
        return _py3dna.DefinitionReader_getJointCount(self)

    def getJointName(self, index):
        r"""
        Name of the requested joint.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of joint names.
        Warning: 
            The index must be less than the value returned by getJointCount.
        :rtype: :py:class:`StringView`
        :return: View over the joint name string.
        """
        return _py3dna.DefinitionReader_getJointName(self, index)

    def getJointIndexListCount(self):
        r"""
        Number of joint index lists.
        Notes: 
            This value is useful only in the context of DefinitionWriter.
        """
        return _py3dna.DefinitionReader_getJointIndexListCount(self)

    def getJointIndicesForLOD(self, lod):
        r"""
        List of joint indices for the specified LOD.
        :type lod: int
        :param lod:
                The level of detail which joints are being requested.
        Warning: 
            The lod index must be less than the value returned by getLODCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the joint indices.
        See also: getLODCount
        See also: getJointName
        """
        return _py3dna.DefinitionReader_getJointIndicesForLOD(self, lod)

    def getJointParentIndex(self, index):
        r"""
        Index of the requested joint's parent.
        Notes: 
            The joint hierarchy may be traversed and reconstructed using this function. Example:
            Joint names: [A, B, C, D, E, F, G, H, I]
            Hierarchy:   [0, 0, 0, 1, 1, 4, 2, 6, 2]
            Describes the following hierarchy:
            A
            + B
            | + D
            | + E
            |   + F
            + C
              + G
              | + H
              + I

            Requesting the parent index of joint 5 (joint name: F) would return 4 (joint name: E).
            Requesting the parent index of the root joint: 0 (joint name: A) would return the same index 0.
            An out of bounds request (an index greater than the number of joints returns UINT16_MAX).
        :type index: int
        :param index:
                The joint index which parent is being requested.
        """
        return _py3dna.DefinitionReader_getJointParentIndex(self, index)

    def getBlendShapeChannelCount(self):
        return _py3dna.DefinitionReader_getBlendShapeChannelCount(self)

    def getBlendShapeChannelName(self, index):
        r"""
        Name of the requested blend shape channel.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of blend shape channel names.
        Warning: 
            The index must be less than the value returned by BlendShapeChannelExtentReader::getBlendShapeChannelCount.
        :rtype: :py:class:`StringView`
        :return: View over the blend shape channel name string.
        """
        return _py3dna.DefinitionReader_getBlendShapeChannelName(self, index)

    def getBlendShapeChannelIndexListCount(self):
        r"""
        Number of blend shape channel index lists.
        Notes: 
            This value is useful only in the context of DefinitionWriter.
        """
        return _py3dna.DefinitionReader_getBlendShapeChannelIndexListCount(self)

    def getBlendShapeChannelIndicesForLOD(self, lod):
        r"""
        List of blend shape channel indices for the specified LOD.
        :type lod: int
        :param lod:
                The level of detail which blend shape channels are being requested.
        Warning: 
            The lod index must be less than the value returned by getLODCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the blend shape channel indices.

            These LOD indices are not interchangeable with the LOD values from BehaviorReader::getBlendShapeChannelLODs.
        See also: getLODCount
        See also: getBlendShapeChannelName
        """
        return _py3dna.DefinitionReader_getBlendShapeChannelIndicesForLOD(self, lod)

    def getAnimatedMapCount(self):
        return _py3dna.DefinitionReader_getAnimatedMapCount(self)

    def getAnimatedMapName(self, index):
        r"""
        Name of the requested animated map.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of animated map names.
        Warning: 
            The index must be less than the value returned by getAnimatedMapCount.
        :rtype: :py:class:`StringView`
        :return: View over the animated map name string.
        """
        return _py3dna.DefinitionReader_getAnimatedMapName(self, index)

    def getAnimatedMapIndexListCount(self):
        r"""
        Number of animated map index lists.
        Notes: 
            This value is useful only in the context of DefinitionWriter.
        """
        return _py3dna.DefinitionReader_getAnimatedMapIndexListCount(self)

    def getAnimatedMapIndicesForLOD(self, lod):
        r"""
        List of animated map indices for the specified LOD.
        :type lod: int
        :param lod:
                The level of detail which animated maps are being requested.
        Warning: 
            The lod index must be less than the value returned by getLODCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the animated map indices.
        See also: getLODCount
        See also: getAnimatedMapName
        """
        return _py3dna.DefinitionReader_getAnimatedMapIndicesForLOD(self, lod)

    def getMeshCount(self):
        return _py3dna.DefinitionReader_getMeshCount(self)

    def getMeshName(self, index):
        r"""
        Name of the requested mesh.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of mesh names.
        Warning: 
            The index must be less than the value returned by getMeshCount.
        :rtype: :py:class:`StringView`
        :return: View over the mesh name string.
        """
        return _py3dna.DefinitionReader_getMeshName(self, index)

    def getMeshIndexListCount(self):
        r"""
        Number of mesh index lists.
        Notes: 
            This value is useful only in the context of DefinitionWriter.
        """
        return _py3dna.DefinitionReader_getMeshIndexListCount(self)

    def getMeshIndicesForLOD(self, lod):
        r"""
        List of mesh indices for the specified LOD.
        :type lod: int
        :param lod:
                The level of detail which meshes are being requested.
        Warning: 
            The lod index must be less than the value returned by getLODCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the mesh indices.
        See also: getLODCount
        See also: getMeshName
        """
        return _py3dna.DefinitionReader_getMeshIndicesForLOD(self, lod)

    def getMeshBlendShapeChannelMappingCount(self):
        r"""            Number of mesh-blend shape channel mapping items."""
        return _py3dna.DefinitionReader_getMeshBlendShapeChannelMappingCount(self)

    def getMeshBlendShapeChannelMapping(self, index):
        r"""
        :type index: int
        :param index:
                A mapping's position in the zero-indexed array of mesh-blend shape channel mappings.
        Warning: 
            The index must be less than the value returned by getMeshBlendShapeChannelMappingCount.
        :rtype: :py:class:`MeshBlendShapeChannelMapping`
        :return: A structure holding the mesh index and the associated blend shape channel index.
        """
        return _py3dna.DefinitionReader_getMeshBlendShapeChannelMapping(self, index)

    def getMeshBlendShapeChannelMappingIndicesForLOD(self, lod):
        r"""
        List of mesh-blend shape channel mapping indices for the specified LOD.
        Notes: 
            The indices from this list can be used with the getMeshBlendShapeChannelMapping API
            to retrieve individual mapping items.
        :type lod: int
        :param lod:
                The level of detail which meshes are being requested.
        Warning: 
            The lod index must be less than the value returned by getLODCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the mesh blend shape channel mapping indices.
        See also: getLODCount
        See also: getMeshBlendShapeChannelMapping
        """
        return _py3dna.DefinitionReader_getMeshBlendShapeChannelMappingIndicesForLOD(self, lod)

    def getNeutralJointTranslation(self, index):
        r"""
        :type index: int
        :param index:
                A joint's position in the zero-indexed array of joint translations.
        Warning: 
            The index must be less than the value returned by getJointCount.
        :rtype: dna::Vector3
        :return: The joint's translation (x, y, z).
        """
        return _py3dna.DefinitionReader_getNeutralJointTranslation(self, index)

    def getNeutralJointTranslationXs(self):
        r"""
        List of all translation X values.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getNeutralJointTranslation.
        :rtype: dna::ConstArrayView< float >
        :return: View over all X values.
        See also: getNeutralJointTranslation
        """
        return _py3dna.DefinitionReader_getNeutralJointTranslationXs(self)

    def getNeutralJointTranslationYs(self):
        r"""
        List of all translation Y values.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getNeutralJointTranslation.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Y values.
        See also: getNeutralJointTranslation
        """
        return _py3dna.DefinitionReader_getNeutralJointTranslationYs(self)

    def getNeutralJointTranslationZs(self):
        r"""
        List of all translation Z values.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getNeutralJointTranslation.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Z values.
        See also: getNeutralJointTranslation
        """
        return _py3dna.DefinitionReader_getNeutralJointTranslationZs(self)

    def getNeutralJointRotation(self, index):
        r"""
        :type index: int
        :param index:
                A joint's position in the zero-indexed array of joint rotations.
        Warning: 
            The index must be less than the value returned by getJointCount.
        :rtype: dna::Vector3
        :return: The joint's rotation (x, y, z).
        """
        return _py3dna.DefinitionReader_getNeutralJointRotation(self, index)

    def getNeutralJointRotationXs(self):
        r"""
        List of all rotation X values.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getNeutralJointRotation.
        :rtype: dna::ConstArrayView< float >
        :return: View over all X values.
        See also: getNeutralJointRotation
        """
        return _py3dna.DefinitionReader_getNeutralJointRotationXs(self)

    def getNeutralJointRotationYs(self):
        r"""
        List of all rotation Y values.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getNeutralJointRotation.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Y values.
        See also: getNeutralJointRotation
        """
        return _py3dna.DefinitionReader_getNeutralJointRotationYs(self)

    def getNeutralJointRotationZs(self):
        r"""
        List of all rotation Z values.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getNeutralJointRotation.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Z values.
        See also: getNeutralJointRotation
        """
        return _py3dna.DefinitionReader_getNeutralJointRotationZs(self)

# Register DefinitionReader in _py3dna:
_py3dna.DefinitionReader_swigregister(DefinitionReader)

class BehaviorReader(DefinitionReader):
    r"""
    Read-only accessors for DNA attributes that define the rig's evaluation.
    Warning: 
        Implementors should inherit from Reader itself and not this class.
    See also: Reader
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getGUIToRawInputIndices(self):
        r"""
        Input indices used for mapping gui to raw controls.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of input indices.
        """
        return _py3dna.BehaviorReader_getGUIToRawInputIndices(self)

    def getGUIToRawOutputIndices(self):
        r"""
        Output indices used for mapping gui to raw controls.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of output indices.
        """
        return _py3dna.BehaviorReader_getGUIToRawOutputIndices(self)

    def getGUIToRawFromValues(self):
        r"""
        Filter values(lower-bounds) used to decide whether a particular
            entry should be evaluated or not during gui to raw control mapping.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of filter values.
        """
        return _py3dna.BehaviorReader_getGUIToRawFromValues(self)

    def getGUIToRawToValues(self):
        r"""
        Filter values(upper-bounds) used to decide whether a particular
            entry should be evaluated or not during gui to raw control mapping.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of filter values.
        """
        return _py3dna.BehaviorReader_getGUIToRawToValues(self)

    def getGUIToRawSlopeValues(self):
        r"""
        Computational values(slope/gradient) used for calculating the
            output value during gui to raw control mapping.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of computational values.
        """
        return _py3dna.BehaviorReader_getGUIToRawSlopeValues(self)

    def getGUIToRawCutValues(self):
        r"""
        Computational values(vertical intercept) used for calculating the
            output value during gui to raw control mapping.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of computational values.
        """
        return _py3dna.BehaviorReader_getGUIToRawCutValues(self)

    def getPSDCount(self):
        r"""            The number of distinct PSD expressions."""
        return _py3dna.BehaviorReader_getPSDCount(self)

    def getPSDRowIndices(self):
        r"""
        PSD(input) indices.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of PSD indices.
        """
        return _py3dna.BehaviorReader_getPSDRowIndices(self)

    def getPSDColumnIndices(self):
        r"""
        Control(input) indices.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of control indices.
        """
        return _py3dna.BehaviorReader_getPSDColumnIndices(self)

    def getPSDValues(self):
        r"""
        Weights associated with each PSD row and column pair.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of weights.
        """
        return _py3dna.BehaviorReader_getPSDValues(self)

    def getJointRowCount(self):
        r"""            Number of rows in the entire, uncompressed joint matrix."""
        return _py3dna.BehaviorReader_getJointRowCount(self)

    def getJointColumnCount(self):
        r"""            Number of columns in the entire, uncompressed joint matrix."""
        return _py3dna.BehaviorReader_getJointColumnCount(self)

    def getJointVariableAttributeIndices(self, lod):
        r"""
        Joint attribute indices (output indices) for the requested LOD.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of joint indices.
        """
        return _py3dna.BehaviorReader_getJointVariableAttributeIndices(self, lod)

    def getJointGroupCount(self):
        r"""            Number of joint groups present in the entire joint matrix."""
        return _py3dna.BehaviorReader_getJointGroupCount(self)

    def getJointGroupLODs(self, jointGroupIndex):
        r"""
        Number of rows per each level of detail for the requested joint group.
        Notes: 
            Each element's position represents the level itself, while the value denotes
            the number of rows within the joint group belonging to that level. e.g.:
            [12, 9, 3]
             |   |  + LOD-2 contains first 3 rows
             |   + LOD-1 contains first 9 rows
             + LOD-0 contains first 12 rows
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Warning: 
            jointGroupIndex must be less than the value returned by getJointGroupCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of LOD bounds.
        """
        return _py3dna.BehaviorReader_getJointGroupLODs(self, jointGroupIndex)

    def getJointGroupInputIndices(self, jointGroupIndex):
        r"""
        Column indices that the requested joint group contains.
        Notes: 
            The column indices point into the entire, uncompressed joint matrix.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Warning: 
            jointGroupIndex must be less than the value returned by getJointGroupCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of column indices.
        """
        return _py3dna.BehaviorReader_getJointGroupInputIndices(self, jointGroupIndex)

    def getJointGroupOutputIndices(self, jointGroupIndex):
        r"""
        Row indices that the requested joint group contains.
        Notes: 
            The row indices point into the entire, uncompressed joint matrix.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Warning: 
            jointGroupIndex must be less than the value returned by getJointGroupCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of row indices.
        """
        return _py3dna.BehaviorReader_getJointGroupOutputIndices(self, jointGroupIndex)

    def getJointGroupValues(self, jointGroupIndex):
        r"""
        Values that the requested joint group contains.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Warning: 
            jointGroupIndex must be less than the value returned by getJointGroupCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of values.
        """
        return _py3dna.BehaviorReader_getJointGroupValues(self, jointGroupIndex)

    def getJointGroupJointIndices(self, jointGroupIndex):
        r"""
        Joint indices that the requested joint group contains.
        Notes: 
            These joint indices can be used to get the joint names through DefinitionReader::getJointName.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Warning: 
            jointGroupIndex must be less than the value returned by getJointGroupCount.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of joint indices.
        See also: DefinitionReader
        """
        return _py3dna.BehaviorReader_getJointGroupJointIndices(self, jointGroupIndex)

    def getBlendShapeChannelLODs(self):
        r"""
        Input index count per each level of detail for blend shape channels.
        Notes: 
            Each element's position represents the level itself  (e.g. [0,1,2,3,4,5] Value 0 is LOD with highest of details,
            value 5 is LOD with lowest details), while the value denotes the number of input indices belonging to that level.
        Warning: 
            These LOD values are not interchangeable with the LOD indices from DefinitionReader::getBlendShapeChannelIndicesForLOD.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of LOD bounds.
        """
        return _py3dna.BehaviorReader_getBlendShapeChannelLODs(self)

    def getBlendShapeChannelInputIndices(self):
        r"""
        Input indices used to index into the input vector.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of input indices.
        """
        return _py3dna.BehaviorReader_getBlendShapeChannelInputIndices(self)

    def getBlendShapeChannelOutputIndices(self):
        r"""
        Output indices specify the positions of blend shape channel output values.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of output indices.
        """
        return _py3dna.BehaviorReader_getBlendShapeChannelOutputIndices(self)

    def getAnimatedMapLODs(self):
        r"""
        Row count per each level of detail for animated maps.
        Notes: 
            Each element's position represents the level itself  (e.g. [0,1,2,3,4,5] Value 0 is LOD with highest of details,
            value 5 is LOD with lowest details), while the value denotes the number of rows (within the conditional table),
            belonging to that level.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of LOD bounds.
        """
        return _py3dna.BehaviorReader_getAnimatedMapLODs(self)

    def getAnimatedMapInputIndices(self):
        r"""
        Input indices used to index into the array of input values.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of input indices.
        """
        return _py3dna.BehaviorReader_getAnimatedMapInputIndices(self)

    def getAnimatedMapOutputIndices(self):
        r"""
        Output indices that specify the computed output value's position.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the array of output indices.
        """
        return _py3dna.BehaviorReader_getAnimatedMapOutputIndices(self)

    def getAnimatedMapFromValues(self):
        r"""
        Filter values(lower-bounds) used to decide whether a particular
            entry should be evaluated or not.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of filter values.
        """
        return _py3dna.BehaviorReader_getAnimatedMapFromValues(self)

    def getAnimatedMapToValues(self):
        r"""
        Filter values(upper-bounds) used to decide whether a particular
            entry should be evaluated or not.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of filter values.
        """
        return _py3dna.BehaviorReader_getAnimatedMapToValues(self)

    def getAnimatedMapSlopeValues(self):
        r"""
        Computational values(slope/gradient) used for calculating the output value.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of computational values.
        """
        return _py3dna.BehaviorReader_getAnimatedMapSlopeValues(self)

    def getAnimatedMapCutValues(self):
        r"""
        Computational values(vertical intercept) used for calculating the output value.
        :rtype: dna::ConstArrayView< float >
        :return: View over the array of computational values.
        """
        return _py3dna.BehaviorReader_getAnimatedMapCutValues(self)

# Register BehaviorReader in _py3dna:
_py3dna.BehaviorReader_swigregister(BehaviorReader)

class GeometryReader(DefinitionReader):
    r"""
    Read-only accessors to the geometry data associated with a rig.
    Warning: 
        Implementors should inherit from Reader itself and not this class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getVertexPositionCount(self, meshIndex):
        r"""
        Number of vertex positions in the entire mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getVertexPositionCount(self, meshIndex)

    def getVertexPosition(self, meshIndex, vertexIndex):
        r"""
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type vertexIndex: int
        :param vertexIndex:
                The index of the vertex position in the zero-indexed array of vertex positions.

            vertexIndex must be less than the value returned by getVertexPositionCount.
        Notes: 
            The vertices are sorted by the vertex ID.
        :rtype: dna::Position
        :return: The vertex position.
        """
        return _py3dna.GeometryReader_getVertexPosition(self, meshIndex, vertexIndex)

    def getVertexPositionXs(self, meshIndex):
        r"""
        List of all vertex position X values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexPosition.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all X values.
        See also: getVertexPosition
        """
        return _py3dna.GeometryReader_getVertexPositionXs(self, meshIndex)

    def getVertexPositionYs(self, meshIndex):
        r"""
        List of all vertex position Y values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexPosition.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Y values.
        See also: getVertexPosition
        """
        return _py3dna.GeometryReader_getVertexPositionYs(self, meshIndex)

    def getVertexPositionZs(self, meshIndex):
        r"""
        List of all vertex position Z values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexPosition.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Z values.
        See also: getVertexPosition
        """
        return _py3dna.GeometryReader_getVertexPositionZs(self, meshIndex)

    def getVertexTextureCoordinateCount(self, meshIndex):
        r"""
        Number of texture coordinates in the entire mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getVertexTextureCoordinateCount(self, meshIndex)

    def getVertexTextureCoordinate(self, meshIndex, textureCoordinateIndex):
        r"""
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type textureCoordinateIndex: int
        :param textureCoordinateIndex:
                The index of the texture coordinate in the zero-indexed array of texture coordinates.

            textureCoordinateIndex must be less than the value returned by getVertexTextureCoordinateCount.
        :rtype: dna::TextureCoordinate
        :return: The texture coordinate.
        """
        return _py3dna.GeometryReader_getVertexTextureCoordinate(self, meshIndex, textureCoordinateIndex)

    def getVertexTextureCoordinateUs(self, meshIndex):
        r"""
        List of all texture coordinate U values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexTextureCoordinate.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all U values.
        See also: getVertexTextureCoordinate
        """
        return _py3dna.GeometryReader_getVertexTextureCoordinateUs(self, meshIndex)

    def getVertexTextureCoordinateVs(self, meshIndex):
        r"""
        List of all texture coordinate V values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexTextureCoordinate.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all V values.
        See also: getVertexTextureCoordinate
        """
        return _py3dna.GeometryReader_getVertexTextureCoordinateVs(self, meshIndex)

    def getVertexNormalCount(self, meshIndex):
        r"""
        Number of vertex normals in the entire mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getVertexNormalCount(self, meshIndex)

    def getVertexNormal(self, meshIndex, normalIndex):
        r"""
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type normalIndex: int
        :param normalIndex:
                The index of the vertex normal in the zero-indexed array of vertex normals.

            normalIndex must be less than the value returned by getVertexNormalCount.
        :rtype: dna::Normal
        :return: The vertex normal.
        """
        return _py3dna.GeometryReader_getVertexNormal(self, meshIndex, normalIndex)

    def getVertexNormalXs(self, meshIndex):
        r"""
        List of all normal X values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexNormal.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all X values.
        See also: getVertexNormal
        """
        return _py3dna.GeometryReader_getVertexNormalXs(self, meshIndex)

    def getVertexNormalYs(self, meshIndex):
        r"""
        List of all normal Y value for the referenced meshs.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexNormal.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Y values.
        See also: getVertexNormal
        """
        return _py3dna.GeometryReader_getVertexNormalYs(self, meshIndex)

    def getVertexNormalZs(self, meshIndex):
        r"""
        List of all normal Z values for the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexNormal.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Z values.
        See also: getVertexNormal
        """
        return _py3dna.GeometryReader_getVertexNormalZs(self, meshIndex)

    def getVertexLayoutCount(self, meshIndex):
        r"""
        Number of vertex layouts in the entire mesh.
        Notes: 
            A vertex layout is a collection of vertex attributes.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getVertexLayoutCount(self, meshIndex)

    def getVertexLayout(self, meshIndex, layoutIndex):
        r"""
        Vertex layouts contain only attribute indices which can be used to query
            the actual attributes, such as positions, texture coordinates and normals,
            which are associated with the vertex.
        Notes: 
            The indices from a layout are usable with the above defined APIs.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type layoutIndex: int
        :param layoutIndex:
                The index of the layout in the zero-indexed array of vertex layouts.

            layoutIndex must be less than the value returned by getVertexLayoutCount.
        See also: getVertexPosition
        See also: getVertexTextureCoordinate
        See also: getVertexNormal
        """
        return _py3dna.GeometryReader_getVertexLayout(self, meshIndex, layoutIndex)

    def getVertexLayoutPositionIndices(self, meshIndex):
        r"""
        Position indices for each vertex of the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexLayout.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< std::uint32_t >
        :return: View over all vertex position indices values.
        See also: getVertexLayout
        """
        return _py3dna.GeometryReader_getVertexLayoutPositionIndices(self, meshIndex)

    def getVertexLayoutTextureCoordinateIndices(self, meshIndex):
        r"""
        Texture coordinate indices for each vertex of the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexLayout.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< std::uint32_t >
        :return: View over all vertex texture coordinate indices.
        See also: getVertexLayout
        """
        return _py3dna.GeometryReader_getVertexLayoutTextureCoordinateIndices(self, meshIndex)

    def getVertexLayoutNormalIndices(self, meshIndex):
        r"""
        Normal indices for each vertex of the referenced mesh.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getVertexLayout.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :rtype: dna::ConstArrayView< std::uint32_t >
        :return: View over all vertex normal indices.
        See also: getVertexLayout
        """
        return _py3dna.GeometryReader_getVertexLayoutNormalIndices(self, meshIndex)

    def getFaceCount(self, meshIndex):
        r"""
        Number of faces that belong to the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getFaceCount(self, meshIndex)

    def getFaceVertexLayoutIndices(self, meshIndex, faceIndex):
        r"""
        List of vertex layout indices the belong to a face on the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type faceIndex: int
        :param faceIndex:
                A face's position in the zero-indexed array of faces that belong to
                the above referenced mesh.

            faceIndex must be less than the value returned by getFaceCount.
        :rtype: dna::ConstArrayView< std::uint32_t >
        :return: View over the list of vertex layout indices.
        See also: getVertexLayout
        """
        return _py3dna.GeometryReader_getFaceVertexLayoutIndices(self, meshIndex, faceIndex)

    def getMaximumInfluencePerVertex(self, meshIndex):
        r"""
        The maximum number of joints that may influence any single vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getMaximumInfluencePerVertex(self, meshIndex)

    def getSkinWeightsCount(self, meshIndex):
        r"""
        Number of skin weights associated with the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getSkinWeightsCount(self, meshIndex)

    def getSkinWeightsValues(self, meshIndex, vertexIndex):
        r"""
        List of skin weights influencing the requested vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type vertexIndex: int
        :param vertexIndex:
                A position in the zero-indexed array of vertices.

            vertexIndex must be less than the value returned by getVertexPositionCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over the list of skin weights.
        """
        return _py3dna.GeometryReader_getSkinWeightsValues(self, meshIndex, vertexIndex)

    def getSkinWeightsJointIndices(self, meshIndex, vertexIndex):
        r"""
        List of joint indices associated with each skin weight for the specified vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type vertexIndex: int
        :param vertexIndex:
                A position in the zero-indexed array of vertices.

            vertexIndex must be less than the value returned by getVertexPositionCount.
        Notes: 
            The joint indices are stored in the same order as the weights they
            are associated with.
        :rtype: dna::ConstArrayView< std::uint16_t >
        :return: View over the list of joint indices.
        """
        return _py3dna.GeometryReader_getSkinWeightsJointIndices(self, meshIndex, vertexIndex)

    def getBlendShapeTargetCount(self, meshIndex):
        r"""
        Number of blend shapes that belong to the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryReader_getBlendShapeTargetCount(self, meshIndex)

    def getBlendShapeChannelIndex(self, meshIndex, blendShapeTargetIndex):
        r"""
        The matching blend shape channel index of the requested blend shape target.
                   :type meshIndex: int
                   :param meshIndex:
                           A mesh's position in the zero-indexed array of meshes.
                   Warning: 
                       meshIndex must be less than the value returned by getMeshCount.
                   :type blendShapeTargetIndex: int
                   :param blendShapeTargetIndex:
                           A position in the zero-indexed array of blend shape targets within the specified mesh.

                       blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
                   See also: DefinitionReader::getBlendShapeChannelName
        """
        return _py3dna.GeometryReader_getBlendShapeChannelIndex(self, meshIndex, blendShapeTargetIndex)

    def getBlendShapeTargetDeltaCount(self, meshIndex, blendShapeTargetIndex):
        r"""
        Number of deltas that belong to the specified blend shape.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.

            blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
        """
        return _py3dna.GeometryReader_getBlendShapeTargetDeltaCount(self, meshIndex, blendShapeTargetIndex)

    def getBlendShapeTargetDelta(self, meshIndex, blendShapeTargetIndex, deltaIndex):
        r"""
        List of deltas for each affected vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.

            blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
        :type deltaIndex: int
        :param deltaIndex:
                A position in the zero-indexed array of blend shapes deltas.

            deltaIndex must be less than the value returned by getBlendShapeTargetDeltaCount.
        """
        return _py3dna.GeometryReader_getBlendShapeTargetDelta(self, meshIndex, blendShapeTargetIndex, deltaIndex)

    def getBlendShapeTargetDeltaXs(self, meshIndex, blendShapeTargetIndex):
        r"""
        List of all delta X values for the referenced blend shape target.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getBlendShapeTargetDelta.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.

            blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all X values.
        See also: getBlendShapeTargetDelta
        """
        return _py3dna.GeometryReader_getBlendShapeTargetDeltaXs(self, meshIndex, blendShapeTargetIndex)

    def getBlendShapeTargetDeltaYs(self, meshIndex, blendShapeTargetIndex):
        r"""
        List of all delta Y values for the referenced blend shape target.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getBlendShapeTargetDelta.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.

            blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Y values.
        See also: getBlendShapeTargetDelta
        """
        return _py3dna.GeometryReader_getBlendShapeTargetDeltaYs(self, meshIndex, blendShapeTargetIndex)

    def getBlendShapeTargetDeltaZs(self, meshIndex, blendShapeTargetIndex):
        r"""
        List of all delta Z values for the referenced blend shape target.
        Notes: 
            This is an advanced API for performance critical access, for more convenient usage see getBlendShapeTargetDelta.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.

            blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
        :rtype: dna::ConstArrayView< float >
        :return: View over all Z values.
        See also: getBlendShapeTargetDelta
        """
        return _py3dna.GeometryReader_getBlendShapeTargetDeltaZs(self, meshIndex, blendShapeTargetIndex)

    def getBlendShapeTargetVertexIndices(self, meshIndex, blendShapeTargetIndex):
        r"""
        Vertex position indices affected by the referenced blend shape target.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.

            blendShapeTargetIndex must be less than the value returned by getBlendShapeTargetCount.
        Notes: 
            The vertex position indices are stored in the same order as the deltas they
            are associated with.
            These indices can be used to query the associated vertices themselves through getVertexPosition.
        See also: getVertexPosition
        :rtype: dna::ConstArrayView< std::uint32_t >
        :return: View over the list of vertex position indices.
        """
        return _py3dna.GeometryReader_getBlendShapeTargetVertexIndices(self, meshIndex, blendShapeTargetIndex)

# Register GeometryReader in _py3dna:
_py3dna.GeometryReader_swigregister(GeometryReader)

class Reader(BehaviorReader, GeometryReader):
    r"""
    The abstract Reader which its implementations are expected to inherit.
    Notes: 
        This class combines the various different reader interfaces into a single interface.
        The artificial separation into multiple interfaces mirrors the DNA file structure that
        is separated into matching layers under the same names. As these layers can be
        selectively loaded, it might be convenient to slice-off interfaces which layers were
        not loaded.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_Reader

    def unload(self, layer):
        r"""
        Unload all data of the specified layer and all layers dependent on it.
        :type layer: int
        :param layer:
                Layer which data should be unloaded.
        """
        return _py3dna.Reader_unload(self, layer)

# Register Reader in _py3dna:
_py3dna.Reader_swigregister(Reader)

class StreamReader(Reader):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_StreamReader

    def read(self):
        r"""           read data from stream into internal structures."""
        return _py3dna.StreamReader_read(self)

# Register StreamReader in _py3dna:
_py3dna.StreamReader_swigregister(StreamReader)
StreamReader.SignatureMismatchError = _py3dna.cvar.StreamReader_SignatureMismatchError
StreamReader.VersionMismatchError = _py3dna.cvar.StreamReader_VersionMismatchError
StreamReader.InvalidDataError = _py3dna.cvar.StreamReader_InvalidDataError

class BinaryStreamReader(StreamReader):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(*args):
        r"""
        *Overload 1:*

        Factory method for creation of BinaryStreamReader
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Source stream from which data is going to be read.
        :type layer: int, optional
        :param layer:
                Specify the layer up to which the data needs to be loaded.
        Notes: 
            The Definition data layer depends on and thus implicitly loads the Descriptor layer.
            The Behavior data layer depends on and thus implicitly loads the Definition layer.
            The Geometry data layer depends on and thus also implicitly loads the Definition layer.
        :type maxLOD: int, optional
        :param maxLOD:
                The maximum level of details to be loaded.

            A value of zero indicates to load all LODs.
        Warning: 
            The maxLOD value must be less than the value returned by getLODCount.
        See also: getLODCount
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy

        |

        *Overload 2:*

        Factory method for creation of BinaryStreamReader
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Source stream from which data is going to be read.
        :type layer: int
        :param layer:
                Specify the layer up to which the data needs to be loaded.
        Notes: 
            The Definition data layer depends on and thus implicitly loads the Descriptor layer.
            The Behavior data layer depends on and thus implicitly loads the Definition layer.
            The Geometry data layer depends on and thus also implicitly loads the Definition layer.
        :type maxLOD: int
        :param maxLOD:
                The maximum level of details to be loaded.
        :type minLOD: int
        :param minLOD:
                The minimum level of details to be loaded.

            A range of [0, LOD count - 1] for maxLOD / minLOD respectively indicates to load all LODs.
        Warning: 
            Both maxLOD and minLOD values must be less than the value returned by getLODCount.
        See also: getLODCount
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy

        |

        *Overload 3:*

        Factory method for creation of BinaryStreamReader
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Source stream from which data is going to be read.
        :type layer: int
        :param layer:
                Specify the layer up to which the data needs to be loaded.
        Notes: 
            The Definition data layer depends on and thus implicitly loads the Descriptor layer.
            The Behavior data layer depends on and thus implicitly loads the Definition layer.
            The Geometry data layer depends on and thus also implicitly loads the Definition layer.
        :type maxLOD: int
        :param maxLOD:
                The maximum level of details to be loaded.
        :type minLOD: int
        :param minLOD:
                The minimum level of details to be loaded.

            A range of [0, LOD count - 1] for maxLOD / minLOD respectively indicates to load all LODs.
        Warning: 
            Both maxLOD and minLOD values must be less than the value returned by getLODCount.
        See also: getLODCount
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy

        |

        *Overload 4:*

        Factory method for creation of BinaryStreamReader
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Source stream from which data is going to be read.
        :type layer: int
        :param layer:
                Specify the layer up to which the data needs to be loaded.
        Notes: 
            The Definition data layer depends on and thus implicitly loads the Descriptor layer.
            The Behavior data layer depends on and thus implicitly loads the Definition layer.
            The Geometry data layer depends on and thus also implicitly loads the Definition layer.
        :type lods: int
        :param lods:
                An array specifying which exact lods to load.
        Warning: 
            All values in the array must be less than the value returned by getLODCount.
        See also: getLODCount
        :type lodCount: int
        :param lodCount:
                The number of elements in the lods array.

            There cannot be more elements in the array than the value returned by getLODCount.
        See also: getLODCount
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy

        |

        *Overload 5:*

        Factory method for creation of BinaryStreamReader
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Source stream from which data is going to be read.
        :type layer: int
        :param layer:
                Specify the layer up to which the data needs to be loaded.
        Notes: 
            The Definition data layer depends on and thus implicitly loads the Descriptor layer.
            The Behavior data layer depends on and thus implicitly loads the Definition layer.
            The Geometry data layer depends on and thus also implicitly loads the Definition layer.
        :type lods: int
        :param lods:
                An array specifying which exact lods to load.
        Warning: 
            All values in the array must be less than the value returned by getLODCount.
        See also: getLODCount
        :type lodCount: int
        :param lodCount:
                The number of elements in the lods array.

            There cannot be more elements in the array than the value returned by getLODCount.
        See also: getLODCount
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.BinaryStreamReader_create(*args)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a BinaryStreamReader instance.
        :type instance: :py:class:`BinaryStreamReader`
        :param instance:
                Instance of BinaryStreamReader to be freed.
        See also: create
        """
        return _py3dna.BinaryStreamReader_destroy(instance)
    __swig_destroy__ = _py3dna.delete_BinaryStreamReader

# Register BinaryStreamReader in _py3dna:
_py3dna.BinaryStreamReader_swigregister(BinaryStreamReader)

def BinaryStreamReader_create(*args):
    r"""
    *Overload 1:*

    Factory method for creation of BinaryStreamReader
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Source stream from which data is going to be read.
    :type layer: int, optional
    :param layer:
            Specify the layer up to which the data needs to be loaded.
    Notes: 
        The Definition data layer depends on and thus implicitly loads the Descriptor layer.
        The Behavior data layer depends on and thus implicitly loads the Definition layer.
        The Geometry data layer depends on and thus also implicitly loads the Definition layer.
    :type maxLOD: int, optional
    :param maxLOD:
            The maximum level of details to be loaded.

        A value of zero indicates to load all LODs.
    Warning: 
        The maxLOD value must be less than the value returned by getLODCount.
    See also: getLODCount
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy

    |

    *Overload 2:*

    Factory method for creation of BinaryStreamReader
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Source stream from which data is going to be read.
    :type layer: int
    :param layer:
            Specify the layer up to which the data needs to be loaded.
    Notes: 
        The Definition data layer depends on and thus implicitly loads the Descriptor layer.
        The Behavior data layer depends on and thus implicitly loads the Definition layer.
        The Geometry data layer depends on and thus also implicitly loads the Definition layer.
    :type maxLOD: int
    :param maxLOD:
            The maximum level of details to be loaded.
    :type minLOD: int
    :param minLOD:
            The minimum level of details to be loaded.

        A range of [0, LOD count - 1] for maxLOD / minLOD respectively indicates to load all LODs.
    Warning: 
        Both maxLOD and minLOD values must be less than the value returned by getLODCount.
    See also: getLODCount
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy

    |

    *Overload 3:*

    Factory method for creation of BinaryStreamReader
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Source stream from which data is going to be read.
    :type layer: int
    :param layer:
            Specify the layer up to which the data needs to be loaded.
    Notes: 
        The Definition data layer depends on and thus implicitly loads the Descriptor layer.
        The Behavior data layer depends on and thus implicitly loads the Definition layer.
        The Geometry data layer depends on and thus also implicitly loads the Definition layer.
    :type maxLOD: int
    :param maxLOD:
            The maximum level of details to be loaded.
    :type minLOD: int
    :param minLOD:
            The minimum level of details to be loaded.

        A range of [0, LOD count - 1] for maxLOD / minLOD respectively indicates to load all LODs.
    Warning: 
        Both maxLOD and minLOD values must be less than the value returned by getLODCount.
    See also: getLODCount
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy

    |

    *Overload 4:*

    Factory method for creation of BinaryStreamReader
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Source stream from which data is going to be read.
    :type layer: int
    :param layer:
            Specify the layer up to which the data needs to be loaded.
    Notes: 
        The Definition data layer depends on and thus implicitly loads the Descriptor layer.
        The Behavior data layer depends on and thus implicitly loads the Definition layer.
        The Geometry data layer depends on and thus also implicitly loads the Definition layer.
    :type lods: int
    :param lods:
            An array specifying which exact lods to load.
    Warning: 
        All values in the array must be less than the value returned by getLODCount.
    See also: getLODCount
    :type lodCount: int
    :param lodCount:
            The number of elements in the lods array.

        There cannot be more elements in the array than the value returned by getLODCount.
    See also: getLODCount
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy

    |

    *Overload 5:*

    Factory method for creation of BinaryStreamReader
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Source stream from which data is going to be read.
    :type layer: int
    :param layer:
            Specify the layer up to which the data needs to be loaded.
    Notes: 
        The Definition data layer depends on and thus implicitly loads the Descriptor layer.
        The Behavior data layer depends on and thus implicitly loads the Definition layer.
        The Geometry data layer depends on and thus also implicitly loads the Definition layer.
    :type lods: int
    :param lods:
            An array specifying which exact lods to load.
    Warning: 
        All values in the array must be less than the value returned by getLODCount.
    See also: getLODCount
    :type lodCount: int
    :param lodCount:
            The number of elements in the lods array.

        There cannot be more elements in the array than the value returned by getLODCount.
    See also: getLODCount
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.BinaryStreamReader_create(*args)

def BinaryStreamReader_destroy(instance):
    r"""
    Method for freeing a BinaryStreamReader instance.
    :type instance: :py:class:`BinaryStreamReader`
    :param instance:
            Instance of BinaryStreamReader to be freed.
    See also: create
    """
    return _py3dna.BinaryStreamReader_destroy(instance)

class JSONStreamReader(StreamReader):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(stream, memRes=None):
        r"""
        Factory method for creation of JSONStreamReader
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Source stream from which data is going to be read.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.JSONStreamReader_create(stream, memRes)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a JSONStreamReader instance.
        :type instance: :py:class:`JSONStreamReader`
        :param instance:
                Instance of JSONStreamReader to be freed.
        See also: create
        """
        return _py3dna.JSONStreamReader_destroy(instance)
    __swig_destroy__ = _py3dna.delete_JSONStreamReader

# Register JSONStreamReader in _py3dna:
_py3dna.JSONStreamReader_swigregister(JSONStreamReader)

def JSONStreamReader_create(stream, memRes=None):
    r"""
    Factory method for creation of JSONStreamReader
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Source stream from which data is going to be read.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.JSONStreamReader_create(stream, memRes)

def JSONStreamReader_destroy(instance):
    r"""
    Method for freeing a JSONStreamReader instance.
    :type instance: :py:class:`JSONStreamReader`
    :param instance:
            Instance of JSONStreamReader to be freed.
    See also: create
    """
    return _py3dna.JSONStreamReader_destroy(instance)


BinaryStreamReaderImpl = BinaryStreamReader

class BinaryStreamReaderImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(BinaryStreamReaderImpl, name)

    def __dir__(cls):
        return [name for name in dir(BinaryStreamReaderImpl) if name not in ("create","destroy")]

class BinaryStreamReader(with_metaclass(BinaryStreamReaderImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = BinaryStreamReaderImpl.create(*args, **kwargs)

    def __del__(self):
        BinaryStreamReaderImpl.destroy(self._instance)

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


JSONStreamReaderImpl = JSONStreamReader

class JSONStreamReaderImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(JSONStreamReaderImpl, name)

    def __dir__(cls):
        return [name for name in dir(JSONStreamReaderImpl) if name not in ("create","destroy")]

class JSONStreamReader(with_metaclass(JSONStreamReaderImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = JSONStreamReaderImpl.create(*args, **kwargs)

    def __del__(self):
        JSONStreamReaderImpl.destroy(self._instance)

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

class DescriptorWriter(object):
    r"""
    Write-only accessors to various metadata about the character and the rig.
    Warning: 
        Implementors should inherit from Writer itself and not this class.
    See also: Writer
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def setName(self, name):
        r"""
        :type name: string
        :param name:
                A null-terminated string.
        Notes: 
            The passed in name is copied, which will involve an allocation.
        """
        return _py3dna.DescriptorWriter_setName(self, name)

    def setArchetype(self, archetype):
        return _py3dna.DescriptorWriter_setArchetype(self, archetype)

    def setGender(self, gender):
        return _py3dna.DescriptorWriter_setGender(self, gender)

    def setAge(self, age):
        return _py3dna.DescriptorWriter_setAge(self, age)

    def clearMetaData(self):
        r"""            Empties the metadata storage, delete all key-value pairs."""
        return _py3dna.DescriptorWriter_clearMetaData(self)

    def setMetaData(self, key, value):
        r"""
        Associate the metadata value with the given key.
        :type key: string
        :param key:
                A unique, null-terminated key, to which the given value will be assigned.
        :type value: string
        :param value:
                A null-terminated, metadata value, which is to be assigned to the given key.
        Notes: 
            Consecutive calls using the same key will overwrite any existing data.

            Passing nullptr as the value argument will cause the associated key to be deleted.
        """
        return _py3dna.DescriptorWriter_setMetaData(self, key, value)

    def setTranslationUnit(self, unit):
        return _py3dna.DescriptorWriter_setTranslationUnit(self, unit)

    def setRotationUnit(self, unit):
        return _py3dna.DescriptorWriter_setRotationUnit(self, unit)

    def setCoordinateSystem(self, system):
        return _py3dna.DescriptorWriter_setCoordinateSystem(self, system)

    def setLODCount(self, lodCount):
        r"""
        Available levels of detail (e.g. 6 which means the following levels are available:
            [0,1,2,3,4,5], where 0 is the LOD with the highest details, and 5 is the LOD with
            lowest details).
        :type lodCount: int
        :param lodCount:
                The number of levels available.
        """
        return _py3dna.DescriptorWriter_setLODCount(self, lodCount)

    def setDBMaxLOD(self, lod):
        r"""            The maximum level of detail stored in the DNA data for this character."""
        return _py3dna.DescriptorWriter_setDBMaxLOD(self, lod)

    def setDBComplexity(self, name):
        r"""
        Name of the input control interface used to drive this character rig.
        :type name: string
        :param name:
                A null-terminated string.
        Notes: 
            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DescriptorWriter_setDBComplexity(self, name)

    def setDBName(self, name):
        r"""
        Name of the database from which the character originates.
        :type name: string
        :param name:
                A null-terminated string.
        Notes: 
            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DescriptorWriter_setDBName(self, name)

# Register DescriptorWriter in _py3dna:
_py3dna.DescriptorWriter_swigregister(DescriptorWriter)

class DefinitionWriter(DescriptorWriter):
    r"""
    Write-only accessors for DNA attributes that represent the rig's static data.
    Warning: 
        Implementors should inherit from Writer itself and not this class.
    See also: Writer
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def clearGUIControlNames(self):
        r"""            Delete all stored GUI control names."""
        return _py3dna.DefinitionWriter_clearGUIControlNames(self)

    def setGUIControlName(self, index, name):
        r"""
        Name of the specified GUI control.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of GUI control names.
        Notes: 
            The control name storage will be implicitly resized (if needed) to provide
            storage for the number of names that is inferred from the specified index.
        :type name: string
        :param name:
                A null-terminated string.

            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DefinitionWriter_setGUIControlName(self, index, name)

    def clearRawControlNames(self):
        r"""            Delete all stored raw control names."""
        return _py3dna.DefinitionWriter_clearRawControlNames(self)

    def setRawControlName(self, index, name):
        r"""
        Name of the specified raw control.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of raw control names.
        Notes: 
            The control name storage will be implicitly resized (if needed) to provide
            storage for the number of names that is inferred from the specified index.
        :type name: string
        :param name:
                A null-terminated string.

            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DefinitionWriter_setRawControlName(self, index, name)

    def clearJointNames(self):
        r"""            Delete all stored joint names."""
        return _py3dna.DefinitionWriter_clearJointNames(self)

    def setJointName(self, index, name):
        r"""
        Name of the specified joint.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of joint names.
        Notes: 
            The joint name storage will be implicitly resized (if needed) to provide
            storage for the number of names that is inferred from the specified index.
        :type name: string
        :param name:
                A null-terminated string.

            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DefinitionWriter_setJointName(self, index, name)

    def clearJointIndices(self):
        r"""            Delete all stored joint indices."""
        return _py3dna.DefinitionWriter_clearJointIndices(self)

    def setJointIndices(self, index, jointIndices):
        r"""
        Store a list of joint indices onto a specified index.
        :type index: int
        :param index:
                A position in a zero-indexed array where joint indices are stored.
        Notes: 
            The index denotes the position of an entire joint index list,
            not the position of it's individual elements, i.e. the row index in a 2D
            matrix of joint indices.

            The joint index storage will be implicitly resized (if needed) to provide
            storage for the number of joint indices that is inferred from the specified index.
        :type jointIndices: int
        :param jointIndices:
                The source address from which the joint indices are to be copied.

            These indices can be used to access joint names through DefinitionReader::getJointName.
        :type count: int
        :param count:
                The number of joint indices to copy.
        """
        return _py3dna.DefinitionWriter_setJointIndices(self, index, jointIndices)

    def clearLODJointMappings(self):
        r"""            Delete all stored LOD to joint list index mapping entries."""
        return _py3dna.DefinitionWriter_clearLODJointMappings(self)

    def setLODJointMapping(self, lod, index):
        r"""
        Set which joints belong to which level of detail.
        :type lod: int
        :param lod:
                The actual level of detail to which the joints are being associated.
        :type index: int
        :param index:
                The index onto which joints indices were assigned using setJointIndices.
        See also: setJointIndices
        """
        return _py3dna.DefinitionWriter_setLODJointMapping(self, lod, index)

    def clearBlendShapeChannelNames(self):
        r"""            Delete all stored blend shape channel names."""
        return _py3dna.DefinitionWriter_clearBlendShapeChannelNames(self)

    def setBlendShapeChannelName(self, index, name):
        r"""
        Name of the specified blend shape channel.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of blend shape channel names.
        Notes: 
            The blend shape channel name storage will be implicitly resized (if needed) to provide
            storage for the number of names that is inferred from the specified index.
        :type name: string
        :param name:
                A null-terminated string.

            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DefinitionWriter_setBlendShapeChannelName(self, index, name)

    def clearBlendShapeChannelIndices(self):
        r"""            Delete all stored blend shape channel indices."""
        return _py3dna.DefinitionWriter_clearBlendShapeChannelIndices(self)

    def setBlendShapeChannelIndices(self, index, blendShapeChannelIndices):
        r"""
        Store a list of blend shape channel name indices onto a specified index.
        :type index: int
        :param index:
                A position in a zero-indexed array where blend shape channel name indices are stored.
        Notes: 
            The index denotes the position of an entire blend shape channel index list,
            not the position of it's individual elements, i.e. the row index in a 2D
            matrix of blend shape channel indices.

            The blend shape channel index storage will be implicitly resized (if needed) to provide storage
            for the number of blend shape channel name indices that is inferred from the specified index.
        :type blendShapeChannelIndices: int
        :param blendShapeChannelIndices:
                The source address from which the blend shape channel name indices are to be copied.

            These indices can be used to access blend shape channel names through DefinitionReader::getBlendShapeChannelName.
        :type count: int
        :param count:
                The number of blend shape channel name indices to copy.
        """
        return _py3dna.DefinitionWriter_setBlendShapeChannelIndices(self, index, blendShapeChannelIndices)

    def clearLODBlendShapeChannelMappings(self):
        r"""            Delete all stored LOD to blend shape channel list index mapping entries."""
        return _py3dna.DefinitionWriter_clearLODBlendShapeChannelMappings(self)

    def setLODBlendShapeChannelMapping(self, lod, index):
        r"""
        Set which blend shape channels belong to which level of detail.
        :type lod: int
        :param lod:
                The actual level of detail to which the blend shape channels are being associated.
        :type index: int
        :param index:
                The index onto which blend shape channel name indices were assigned using setBlendShapeChannelIndices.
        Warning: 
            The LOD indices set here are not interchangeable with the LOD values set in BehaviorWriter::setBlendShapeChannelLODs.
        See also: setBlendShapeChannelIndices
        """
        return _py3dna.DefinitionWriter_setLODBlendShapeChannelMapping(self, lod, index)

    def clearAnimatedMapNames(self):
        r"""            Delete all stored animated map names."""
        return _py3dna.DefinitionWriter_clearAnimatedMapNames(self)

    def setAnimatedMapName(self, index, name):
        r"""
        Name of the specified animated map.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of animated map names.
        Notes: 
            The animated map name storage will be implicitly resized (if needed) to provide
            storage for the number of names that is inferred from the specified index.
        :type name: string
        :param name:
                A null-terminated string.

            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DefinitionWriter_setAnimatedMapName(self, index, name)

    def clearAnimatedMapIndices(self):
        r"""            Delete all stored animated map indices."""
        return _py3dna.DefinitionWriter_clearAnimatedMapIndices(self)

    def setAnimatedMapIndices(self, index, animatedMapIndices):
        r"""
        Store a list of animated map name indices onto a specified index.
        :type index: int
        :param index:
                A position in a zero-indexed array where animated map name indices are stored.
        Notes: 
            The index denotes the position of an entire animated map index list,
            not the position of it's individual elements, i.e. the row index in a 2D
            matrix of animated map indices.

            The animated map index storage will be implicitly resized (if needed) to provide storage
            for the number of animated map name indices that is inferred from the specified index.
        :type animatedMapIndices: int
        :param animatedMapIndices:
                The source address from which the animated map name indices are to be copied.

            These indices can be used to access animated map names through DefinitionReader::getAnimatedMapName.
        :type count: int
        :param count:
                The number of animated map name indices to copy.
        """
        return _py3dna.DefinitionWriter_setAnimatedMapIndices(self, index, animatedMapIndices)

    def clearLODAnimatedMapMappings(self):
        r"""            Delete all stored LOD to animated map list index mapping entries."""
        return _py3dna.DefinitionWriter_clearLODAnimatedMapMappings(self)

    def setLODAnimatedMapMapping(self, lod, index):
        r"""
        Set which animated maps belong to which level of detail.
        :type lod: int
        :param lod:
                The actual level of detail to which the animated maps are being associated.
        :type index: int
        :param index:
                The index onto which animated map indices were assigned using setAnimatedMapIndices.
        See also: setAnimatedMapIndices
        """
        return _py3dna.DefinitionWriter_setLODAnimatedMapMapping(self, lod, index)

    def clearMeshNames(self):
        r"""            Delete all stored mesh names."""
        return _py3dna.DefinitionWriter_clearMeshNames(self)

    def setMeshName(self, index, name):
        r"""
        Name of the specified mesh.
        :type index: int
        :param index:
                A name's position in the zero-indexed array of mesh names.
        Notes: 
            The mesh name storage will be implicitly resized (if needed) to provide
            storage for the number of names that is inferred from the specified index.
        :type name: string
        :param name:
                A null-terminated string.

            The passed in name is copied, which will involve an additional allocation.
        """
        return _py3dna.DefinitionWriter_setMeshName(self, index, name)

    def clearMeshIndices(self):
        r"""            Delete all stored mesh indices."""
        return _py3dna.DefinitionWriter_clearMeshIndices(self)

    def setMeshIndices(self, index, meshIndices):
        r"""
        Store a list of mesh name indices onto a specified index.
        :type index: int
        :param index:
                A position in a zero-indexed array where mesh name indices are stored.
        Notes: 
            The index denotes the position of an entire mesh index list,
            not the position of it's individual elements, i.e. the row index in a 2D
            matrix of mesh indices.

            The mesh index storage will be implicitly resized (if needed) to provide storage
            for the number of mesh name indices that is inferred from the specified index.
        :type meshIndices: int
        :param meshIndices:
                The source address from which the mesh name indices are to be copied.

            These indices can be used to access mesh names through DefinitionReader::getMeshName.
        :type count: int
        :param count:
                The number of mesh name indices to copy.
        """
        return _py3dna.DefinitionWriter_setMeshIndices(self, index, meshIndices)

    def clearLODMeshMappings(self):
        r"""            Delete all stored LOD to mesh list index mapping entries."""
        return _py3dna.DefinitionWriter_clearLODMeshMappings(self)

    def setLODMeshMapping(self, lod, index):
        r"""
        Set which meshes belong to which level of detail.
        :type lod: int
        :param lod:
                The actual level of detail to which the meshes are being associated.
        :type index: int
        :param index:
                The index onto which mesh indices were assigned using setMeshIndices.
        See also: setMeshIndices
        """
        return _py3dna.DefinitionWriter_setLODMeshMapping(self, lod, index)

    def clearMeshBlendShapeChannelMappings(self):
        r"""            Delete all stored mesh to blend shape channel mapping entries."""
        return _py3dna.DefinitionWriter_clearMeshBlendShapeChannelMappings(self)

    def setMeshBlendShapeChannelMapping(self, index, meshIndex, blendShapeChannelIndex):
        r"""
        Associate a blend shape channel with it's mesh.
        :type index: int
        :param index:
                A mapping's position in the zero-indexed array of mesh-blend shape channel mappings.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of mesh names.
        :type blendShapeChannelIndex: int
        :param blendShapeChannelIndex:
                A blend shape channel's position in the zero-indexed array of blend shape channel names.
        """
        return _py3dna.DefinitionWriter_setMeshBlendShapeChannelMapping(self, index, meshIndex, blendShapeChannelIndex)

    def setJointHierarchy(self, jointIndices):
        r"""
        A simple array describing the parent-child relationships between joints.
        Notes: 
            Example:
            Joint names: [A, B, C, D, E, F, G, H]
            Hierarchy:   [0, 0, 0, 1, 1, 4, 2, 2]
            Describes the following hierarchy:
            A
            + B
            | + D
            | + E
            |   + F
            + C
              + G
              + H
        :type jointIndices: int
        :param jointIndices:
                The source address from which the joint indices are to be copied.

            These indices can be used to access joint names through DefinitionReader::getJointName.
        :type count: int
        :param count:
                The number of joint indices to copy.
        """
        return _py3dna.DefinitionWriter_setJointHierarchy(self, jointIndices)

    def setNeutralJointTranslations(self, translations):
        r"""
        :type translations: dna::Vector3
        :param translations:
                The source address from which the translations are to be copied.
        :type count: int
        :param count:
                The number of translation values to copy.
        """
        return _py3dna.DefinitionWriter_setNeutralJointTranslations(self, translations)

    def setNeutralJointRotations(self, rotations):
        r"""
        :type rotations: dna::Vector3
        :param rotations:
                The source address from which the rotations are to be copied.
        :type count: int
        :param count:
                The number of rotation values to copy.
        """
        return _py3dna.DefinitionWriter_setNeutralJointRotations(self, rotations)

# Register DefinitionWriter in _py3dna:
_py3dna.DefinitionWriter_swigregister(DefinitionWriter)

class BehaviorWriter(DefinitionWriter):
    r"""
    Write-only accessors for DNA attributes that define the rig's evaluation.
    Warning: 
        Implementors should inherit from Writer itself and not this class.
    See also: Writer
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def setGUIToRawInputIndices(self, inputIndices):
        r"""
        Input indices used for mapping gui to raw controls.
        :type inputIndices: int
        :param inputIndices:
                The source address from which the input indices are to be copied.
        :type count: int
        :param count:
                The number of input indices to copy.
        """
        return _py3dna.BehaviorWriter_setGUIToRawInputIndices(self, inputIndices)

    def setGUIToRawOutputIndices(self, outputIndices):
        r"""
        Output indices used for mapping gui to raw controls.
        :type outputIndices: int
        :param outputIndices:
                The source address from which the output indices are to be copied.
        :type count: int
        :param count:
                The number of output indices to copy.
        """
        return _py3dna.BehaviorWriter_setGUIToRawOutputIndices(self, outputIndices)

    def setGUIToRawFromValues(self, fromValues):
        r"""
        Filter values(lower-bounds) used to decide whether a particular
            entry should be evaluated or not during gui to raw control mapping.
        :type fromValues: float
        :param fromValues:
                The source address from which the filter values are to be copied.
        :type count: int
        :param count:
                The number of filter values to copy.
        """
        return _py3dna.BehaviorWriter_setGUIToRawFromValues(self, fromValues)

    def setGUIToRawToValues(self, toValues):
        r"""
        Filter values(upper-bounds) used to decide whether a particular
            entry should be evaluated or not during gui to raw control mapping.
        :type toValues: float
        :param toValues:
                The source address from which the filter values are to be copied.
        :type count: int
        :param count:
                The number of filter values to copy.
        """
        return _py3dna.BehaviorWriter_setGUIToRawToValues(self, toValues)

    def setGUIToRawSlopeValues(self, slopeValues):
        r"""
        Computational values(slope/gradient) used for calculating the
            output value during gui to raw control mapping.
        :type slopeValues: float
        :param slopeValues:
                The source address from which the computational values are to be copied.
        :type count: int
        :param count:
                The number of computational values to copy.
        """
        return _py3dna.BehaviorWriter_setGUIToRawSlopeValues(self, slopeValues)

    def setGUIToRawCutValues(self, cutValues):
        r"""
        Computational values(vertical intercept) used for calculating the
            output value during gui to raw control mapping.
        :type cutValues: float
        :param cutValues:
                The source address from which the computational values are to be copied.
        :type count: int
        :param count:
                The number of computational values to copy.
        """
        return _py3dna.BehaviorWriter_setGUIToRawCutValues(self, cutValues)

    def setPSDCount(self, count):
        r"""            The number of distinct PSD expressions."""
        return _py3dna.BehaviorWriter_setPSDCount(self, count)

    def setPSDRowIndices(self, rowIndices):
        r"""
        PSD(input) indices which will become the rows of the PSD matrix.
        :type rowIndices: int
        :param rowIndices:
                The source address from which the PSD indices are to be copied.
        :type count: int
        :param count:
                The number of PSD indices to copy.
        """
        return _py3dna.BehaviorWriter_setPSDRowIndices(self, rowIndices)

    def setPSDColumnIndices(self, columnIndices):
        r"""
        Control(input) indices which will become the columns of the PSD matrix.
        :type columnIndices: int
        :param columnIndices:
                The source address from which the control indices are to be copied.
        :type count: int
        :param count:
                The number of control indices to copy.
        """
        return _py3dna.BehaviorWriter_setPSDColumnIndices(self, columnIndices)

    def setPSDValues(self, weights):
        r"""
        Weights associated with each PSD row and column pair.
        :type weights: float
        :param weights:
                The source address from which the weight values are to be copied.
        :type count: int
        :param count:
                The number of weight values to copy.
        """
        return _py3dna.BehaviorWriter_setPSDValues(self, weights)

    def setJointRowCount(self, rowCount):
        r"""            Number of rows in the entire, uncompressed joint matrix."""
        return _py3dna.BehaviorWriter_setJointRowCount(self, rowCount)

    def setJointColumnCount(self, columnCount):
        r"""            Number of columns in the entire, uncompressed joint matrix."""
        return _py3dna.BehaviorWriter_setJointColumnCount(self, columnCount)

    def clearJointGroups(self):
        r"""            Delete all joint groups."""
        return _py3dna.BehaviorWriter_clearJointGroups(self)

    def deleteJointGroup(self, jointGroupIndex):
        r"""
        Delete the specified joint group.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Warning: 
            jointGroupIndex must be less than the value returned by getJointGroupCount.
        """
        return _py3dna.BehaviorWriter_deleteJointGroup(self, jointGroupIndex)

    def setJointGroupLODs(self, jointGroupIndex, lods):
        r"""
        Number of rows per each level of detail for the specified joint group.
        Notes: 
            Each element's position represents the level itself, while the value denotes
            the number of rows within the joint group belonging to that level. e.g.:
            [12, 9, 3]
             |   |  + LOD-2 contains first 3 rows
             |   + LOD-1 contains first 9 rows
             + LOD-0 contains first 12 rows
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.

            The joint group storage will be implicitly resized (if needed) to provide
            storage for the number of joint groups that is inferred from the specified index.
        :type lods: int
        :param lods:
                The source address from which the lod bounds are to be copied.
        :type count: int
        :param count:
                The number of lod bounds to copy.
        """
        return _py3dna.BehaviorWriter_setJointGroupLODs(self, jointGroupIndex, lods)

    def setJointGroupInputIndices(self, jointGroupIndex, inputIndices):
        r"""
        Column indices that the specified joint group contains.
        Notes: 
            The column indices point into the entire, uncompressed joint matrix.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.

            The joint group storage will be implicitly resized (if needed) to provide
            storage for the number of joint groups that is inferred from the specified index.
        :type inputIndices: int
        :param inputIndices:
                The source address from which the column indices are to be copied.
        :type count: int
        :param count:
                The number of column indices to copy.
        """
        return _py3dna.BehaviorWriter_setJointGroupInputIndices(self, jointGroupIndex, inputIndices)

    def setJointGroupOutputIndices(self, jointGroupIndex, outputIndices):
        r"""
        Row indices that the specified joint group contains.
        Notes: 
            The row indices point into the entire, uncompressed joint matrix.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.

            The joint group storage will be implicitly resized (if needed) to provide
            storage for the number of joint groups that is inferred from the specified index.
        :type outputIndices: int
        :param outputIndices:
                The source address from which the row indices are to be copied.
        :type count: int
        :param count:
                The number of row indices to copy.
        """
        return _py3dna.BehaviorWriter_setJointGroupOutputIndices(self, jointGroupIndex, outputIndices)

    def setJointGroupValues(self, jointGroupIndex, values):
        r"""
        Values that the specified joint group contains.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Notes: 
            The joint group storage will be implicitly resized (if needed) to provide
            storage for the number of joint groups that is inferred from the specified index.
        :type values: float
        :param values:
                The source address from which the values are to be copied.
        :type count: int
        :param count:
                The number of values to copy.
        """
        return _py3dna.BehaviorWriter_setJointGroupValues(self, jointGroupIndex, values)

    def setJointGroupJointIndices(self, jointGroupIndex, jointIndices):
        r"""
        Joint indices that the specified joint group contains.
        :type jointGroupIndex: int
        :param jointGroupIndex:
                A joint group's position in the zero-indexed array of joint groups.
        Notes: 
            The joint group storage will be implicitly resized (if needed) to provide
            storage for the number of joint groups that is inferred from the specified index.
        :type jointIndices: int
        :param jointIndices:
                The source address from which the joint indices are to be copied.
        :type count: int
        :param count:
                The number of joint indices to copy.
        """
        return _py3dna.BehaviorWriter_setJointGroupJointIndices(self, jointGroupIndex, jointIndices)

    def setBlendShapeChannelLODs(self, lods):
        r"""
        Input index count per each level of detail for blend shapes.
        Notes: 
            Each element's position represents the level itself  (e.g. [0,1,2,3,4,5] Value 0 is LOD with highest of details,
            value 5 is LOD with lowest details), while the value denotes the number of input indices belonging to that level.
        :type lods: int
        :param lods:
                The source address from which the lod bounds are to be copied.
        :type count: int
        :param count:
                The number of lod bounds to copy.
        Warning: 
            The LOD values set here are not interchangeable with the LOD indices set in DefinitionWriter::setBlendShapeNameIndices
            and DefinitionWriter::setLODBlendShapeMapping
        """
        return _py3dna.BehaviorWriter_setBlendShapeChannelLODs(self, lods)

    def setBlendShapeChannelInputIndices(self, inputIndices):
        r"""
        Input indices used to index into the input vector.
        :type inputIndices: int
        :param inputIndices:
                The source address from which the input indices are to be copied.
        :type count: int
        :param count:
                The number of input indices to copy.
        """
        return _py3dna.BehaviorWriter_setBlendShapeChannelInputIndices(self, inputIndices)

    def setBlendShapeChannelOutputIndices(self, outputIndices):
        r"""
        Output indices specify the positions of blend shape output values.
        :type outputIndices: int
        :param outputIndices:
                The source address from which the output indices are to be copied.
        :type count: int
        :param count:
                The number of output indices to copy.
        """
        return _py3dna.BehaviorWriter_setBlendShapeChannelOutputIndices(self, outputIndices)

    def setAnimatedMapLODs(self, lods):
        r"""
        Row count per each level of detail for animated maps.
        Notes: 
            Each element's position represents the level itself  (e.g. [0,1,2,3,4,5] Value 0 is LOD with highest of details,
            value 5 is LOD with lowest details), while the value denotes the number of rows (within the conditional table),
            belonging to that level.
        :type lods: int
        :param lods:
                The source address from which the lod bounds are to be copied.
        :type count: int
        :param count:
                The number of lod bounds to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapLODs(self, lods)

    def setAnimatedMapInputIndices(self, inputIndices):
        r"""
        Input indices used to index into the array of input values.
        :type inputIndices: int
        :param inputIndices:
                The source address from which the input indices are to be copied.
        :type count: int
        :param count:
                The number of input indices to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapInputIndices(self, inputIndices)

    def setAnimatedMapOutputIndices(self, outputIndices):
        r"""
        Output indices that specify the computed output value's position.
        :type outputIndices: int
        :param outputIndices:
                The source address from which the output indices are to be copied.
        :type count: int
        :param count:
                The number of output indices to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapOutputIndices(self, outputIndices)

    def setAnimatedMapFromValues(self, fromValues):
        r"""
        Filter values(lower-bounds) used to decide whether a particular
            entry should be evaluated or not.
        :type fromValues: float
        :param fromValues:
                The source address from which the filter values are to be copied.
        :type count: int
        :param count:
                The number of filter values to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapFromValues(self, fromValues)

    def setAnimatedMapToValues(self, toValues):
        r"""
        Filter values(upper-bounds) used to decide whether a particular
            entry should be evaluated or not.
        :type toValues: float
        :param toValues:
                The source address from which the filter values are to be copied.
        :type count: int
        :param count:
                The number of filter values to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapToValues(self, toValues)

    def setAnimatedMapSlopeValues(self, slopeValues):
        r"""
        Computational values(slope/gradient) used for calculating the output value.
        :type slopeValues: float
        :param slopeValues:
                The source address from which the computational values are to be copied.
        :type count: int
        :param count:
                The number of computational values to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapSlopeValues(self, slopeValues)

    def setAnimatedMapCutValues(self, cutValues):
        r"""
        Computational values(vertical intercept) used for calculating the output value.
        :type cutValues: float
        :param cutValues:
                The source address from which the computational values are to be copied.
        :type count: int
        :param count:
                The number of computational values to copy.
        """
        return _py3dna.BehaviorWriter_setAnimatedMapCutValues(self, cutValues)

# Register BehaviorWriter in _py3dna:
_py3dna.BehaviorWriter_swigregister(BehaviorWriter)

class GeometryWriter(DefinitionWriter):
    r"""
    Write-only accessors for the geometry data associated with a rig.
    Warning: 
        Implementors should inherit from Writer itself and not this class.
    See also: Writer
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def clearMeshes(self):
        r"""            Delete all meshes."""
        return _py3dna.GeometryWriter_clearMeshes(self)

    def deleteMesh(self, meshIndex):
        r"""
        Delete the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryWriter_deleteMesh(self, meshIndex)

    def setVertexPositions(self, meshIndex, positions):
        r"""
        List of vertex positions.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type positions: dna::Position
        :param positions:
                The source address from which the vertex positions are to be copied.
        :type count: int
        :param count:
                The number of vertex positions to copy.
        Notes: 
            The mesh storage will be implicitly resized (if needed) to provide
            storage for the number of meshes that is inferred from the specified index.
        """
        return _py3dna.GeometryWriter_setVertexPositions(self, meshIndex, positions)

    def setVertexTextureCoordinates(self, meshIndex, textureCoordinates):
        r"""
        List of vertex texture coordinates.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type textureCoordinates: dna::TextureCoordinate
        :param textureCoordinates:
                The source address from which the texture coordinates are to be copied.
        :type count: int
        :param count:
                The number of texture coordinates to copy.
        Notes: 
            The mesh storage will be implicitly resized (if needed) to provide
            storage for the number of meshes that is inferred from the specified index.
        """
        return _py3dna.GeometryWriter_setVertexTextureCoordinates(self, meshIndex, textureCoordinates)

    def setVertexNormals(self, meshIndex, normals):
        r"""
        List of vertex normals.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type normals: dna::Normal
        :param normals:
                The source address from which the normals are to be copied.
        :type count: int
        :param count:
                The number of normals to copy.
        Notes: 
            The mesh storage will be implicitly resized (if needed) to provide
            storage for the number of meshes that is inferred from the specified index.
        """
        return _py3dna.GeometryWriter_setVertexNormals(self, meshIndex, normals)

    def setVertexLayouts(self, meshIndex, layouts):
        r"""
        List of vertex layouts the belong to the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type layouts: dna::VertexLayout
        :param layouts:
                The source address from which the layouts are to be copied.
        :type count: int
        :param count:
                The number of layouts to copy.
        Notes: 
            The mesh storage will be implicitly resized (if needed) to provide
            storage for the number of meshes that is inferred from the specified index.
        """
        return _py3dna.GeometryWriter_setVertexLayouts(self, meshIndex, layouts)

    def clearFaceVertexLayoutIndices(self, meshIndex):
        r"""
        Delete all lists of vertex layout indices for the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryWriter_clearFaceVertexLayoutIndices(self, meshIndex)

    def setFaceVertexLayoutIndices(self, meshIndex, faceIndex, layoutIndices):
        r"""
        Vertex layout indices that belong to the specified face.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type faceIndex: int
        :param faceIndex:
                A face's position in the zero-indexed array of faces that belong to
                the above referenced mesh.
        :type layoutIndices: int
        :param layoutIndices:
                The source address from which the layout indices are to be copied.
        Notes: 
            The layout indices point into the array that is set through setVertexLayouts
        :type count: int
        :param count:
                The number of vertices to copy.

            Both the mesh storage itself and it's face storage will be implicitly
            resized (if needed) to provide storage for the number of meshes and/or
            faces that are inferred from the specified indexes.
        """
        return _py3dna.GeometryWriter_setFaceVertexLayoutIndices(self, meshIndex, faceIndex, layoutIndices)

    def setMaximumInfluencePerVertex(self, meshIndex, maxInfluenceCount):
        r"""
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type maxInfluenceCount: int
        :param maxInfluenceCount:
                The maximum number of joints that may influence any single vertex.
        """
        return _py3dna.GeometryWriter_setMaximumInfluencePerVertex(self, meshIndex, maxInfluenceCount)

    def clearSkinWeights(self, meshIndex):
        r"""
        Delete all skin weights for the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryWriter_clearSkinWeights(self, meshIndex)

    def setSkinWeightsValues(self, meshIndex, vertexIndex, weights):
        r"""
        List of skin weights influencing the referenced vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type vertexIndex: int
        :param vertexIndex:
                A position in the zero-indexed array of vertex positions.
        :type weights: float
        :param weights:
                The source address from which the weights are to be copied.
        :type count: int
        :param count:
                The number of weights to copy.
        Notes: 
            Both the mesh storage itself and it's skin weight storage will be implicitly
            resized (if needed) to provide storage for the number of meshes and/or
            skin-weight lists that are inferred from the specified indexes.
        Warning: 
            The sum of weights must add up to 1.
        """
        return _py3dna.GeometryWriter_setSkinWeightsValues(self, meshIndex, vertexIndex, weights)

    def setSkinWeightsJointIndices(self, meshIndex, vertexIndex, jointIndices):
        r"""
        List of joint indices associated with each skin weight for the specified vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type vertexIndex: int
        :param vertexIndex:
                A position in the zero-indexed array of vertex positions.
        :type jointIndices: int
        :param jointIndices:
                The source address from which the joint indices are to be copied.
        :type count: int
        :param count:
                The number of joint indices to copy.
        Notes: 
            Both the mesh storage itself and it's joint index list storage will be implicitly
            resized (if needed) to provide storage for the number of meshes and/or
            joint index lists that are inferred from the specified indexes.
        Warning: 
            The joint indices must be stored in the same order as the weights they
            are associated with.
        """
        return _py3dna.GeometryWriter_setSkinWeightsJointIndices(self, meshIndex, vertexIndex, jointIndices)

    def clearBlendShapeTargets(self, meshIndex):
        r"""
        Delete all blend shape targets for the specified mesh.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        Warning: 
            meshIndex must be less than the value returned by getMeshCount.
        """
        return _py3dna.GeometryWriter_clearBlendShapeTargets(self, meshIndex)

    def setBlendShapeChannelIndex(self, meshIndex, blendShapeTargetIndex, blendShapeChannelIndex):
        r"""
        The matching blend shape channel index of the specified blend shape target.
                   Notes: 
                       Associate the mesh-local blend shape target index with the absolute blend shape channel
                       index as found in the Definition layer.
                   :type meshIndex: int
                   :param meshIndex:
                           A mesh's position in the zero-indexed array of meshes.
                   :type blendShapeTargetIndex: int
                   :param blendShapeTargetIndex:
                           A position in the zero-indexed array of blend shape targets within the specified mesh.
                   :type blendShapeChannelIndex: int
                   :param blendShapeChannelIndex:
                           The index of the specified blend shape channel in the Definition layer.

                       Both the mesh storage itself and it's blend shape target storage will be implicitly
                       resized (if needed) to provide storage for the number of meshes and/or
                       blend shape targets that are inferred from the specified indexes.
        """
        return _py3dna.GeometryWriter_setBlendShapeChannelIndex(self, meshIndex, blendShapeTargetIndex, blendShapeChannelIndex)

    def setBlendShapeTargetDeltas(self, meshIndex, blendShapeTargetIndex, deltas):
        r"""
        List of deltas for each affected vertex.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.
        :type deltas: dna::Delta
        :param deltas:
                The source address from which the blend shape target deltas are to be copied.
        :type count: int
        :param count:
                The number of blend shape target deltas to copy.
        Notes: 
            Both the mesh storage itself and it's blend shape target storage will be implicitly
            resized (if needed) to provide storage for the number of meshes and/or
            blend shape targets that are inferred from the specified indexes.
        """
        return _py3dna.GeometryWriter_setBlendShapeTargetDeltas(self, meshIndex, blendShapeTargetIndex, deltas)

    def setBlendShapeTargetVertexIndices(self, meshIndex, blendShapeTargetIndex, vertexIndices):
        r"""
        Vertex position indices affected by the specified blend shape target.
        :type meshIndex: int
        :param meshIndex:
                A mesh's position in the zero-indexed array of meshes.
        :type blendShapeTargetIndex: int
        :param blendShapeTargetIndex:
                A position in the zero-indexed array of blend shape targets within the specified mesh.
        :type vertexIndices: int
        :param vertexIndices:
                The source address from which the vertex position indices are to be copied.
        :type count: int
        :param count:
                The number of vertex position indices to copy.
        Notes: 
            Both the mesh storage itself and it's blend shape target storage will be implicitly
            resized (if needed) to provide storage for the number of meshes and/or
            blend shape targets that are inferred from the specified indexes.
        Warning: 
            The vertex position indices must be stored in the same order as the deltas
            they are associated with.
        """
        return _py3dna.GeometryWriter_setBlendShapeTargetVertexIndices(self, meshIndex, blendShapeTargetIndex, vertexIndices)

# Register GeometryWriter in _py3dna:
_py3dna.GeometryWriter_swigregister(GeometryWriter)

class Writer(BehaviorWriter, GeometryWriter):
    r"""
    The abstract Writer which its implementations are expected to inherit.
    Notes: 
        This class combines the various different writer interfaces into a single interface.
        The artificial separation into multiple interfaces in this case just mirrors the
        structure of the Reader hierarchy, as it's not possible to selectively write only
        specific layers.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_Writer

    def setFrom(self, *args):
        r"""
        Initialize the Writer from the given Reader.
        Notes: 
            This function copies all the data from the given Reader into the Writer instance,
            by calling each getter function of the Reader, and passing the return values to
            the matching setter functions in the Writer.
            It is implemented in the abstract class itself to provide the functionality for
            all DNA Writers.
        :type source: :py:class:`Reader`
        :param source:
                The source DNA Reader from which the data needs to be copied.
        :type layer: int, optional
        :param layer:
                Limit which layers should be taken over from the given source reader.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Optional memory resource to use for temporary allocations during copying.
        """
        return _py3dna.Writer_setFrom(self, *args)

# Register Writer in _py3dna:
_py3dna.Writer_swigregister(Writer)

class StreamWriter(Writer):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dna.delete_StreamWriter

    def write(self):
        r"""            Write data to stream from internal structures."""
        return _py3dna.StreamWriter_write(self)

# Register StreamWriter in _py3dna:
_py3dna.StreamWriter_swigregister(StreamWriter)

class BinaryStreamWriter(StreamWriter):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(stream, memRes=None):
        r"""
        Factory method for creation of BinaryStreamWriter
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Stream into which the data is going to be written.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.BinaryStreamWriter_create(stream, memRes)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a BinaryStreamWriter instance.
        :type instance: :py:class:`BinaryStreamWriter`
        :param instance:
                Instance of BinaryStreamWriter to be freed.
        See also: create
        """
        return _py3dna.BinaryStreamWriter_destroy(instance)
    __swig_destroy__ = _py3dna.delete_BinaryStreamWriter

# Register BinaryStreamWriter in _py3dna:
_py3dna.BinaryStreamWriter_swigregister(BinaryStreamWriter)

def BinaryStreamWriter_create(stream, memRes=None):
    r"""
    Factory method for creation of BinaryStreamWriter
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Stream into which the data is going to be written.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.BinaryStreamWriter_create(stream, memRes)

def BinaryStreamWriter_destroy(instance):
    r"""
    Method for freeing a BinaryStreamWriter instance.
    :type instance: :py:class:`BinaryStreamWriter`
    :param instance:
            Instance of BinaryStreamWriter to be freed.
    See also: create
    """
    return _py3dna.BinaryStreamWriter_destroy(instance)

class JSONStreamWriter(StreamWriter):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(stream, indentWidth=4, memRes=None):
        r"""
        Factory method for creation of JSONStreamWriter
        :type stream: :py:class:`BoundedIOStream`
        :param stream:
                Stream into which the data is going to be written.
        :type indentWidth: int, optional
        :param indentWidth:
                Number of spaces to use for indentation.
        :type memRes: :py:class:`MemoryResource`, optional
        :param memRes:
                Memory resource to be used for allocations.
        Notes: 
            If a memory resource is not given, a default allocation mechanism will be used.
        Warning: 
            User is responsible for releasing the returned pointer by calling destroy.
        See also: destroy
        """
        return _py3dna.JSONStreamWriter_create(stream, indentWidth, memRes)

    @staticmethod
    def destroy(instance):
        r"""
        Method for freeing a JSONStreamWriter instance.
        :type instance: :py:class:`JSONStreamWriter`
        :param instance:
                Instance of JSONStreamWriter to be freed.
        See also: create
        """
        return _py3dna.JSONStreamWriter_destroy(instance)
    __swig_destroy__ = _py3dna.delete_JSONStreamWriter

# Register JSONStreamWriter in _py3dna:
_py3dna.JSONStreamWriter_swigregister(JSONStreamWriter)

def JSONStreamWriter_create(stream, indentWidth=4, memRes=None):
    r"""
    Factory method for creation of JSONStreamWriter
    :type stream: :py:class:`BoundedIOStream`
    :param stream:
            Stream into which the data is going to be written.
    :type indentWidth: int, optional
    :param indentWidth:
            Number of spaces to use for indentation.
    :type memRes: :py:class:`MemoryResource`, optional
    :param memRes:
            Memory resource to be used for allocations.
    Notes: 
        If a memory resource is not given, a default allocation mechanism will be used.
    Warning: 
        User is responsible for releasing the returned pointer by calling destroy.
    See also: destroy
    """
    return _py3dna.JSONStreamWriter_create(stream, indentWidth, memRes)

def JSONStreamWriter_destroy(instance):
    r"""
    Method for freeing a JSONStreamWriter instance.
    :type instance: :py:class:`JSONStreamWriter`
    :param instance:
            Instance of JSONStreamWriter to be freed.
    See also: create
    """
    return _py3dna.JSONStreamWriter_destroy(instance)


BinaryStreamWriterImpl = BinaryStreamWriter

class BinaryStreamWriterImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(BinaryStreamWriterImpl, name)

    def __dir__(cls):
        return [name for name in dir(BinaryStreamWriterImpl) if name not in ("create","destroy")]

class BinaryStreamWriter(with_metaclass(BinaryStreamWriterImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = BinaryStreamWriterImpl.create(*args, **kwargs)

    def __del__(self):
        BinaryStreamWriterImpl.destroy(self._instance)

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


JSONStreamWriterImpl = JSONStreamWriter

class JSONStreamWriterImplReflectionMixin(type):

    def __getattr__(cls, name):
        return getattr(JSONStreamWriterImpl, name)

    def __dir__(cls):
        return [name for name in dir(JSONStreamWriterImpl) if name not in ("create","destroy")]

class JSONStreamWriter(with_metaclass(JSONStreamWriterImplReflectionMixin, object)):
    __slots__ = ('_args', '_kwargs', '_instance')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._instance = JSONStreamWriterImpl.create(*args, **kwargs)

    def __del__(self):
        JSONStreamWriterImpl.destroy(self._instance)

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



