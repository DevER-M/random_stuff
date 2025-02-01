from time import time
def bin_search(lis,num:int):
    low=0
    high=len(lis)-1
    while low<=high:
        mid=low+(high-low)//2
        if lis[mid]==num:
            return mid
        elif lis[mid]>num:
            high=mid-1
        else:
            low=mid+1
    return None
t=time()
li=range(1000000000000000000)
print(bin_search(li))
print(time()-t)