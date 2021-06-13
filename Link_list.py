''' link list is the chain of nodes. list contents a data field and a refrence field
        NODE-----NODE-----NODE-----NODE
        NODE(can content)===>   data|link     OR    Prv.link|data|next link
        
            3 types of linked list
                single linked list
                double linked list
                circular linked list
    '''

# single linked list

#creat a Node 
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

#creat a class to link the Node
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!!")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n =self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


LL1=LinkedList()
LL1.add_begin(10)
LL1.add_end(200)
LL1.add_begin(20)
LL1.print_LL()

