class GameState:
    def __init__(self,board,char='X',oppchar='O'):
        self.char = char
        self.oppchar = oppchar
        self.board = board
        self.winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def get_score(self):
        '''returns if a game_state has been won or filled up'''
        if self.board.count(self.char) + self.board.count(self.oppchar) == 9:
            return 0
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.char and self.board[combo[1]] == self.char and self.board[combo[2]] == self.char:
                return 1    
            elif self.board[combo[0]] == self.oppchar and self.board[combo[1]] == self.oppchar and self.board[combo[2]] == self.oppchar:
                return -1         
        return None

    @staticmethod
    def return_state(score):
        if score == 0:
            return('TIED')
        elif score == 1:
            return('WON')
        elif score == -1:
            return('LOST')
        else:
            return('ERROR')

    def pretty_print(self):
        '''prints a list by 3 chars, joined by spaces'''
        print(' '.join(self.board[:3]))
        print(' '.join(self.board[3:6]))
        print(' '.join(self.board[6:9]))

    def get_possible_moves(self):
        '''returns all possible squares to place a character'''
        return [index for index, square in enumerate(self.board) if square != self.char and square != self.oppchar]

    def get_next_state(self, move, our_turn):
        '''returns the gamestate with the move filled in'''
        copy = self.board[:]
        copy[move] = self.char if our_turn else self.oppchar
        return GameState(copy, char=self.char, oppchar=self.oppchar)


