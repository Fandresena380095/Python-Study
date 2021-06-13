'''
If you want to acces a data very fastly:
Every node has to parts:

data  | next
17    | (link to the next node)-->

The LAST NODE will have no pointer anymore
(link = None)
The ROOT NODE is at the very front

operations are going to be:
- find(data)
- add(data)
- remove(data)
- print_list()


add(data): (add at the beginnig)
- create a new node out of the data
- point it to the root node
- change root to data

remove(data): (data will be cut out,data's pointer is changed to data-1 pointer)
- Find data(check from the root--> to the number)
- Select the node of data-1(previous node of data)
- Change the [pointer of data-1] to the [pointer of data]
'''

class Node:
    def __init__(self,d ,n=None , p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p  #not used in a standard linked list

    def __str__(self):
        return ('('+str(self.data)+')')


class LinkedList :

    def __init__(self, r=None):
        self.root = r #root node
        self.size = 0

    def add(self ,d):
        new_node = Node(d ,self.root) #pass the data ,and the next node as root nodes
        self.root = new_node #new node is going to be the root node
        self.size += 1

    def find(self,d): #find d
        this_node = self.root #iterate throught the list one at a time from the root
        while this_node is not None: #as long as the node exists
            if this_node.data == d: 
                return d
            else :
                this_node = this_node.next_node
        return None

    def remove(self ,d):
        this_node = self.root
        prev_node = None

        while this_node is not None :
            if this_node.data == d:  #if we find d
                if prev_node is not None: #if data is not root node
                    prev_node.next_node = this_node.next_node
                else : #data is the root node
                    self.root = this_node.next_node #root = 2nd node
                self.size -= 1                      #that will remove the root
                return True #data is removed
            else:
                prev_node = this_node #a=b
                this_node = this_node.next_node #b=c
        return False #if data not found


    def print_list(self):
        this_node = self.root #iterate one at the time from the loop
        while this_node is not None:
            print(this_node , end ='->')
            this_node = this_node.next_node
        print('None')



m = LinkedList()
m.add(12)
m.add(16)
m.add(32)
m.add(56)
m.print_list()

print("size =",m.size)
m.remove(56)
m.remove(12)
m.print_list()
print("new size =",m.size)
print(m.find(32))
print(m.root)























        





























