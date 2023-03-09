from __future__ import annotations
import json
from copy import deepcopy
from typing import final, TypeVar


_T = TypeVar('_T')

class General(object):

    COPY_NIL = 0       # copy() was not called
    COPY_OK = 1        # last copy() call completed ok
    COPY_ATTR_ERR = 2  # other object have no attribute copied from this object

    def __init__(self, *args, **kwargs):
        self._copy_status = self.COPY_NIL

    @final
    def copy(self, other: _T) -> None:
        """Copy the contents of one object to another existing object."""
        if type(self) == type(other):
            for atrribute in vars(other):
                if not atrribute.endswith('status'):
                    setattr(self, atrribute, self.deepcopy(getattr(other, atrribute)))
            self._copy_status = self.COPY_OK
        else:
            self._copy_status = self.COPY_ATTR_ERR
            raise TypeError(f"Can't copy object of type {type(other).__name__} to object of type {type(self).__name__}")

    @final
    def clone(self):
        """Create a new object and deeply copy the contents of the original object."""
        return self.deepcopy(self)

    @final
    def __eq__(self, other: _T) -> bool:
        """Compare two objects for equality."""
        if type(self) != type(other):
            return False
        return vars(self) == vars(other)

    @final
    def __ne__(self, other):
        """Compare two objects for inequality."""
        return not self.__eq__(other)

    @final
    def serialize(self):
        """Return a string representation of the object suitable for I/O."""
        return json.dumps(vars(self))

    @final
    @classmethod
    def deserialize(cls, json_str):
        """Create a new object and set its contents based on the provided string."""
        obj = cls()
        atrributes = json.loads(json_str)
        for atrribute in atrributes:
            setattr(obj, atrribute, atrributes[atrribute])
        return obj

    def __str__(self):
        """Return a string representation of the object."""
        return f"{type(self).__name__}: {str(self.__dict__)}"

    def is_instance(self, cls):
        """Return True if the object is an instance of the specified type."""
        return isinstance(self, cls)

    def get_real_class(self):
        """Return the actual class of the object."""
        return type(self)


class Any(General):
    pass
