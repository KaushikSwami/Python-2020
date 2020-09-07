# create list
name=[]
print(type(name))
name=['kaushik','venkat','swaminav','babbi']
print(name,type(name))

# if we want to get the value from existing index we follow the below

print(name[0])

# adding the item in the list
# -----> append
# -----> extend
# -----> insert

# append function ---> will add single item in the list
name.append("kaushbabbi")
print(name)
# o/p ---> ['kaushik', 'venkat', 'swaminav', 'babbi', 'kaushbabbi']
# it maintains the insertion order
name.append("venkat")
print(name)
# o/p ----> ['kaushik', 'venkat', 'swaminav', 'babbi', 'kaushbabbi', 'venkat']
# duplicate values are considered in list

# extend function -----> will add multiple items
ls=['name1','name2','name3']
name.extend(ls)
print(name)
# o/p ----> ['kaushik', 'venkat', 'swaminav', 'babbi', 'kaushbabbi', 'venkat', 'name1', 'name2', 'name3']

# insert function -----> will insert in the required index in the list
name.insert(3,'special_name')
name.insert(4,['a','b','c']) # will be considered as one single list in one index
print(name)
print(name[3])
# o/p ----> ['kaushik', 'venkat', 'swaminav', 'special_name', ['a', 'b', 'c'], 'babbi', 'kaushbabbi', 'venkat', 'name1', 'name2', 'name3']
# o/p ----> special_name

# removing item from the list

# --------> remove()
# will remove the select element from the list (arg should be the the element)
mobile=['honor','mi','nokia','samsung']
mobile.remove('mi')
print(mobile)

# ---------> pop()
# pop() will in default remove the last item in the list
mobile.pop()
print(mobile)

new=['vivo','oppo','poco','mi']
mobile.extend(new)
print(mobile)

# ---------> pop(index)
# pop(index) will remove the item in the mentioned index
mobile.pop(3)
print(mobile)

# ---------> clear()
# clear() will remove all the items in the list and return an empty list
mobile.clear()
print(mobile)

new_list=['poco','mi','samsung','nokia','honor','realme','pixel','vivo','oppo','mi','poco','samsung']
mobile.extend(new_list)

# ----------> index()
# index('item') will provide the index in which the item is located
print(mobile.index('honor'))

# ----------> count(item)
# count(item)
print(mobile.count('samsung'))

