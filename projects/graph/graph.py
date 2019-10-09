"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can't create edge based on given vertices!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        """
        # Create a queue
        qq = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        qq.enqueue(starting_vertex)
        # While: queue not empty
        while qq.size() > 0:
            # Pop first node out of queue
            vertex = qq.dequeue()
            # If not visited
            if vertex not in visited:
                # Mark as visited
                visited.add(vertex)
                print(vertex)
                # Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)
        # Goto top of loop
        
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        #if node hasn't been visited, add it to visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            #for every neighbor node
            for child_vertex in self.vertices[starting_vertex]:
                if child_vertex not in visited:
                    self.dft_recursive(child_vertex, visited)
        
            return visited
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        #create Queue
        q = Queue()
        #append the starting vertex to queue
        q.enqueue([starting_vertex])
        #create visited set
        visited = set()
        #While there is something in the Queue
        while q.size() > 0:
            #use the dequeue method for path
            path = q.dequeue()
            #the last node in the path is current node
            node = path[-1]
            if node not in visited:
                #if the node is the destination_vertex, then return the path
                if node == destination_vertex:
                    return path
                #else add the node to visited
                else:
                    visited.add(node)
                    #for every neighbor node
                    for next_node in self.vertices[node]:
                        #create a copy of the path
                        new_path = path.copy()
                        #append the next nodes to the path
                        new_path.append(next_node)
                        #append the copied path to Queue
                        q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack
        stack = Stack()
        # create a visited set
        visited = set()
        # Add the starting path to Stack
        stack.push([starting_vertex])
        # While there is something in the stack
        while stack.size() > 0:
            path = stack.pop()
            node = path[-1]

            # If node matches the destination vertex then return the path
            if node == destination_vertex:
                return path

            #If node is not in visited, add it
            if node not in visited:
                visited.add(node)

                # Find new paths and push to stack.
                for next_node in self.vertices[node]:
                    if next_node not in visited:
                        new_path = path.copy()
                        new_path.append(next_node)

                        stack.push(new_path)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("starting DFT")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("starting BFT")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("starting DFT recursive")
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("starting BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("starting DFS")
    print(graph.dfs(1, 6))
