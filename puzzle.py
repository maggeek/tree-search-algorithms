"""
class Puzzle has the necessary functions to solve nPuzzle problem:
- get_next_states() finds the next possible states from a current state
- move() updates the state after the agent moves
and attributes: start_state, goal_state, board_size and tiles_no
"""
class Puzzle():
    
    def __init__(self, start_state, goal_state, board_size):
        self.start = start_state
        self.goal = goal_state
        self.board_size = board_size
        #calculate how many tiles on the board
        self.tiles_no = len(self.start) - 1

    def get_next_states(self, state):
        """get a list of next possible states for expanded node"""
        state = list(state)
        agent_pos = state[self.tiles_no]
        next_states = []
        #move up
        if agent_pos[0] > 1:
            agent_next = (agent_pos[0]-1,agent_pos[1])
            state1 = self.move(agent_next,state,agent_pos)
            next_states.append(list(state1))   
        #move down
        if agent_pos[0] < self.board_size[0]:
            agent_next = (agent_pos[0]+1,agent_pos[1])
            state2 = self.move(agent_next,state,agent_pos)
            next_states.append(list(state2))            
        #move left
        if agent_pos[1] > 1:
            agent_next = (agent_pos[0],agent_pos[1]-1)      
            state3 = self.move(agent_next,state,agent_pos)
            next_states.append(list(state3))
        #move right    
        if agent_pos[1] < self.board_size[1]:
            agent_next = (agent_pos[0],agent_pos[1]+1)
            state4 = self.move(agent_next,state,agent_pos)
            next_states.append(list(state4))
        return next_states
    
    def move(self,agent_next, state, agent_pos):
        """update the state after agent's move"""
        state = list(state)
        #check if there is a tile where the agent has just moved
        if agent_next in state:
        #check which tile and swap it with agent
            ind = state.index(agent_next)
            state[ind] = agent_pos
        state[self.tiles_no] = agent_next
        return state