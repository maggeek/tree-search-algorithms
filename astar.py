import puzzle

"""
Class AStar inherits from Puzzle class.
It performs an A* search with a choice of 2 heuristics:
- counting misplaced tiles
- calculating a total Manhattan distance
"""
class AStar(puzzle.Puzzle):
    
    def astar(self, heuristic):
        """perform an A* search"""
        #check what heuristic is used and make a list with heuristic evaluation and start state
        if heuristic == 'distance':
            frontier = [[self.heuristic_distance(self.start,self.goal), self.start]]
        elif heuristic == 'misplaced':
            frontier = [[self.heuristic_misplaced(self.start,self.goal), self.start]]     
        explored = []
        while frontier:
            i = 0
            for j in range(1, len(frontier)):
                if frontier[i][0] > frontier[j][0]:
                    i = j
            path = frontier[i]
            #update the frontier
            frontier = frontier[:i] + frontier[i+1:]
            current_state = path[-1]
            if len(explored) < 50:
                print("Parent state: ", current_state)
            #check if the state is the goal state
            if current_state[0:self.tiles_no] == self.goal[0:self.tiles_no]: 
                break
            #get the neighbouring states
            neighbours = list(self.get_next_states(current_state))
            if len(explored) < 50:
                print("Neighbouring states: ", neighbours)
            #iterate through the neighbouring states
            for neighbour in neighbours:
                #if the neighbouring state has not been explored already,
                #update solution path with help of the heuristic function
                if neighbour not in explored:
                    if heuristic == 'distance':
                        newpath = [path[0] + self.heuristic_distance(neighbour,self.goal) - self.heuristic_distance(current_state,self.goal)] + path[1:] + [neighbour] 
                    elif heuristic == 'misplaced':
                        newpath = [path[0] + self.heuristic_misplaced(neighbour,self.goal) - self.heuristic_misplaced(current_state,self.goal)] + path[1:] + [neighbour] 
                    #add a new path to the frontier
                    frontier.append(newpath)
                    #add the state to the explored states
                    explored.append(neighbour)
        print("Expanded nodes: ", len(explored))
        print("Solution: ", path)

    def heuristic_distance(self,state1,state2):
        """calculate a total Manhattan distance"""
        distance = 0
        for i in range(3):
            if state1[i] != state2[i]:
                distance += abs(state2[i][0] - state1[i][0]) + abs(state2[i][1] - state1[i][1])
        return distance

    def heuristic_misplaced(self,state1,state2):
        """count the number of misplaced tiles"""
        misplaced = 0
        for i in range(self.tiles_no):
            if state1[i] != state2[i]:
                misplaced += 1
        return misplaced