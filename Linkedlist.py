class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None

    def view(self):
        if self.start==None:
            print('linked list is empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.value)
                temp=temp.next

    def deletefirst(self):
        if self.start==None:
            print('Linked list is empty')
        else:
            self.start=self.start.next    

    def insert_Node(self,val):
        Newnode=Node(val)
        if self.start==None:
            self.start=Newnode;
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=Newnode    
        
l=Linked_list()
l.insert_Node(10)
l.insert_Node(20)
l.insert_Node(30)
l.deletefirst()
l.view()