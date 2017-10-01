# Tic_Tac_Toe
A python script to evaluate any position in Tic Tac Toe.

# Running this code on your machine:
1. Have a functioning Python 2.7+ version installed
2. Clone this repository
3. Open a terminal and cd into src
4. Run python and import main (and optionally import positions)
5. Run main.solve() on a position (either make your own or use one from positions.py)

Examples:

```python
main.solve([['_', 'O', 'X'], ['_', 'X', '_'], ['O', '_', 'X']])
main.solve(positions.o_wins_1)
```

Use capital X, capital O, and underscores for X, O, and blanks respectively.

Always pass in a 3x3 list.

# Explanation of the Code
This code is meant to follow minimax strictly by building a full decision tree under the position.

The position is evaluated from the bottom up, assuming both X and O are perfect players.

The program deliberately does not take advantage of storing positions or checking for symmetry.

There is a performance hit as a result (opening position: ~15 seconds, 1 Move: ~2 seconds, 2+ Moves: Instant)
