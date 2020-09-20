class A:

    def method_A(self):
        print('iam from class a')

class B(A):

    def method_B(self):
        print('iam from class b')


b=B()
b.method_A()
b.method_B()