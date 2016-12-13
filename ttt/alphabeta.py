#Using wikipedia pseudocode w/o depth
def alphabeta(game_state, alpha=-2, beta=2, our_turn=True):
    if game_state.is_gameover():
        return game_state.score(), None
    if our_turn:
        score = -2
        for move in game_state.get_possible_moves():
            child = game_state.get_next_state(move, True)
            temp_max, _ = alphabeta(child, alpha, beta, False)
            if temp_max > score:
                score = temp_max
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return score, best_move
    else:
        score = 2
        for move in game_state.get_possible_moves():
            child = game_state.get_next_state(move, False)
            temp_min, _ = alphabeta(child, alpha, beta, True)
            if temp_min < score:
                score = temp_min
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return score, best_move
    
