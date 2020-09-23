class Animal:
    def roar(self,name):
        self.n=name
        print(self.n,'will roar')

    def hunt(self,name):
        self.n=name
        print(self.n,'will hunt')



class Lion(Animal):
    print('iam lion')


l=Lion()
l.roar('lion')
l.hunt('lion')
