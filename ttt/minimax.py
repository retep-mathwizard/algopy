#http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html
#Lambda - https://www.programiz.com/python-programming/anonymous-function
#Map - http://book.pythontips.com/en/latest/map_filter.html

'''max and min will call on each other recusively, until a terminal state'''
def max_play(game_state):
    '''if the game is over returns score, otherwise calls min_play on it's childen (possible moves from the state) and returns the maximum'''
    if game_state.is_gameover():
        return game_state.score()
    return max(map(lambda move: min_play(game_state.get_next_state(move, True)), game_state.get_possible_moves()))

def min_play(game_state):
    '''if the game is over returns score, otherwise calls max_play on it's childen (possible moves from the state) and returns the minimum'''
    if game_state.is_gameover():
        return game_state.score()
    return min(map(lambda move: max_play(game_state.get_next_state(move, False)), game_state.get_possible_moves()))

def minimax(game_state):
    '''returns the max of mapping the (move, score) tuple to the possible move using the second part of the tuple (score)'''
    return max(map(lambda move: (move, min_play(game_state.get_next_state(move, True))), game_state.get_possible_moves()), key = lambda x: x[1])
