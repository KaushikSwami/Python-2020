# function definitions--- def--> method name:
# function call---

# types of functions
# build in functions
# user definded functions

# def add_two_num():
#    a=10
 #   b=20
  #  return (a+b)

#val=add_two_num()
#print(val)

#def add(a,b,c=150):
#    print(a,b,c)
 #   return(a+b+c)

#print(add(b=20,a=200))

def add(*args):
    print(args)
    return sum(args)

add(1,2,3,4,5)



