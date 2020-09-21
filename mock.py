# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        # use a list to store the clicks
        # helper method to find neighbors
        
        def findNeighbor(board, click):
            res = []
            row = [0]
            column = [0]
            if len(board)>1:
                if click[0] == 0:
                    row = [0, 1]
                elif click[0] == len(board) - 1:
                    row = [-1, 0]
                else:
                    row = [-1,  0,  1]
            if len(board[0])>1:
                if click[1] == 0:
                    column = [0, 1]
                elif click[1] == len(board[0]) - 1:
                    column = [-1, 0]
                else:
                    column = [-1, 0, 1]
            for num1 in row:
                for num2 in column:
                    neighbor = [click[0] + num1, click[1] + num2]
                    if (not neighbor in res) and not (num1 == 0 and num2 == 0) and (board[neighbor[0]][neighbor[1]] != 'B'):
                        res.append(neighbor)
            return res
        
        clicks = []
        clicks.append(click)
        while(clicks):
            click = clicks.pop()

            if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
            else:
                
                neighbors = findNeighbor(board, click)     
                #print(neighbors)
                count = 0
                for neighbor in neighbors:
                    if board[neighbor[0]][neighbor[1]] == 'M':
                        count += 1
                if count > 0:
                    board[click[0]][click[1]] = str(count)
                else:
                    board[click[0]][click[1]] = 'B'
                    for neighbor in neighbors:
                        clicks.append(neighbor)
                        board[neighbor[0]][neighbor[1]] = 'B'
                        #print(board)
                        
        return board
                        
        