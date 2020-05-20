class queue:
       def __init__(self):
          self.a=[]
                           
       def enqueue(self,value):
           self.a.append(value)
       
       def dequeu(self):
         self.a.reverse()
         self.a.pop()          
       
       def disp(self):
          print(self.a)
       
s=queue()
s.enqueue(10)         
s.enqueue(30)         
s.enqueue(50)         
s.dequeu()
s.disp()