name=['venkat','kaushik','swaminav','babbi','venkatesh','newname']
new_name_list=[]

#for i in range(0,len(name),2):
 #   print(i)
  #  print(name[i])
   # new_name_list.append(name[i])
#print(new_name_list)

for i in range(len(name)-1,0,-2):
    print(i)
    print(name[i])
    new_name_list.append(name[i])
print(new_name_list)

