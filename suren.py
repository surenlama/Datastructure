pos=-1
def search(list,n):
  lower=0
  upper=len(list)-1

  while lower <=upper:
     r=(lower+upper) // 2  

     if list[r] == n:
        globals()['pos']=r
        return True
      
     else:
         if list[r]<n:
             lower= r+1
         else :
             upper=r-1
  return  False        

list=[4,7,5,12,99,102,44,65,34,21]
n=34

if search(list,n):
   print("Found at",pos+1)
else:
   print("Not Found")
      

