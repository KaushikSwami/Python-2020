def up(data):
    return data.upper()

print(up("abc"))

fn=lambda a:a.upper()

print(list(map(fn,"hello".split())))