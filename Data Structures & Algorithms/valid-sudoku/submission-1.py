class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        src = set()
        x=0
        y=3
        while y<10:
            #print("x=",x,"y=",y)
            for i in range(0,9):
                for j in range(x,y):
                    #print(i,j)
                    if board[i][j]!='.':
                        #print(board[i][j])
                        if board[i][j] in src:
                            return False
                        src.add(board[i][j])
                if (i+1)%3==0:
                    src = set()    
            
            x+=3
            y+=3
        sr = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    if board[i][j] in sr:
                        return False
                    sr.add(board[i][j])
            sr = set()
        sc = set()
        for i in range(0,9):
            for j in range(0,9):
                print(j,i)
                if board[j][i]!='.':
                    if board[j][i] in sc:
                        return False
                    sc.add(board[j][i])
            sc = set()

        return True