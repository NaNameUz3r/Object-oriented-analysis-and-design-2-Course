from task_9_solution import Any, General
from task_11_solution import Void

# здесь наследуем General от General только для сокращения кода решения. На практике так делать не стоит.
class General(General):

    ASSIGNMENT_NIL = 0
    ASSIGNMENT_OK = 1
    ASSIGNMENT_MISSMATCH = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._assignment_status = self.ASSIGNMENT_NIL

    def assignment_attempt(self, target_name: str, source) -> None:
        target_type = type(getattr(self, target_name))
        if isinstance(source, target_type):
            setattr(self, target_name, source)
            self._assignment_status = self.ASSIGNMENT_OK
        else:
            setattr(self, target_name, Void())
            self._assignment_status = self.ASSIGNMENT_MISSMATCH

    def get_assignment_attempt_status(self) -> int:
        """Last assignment_attempt() call status"""
        return self._assignment_status

class Any(General, Any): ...


class Vehicle:
    def drive(self):
        print('Vehicle is driving')


class Car_(Vehicle, Any): ...

class Aircraft:
    def fly(self):
        print("Aircraft is flying")

class Plane_(Aircraft, Any): ...

class Human(Any):
    def driving(self):
        print(f'{type(self).__name__} ontrols a transport')

class Driver(Human):
    def __init__(self, vehicle: Any,
                 *args, **kwargs):
        super().__init__(vehicle, *args, **kwargs)
        self.vehicle = vehicle


vehicle1 = Vehicle()
driver = Driver(vehicle1)

someCar = Car_()
somePlane = Plane_()
driver.assignment_attempt('vehicle', someCar)
print(driver.get_assignment_attempt_status())
# 1
driver.assignment_attempt('vehicle', somePlane)
print(driver.get_assignment_attempt_status())
# 2