
# signature for map is --- > map(function,collection)
val=[1,2,3,4,5,6,7,8,9]

def multiply(a):
    return a*2

print(list(map(multiply,val)))
