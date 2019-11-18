# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:20:42 2019

@author: sullia4
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
    
    
    
    
    
    
    
    
def our_turn(move, board):
    placement(True, move, board)
    print(move + 1)

def their_turn(board):
    print("?")
    theirmove = int(input("Input Col num => ")) - 1
    placement(False, theirmove, board)
    return runseach()

def runseach():
    row = random.randint(0,6)
    return row

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
    while string != "stop":
        if first:
            our_turn(move, board)
        else:
          move = their_turn(board)
        first = not first
        for a in range(len(board)):
            outstring = ""
            for b in range(len(board[0])):
                outstring+= board[a][b] + " "
            print(outstring)
            