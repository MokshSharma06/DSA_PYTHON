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
        ptrr = self.head
        while ptrr:
            print(ptrr.data, end=" -> ")
            ptrr = ptrr.next
        print("None")


ll =LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(12)
ll.insert_at_beginning(14)
ll.insert_at_beginning(15)
ll.print_list()

