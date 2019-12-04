"""
Created on Thu Nov 14 14:20:42 2019
@author: sullia4 and mcdanz
2 players no win con
"""
import random

def determine_piece(player):
    if player:
        return "X"
    else:
        return "O"
    
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
                    print(cmax)
            else:
                count = 0
                
    
    elif(direction == "vertical"):
        for i in range(6):
            if board[i][col] == piece:
                count += 1
                if cmax < count:
                    cmax = count
                    print(cmax)
            else:
                count = 0
                
    elif(direction == "diagonalneg"):
        while(row != len(board) and col != len(board[0])):
            if board[row][col] == piece:
                print("Board:", board[row][col], "player:", piece)
                count += 1
                if cmax < count:
                    cmax = count
                    print(cmax)
            else:
                count = 0
            row += 1
            col += 1
            
    elif(direction == "diagonalpos"):
        while row != len(board) and col != -1:
            if board[row][col] == piece:
                count += 1
                if cmax < count:
                    cmax = count
                    print(cmax)
            else:
                count = 0
            row += 1
            col -= 1
    
    if(cmax >= 4):
        print("row:", row, "col:", col)
        return True
    else:
        return False
        


def check_win(board, row, col, piece): 
    count1 = 0
    if(board[row].count(piece) >= 4):
        if is_consecutive(board, row, col, "horizontal", piece):
            return True
        
    for i in range(6):
        if(board[i][col] == piece):
            count1 += 1
    
    if(count1 >= 4):
        if is_consecutive(board, row, col, "vertical", piece):
            return True
        
    rowt = row
    colt = col
    count1 = 0
    
    while(rowt != len(board) - 1 and colt != len(board[0]) - 1):
        rowt += 1
        colt += 1
    
    while(colt != -1 and rowt != -1):
        if(board[rowt][colt] == piece):
            count1 += 1
        rowt -= 1
        colt -= 1
    
    if(count1 >= 4):
        if is_consecutive(board, rowt, colt, "diagonalneg", piece):
            return True
        
    rowt = row
    colt = col
    count1 = 0
    
    while(rowt != len(board) - 1 and col != -1):
        rowt += 1
        colt -= 1
    
    while(colt != len(board[0]) and rowt != -1):
        if(board[rowt][colt] == piece):
            count1 += 1
        rowt -= 1
        colt += 1
    
    rowt+= 1
    colt-=1
    
    if(count1 >= 4):
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
    board[row][col] = "."
    return win
    
def testoneup(player, col, board):
    if row_num(col, board) != 0:
        if player:
            piece = "X"
        else:
            piece = "O"
        row = -1
        while row == -1:
            row = row_num(col,board)
        board[row][col] = piece
        piece = determine_piece(not player)
        board[row - 1][col] = piece
        win = check_win(board, row -1, col, piece)
        board[row][col] = "."
        board[row - 1][col] = "."
        #return if our AI loses if we play the move
        return not win   
    return True     
        
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
    print("?")
    theirmove = int(input("Input Col num => ")) - 1
    result = placement(player, theirmove, board)
    return (runseach(board, not player), result)



def runseach(board, player):
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
    
    n = 0
    
    while n < 50:
        col = random.randint(0, 6)
        n += 1
        if row_num(col, board) == -1:
            continue
        elif testoneup(player, col, board):
            break
        
    if n >= 49:
        while True:
            col = random.randint(0, 6)
            if row_num != -1:
                break
    
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
        
    move = 3
    win = False
    
    while string != "stop":
        if first:
            win = our_turn(first, move, board)
            if win: 
                break      
        else:
          move, wins = their_turn(first, board)
          if wins:
              break
              
        first = not first
        for a in range(len(board)):
            outstring = ""
            for b in range(len(board[0])):
                outstring+= board[a][b] + " "
            print(outstring)
            
        if board[0].count(".") == 0:
            print("draw")
            break

    for a in range(len(board)):
        outstring = ""
        for b in range(len(board[0])):
            outstring+= board[a][b] + " "
        print(outstring)
    print("WIN!")
