# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(word, board, i, j, 0):
                    return True
        return False
    
    def backtrack(self, word, board, i, j, idx):
        if board[i][j] != word[idx]:
            return False           
        if len(word) - idx == 1: return True
        letter = board[i][j]
        board[i][j] = "#"
        neighbors = self.getNeighbors(i,j, board)
        for neighbor in neighbors:
            if self.backtrack(word, board, neighbor[0], neighbor[1], idx + 1): return True
        board[i][j] = letter
        
    def getNeighbors(self, i, j, matrix):
        neighbors = []
        if i > 0:
            neighbors.append([i-1, j])
        if i < len(matrix) - 1:
            neighbors.append([i+1,j])
        if j > 0:
            neighbors.append([i, j-1])
        if j < len(matrix[0]) - 1:
            neighbors.append([i, j + 1])
        return neighbors
        
