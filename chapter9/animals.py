from . level2 import Animate


class Animals(Animate):
    def breathe(self):
        pass

    def move(self):
        pass

    def eat_food(self):
        pass


class Mammals(Animate):
    pass


class Giraffes(Mammals):
    pass


class Cat(Mammals):
    pass


class Human(Mammals):
    pass