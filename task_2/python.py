class Parent:
    def __init__(self, value):
        self.value = value
        
    def parent_method(self):
        print("Привет из Родительского класса!")
        

class Child(Parent):
    # Здесь класс Child как расширяет (extension) так и специализирует (specialization) 
    # свой родительский класс Parent.

    # Добавление нового метода — расширение.
    def child_method(self):
        print("Привет из нового метода класса-потомка")
        
    # Переопределение родительского метода — спецификация.
    def parent_method(self):
        print("Привет из специальной версии родительского метода, переопределенного в потомке!")

parent_instance = Parent(5)
parent_instance.parent_method() # Выведет: "Привет из Родительского класса!"

child_instance = Child(10)
child_instance.parent_method() # Выведет: "Привет из специальной версии родительского метода, переопределенного в потомке!"
child_instance.child_method() # Выведет: "Привет из нового метода класса-потомка"
