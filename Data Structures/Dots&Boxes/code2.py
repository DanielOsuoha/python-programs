class DotsAndBoxes:
    """"""
    def __init__(self, player1, player2, board_size):
        self.players = [player1, player2]
        self.turns = 0
        self.size = board_size * 2 -1
        self.edges = set()
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        for row in range(0, self.size, 2):
            for col in range(0, self.size, 2):
                self.board[row][col] = '.'

def main():
    import sys
    input = sys.stdin.readline
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")
    board_size = input("Size of board: ")
    game = DotsAndBoxes(player1, player2, board_size)