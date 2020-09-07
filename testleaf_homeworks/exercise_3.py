# 3) Write a program to generate and print another
# tuple whose values are even numbers in the given tuple

# Sample Input : (1,2,3,4,5,6,7,8,9,10)
# Expected Output : (2, 4, 6, 8, 10)

value= (1,2,3,4,5,6,7,8,9,10)
print(type(value))
for i in range(1,len(value),2):
    print(value[i])

# o/p
#<class 'tuple'>
#2
#4
#6
#8
#10


