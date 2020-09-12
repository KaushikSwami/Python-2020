# 1. Write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# input  : 8
#     output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


dict={}
for i in range(1,9):
    dict[i]=i*i

print(dict)
