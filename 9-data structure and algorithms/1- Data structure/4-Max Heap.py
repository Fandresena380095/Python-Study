'''
MAXHEAP

- it is a binary tree
- it has child nodes and parents
- Node <= Parent


            1) 25  Parent  
               / \
              /   \
             /     \
          2)16    3)24   
            / \      \
           /   \      \
          /     \   6) 12
         /   5) 11
       4)5
       / \
      /   \
     /     \
   7)2   8) 3 Node      

This will help you sort items ,pop, add, extremly fast

index:1--2--3--4--5--6--7--8
Node: 25-16-24-5--11-12-2--3
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
indexing
i = 4
parent(i) = i/2 = 2
leftchild(i) = i*2 = 8
rightchild(i) = i*2+1 = 9


operations :
push(insert) = - Add a value to the end of the array
               - Float it Up to its right position (compare to its parent and swap)
               - Then compare the value to its new parent 

peek(get max) = - Return the index n1

pop(remove) = - Swap the biggest value to a node (to remove it)
              - Bubble the node down to its correct position
              - Return the max value we poped
'''

'''
M E T H O D S      U S E D
Public functions used :
push,peek,pop

Private functions :
swap, __floatUp,__bubbleDown,__str.
'''
class MaxHeap():
    def __init__(self, items= []): #You will have the option to put a pre defined list
        super().__init__() 
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) -1)

    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) -1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1,len(self.heap) -1) #swap max with the last item
            max = self.heap.pop() #pop<up the last item
            self.__bubbleDown(1) #we bubble down the first item we moved
        elif len(self.heap) == 2: #one of those is the zero
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self ,i,j):
        self.heap[i],self.heap[j] = self.heap[j] ,self.heap[i]

    def __floatUp(self,index):
        parent = index//2
        if index <= 1: #top position
            return
        elif self.heap[index] > self.heap[parent]: #compare to its parent
            self.__swap(index,parent)
            self.__floatUp(parent)

    def __bubbleDown(self,index):
        left = index *2 #left child ,right child
        right = index *2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left #swap positions
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index :
            self.__swap(index,largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return  str(self.heap)



m = MaxHeap([95,3,21,36,32,88,86])
print(m)
m.push(10)
print(m)
print(m.pop())
print(m)
print(m.pop())
print(m)
print(m.pop())
print(m)






















    

















            































