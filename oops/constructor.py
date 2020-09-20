class Testleaf:

    # any function with __ is called magical function
    def __init__(self,name,number): # ------> constructor  instance variable
        self.n=name
        self.ph=number
        print('iam from init')

    def method(self):   # ----------> instance function
        print('function',self.n,self.ph)

# any oops language when object is created the first constructor is called


obj=Testleaf('venkatesh','123456')
obj.method()

obj1=Testleaf('kauhsik','230976')
obj1.method()



