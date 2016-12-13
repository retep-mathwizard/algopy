'''
Tutorial at: http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html
Review at - http://codereview.stackexchange.com/questions/149363/minimax-tic-tac-toe-implementation/149605#149605
'''
from operator import itemgetter
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
    '''returns the max of mapping the (move, score) tuple to the possible move using [1] of the tuple the (score)'''
    return max(map(lambda move: (move, min_play(game_state.get_next_state(move, True))), game_state.get_possible_moves()), key = itemgetter(1))

