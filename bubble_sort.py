def bubblesort(li:list):
    length=len(li)
    for i in range(length-1):
        for j in range(length-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li

lis=[e for e in range(100,0,-1)]
print(lis)
print(bubblesort(lis))