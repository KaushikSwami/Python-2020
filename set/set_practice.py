st={}
print(type(st))
# by default the type of the above empty set will be dictonary , based on the input in the set only the type will be determined

pan={'ANS12309','ANS345SR','ANS23450','ANS569VC','ANS3456TD','ANS23410V'}
print(type(pan))
print(pan)
# to add a single item into a set
# the item will be added anywhere , since set will not maintain the order

pan.add('ANS234ER4')
print(pan)

# to add a collection of items we can use update function

pan.update({'ABC123','ABC098','ABC876','ABC687'})

for i in pan:
    print(i)

num={100,200,300,400,500,600}
num.discard(200)
print(num)
num.remove(200)
 
