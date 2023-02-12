class Vehicle:
    def drive(self):
        print('Vehicle is driving')

class Car(Vehicle):
    # Здесь, переопределяя метод родительского класса, в Python автоматически
    # используется динамическое связывание, так как все методы в Python исходно виртуальные.  
    def drive(self):
        print('Car is driving')

car = Car()
car.drive()
# метод вызывается с учетом динамического связывания, т.е. переопределенный в наследнике.
>>> Car is driving

# метод вызывается с учетом статического связывания, т.е. "оригинальный" метод класса.
Vehicle.drive(car)
>>> Vehicle is driving