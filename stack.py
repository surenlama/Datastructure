class Stack:
   
   arr=[]
   top=-1
   size=4
   def push(self,value):
    
      if top==size:
         print('stack is full')
      else:
         top=top+1
         arr[top].append(value)

   def pop(self,value):
      
      if top==-1:
         print('Stack is empty')
      else:
         top=top-1   

   def display(self):
    
      for i in range(top):
         print(arr[top])

s=Stack()
s.push(10)
s.push(20)
s.display()      
   