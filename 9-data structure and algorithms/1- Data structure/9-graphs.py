'''
Graphs are ideal to build real world projects

There are 2 types of graphs:
- Undirected graph (2 way connected graphs),example a friendship connexion ,
a connected road
- Directed graph (1 way connection) ,example a one way flight between cities,


There are 2 common way to implement graphs :
- Using an adjacency list 
- Using an adjacency matrix

IN AN UNDIRECTED GRAPH :
             B    
            /|
           / |
          /  |
         A---C
         |  / \
         | /   \
         |/     \
         E       D

__Adjacency list__
A: B,C,D
B: A,C
C: A,B,D,E
D: C
E: A,C

__Adjacency matrix__:

    A    B    C    D    E

A   0    1    1    0    1

B   1    0    1    0    0

C   1    1    0    1    1

D   0    0    1    0    0

E   1    0    1    0    0                     

__it is easrier if you have a WEIGHTED edges if you use a matrix ,you
would use a tuple in an adjacency list otherwise

    A    B    C    D    E

A   0    8    9    0    6

B   8    0    5    0    0

C   9    5    0    3    1

D   0    0    3    0    0

E   6    0    1    0    0


IN A DIRECTED GRAPH : --* (direction)
             B    
            /*
           / |
          *  |
         A--*C
         *  / \
         | /   \
         |*     *
         E       D

__Adjacency list__:
A: C
B: A
C: B,D,E
D:
E: A

__Adjacency matrix__:

    A    B    C    D    E

A   0    0    1    0    0

B   1    0    0    0    0

C   0    1    0    1    1

D   0    0    0    0    0

E   1    0    0    0    0 


Which implementation is better ?(E=Edge ,V=Vertex(links))
__In a DENSE graph where__ :
        |E| = |V|**2

__In a SPARSE graph where__ :
        |E| = +/- |V|


Adjacency list :
+ Faster and uses less space for sparse graphs
- Slower for dense graphs

Adjancency Matrix :
+ Faster for dense graphs
+ Simplier for Weighted edges
- Uses more space |E| = |V|**2

'''

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = set() #empty set for the vertex's neighbor

    def add_neighbor(self,v):
        self.neighbors.add(v) #add to the neighbor's set



class Graph:
    vertices = {} # {vertex name : vertex objects}

    def add_vertex(self,vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex #add that vertex to the vertices
            return True
        else :
            return False

    def add_edge(self, u,v): #between u and v
        if u in self.vertices and v in self.vertices : #check if both vertices exist in the graph
            self.vertices[u].add_neighbor(v) #add u to v's neighborlist
            self.vertices[v].add_neighbor(u) #add v to u's neighborlist
            return True
        else:
            return False


    def print_graph(self):
        for key in sorted(list(self.vertices.keys())) :
            print(key ,sorted(list(self.vertices[key].neighbors)))
        

#ways to add vertex to the graph
g = Graph()
a = Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A') ,ord('L')): #for i in range(numberical order A to L)
    g.add_vertex(Vertex(chr(i)))# converts the numerical order to character again

#implement edges
edges = ['AB','AE','BF','CG','AK','DE','DH','EH','FG','FI','FJ','AF']

for edge in edges :
    g.add_edge(edge[0], edge[1])

g.print_graph()



















































































































