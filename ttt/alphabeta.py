#Using wikipedia pseudocode w/o depth
def alphabeta(game_state, alpha, beta, our_turn=True):
    if game_state.is_gameover():
        return (None, game_state.score())
    if our_turn:
        score = -9999
        for move in game_state.get_possible_moves():
            child = game_state.get_next_state(move, True)
            temp_max = alphabeta(child, alpha, beta, False)
            if temp_max[1] > score:
                print(score)
                score = temp_max[1]
                max_tuple = temp_max
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_tuple
    else:
        score = 9999
        for move in game_state.get_possible_moves():
            child = game_state.get_next_state(move, False)
            temp_min = alphabeta(child, alpha, beta, True)
            if temp_min[1] < score:
                score = temp_min[1]
                min_tuple = temp_min
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_tuple
    
