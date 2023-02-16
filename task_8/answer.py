# Возьмем пример кода из прошлого ответа
class Vehicle:
    def drive(self):
        print('Vehicle is driving')

class Car(Vehicle): 
    def drive(self):
        print('Car is driving')

car = Car()
car.drive()
# >>> Car is driving

# Здесь можно увидеть ковариантную типизацию — передаем в метод предка инстанс потомка.
Vehicle.drive(car)
# >>> Vehicle is driving



# Примером контравариантности в Python может послужить следующий код:
class Animal:
    def make_sound(self) -> None:
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self) -> None:
        print("Woof!")

def pet_animal(animal: Animal) -> None:
    animal.make_sound()

# Валидное использование:
my_dog = Dog()
pet_animal(my_dog) 
# >>> Woof!

# В этом примере Animal является предком Dog, а функция pet_animal принимает аргумент типа Animal. 
# Однако, поскольку Dog является наследникм Animal, также допустимо передавать экземпляр Dog в pet_animal.