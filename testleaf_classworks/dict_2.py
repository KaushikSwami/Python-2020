txt='testleaf'
ch='e'
dict={}
count=0

for i in txt:
    if i==ch:
        count=count+1
        dict[i]=count
print(dict)

