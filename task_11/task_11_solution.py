
from task_9.task_9_solution import Any

void = None
Void = type(None)


class VoidType:
    def __new__(self, *args, **kwargs):
        return void

class Vehicle:
    def drive(self):
        print('Vehicle is driving')

class Car(Vehicle):
    def drive(self):
        print('Car is driving')

class Car_(Car, Any):
    ...


class CarHierarchyClosure(Car_, VoidType):
    ...

# с = CarHierarchyClosure()
# c.serializer()
# ^ вызовет ошибку 'NoneType' object has no attribute 'serialize'
