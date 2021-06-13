'''
Trees are primordial for searches....as it will narrow down the
possibilities if you want to access a data within a billion ones

- Each part of the tree is called a NODE
- Each connexion is called an EDGE
- The first node is called the ROOT NODE
-      PARENT NODE         5
                          / \
       CHILD NODE        1  12 (12 and 5 are SIBLINGS NODES)

- In a BINARY tree, a parent can have 0 or 1 or 2 children
- The very bottom node is called LEAF NODE
- SUBTREE = any part of the tree that is itself a tree
    (sublevel that has the form of a tree)



- node 5 [node 3 and 4 are 5's descendants]
    |
    V
  node 3
    |
    V
  node 4 [node 5 and 3 are 4's ancestors)

- In a binary search tree :
    °each node is greater than every node in it's left subtree
    °each node is smaller than every node in it's right subtree
                                R <[x]<L :
                                
                     15         8<[15]<24
                   /    \
                  8     24      5<[8]<11
                 /  \
                5    11         2<[5]<6
               /  \
              2    6



B I N A R Y   S E A R C H   T R E E S   OPERATIONS:
- insert
- find
- delete
- get_size
- traversals (walk throught the tree node by node

__INSERT__:
- start at root
- always insert as a leaf (at the very bottom)

             insert [x] : While [x] is not a leaf: COMPARE x to (p)
                          -if x  < (p)
                           x goes to the LEFT
                          -if x  > (p)
                           x goes to the RIGHT

                  (15)  
                 /    \
                /      \
               /        \ 
             (8)       (24)
             / \            \
            /   \            \
           /     \            \     
         (5)     (11)         (28)
         /\        \           /
        /  \        \         /
       /    \        \       /
      2      6       13     12


__FIND__ :
- it uses the same comparison process as the insert() method
- you can see that through the comparison method ,it cuts in half
the remaining possibilities everytime we move down in the tree

__DELETE__:
3 possibles cases :

1__Delete a LEAF NODE:
It will simply delete the leave note.

2__Delete a node with 1 child:
-PROMOTE the CHILD to the Node's position
(it will also promote the entire subtree)
(In our example ,if you delete 11,13 will take its place)

3__Delete a node x with 2 children: 
- go down to the right child of x 
- if :
   1-x.biggest_child has no Left node : promote the entire node 
   2-x.biggest_child has a left node(y) : swap the position of x to
                                the Left node y
(resume :delete(x) :GoDown right then left
                   if Left(l) exists : swap x to l ,then delete x
                   else : delelte x ,Promote the subtree)

__GET_SIZE__
returns the number of nodes
Works recursively :
size = 1 + size(left subtree) + size(right subtree)

__PREORDER TRAVERSALS__
- visit the root first
- visit the root's subtree
 (Left before Right)

 __INORDER TRAVERSAL__
- visit the bottom left leave first
-visit the root in between


ADVANTAGES :
It is extremely fast ,it has a complexity of
O(h) = 0(log n)
(In a balanced BST with 10,000,000 nodes ,it takes 30 comparisons) 
'''

class Tree:
    def __init__(self,data, left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data :
            return False #duplicate value
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else :
                self.left = Tree(data) #it will be the left subtree of its parent's node
                return True
        else :
            if self.right is not None:
                return self.right.insert(data)
            else :
                self.right = Tree(data) #creates a new subtree out of data
                return True

    def find(self, data):
        if self.data == data :
            return data
        elif self.data > data:
            if self.left is None: #if we reach the bottom and we didn't find
                return False      #the data yet
            else :
                return self.left.find(data)
        elif self.data < data  :
            if self.right is None:
                return False
            else :
                return self.right.find(data)


    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left : #loop to say = as long as self.left exists
            return 1 + self.left.get_size()
        elif self.right :
            return 1 + self.right.get_size()
        else :
            return 1

    def preorder(self):
        if self is not None:
            print(self.data , end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right :
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data , end=' ')
            if self.right is not None:
                self.right.inorder()

#the very differences between those 2 are the position of the print statement



tree = Tree(7)
tree.insert(9)

for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
    tree.insert(i)

for i in range(16):
    print(tree.find(i) ,end=' ') #it will print False to 0,5,8

    
print('\n' ,tree.get_size())

print("Preorder :")
tree.preorder()
print()
print("Inorder :")
tree.inorder()
print()


'''
1:52:03
'''
























            



    
                
































































