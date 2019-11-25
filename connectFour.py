"""
Created on Thu Nov 14 14:20:42 2019
@author: sullia4 and mcdanz
2 players no win con
"""
import random

def clear_board():
    board= []
    for a in range(6):
        board.append(["."] * 7)
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
    cmax = 0
    if(direction == "horizontal"):
        for i in range(len(board[0])):
            if(board[row][i] == piece):
                count += 1
                if cmax < count:
                    cmax = count
            else:
                count = 0
                
    
    elif(direction == "vertical"):
        for i in range(6):
            if(board[i][col] == piece):
                count += 1
                if cmax < count:
                    cmax = count
            else:
                count = 0
                
    elif(direction == "diagonalneg"):
        while(row != len(board) and col != len(board[0])):
            if(board[row][col] == piece):
                count += 1
                if cmax < count:
                    cmax = count
            else:
                count = 0
            row += 1
            col += 1
            print(cmax, " ", count)
            
    elif(direction == "diagonalpos"):
        print("Row, col", row, col)
        while row != len(board) and col != -1:
            if(board[row][col] == piece):
                count += 1
                if cmax < count:
                    cmax = count
            else:
                count = 0
            row += 1
            col -= 1

    if(cmax >= 4):
        return True
    else:
        return False
        


def check_win(board, row, col, piece): 
    count = 0
    print("This is the peice used",piece)
    if(board[row].count(piece) >= 4):
        if is_consecutive(board, row, col, "horizontal", piece):
            return True
        
    for i in range(6):
        if(board[i][col] == piece):
            count += 1
    
    if(count >= 4):
        if is_consecutive(board, row, col, "vertical", piece):
            return True
        
    rowt = row
    colt = col
    count = 0
    
    while(rowt != len(board) - 1 and colt != len(board[0]) - 1):
        rowt += 1
        colt += 1
    
    while(colt != -1 and rowt != -1):
        if(board[rowt][colt] == piece):
            count += 1
        rowt -= 1
        colt -= 1
    
    if(count >= 4):
        print("Diagneg was cheked")
        if is_consecutive(board, rowt, colt, "diagonalneg", piece):
            return True
        
    rowt = row
    colt = col
    count = 0
    
    while(rowt != len(board) - 1 and col != -1):
        rowt += 1
        colt -= 1
    print("This is row t",rowt, colt)
    
    while(colt != len(board[0]) and rowt != -1):
        if(board[rowt][colt] == piece):
            count += 1
        rowt -= 1
        colt += 1
    
    rowt+= 1
    colt-=1
    
    if(count >= 4):
        print("Diag pos was checked")
        if is_consecutive(board, rowt, colt, "diagonalpos", piece):
            return True
    return False
            

def testPlacement(player, col, board):
    if player:
        piece = "X"
    else:
        piece = "O"
    row = -1
    while row == -1:
        row = row_num(col,board)
    board[row][col] = piece
     
    win = check_win(board, row, col, piece)     
    #if(not win):
    board[row][col] = "."
    print("Is win: ", piece , win)
    return win
    
        
        
def placement(player, col, board):
    if player:
        piece = "X"
    else:
        piece = "O"
    row = -1
    while row == -1:
        row = row_num(col,board)
    board[row][col] = piece
    
    return check_win(board, row, col, piece)
    
    

def our_turn(player, move, board):
    result = placement(player, move, board)
    print(move + 1)
    return result



def their_turn(player, board):
    if(player):
        piece = "X"
    else:
        piece = "O"
        
    print("?")
    theirmove = int(input("Input Col num => ")) - 1
    result = placement(player, theirmove, board)
    return (runseach(board, not player), result)



def runseach(board, player):
    #row = random.randint(0,6)
    #row = int(input("X player row => ")) - 1
    losPos = -1  
    for i in range(7):
        row = -1
        row = row_num(i, board)
        if(row == -1):
            continue
        
        win = testPlacement(player, i, board)
        lose = testPlacement(not player, i, board)
        
        if(win):
            return i
        elif(lose):
            losPos = i
    
    if(losPos != -1):
        return losPos
    
    col = random.randint(0, 6)
    return col



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
        
    move = 6
    win = False
    
    while string != "stop":
        if first:
            win = our_turn(first, move, board)
            if win:
                print(first)  
                break      
        else:
          move, wins = their_turn(first, board)
          if wins:
              print(first)
              break
              
        first = not first
        for a in range(len(board)):
            outstring = ""
            for b in range(len(board[0])):
                outstring+= board[a][b] + " "
            print(outstring)
    
    for a in range(len(board)):
        outstring = ""
        for b in range(len(board[0])):
            outstring+= board[a][b] + " "
        print(outstring)
    print("WIN!")