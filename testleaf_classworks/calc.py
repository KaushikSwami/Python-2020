class Calculator:

    def add_two_num(self,a,b):
        c=a+b
        return c

    def add_items(self,*args):
        ls=sum(args)
        return ls

    def sum_items(self,*args):
        count=0
        for i in args:
            count=count+int(i)
        return str(count)

obj1=Calculator()
x=obj1.add_two_num(10,20)
print(x)











