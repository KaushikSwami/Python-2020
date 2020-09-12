a={'PAN01':'kaushik','PAN02':'babbi'}
print(a,type(a))
print(a['PAN02'])
print(a.get('PAN02'))
a['PAN03']=100
print(a)


for i,j in a.items():
    print(i,j)
