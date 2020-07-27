class Node():
    def __init__(self,data):
       self.data=data
       self.next=None

class linked_list():
    def __init__(self):
        self.start=None
        
    def insert(self,val):
       Newnode=Node(val)
       if self.start==None:
          self.start=Newnode
       else:
           temp=self.start
           while temp.next!=None:
               temp=temp.next
           temp.next=Newnode

    def delete(self):
        if self.start==None:
            print('Empty')  
        else:
            self.start=self.start.next

    def display(self):
        if self.start==None:
            print('Empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.data)
                temp=temp.next
    def first_insert(self,value):
        Newnode=Node(value)
        Newnode.next=self.start
        self.start=Newnode

    def specific_position(self,n,value):
        temp=self.start
        i=0    
        while i<n:
            temp=temp.next
            i+=1
        Newnode=Node(value) 
        Newnode.next=temp.next
        temp.next=Newnode

l=linked_list()
l.insert(10)
l.insert(20)

l.display()
print()
l.specific_position(0,7)
l.display()      
print()