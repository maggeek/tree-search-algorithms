import bfs
import dfs
import iddfs
import astar

"""
main.py declares a start state, a goal state and a size of a board.
It then creates 4 objects, one of each class of 4 different searches,
declaring their arguments, as stated above.
It then calls methods in within these classes to perform the searches.
"""
if __name__ == "__main__":
    start_state = [(4,1),(4,2),(4,3),(4,4)]
    goal_state = [(2,2),(3,2),(4,2),(1,1)]
    board_size = (4,4)
    breadth = bfs.BFS(start_state, goal_state, board_size)
    #breadth.bfs_graph()
    #breadth.bfs_tree()
    depth = dfs.DFS(start_state, goal_state, board_size)
    depth.dfs_graph()
    #depth.dfs_tree_not_randomised()
    #depth.dfs_tree_randomised()
    iddfs = iddfs.IDDFS(start_state, goal_state, board_size)
    #iddfs.iddfs()
    astar = astar.AStar(start_state, goal_state, board_size)
    #astar.astar('distance')