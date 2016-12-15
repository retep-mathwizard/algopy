'''
http://codereview.stackexchange.com/questions/149363/minimax-tic-tac-toe-implementation/149605#149605
'''
from operator import itemgetter

def minimax(game_state, our_turn):
    '''if the game is over returns (None, score), otherwise recurses to find the best move and returns it and the score.'''
    score = game_state.get_winner()
    if game_state.is_gameover():
        return game_state.score()
    moves = ((move, minimax(game_state.get_next_state(move, our_turn), not our_turn)) for move in game_state.get_possible_moves())
    return (max if our_turn else min)(moves, key=itemgetter(1))

moves = []

def expanded_minimax(game_state, our_turn):
    global moves
    if game_state.is_gameover():
        return game_state.score()
    
    for move in game_state.get_possible_moves():
        child = game_state.get_next_state(move, our_turn)
        score = expanded_minimax(child, not our_turn)
        moves.append(move, score)
        
    if our_turn:
        return max(moves, key=itemgetter(1))
    else:
        return min(moves, key=itemgetter(1))
