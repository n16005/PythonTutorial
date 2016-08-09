from . level2 import Animate


class Animals(Animate):
    def breathe(self):
        pass

    def move(self):
        print('moving')

    def eat_food(self):
        print('eating food')


class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')


class Giraffes(Mammals):
    def eat_Leaves_from_trees(self):
        print('eating Leaves')


class Cat(Mammals):
    pass

class Human(Mammals):
    def _init_(self, name):
        self.name - name

    def self_introduction(self):
        pass


class Human(Mammals):
    pass