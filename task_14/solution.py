from typing import Any as AnyT, Union

from task_9_solution import Any, General
from task_11_solution import Void

class General(General):
    ...

class Any(General, Any):
    def __add__(self, other):
        raise NotImplementedError()


class Vector(Any):

    def __init__(self, *args: AnyT, **kwargs):
        super().__init__(*args, **kwargs)
        self.seq = args
        self._size = len(args)

    def __add__(self, other: 'Vector') -> Union['Vector', Void]:
        if self._size != other._size:
            vector_sum = Void
        else:
            vector_sum = self._add_vectors(other)

        return vector_sum

    def _add_vectors(self, other: 'Vector') -> 'Vector':
        sum_seq = []
        for item_1, item_2 in zip(self.seq, other.seq):
            sum_seq.append(item_1 + item_2)

        sum_vector = Vector(*sum_seq)
        return sum_vector

    def traverse_sequences(self) -> tuple:
        _self_func_name = self.traverse_sequences.__name__
        return tuple(getattr(item, _self_func_name, lambda: item)() for item in self.seq)

# vector1 = Vector(1,2,3)
# vector2 = Vector(2,2,2)
# vector3 = Vector(666)
# vector4 = Vector(999)
# print(vector1+vector3 is Void)
# # >>> True
# print((vector1+vector2).seq)
# # # >>> (3,4,5)
# nested_vectors_1 = Vector(Vector(vector1), Vector(vector2))
# nested_vectors_2 = Vector(Vector(vector3), Vector(vector4))
# print(nested_vectors_1.traverse_sequences())
# # >>> (((1, 2, 3),), ((2, 2, 2),))
# print(nested_vectors_2.traverse_sequences())
# # >>> (((666,),), ((999,),))