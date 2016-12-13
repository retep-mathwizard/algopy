def minimax(game_state, our_turn=True):
    if game_state.is_gameover(): 
        return game_state.score(), None
    if our_turn:
        score = -2
        for move in game_state.get_possible_moves():
            child = game_state.get_next_state(move, True)
            temp_score, _  = minimax(child, False)
            if temp_score > score:
                score = temp_score
                best_move = move
        return score, best_move
    else:
        score = 2
        for move in game_state.get_possible_moves():
            child = game_state.get_next_state(move, False)
            temp_score, _ = minimax(child, True)
            if temp_score < score:
                score = temp_score
                best_move = move
        return score, best_move

