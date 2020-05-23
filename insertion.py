lst=[5,4,10,1,6,2]
for i in range(1,len(lst)):
    temp=lst[i]
    j=i-1
    while j>=0 and lst[j]>temp:
        lst[j+1]=lst[j]
        j=j-1

    lst[j+1]=temp    
print(lst)
