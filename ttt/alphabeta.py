#My mind broke. WIP
def alpha_beta(game_state, alpha, beta):
    if game_state.is_gameover():
        return game_state.score()

def max_play(game_state, alpha, beta):
    if game_state.is_gameover():
        return game_state.score()

def min_play(game_state, alpha, beta):

    if game_state.is_gameover():
        return game_state.score()
    moves = game_state.get_possible_moves()
    for move in moves:
        copy = game_state.get_next_state(move, False)
        score = max_play(copy)

        if beta <= alpha:
            break
