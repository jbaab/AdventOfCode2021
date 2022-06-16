import numpy as np

"""Day 04"""
class Bin_board():
    """class that represents a bingo board"""
    def __init__(self, np_board) -> None:
        self.board = np_board
        # Boolean mask to mark the hits
        self.hits = np.ma.make_mask(np.zeros((5,5)), shrink=False)

    def update_hit(self, val):
        """ updates hit mask with a drawn number"""
        hit = self.board == val
        self.hits = self.hits | hit

    def check_win(self):
        """checks if row or column is True"""
        x = np.any(np.all(self.hits, axis=0))
        y = np.any(np.all(self.hits, axis=1))
        return x | y

    def win(self, curr_ran):
        """calculates the winning score according AOC2021"""
        return np.sum(self.board[~self.hits])*curr_ran

class Bingo():
    def __init__(self, ran_numbers) -> None:
        self.ran_numbers = ran_numbers
        self.boards = []
    def addboard(self, board):
        self.boards.append(board)
    
    def run(self):
        """plays Bingo: Draws numbers from the List and marks hits on each
        board. If one board won, calculates score"""
        for ran in self.ran_numbers:
            for board in self.boards:
                board.update_hit(ran)
                if board.check_win():
                    return board.win(ran)

    def run_step2(self):
        """plays Bingo: Draws numbers from the List and marks hits on each
        board. calculates score of the board that wins last"""
        win_list = []
        for ran in self.ran_numbers:
            for board in self.boards:
                board.update_hit(ran)
                if board.check_win():
                    win_list.append((board,ran))
                    self.boards.remove(board)
        return win_list[-1][0].win(win_list[-1][1])


def main():
    # random number input:
    with open('04\\input.txt', 'r') as inp_txt:
        ran_inp = inp_txt.readline()
    ran_inp = list(map(int,ran_inp.split(",")))
    # bingo boards
    bin_sets = np.loadtxt('04\\input.txt', skiprows=2)
    # game instance
    game = Bingo(ran_inp)
    for i in range(0,bin_sets.shape[0],5):
        game.addboard(Bin_board(bin_sets[i:i+5,]))

    # step 1
    result1 = game.run()
    print(f"Step 1: {result1}")
    # step 2
    result2 = game.run_step2()
    print(f"Step 2: {result2}")

if __name__ == "__main__":
    main()