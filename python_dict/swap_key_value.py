d = {"a": 1, "b": 2, "c": 1, "d":5}

inverted={}

for k,v in d.items():
    if v not in inverted:
        inverted[v]=[k]
    else:
        inverted[v].append(k)

print(inverted)