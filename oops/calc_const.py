class Calc_maths:

    def __init__(self,a,b):
        self.value1=float(input('enter the a :'))
        self.value2=float(input('enter the b :'))
        print("the constructor")

    def add(self):
        return self.value1+self.value2

    def subtract(self):
        return self.value1-self.value2

    def multiply(self):
        return self.value1*self.value2

    def divide(self):
        return self.value1/self.value2




c=Calc_maths(10,20)
addition=c.add()
print('the sum is :',addition)
subtraction=c.subtract()
print('the difference is :',subtraction)
multiplication=c.multiply()
print('the multiply is :',multiplication)
division=c.divide()
print('the prod is :',division)