import puzzle
import random

"""
Class DFS inherits from Puzzle class.
It performs a depth-first search, both as a graph and a tree search.
"""
class DFS(puzzle.Puzzle):
  
    def dfs_graph(self):
        """perform a depth-first search as a graph search"""
        stack = [self.start]
        explored = []
        found = False
        while not found and stack:
            #pop the deepest node from the stack
            current_state = stack.pop()
            if len(explored) < 50:
                print("Parent state: ", current_state)
            #get the neighbouring states
            neighbours = list(self.get_next_states(current_state))
            if len(explored) < 50:
                print("Its neighbouring states: ", neighbours)
            neighbours = list(reversed(neighbours))
            for neighbour in neighbours:
                #check if the node is already explored
                if neighbour not in explored:
                    #if not, add to explored nodes
                    explored.append(neighbour)
                    #check if the state is the goal state
                    if neighbour[0:self.tiles_no] == self.goal[0:self.tiles_no]:
                        found = True
                        break
                    #add node to the stack
                    stack.append(neighbour)     
        if found:
            print(len(explored))
            return len(explored)
    
    def dfs_tree_not_randomised(self):
        """perform a depth-first search as a tree search"""
        stack = [self.start]
        found = False
        time = 0
        while not found and stack:
            #pop the deepest node from the stack
            current_state = stack.pop()
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
                #add node to the stack
                stack.append(neighbour)          
        if found:
            print(time)
            return time
    
    def dfs_tree_randomised(self):
        """perform a depth-first search as a tree search
        with a random choice of the next state to explore"""   
        stack = [self.start]
        found = False
        time = 0
        while not found and stack:
            #pop the deepest node from the stack
            current_state = stack.pop()
            if time < 100:
                print("Parent state: ", current_state)
            #get the neighbouring states
            neighbours = list(self.get_next_states(current_state))
            if time < 100:
                print("Its neighbouring states: ", neighbours)
            #randomly picks a state from the neighbouring states
            neighbour = neighbours[random.randrange(len(neighbours))]
            #count the explored nodes
            time += 1
            #check if the state is the goal state
            if neighbour[0:self.tiles_no] == self.goal[0:self.tiles_no]:
                found = True
                break
            #add node to the stack
            stack.append(neighbour)          
        if found:
            print(time)
            return time