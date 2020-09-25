class Base_1:
    def method_1(self):
        print('this is method from base_1 class')

class Base_2:
    def method_2(self):
        print('this is method from base_2 class')

class Child(Base_1,Base_2):
    def child_method(self):
        print('this is method from child class')


c=Child()
c.method_1()
c.method_2()
c.child_method()

