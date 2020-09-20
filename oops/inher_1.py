class A:

    def method_A(self):
        print('iam from class a')

class B(A):

    def method_B(self):
        print('iam from class b')

class C(B):
    def method_C(self):
        print('iam from class c')



c=C()
c.method_A()
c.method_B()
c.method_C()

