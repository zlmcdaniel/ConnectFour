"""
Created on Thu Nov 14 14:20:42 2019
@author: sullia4 and mcdanz
2 players no win con
"""
import random

def clear_board():
    board= []
    for a in range(6):
        board.append(['.'] * 7)
    return board

def row_num(col, board):
    n = int(len(board) - 1)
    while True:
        if board[n][col] == ".":
            return n
        n-= 1
        if n < 0:
            return -1
        

def is_consecutive(board, row, col, direction, piece):
    count = 0
    
    if(direction == "horizontal"):
        for i in range(6):
            if(board[row][i] == piece):
                count += 1
            else:
                count = 0
        
    elif(direction == "vertical"):
        for i in range(6):
            if(board[i][col] == piece):
                count += 1
            else:
                count = 0
                
    elif(direction == "diagonalneg"):
        while(row != len(board) and col != len(board[0])):
            if(board[row][col] == piece):
                count += 1
            else:
                count = 0
            row += 1
            col += 1
            
    elif(direction == "diagonalpos"):
        while(row != 0 and col != len(board[0])):
            if(board[row][col] == piece):
                count += 1
            else:
                count = 0
            row -= 1
            col += 1
    
    if(count >= 4):
        return True
    else:
        return False
        


def check_win(board, row, col, piece): 
    count = 0       
    print("count:" , (board[5]).count(piece))
    if(board[5].count(piece) >= 4):
        return is_consecutive(board, row, col, "horizontal", piece)
        
    for i in range(6):
        if(board[i][col] == piece):
            count += 1
    
    if(count >= 4):
        return is_consecutive(board, row, col, "vertical", piece)
        
    rowt = row
    colt = col
    count = 0
    
    while(rowt != len(board) - 1 and colt != len(board[0]) - 1):
        rowt += 1
        colt += 1
    
    while(colt != 0 and rowt != 0):
        if(board[rowt][colt] == piece):
            count += 1
        rowt -= 1
        colt -= 1
    
    if(count >= 4):
        return is_consecutive(board, rowt, colt, "diagonalneg", piece)
        
    rowt = row
    colt = col
    count = 0
    
    while(rowt != len(board) - 1 and col != 0):
        rowt += 1
        colt -= 1
    
    while(colt != len(board[0]) - 1 and rowt != 0):
        if(board[rowt][colt] == piece):
            count += 1
        rowt -= 1
        colt += 1
    
    if(count >= 4):
        return is_consecutive(board, rowt, colt, "diagonalpos", piece)
            

        
    
        
        
def placement(player, col, board):
    if player:
        piece = "X"
    else:
        piece = "O"
    row = -1
    while row == -1:
        row = row_num(col,board)
        
##    if row == -1:
## Where we put error        print(invalid)
    board[row][col] = piece
    
    return check_win(board, row, col, piece)
    
    
def our_turn(player, move, board):
    result = placement(player, move, board)
    print(move + 1)
    return result

def their_turn(player, board):
    print("?")
    theirmove = int(input("Input Col num => ")) - 1
    result = placement(player, theirmove, board)
    return (runseach(), result)

def runseach():
    row = random.randint(0,6)
    return 1

if __name__ == "__main__":
    ## intrum stuff
    board = clear_board()
    first = True
    string= ""
    print('p')
    start = int(input("Player Start => "))
    
    if start == 1:
        first = True
    else:
        first = False
    move = 3
    win = False
    while string != "stop":
        if first:
            win = our_turn(first, move, board)
        else:
          move, win = their_turn(first, board)
        first = not first
        for a in range(len(board)):
            outstring = ""
            for b in range(len(board[0])):
                outstring+= board[a][b] + " "
            print(outstring)
        if(win == True):
            print("WIN!")
            break
            