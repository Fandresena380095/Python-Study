class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}


    def add_vertex(self, vertex):
        if isinstance(vertex ,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            print(">self vertices :",self.vertices)
            print(">self.edges pre-transfo :",self.edges)
            #(for loop appends a column of zeros to the edges' matrix)
            for row in self.edges: #this will add 0 to each matrices of the matrix
                row.append(0)
                print(row)
            print(">self.edges after-forloop :",self.edges)
            #append a row of zeros to the bottom of the edges' matrix
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            print(">self.edges final stage :",self.edges)
            print(">self.edge_indices :",self.edge_indices)
            print()
            print()
            return True
        else:
            return False


    def add_edge(self ,v,u, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v,i in sorted(self.edge_indices.items()):
            print(v+' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')


    

g  = Graph()
a = Vertex("A")
g.add_vertex(a)
b = Vertex("B")
g.add_vertex(b)
c = Vertex("C")
g.add_vertex(c)
d = Vertex("D")
g.add_vertex(d)
e = Vertex("E")
g.add_vertex(e)
    
    
