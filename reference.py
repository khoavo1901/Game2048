import random

class Game2048():
    def __init__(self):
        """
        Initializes a 4x4 matrix (game board) filled with zeros.
        """
        self. matrix = [[0] * 4 for _ in range(4)]

    #
    def add_2_random(self):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

        # check if the random cell is empty or not
        while(self.matrix[r][c] != 0):
            r = random.randint(0, 3)
            c = random.randint(0, 3)
        
        self.matrix[r][c] = 2
    
    def combine(mat):
        