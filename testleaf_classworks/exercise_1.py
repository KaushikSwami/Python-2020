#1) Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
#Sample Input : 34,67,55,33,12,98 Expected output : ['34', '67', '55', '33', '12', '98']

a=input("enter the numbers :")
value=a.split(",")
print(value,type(value))
print(tuple(value),type(value))

# o/p
# enter the numbers :34,67,55,33,12,98
# ['34', '67', '55', '33', '12', '98'] <class 'list'>
# ('34', '67', '55', '33', '12', '98') <class 'list'>



