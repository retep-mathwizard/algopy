#http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html
#Review - http://codereview.stackexchange.com/questions/149363/minimax-tic-tac-toe-implementation/149605#149605
from operator import itemgetter
def minimax(game_state, our_turn):
    score = game_state.get_score()
    if score is not None:
        return (None, score)
    #returns the move score pairs, using opposites (not our_turn) 
    #tuple of move, score for move 
    for move in game_state.get_possible_moves():
        moves = ((move, minimax(game_state.get_next_state(move, our_turn)), not our_turn)
    if our_turn:
        return max(moves, key=itemgetter(1))
    else:
        return min(moves, key=itemgetter(1))
    return (max if our_turn else min)(moves, key=itemgetter(1))
    
