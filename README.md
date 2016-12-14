# pyai
Algorithms in Python


+ Minimax
+ Alpha-Beta
+ Negamax
+ Alpha-Beta Negamax


Note: To add depth, add a depth argument to the function, and when calling it use `depth - 1`. 
Check if depth equals 0, if so return the value of the node.

Added code:
```
minimax(depth):
  if depth == 0:
    return 
  minimax(depth - 1)
```
