'''
A doubly linked list has 3 pieces of data:
    prev , data , next
    <--    23      -->

A delete operation is going to be tricky: this = d

prev                    this             next

                    °prev.next = this.next
                  
|.|4|->|              |<-|23|->|        |<-|21|.|
                                   
                    °next.prev = this.prev


advantages =
- Can iterate list in both directions
- Can delete a node without iterating to the list
(you can start by the tail to iterate through the list)

'''
class Node:
    def __init__(self,d ,n=None , p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p  #not used in a standard linked list

    def __str__(self):
        return ('('+str(self.data)+')')


class DoublyLinkedList :

    def __init__(self, r=None):
        self.root = r #root node
        self.last = r #so that you can access to the tail end of the list
        self.size = 0

    def add(self ,d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else :
            new_node = Node(d ,self.root)
            self.root.prev_node = new_node
            self.root = new_node
            #last will take the value of the original root node
        self.size += 1

    def find(self,d): #find d
        this_node = self.root 
        while this_node is not None: 
            if this_node.data == d: 
                return d
            elif this_node.next_node == None:
                return False
            else :
                this_node = this_node.next_node
        

    def remove(self ,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None: #delete a middle node
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.previous_node = this_node.prev_node
                    else : #delete the last node
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else : #delete the root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root #points to itself
                self.size -= 1
                return True #data removed
            else :
                this_node = this_node.next_node
        return False



    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node ,end= '->')
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node ,end='->')
        print()



dll = DoublyLinkedList()
for i in [5,9,3,8,9,32]:
    dll.add(i)

print("size =",dll.size)
dll.print_list()
dll.remove(8)
dll.print_list()
dll.remove(5)
dll.remove(32)
dll.print_list()

print(dll.last)



























































