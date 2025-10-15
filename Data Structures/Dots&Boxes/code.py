"""
You are to implement the core logic for the game Dots and Boxes.

There are two players who take turns connecting two adjacent dots on an n × n grid. 
A move is represented by the coordinates of the two dots being connected. 
If a player completes a box (meaning they place the fourth and final edge around a square), they immediately win the game.

Your function should process a sequence of moves and determine if any player completes a box.
If a box is formed, return the name of the player who won. 
Otherwise, continue until all moves are processed.

You can assume input will either come interactively (via input()) or from an array of moves.



Notes:

variables 

Track the game statem -> 2d matrix
. . .   cols-1 * rows + rows-1 * cols

.-. .
  |
. . .

connections

dots = (even, even)
horizontal = (even, odd)
vertical = (odd, even)
center_of_boxes = (odd, odd)


for horizontal lines -> check top and bottom (r-1, c), (r+1, c)
for vertical lines -> check left and right (r, c-1), (r, c+1)
players and turns
track the connections (edges) -> set of tuples ((r1, c1), (r2, c2)) -> sort 


Organized into a class with methods 

constructor 

process input -> list of moves -> [[(r1, c1), (r2, c2)],...]

validate move
integers
within bounds of the board
dots should be adjacent (rows or cols)
this edge or connection does not already exist

play the move
update the representation of the board
update the connections 

check for boxes -> player or



switch turns

"""

class DotsAndBoxes:
    def __init__(self, player1, player2, size):
        self.size = size
        self.players = [player1, player2]
        self.turns = 0
        self.edges = set()
        size = self.size * 2 - 1 
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        for row in range(size):
            for col in range(size):
                if not row & 1 and not col & 1:
                    self.board[row][col] = '.'
        
    def play(self, moves):
        for start, end in moves:
            if self.validate_move(start, end):
                result = self.make_move(start, end) # -> {box_formed: True/False, winner: playerx}
                if result['box_formed']:
                    return f'{result['winner']} has won the game!'
                if result['game_over']:
                    return f'The game has ended.'
        return 'The game has ended without a winner.'
                
    def validate_move(self, start, end):
        row1, col1 = start
        row2, col2 = end
        if not (0 <= row1 < self.size*2 -1  and 0 <= col1< self.size*2-1 and
                0 <= row2 < self.size*2 -1  and 0 <= col2 < self.size*2-1):
            return False
        edge = tuple(sorted(start, end))
        if edge in self.edges:
            return False
        if not ((row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1)):
            return False
        return True
    
    def make_move(self, start, end):
        self.edges.add(tuple(sorted(start, end)))
        row1, col1 = start
        row2, col2 = end
        row = col = None
        result = {
            "box_formed": False,
            "winner" : None,
            "game_over": False
        }
        if row1 == row2:
            row = row1
            col = min(col1*2, col2*2) + 1
            self.board[row][col] = '-'
            if self.box_formed(row-1, col) or self.box_formed(row+1, col):
                result['box_formed'] = True
                result['winner'] = self.players[self.turns]
        else:
            row = min(row1*2, row2*2) + 1
            col = col1
            self.board[row][col] = '|'
            if self.box_formed(row, col-1) or self.box_formed(row, col+1):
                result['box_formed'] = True
                result['winner'] = self.players[self.turns]
        self.update_turns()
        return result

    def box_formed(self, row, col):
        if not (0 <= row < self.size*2 -1  and 0 < col < self.size*2-1):
            return False
        return self.board[row-1][col] == self.board[row+1][col] == '-' and self.board[row][col-1] == self.board[row][col+1] == '|'

    def update_turns(self):
        self.turns ^= 1
    
def main():
    pass