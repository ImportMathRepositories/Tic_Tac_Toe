# Solves the exact evaluation of any tic tac toe position

import copy

# Square definitions
X_SQUARE = 'X'
O_SQUARE = 'O'
BLANK = '_'

# Evaluation definitions
X_WINS = 'X wins!'
O_WINS = 'O wins!'
DRAW = 'Draw!'

# Returns true if X's turn to move, false otherwise
def is_X_turn(pos):
	x_count = 0
	for row in pos:
		x_count += row.count(X_SQUARE)
		x_count -= row.count(O_SQUARE)
	return x_count == 0

# Returns true if every space is taken, false otherwise
def is_full(pos):
	for row in pos:
		if BLANK in row:
			return False
	return True

# Takes a position, and returns a list of every position that can result from a move
def get_branches(pos, X_turn):
	symbol = X_SQUARE if X_turn else O_SQUARE
	branches = []
	for row in range(3):
		for square in range(3):
			if pos[row][square] == BLANK:
				branches.append(copy.deepcopy(pos))
				branches[-1][row][square] = symbol
	return branches

# Checks for three in a row in the current position, returns evaluation
def get_static_eval(pos):
	potential_wins = []

	# Three in a row
	for row in pos:
		potential_wins.append(set(row))

	# Three in a column
	for i in range(3):
		potential_wins.append(set([pos[k][i] for k in range(3)]))

	# Three in a diagonal
	potential_wins.append(set([pos[i][i] for i in range(3)]))
	potential_wins.append(set([pos[i][2 - i] for i in range(3)]))

	# Checking if any three are the same
	for trio in potential_wins:
		if trio == set([X_SQUARE]):
			return X_WINS
		elif trio == set([O_SQUARE]):
			return O_WINS
	return DRAW

# Returns the dynamic evaluation of any valid position
def solve(pos):
	# Immediately return the static evaluation if it is decisive
	static_eval = get_static_eval(pos)
	if static_eval != DRAW:
		return static_eval

	# Check for full board
	if is_full(pos):
		return DRAW

	# Checking and evaluating every path
	X_turn = is_X_turn(pos)
	branches = get_branches(pos, X_turn)
	branch_evals = [solve(branch) for branch in branches]

	# Returning the result assuming best play
	if X_turn:
		# X options from best to worst
		if X_WINS in branch_evals:
			return X_WINS
		elif DRAW in branch_evals:
			return DRAW
		else:
			return O_WINS
	else:
		# O options from best to worst
		if O_WINS in branch_evals:
			return O_WINS
		elif DRAW in branch_evals:
			return DRAW
		else:
			return X_WINS
