import puzzle

"""
Class DFS inherits from Puzzle class.
It performs an iterative deepening depth-first search.
"""
class IDDFS(puzzle.Puzzle):
           
    def iddfs(self):
        """perform an iterative deepening depth-first search"""
        explored = 0
        depth_limit = 10000
        for depth in range(depth_limit):
            result, explored = self.dls(self.start, depth, explored)
            #print(result)
            #print(explored)
            if result == True:
                #print(depth)
                #print(explored)
                return True
        
    def dls(self, state, depth, explored):
        """perform a depth-limited search"""
        #check if the state is the goal state
        if depth == 0 and state[0:self.tiles_no] == self.goal[0:self.tiles_no]:
            return True, explored
        if depth > 0:
            if explored < 100:
                print("Parent state: ", state)
            #get the neighbouring states
            neighbours = list(self.get_next_states(state))
            if explored < 100:
                print("Its neighbouring states: ", neighbours)
            for neighbour in neighbours:
                #add 1 to explored states
                explored += 1
                found, explored = self.dls(neighbour, depth-1, explored)
                if found is True:
                    return True, explored
        return False, explored