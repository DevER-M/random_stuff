li=[3,3]
t=6
for e in li:
    for f in li[li.index(e)+1:]:
        if e+f==t:
            print(li.index(e),li.index(f,li.index(e)+1))