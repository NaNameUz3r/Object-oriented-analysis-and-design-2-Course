# простейший пример полиморфного вызова в python

# class Alfa():
#     def hello(self):
#         print("Hello")

# class Betta(Alfa):
#     def world(self):
#         print("world")

# x = Betta()
# x.hello()

##############################################################
# ковариантный вызов

from typing import Generic, TypeVar

shunya = TypeVar('shunya', covariant=True)


class Essense():
    def manifestate(self):
        raise NotImplementedError

class Nature(Essense):
    def manifestate(self):
        print('Lights')

class Energy(Essense):
    def manifestate(self):
        print('Rays')

class Form(Generic[shunya]):
    def __init__(self, seed: shunya) -> None:
        self._seed = seed

    def manifestate(self):
        self._seed.manifestate()


def incarnate(form: Form[shunya]):
    form.manifestate()

illusion = Energy()
form = Form(illusion)
incarnate(form)