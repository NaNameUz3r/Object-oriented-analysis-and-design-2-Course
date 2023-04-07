# functional variation inheritance
class Animal:
    def move(self):
        print("Animal moves.")

class Dog(Animal):
    def move(self):
        print("Dog runs.")

class Bird(Animal):
    def move(self):
        print("Bird flies.")

class FlyingDog(Dog):
    def move(self):
        print("FlyingDog flies and runs.")

fido = Dog()
fido.move() # Output: "Dog runs."

tweety = Bird()
tweety.move() # Output: "Bird flies."

airbud = FlyingDog()
airbud.move() # Output: "FlyingDog flies and runs."

###################################################
# type variation inheritance


# Допустим, у нас есть класс Vehicle,
# представляющий любой вид транспорта,
# с базовыми методами move() и stop():
class Vehicle:
    def move(self):
        print("Moving...")

    def stop(self):
        print("Stopping...")

# Теперь мы создаем наследника Car, в котором перегрузим метод move(),
# определив в методе дополнительный аргумент speed:
class Car(Vehicle):
    @overload
    def move(self, speed):
        print(f"Driving at {speed} km/h...")

# Здесь мы переопределяем метод move() с новой сигнатурой (добавлен аргумент speed).
# Теперь, если мы создадим объект Car и вызовем его методы move() и stop(),
# то будет использована новая реализация move() из класса Car, а stop() будет унаследована от родительского класса:
car = Car()
car.move(100) # Output: Driving at 100 km/h...
car.stop() # Output: Stopping...


###################################################
# reification inheritance

# Похоже что это главный лейтмотив, пронизывающий большую часть, если не все занятия по ООАП, как конкретная реализацию наследуемого АТД.

# Предположим некоторый абстрактный класс, представляющий конечный автомат,
# который может переходить между несколькими состояниями,
# выполнять действия при переходе и определять, какие переходы допустимы.
# В этом классе могут быть определены абстрактные методы, которые будут реализованы в классах-наследниках,
# представляющих конкретные конечные автоматы.
class FiniteStateMachine:
    def __init__(self):
        self.current_state = None

    def set_state(self, state):
        self.current_state = state

    def get_state(self):
        return self.current_state

    def execute_action(self):
        pass

    def get_allowed_transitions(self):
        pass


# Реализуем класс-наследник, имплементирующий конечный автомат,
# который реагирует на входные сигналы и переходит между различными состояниями

class SignalDetector(FiniteStateMachine):
    def __init__(self):
        super().__init__()
        self.set_state("IDLE")

    def execute_action(self):
        print("Signal detected!")
        self.set_state("DETECTED")

    def get_allowed_transitions(self):
        if self.current_state == "IDLE":
            return ["DETECTED"]
        else:
            return []

# Здесь метод execute_action переопределен для выполнения действия, связанного с обнаружением сигнала, а метод get_allowed_transitions определен для определения допустимых переходов из текущего состояния.

detector = SignalDetector()
print(detector.get_state()) # IDLE
detector.set_state("DETECTED")
print(detector.get_state()) # DETECTED


###################################################
# structure inheritance


# Cоздадим класс SortableList, который наследуется от класса list из стандартной библиотеки,
# и добавим метод sorted, который возвращает отсортированный список.
# Затем создадим класс насследник UniqueSortedList от SortableList
# и имплементируем новое свойство: добавление только уникальных элементов при использовании метода append.
# Кроме того, мы переопределили методы __add__ и __iadd__, чтобы поддерживать добавление других списков к UniqueSortedList.
#
# Кажется, что этот пример демонстрирует структурное наследование,
# потому что мы не просто конкретизировали стандартный список, а добавили качественно новую абстракцию.


from typing import List, Tuple

class SortableList(List[int]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sorted(self) -> List[int]:
        return sorted(self)


class UniqueSortedList(SortableList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append(self, x: int):
        if x not in self:
            super().append(x)

    def __add__(self, other: List[int]) -> "UniqueSortedList":
        return UniqueSortedList(super().__add__(other))

    def __iadd__(self, other: List[int]) -> "UniqueSortedList":
        for x in other:
            self.append(x)
        return self