def quick(a,low,high):
    if(low<high):
        x=partition(a,low,high)
        quick(a,low,x-1)
        quick(a,x+1,high)


def partition(a,low,high):
    i=low
    j=high+1
    p=a[low]
    while True:

        while True:
            i+=1
            if(a[i]>=p):
                break
        while True:
            j-=1
            if(a[j]<=p):
                break
        if i<j:
            swap(a,i,j)
        if i>=j:
            break
    if(i>j):
        a[low]=a[j]
        a[j]=p
    return j

def swap(a,k,l):
    temp=a[k]
    a[k]=a[l]
    a[l]=temp

a=[33,1,24,17,45,18,78,-18,-45]
a.append(1000000)
quick(a,0,8)
print(a)




