def count(data):
    input=data.split()
    ls=[]
    for i in input:
        ls.append(len(i))
    print(ls)


count("hello how are u")

fn=lambda a : len(a)
print(list(map(fn,"hello how are you".split())))
