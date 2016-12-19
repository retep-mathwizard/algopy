class GameState:
    def __init__(self,board,char='X',oppchar='O'):
        self.char = char
        self.oppchar = oppchar
        self.board = board
        self.winning_combos = (((0,0),(0,1),(0,2),(0,3)),((0,1),(0,2),(0,3),(0,4)),((0,2),(0,3),(0,4),(0,5)),
((1,0),(1,1),(1,2),(1,3)),((1,1),(1,2),(1,3),(1,4)),((1,2),(1,3),(1,4),(1,5)),
((2,0),(2,1),(2,2),(2,3)),((2,1),(2,2),(2,3),(2,4)),((2,2),(2,3),(2,4),(2,5)),
((3,0),(3,1),(3,2),(3,3)),((3,1),(3,2),(3,3),(3,4)),((3,2),(3,3),(3,4),(3,5)),
((4,0),(4,1),(4,2),(4,3)),((4,1),(4,2),(4,3),(4,4)),((4,2),(4,3),(4,4),(4,5)),
((5,0),(5,1),(5,2),(5,3)),((5,1),(5,2),(5,3),(5,4)),((5,2),(5,3),(5,4),(5,5)),
((6,0),(6,1),(6,2),(6,3)),((6,1),(6,2),(6,3),(6,4)),((6,2),(6,3),(6,4),(6,5)),
#Vertical ^
((0,0),(1,0),(2,0),(3,0)),((1,0),(2,0),(3,0),(4,0)),((2,0),(3,0),(4,0),(5,0)),((3,0),(4,0),(5,0),(6,0)),
((0,1),(1,1),(2,1),(3,1)),((1,1),(2,1),(3,1),(4,1)),((2,1),(3,1),(4,1),(5,1)),((3,1),(4,1),(5,1),(6,1)),
((0,2),(1,2),(2,2),(3,2)),((1,2),(2,2),(3,2),(4,2)),((2,2),(3,2),(4,2),(5,2)),((3,2),(4,2),(5,2),(6,2)),
((0,3),(1,3),(2,3),(3,3)),((1,3),(2,3),(3,3),(4,3)),((2,3),(3,3),(4,3),(5,3)),((3,3),(4,3),(5,3),(6,3)),
((0,4),(1,4),(2,4),(3,4)),((1,4),(2,4),(3,4),(4,4)),((2,4),(3,4),(4,4),(5,4)),((3,4),(4,4),(5,4),(6,4)),
((0,5),(1,5),(2,5),(3,5)),((1,5),(2,5),(3,5),(4,5)),((2,5),(3,5),(4,5),(5,5)),((3,5),(4,5),(5,5),(6,5)),
#Horizontal ^
((0,0),(1,1),(2,2),(3,3)),((0,3),(1,2),(2,1),(3,0)),((0,1),(1,2),(2,3),(3,4)),((0,4),(1,3),(2,2),(3,1)),
((0,2),(1,3),(2,4),(3,5)),((0,5),(1,4),(2,3),(3,2)),((1,0),(2,1),(3,2),(4,3)),((1,3),(2,2),(3,1),(4,0)),
((1,1),(2,2),(3,3),(4,4)),((1,4),(2,3),(3,2),(4,1)),((1,2),(2,3),(3,4),(4,5)),((1,5),(2,4),(3,3),(4,2)),
((2,0),(3,1),(4,2),(5,3)),((2,3),(3,2),(4,1),(5,0)),((2,1),(3,2),(4,3),(5,4)),((2,4),(3,3),(4,2),(5,1)),
((2,2),(3,3),(4,4),(5,5)),((2,5),(3,4),(4,3),(5,2)),((3,0),(4,1),(5,2),(6,3)),((3,3),(4,2),(5,1),(6,0)),
((3,1),(4,2),(5,3),(6,4)),((3,4),(4,3),(5,2),(6,1)),((3,2),(4,3),(5,4),(6,5)),((3,5),(4,4),(5,3),(6,2)))
#Diagonal ^
    def is_gameover(self):
        '''returns if a game_state has been won or filled up'''
        if self.score() is 'INCOMPLETE':
            return False
        return True
    def score(self):
        '''returns 1, 0, or -1 corresponding to the score (WIN, TIE, LOSS) from the ai's point of view'''

        for combo in self.winning_combos:
            #broken
            if self.board[combo[0][0]][combo[0][1]] == self.char and self.board[combo[1][0]][combo[1][1]] == self.char and self.board[combo[2][0]][combo[2][1]] == self.char and self.board[combo[3][0]][combo[3][1]] == self.char:
                return 1
            elif self.board[combo[0][0]][combo[0][1]] == self.oppchar and self.board[combo[1][0]][combo[1][1]] == self.oppchar and self.board[combo[2][0]][combo[2][1]] == self.oppchar and self.board[combo[3][0]][combo[3][1]] == self.oppchar:
                return -1
        if self.get_possible_moves() == []:
            return 0
       
        return 'INCOMPLETE'
    @staticmethod
    def return_state(score):
        '''Returns a word for each score'''
        if score == 0:
            return('TIED')
        elif score == 1:
            return('WON')
        elif score == -1:
            return('LOST')
        else:
            return('ERROR:Score was:' + str(score))

    def pretty_print(self):
        '''prints the board joined by spaces'''
        for char_num in range(len(self.board[0])): 
            for col in self.board: 
                print(col[char_num],end='|') 
            print()

    def get_possible_moves(self):
        '''returns all possible squares to place a character'''
        return [index for index, row in enumerate(self.board) if ' ' in row]

    def get_next_state(self, move, our_turn):
        '''returns the gamestate with the move filled in'''
        print(self.board)
        copy = self.board[:]
        for index, char in list(enumerate(copy[move]))[::-1]:
            if char == ' ':
                if our_turn:
                    copy[move][index] = self.char
                    break
                else:
                    copy[move][index] = self.oppchar
                    break
        #copy[move][next(index for index, char in enumerate(copy[move][::-1]) if char==' ')] = self.char if our_turn else self.oppchar
        return GameState(copy, char=self.char, oppchar=self.oppchar)


