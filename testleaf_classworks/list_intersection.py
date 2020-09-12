a=[1,3,6,78,35,55]
b=[12,24,35,24,88,120,155]
set_a=set(a)
print(set_a,type(set_a))
set_b=set(b)
print(set_b,type(set_b))

intersection=(set_a.intersection(set_b))
new_list=list(intersection)
print(new_list,type(new_list))
