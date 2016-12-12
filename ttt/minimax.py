#http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html
#Review - http://codereview.stackexchange.com/questions/149363/minimax-tic-tac-toe-implementation/149605#149605
#((move, 
#play(game_state.get_next_state(move, our_turn)), not our_turn) for move in game_state.get_possible_moves()))
def minimax(game_state, our_turn):
    '''returns the max of mapping the (move, score) tuple to the possible move using the second part of the tuple (score)'''
    score = game_state.get_score()
    if score is not None:
        return None, score
    #returns the move score pairs, using opposites (not our_turn
    '''
    for move in game_state.get_possible_moves:
        moves.append((move, minimax(game_state.get_next_state(move, our_turn), not our_turn)))
    '''
    moves = ((move, minimax(game_state.get_next_state(move, our_turn)), not our_turn) for move in game_state.get_possible_moves())

    return (max if our_turn else min)(moves, key=itemgetter(1))
    
