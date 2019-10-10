import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size():
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            return False # We were unable to create a friendship
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}") 

        # Create friendships
        # Create connections along the way
        # Define or keep track of...
        target_friendships = numUsers * avgFriendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)
            if self.addFriendship(userID, friendID):
                total_friendships += 2
            else:
                collisions += 1

        print(f"COLLISIONS: {collisions}")
                

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        #Use BFS and make a queue
        q = Queue()
        # Use enqueue to append userid to the queue
        q.enqueue([userID])

        #while queue isn't empty
        while q.size() > 0:
            #dequeue
            path = q.dequeue()
            #last on path is the new current user
            node = path[-1]
            #if node hasn't been visited
            if node not in visited:
                #adding this path to the dictionary as A shortest way here
                visited[node] = path
                #for each of the node's neighbor, make a copy, append the node to the copy
                #enqueue the copied path 
                for next_node in self.friendships[node]:
                    copiedPath = path.copy()
                    copiedPath.append(next_node)
                    q.enqueue(copiedPath)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("Print Friendships")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Print Connections")
    print(connections)
    print(f"User in extended social network: {len(connections) - 1}")


    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])

    print(f"Avg length of social path: {total_social_paths/len(connections)}")