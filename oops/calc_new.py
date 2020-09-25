class Cal:

    def __init__(self,a,b):
        self.v1=int(input('enter value 1 : '))
        self.v2=int(input('enter value 2 : '))

    def add(self):
        return self.v1+self.v2


c=Cal(10,20)
addition=c.add()
print(addition)