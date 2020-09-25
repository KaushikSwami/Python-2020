class Dog:
    def __init__(self,name,age):
        self.n=name
        self.a=age
        print('Dog class constructor')

    def color(self):
        print(self.n,'is black')

    def sound(self):
        print(self.n,'barks')


class Cat:
    def __init__(self,name,age):
        self.N=name
        self.A=age

    def color(self):
        print(self.N,'is white')

    def sound(self):
        print(self.N,'meows')


d=Dog('scooby','3')
d.color()
d.sound()

c=Cat('tom','2')
c.color()
c.sound()




