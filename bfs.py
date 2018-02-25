from collections import deque
import puzzle

"""
Class BFS inherits from Puzzle class.
It performs a breadth-first search, both as a graph and a tree search.
"""
class BFS(puzzle.Puzzle):
    
    def bfs_graph(self):
        """perform a breadth-first search as a graph search"""
        explored = []
        queue = deque([self.start])
        found = False
        while not found and queue:
            #pop the shallowest node from the queue
            current_state = queue.popleft()
            if len(explored) < 50:
                print("Parent state: ", current_state)
            #get the neighbouring states
            neighbours = list(self.get_next_states(current_state))
            if len(explored) < 50:
                print("Its neighbouring states: ", neighbours)
            for neighbour in neighbours:
                #check if the node is already explored
                if neighbour not in explored:
                    #if not, add to explored nodes               
                    explored.append(neighbour)
                    #check if the state is the goal state
                    if neighbour[0:self.tiles_no] == self.goal[0:self.tiles_no]:
                        found = True
                        break
                    #add node to the queue               
                    queue.append(neighbour)
        if found:
            print(len(explored))
            return len(explored)
    
    def bfs_tree(self):
        """perform a breadth-first search as a tree search"""
        queue = deque([self.start])
        found = False
        time = 0
        while not found and queue:
            #pop the shallowest node from the queue
            current_state = queue.popleft()
            if time < 100:
                print("Parent state: ", current_state)
            #get the neighbouring states
            neighbours = list(self.get_next_states(current_state))
            if time < 100:
                print("Its neighbouring states: ", neighbours)
            for neighbour in neighbours:
                #count the explored nodes
                time += 1
                #check if the state is the goal state
                if neighbour[0:self.tiles_no] == self.goal[0:self.tiles_no]:
                    found = True
                    break
                #add node to the queue               
                queue.append(neighbour)
        if found:
            print(time)
            return time