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

    # deletion at end

    def delete_node(self):
        # if list is empty 
        if self.head == None:
            print("empty list cant delete anything")
            return
        
        # if only one node is there
        if self.head.next == None:
            self.head = None #deleted
            return
        # more than 2 nodes
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

ll=LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.delete_node()
ll.print_list()
