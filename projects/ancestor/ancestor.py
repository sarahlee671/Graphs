

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    #build our graph
    graph = Graph()
  
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
         
        #build edges in reverse (link kids to parents)
        graph.add_edge(pair[1], pair[0])
    
    #Use BFS
    q = Queue()
    #enqueue the path with the starting node
    q.enqueue([starting_node])

    #Keep track of the longest path
    max_path_length = 1
    #set to -1 if you can't find 
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        # if we have the path with the same length, it gives the lower numberic as the answer (catches a tie)
        if(len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

        # get the copied path of every neighbor vertex, append, and add it to queue
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor


 
