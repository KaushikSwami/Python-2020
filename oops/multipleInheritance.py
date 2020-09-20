class GA:
    def method(self):
        print('GA')

class GB:
    def common(self):
        print('common from GB')


class A(GA,GB):

    def method_A(self):
        print('iam from class a')




class C(A): # will take the method from the class that is displayed first in left side
    def method_C(self):
        print('iam from class c')

c=C()
c.common()
print(C.__mro__)
