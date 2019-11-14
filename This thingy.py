# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:20:42 2019

@author: sullia4
"""

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
        
def placement(player, col, board):
    if player:
        piece = "X"
    else:
        piece = "O"
    row = row_num(col,board)
##    if row == -1:
## Where we put error        print(invalid)
    board[row][col] = piece
    
    
    
    
    
    
    
    
def our_turn(move, board):
    placement(True, move, board)
    print(move)

def their_turn(board):
    print("?")
    theirmove = int(input()) - 1
    placement(False, theirmove, board)
    return runseach()

def runseach():
    pass
    
if __name__ == "__main__":
    ## intrum stuff
    board = clear_board()
    first = True
    string= ""
    print('p')
    start = int(input())
    
    if start == 1:
        first = True
    else:
        first = False
        
    while string != "stop":
        if first:
            our_turn()
        else:
          move = their_turn()
        first = not first