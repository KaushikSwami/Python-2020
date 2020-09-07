# 5) With a given list, write a program to print this
# list after removing all duplicate values with original order reserved.

# Sample Input : [12,24,35,24,88,155,88,120,155]
# Expected output : [12, 24, 35, 88, 155, 120]

list_a=[12,24,35,24,88,155,88,120,155]
set_val=list(set(list_a))
print(set_val,type(set_val))

set_val.sort()
print(set_val)

