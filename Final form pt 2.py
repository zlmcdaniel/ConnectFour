# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:20:42 2019
@author: sullia4 and mcdanz
2 players no win con
"""
import random

## determines what piece the player should be (player true/false)
def determine_piece(player):
    if player:
        return "X"
    else:
        return "O"

##generate new board    
def clear_board():
    board= []
    for a in range(6):
        board.append(["."] * 7)
    return board

## return next valid position for piece, returns -1 if out of bounds
def row_num(col, board):
    n = int(len(board) - 1)
    while True:
        if board[n][col] == ".":
            return n
        n-= 1
        if n < 0:
            return -1
 
##given a direction to check counts if 4 pieces are consecutive for win             
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
        

## initial count to see if consecutive needs to be checked
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
            
## check to see if placement yields a win
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

## test to see if placement would give a win to opponent    
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


def checkTwoInRow(board, theirmove, other, player):
    count = 0
    row = row_num(theirmove, board) + 1
    if player:
        piece = "X"
    else:
        piece = "O"

        for i in range(1, 5):
            if(row_num(i, board) == row_num(theirmove, board) + 1):
                board[row_num(i, board)][i] = piece
                count = 0
                cmax = 0
                for i in range(len(board[0])):
                    if(board[row][i] == piece):
                        count += 1
                        if cmax < count:
                            cmax = count
                    else:
                        count = 0    
                        
                if(cmax == 3):
                    for j in range(7):
                        if(row_num(j, board) == row_num(theirmove, board)) + 1:
                            board[row_num(j, board)][j] = piece
                            
                            count = 0
                            cmax = 0
                            for i in range(len(board[0])):
                                if(board[row][i] == piece):
                                    count += 1
                                    if cmax < count:
                                        cmax = count
                                else:
                                    count = 0 
                            board[row_num(j, board)][j] = "."
                            if(cmax >= 4):
                                board[row_num(i, board)][i] = "."
                                return i
                            
                board[row_num(i, board)][i] = "."
                            
    return -1
            
                            
                        
                    
                
                
        
        
    
    #board[row][col] = piece
    #win = check_win(board, row, col, piece)   
    #board[row][col] = "."



## places piece returns if game winning move        
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
    
    
## when its our turn place piece on our board and print move, return if we won
def our_turn(player, move, board):
    result = placement(player, move, board)
    print(move + 1)
    return result


## on their turn wait for input and place their move on our board, return next position to place piece 
def their_turn(player, board):
    theirmove = int(input("Input Col num => ")) - 1
    result = placement(player, theirmove, board)
    return (runseach(board, not player, theirmove), result)


## run through all possible plays and see if there is an immediate win. If so return that placement. 
##If there was no win but a loss, return loose position. If there is neither a win or lose position 
##find a position on the board that is valid and doesn’t result in a loss next turn. If no such position 
##can be found in 50 trials chose a random valid position. 
def runseach(board, player, theirmove):
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
    
    rowLast = row_num(theirmove, board)
    
    if board[rowLast].count(".") >= 5 and theirmove != 6 and theirmove != 0:
        result = checkTwoInRow(board, theirmove, theirmove + 1, player)
        if result != -1:
            return result
        
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
    ## Generate board set varibles and give moderator data
    board = clear_board()
    first = True
    string= ""
    print('p')
    
    ## Wait for player start
    start = int(input("Player Start => "))
    
    ##Set player start if second return "?"
    if start == 1:
        first = True
    else:
        first = False
        print("?")
    
    ##Set starting move    
    move = 3
    
    win = False
    
    while string != "stop":
        ##on our turn
        if first:
            win = our_turn(first, move, board)
            ##if win stop program
            if win: 
                break      
        ##On their turn
        else:
          move, wins = their_turn(first, board)
          ##if win stop program
          if wins:
              break
        ##Switch player turn      
        first = not first
        for a in range(len(board)):
            outstring = ""
            for b in range(len(board[0])):
                outstring+= board[a][b] + " "
            print(outstring)
        ##check draw    
        if board[0].count(".") == 0:
            print("draw")
            break

    for a in range(len(board)):
        outstring = ""
        for b in range(len(board[0])):
            outstring+= board[a][b] + " "
        print(outstring)
    print("WIN!")