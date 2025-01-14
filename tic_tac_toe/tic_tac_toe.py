class Tic_Tac_Toe:

    def __init__(self):
        self.board = [[0]*3 for i in range(3)]
        self.player = 1

    def get_open_spots(self):
        return [ [i,j] for i in range(3) for j in range(3) if self.board[i][j]==0]

    def is_valid_move(self, row, col):
        if 0<= row <= 2 and 0 <= col <= 2 and self.board[row][col]==0:
            return True
        return False
    
    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.player
            self.player = (self.player + 2) % 2 + 1

    def check_for_winner(self):
        for i in range(3):
            #check columns
            if self.board[i][1] == self.board[i][2] and self.board[i][0] == self.board[i][1] and self.board[i][0] !=0:
                return self.board[i][1]
            #check rows
            if self.board[1][i] == self.board[2][i] and self.board[0][i] == self.board[1][i] and self.board[0][i] !=0:
                return self.board[1][i]
            
            #check diagonals
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[1][1] !=0:
            return self.board[1][1]
            
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] !=0:
            return self.board[1][1]

        if self.get_open_spots() == []:
            return 0
        return -1
    
def print_board():
        chars = ['-', 'X', 'O']
        for r in range(3):
            for c in range(3):
                print(chars[game.board[r][c]], end=' ')
            print()

        
game = Tic_Tac_Toe()
while game.check_for_winner() == -1:
    print_board()
    r,c = eval(input('Enter spot, player ' + str(game.player)+': '))
    game.make_move(r,c)
# print_board()
x = game.check_for_winner()
if x==0:
    print("It's a tie")
else:
    print("Player",x,'wins!')
            
            



