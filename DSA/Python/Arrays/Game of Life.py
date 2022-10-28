#Problem Link: https://leetcode.com/problems/game-of-life/submissions/

def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    m=len(board)
    n=len(board[0])
    l=[0]*(n+2)
    for i in range(m):
        board[i]=[0]+board[i]+[0]

    board=[l]+board+[l]

    print(board)    

    ans=[]

    for i in range(1,m+1):
        for j in range(1,n+1):
            count=0
            count=board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]
            if board[i][j]==1:
                if count<2:
                    ans.append(0)
                elif count>=2 and count<=3:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                if count==3:
                    ans.append(1)
                else:
                    ans.append(0)
    board.pop(0)
    board.pop()
    for i in range(m):
        board[i].pop(0)
        board[i].pop()
    z=0
    for i in range(m):
        for j in range(n):
            board[i][j]=ans[z]
            z+=1
