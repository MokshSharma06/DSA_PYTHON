class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head =None
        
    def insert_at_last(self,data):
        # first case when list is empty
        neww_node =Node(data)
        if self.head==None:
            self.head =neww_node
            return
        
        # traverse at last and insert there
        
        temp = self.head
        while temp.next is not None:
            temp =temp.next
        temp.next=neww_node
        
    def print_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current =current.next
        print("none")
        
ll=LinkedList()
ll.insert_at_last(20)
ll.insert_at_last(30)
ll.print_elements()
