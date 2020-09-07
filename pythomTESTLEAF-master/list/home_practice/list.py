mobile=[]
print(type(mobile))
# o/p ----> <class 'list'>

mobile=['honor','nokia']
print(mobile)
# o/p ----> ['honor', 'nokia']

# .append() method is used to add new items into the list
mobile.append('samsung')
print(mobile)
# o/p ----> ['honor', 'nokia', 'samsung']

# .extend() method is used to add group of items into the list
ls=['1','2','3']
mobile.extend(ls)
print(mobile)
# o/p ----> ['honor', 'nokia', 'samsung', '1', '2', '3']

# .insert() method is used to add item in particular index into the list
mobile.insert(4,'mi')
print(mobile)
# o/p ----> ['honor', 'nokia', 'samsung', '1', 'mi', '2', '3']

mobile.insert(5,['vivo','oppo','poco'])
print(mobile)
# o/p -----> ['honor', 'nokia', 'samsung', '1', 'mi', ['vivo', 'oppo', 'poco'], '2', '3']