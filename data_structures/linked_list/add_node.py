class Node: #define a class named node having data and ref as attributes
    def __init__(self,data:int)->None:
        self.data=data
        self.ref= None 
class LinkedList:
    def __init__(self)->None #define head of the linked list i.e initiate the linked list
        self.head=None
    def print_ll(self): # to print the linked list
        if self.head is None:
            print("The Linked List is empty ")
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data)->None: #to add a node in the beginning 
        new_node= Node(data) #define data of the new node
        new_node.ref= self.head #make the ref or adress of node to the head node
        self.head = new_node 
    def add_end(self,data)->None:
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x)->None:
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        new_node=Node(data)
        new_node.ref= n.ref
        n.ref= new_node 
linked_list= LinkedList() # main driver function here we define the linked list
linked_list.add_begin(11) #added 11 to the beginning of out linked list
linked_list.add_end(100)
linked_list.add_begin(22)
linked_list.add_after(30,11)
linked_list.print_ll()
#https://youtu.be/xRTdfZsAz6Y?si=EMrqVJpXjDDz1kEF
