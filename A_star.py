import heapq

# Define the 8-puzzle game state representation
class PuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = 0  # Cost from the initial state
        self.h = 0  # Heuristic value (estimated cost to reach the goal state)
    
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.board == other.board

    def is_goal(self, goal_state):
        return self.board == goal_state

    def generate_successors(self):
        successors = []
        row, col = self.board.index(0) // 3, self.board.index(0) % 3
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = self.board[:]
                new_board[row * 3 + col], new_board[new_row * 3 + new_col] = new_board[new_row * 3 + new_col], new_board[row * 3 + col]
                successors.append(PuzzleState(new_board, self, move=f"Move {new_board[row*3+col]} to {new_row*3+new_col}"))
        
        return successors

# Define the A* search algorithm
def astar(initial_state, goal_state):
    open_list = [initial_state]
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        closed_set.add(tuple(current_state.board))

        if current_state.is_goal(goal_state):
            path = []
            while current_state.parent:
                path.append(current_state.move)
                current_state = current_state.parent
            path.reverse()
            return path

        for successor in current_state.generate_successors():
            if tuple(successor.board) not in closed_set:
                successor.g = current_state.g + 1
                successor.h = heuristic(successor.board, goal_state.board)
                heapq.heappush(open_list, successor)

    return None  # No solution found

# Define a simple manhattan distance heuristic
def heuristic(board, goal_board):
    distance = 0
    for i in range(9):
        if board[i] != goal_board[i]:
            r1, c1 = i // 3, i % 3
            r2, c2 = goal_board.index(board[i]) // 3, goal_board.index(board[i]) % 3
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance

# Example usage
if __name__ == "__main":
    initial_state = PuzzleState([1, 2, 3, 8, 0, 4, 7, 6, 5])
    goal_state = PuzzleState([1, 2, 3, 8, 0, 4, 7, 6, 5])

    path = astar(initial_state, goal_state)
    if path:
        print("Solution found! Steps:")
        for step in path:
            print(step)
    else:
        print("No solution found.")
