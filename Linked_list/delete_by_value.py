class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # deletion by value

    def delete_node(self,value):
        # if list is empty 
        if self.head == None:
            print("empty list cant delete anything")
            return
        
        # if value in the head
        if self.head.data == value:
            self.head = self.head.next #deleted
            return
        # caase 3 Value in middle / end
        prev = None
        current = self.head
        while current!=None and current.data!=value:
            prev =current
            current =current.next
        prev.next=current.next  # // delete the node

ll=LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.delete_node(10)
ll.print_list()
