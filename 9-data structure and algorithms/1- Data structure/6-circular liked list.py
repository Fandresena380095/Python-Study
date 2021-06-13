'''
Circular linked list are very identical to the normal linked list
but instead of having the last pointer -> None, it points to the root node

the add() operation is going to be quite different:
instead of inserting it to the ROOT NODE ,
you insert it to the SECOND NODE
advantage : good for something that continuously loops
'''
class Node:
    def __init__(self,d ,n=None , p=None):
        self.data = d
        self.next_node = n
        self.previous_node = p  #not used in a standard linked list

    def __str__(self):
        return ('('+str(self.data)+')')


class CircularLinkedList :

    def __init__(self, r=None):
        self.root = r #root node
        self.size = 0

    def add(self ,d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root #point to itself
        else :
            new_node = Node(d ,self.root.next_node) #N2 position
            self.root.next_node = new_node #the root will point to the new node(2nd position)
        self.size += 1

    def find(self,d): #find d
        this_node = self.root #iterate throught the list one at a time from the root
        while True: 
            if this_node.data == d: 
                return d
            elif this_node.next_node == self.root: #after looping through the
                return False                       #entire list
            this_node = this_node.next_node

    def remove(self ,d): #track both this_node and the previous_node
        this_node = self.root
        prev_node = None

        while True :
            if this_node.data == d:  #found
                if prev_node is not None: 
                    prev_node.next_node = this_node.next_node
                else : #if we need to delete the root
                    while this_node.next_node != self.root: #find the very last node to point its node to the root
                        this_node = this_node.next_node #iterates through the nodes
                    this_node.next_node = self.root.next_node #the last item will points to the root's next node
                    self.root = self.root.next_node #new root = previous root's next node
                self.size -= 1
                return True #removed d
            elif this_node.next_node == self.root:
                return False #d not found
            prev_node = this_node
            this_node = this_node.next_node
                     
                    
    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node , end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node ,end= '->')
        print()

cll = CircularLinkedList()
for i in range(3,20) :
    if i%3 == 0:
        cll.add(i)
cll.print_list()
print("Size =",cll.size)

print(cll.find(18))
print(cll.find(7))

print("........................................................")

#print the root 
my_node = cll.root
print(my_node, end='->')

#this will continuously circle back the node
for i in range(20): 
    my_node = my_node.next_node
    print(my_node ,end='->')
print()
print('...................................................................')

cll.print_list()
cll.remove(18)
print(cll.remove(343))
print("New size =",cll.size)
cll.print_list()
cll.remove(3)
print("New size =",cll.size)
cll.print_list()

'''
1:24:56
'''
























        
