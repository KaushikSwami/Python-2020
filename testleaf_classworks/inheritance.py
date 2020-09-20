class Vehicle:

    def apply_brake(self):
        print('apply brakes')

    def sound_horn(self):
        print('sound horn')

class Car(Vehicle):

    def __init__(self,wheel):
        self.w=wheel

    def on_AC(self):
        print('turn on ac')

class Auto(Vehicle):
    def __init__(self,wheel):
        self.wh=wheel

class BMW(Car):
    def bmw_method(self):
        print('BMW')

class bajaj(Auto):
    def auto_bajaj(self):
        print('this is auto')