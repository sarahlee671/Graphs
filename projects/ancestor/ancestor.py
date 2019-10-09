
#Make a graph
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can't create edge based on given vertices!")

# Traverse the graph with BFS
# Looking for shortest paths between any 2 nodes
# Keep track of the lengths of these paths
# And return where the longest path ends
# If there are no parents, return -1
# If it is a tie, return the lowest node number