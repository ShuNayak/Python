# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:34:18 2020

@author: shubh

"""

import random
from IPython.display import clear_output

def display(board):
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("_"+"|"+"_"+"|"+"_")
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("_"+"|"+"_"+"|"+"_")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("_"+"|"+"_"+"|"+"_")


def enterInputs():
    marker =''
    while(marker != 'X' and marker != 'O'):
        marker = input("player 1 enter your value as X or O: ")
    player1 = marker
    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)


def placeMarker(board, marker, position):
    board[position]=marker
    
def winGame(board, mark):
    #win tic tac toe yet?
    #check all rows:
    if (board[4]==board[5]==board[6]==mark) or (board[1]==board[2]==board[3]==mark) or (board[7]==board[8]==board[9]==mark):
        return True
    
    if (board[4]==board[1]==board[7]==mark) or (board[5]==board[2]==board[8]==mark) or (board[6]==board[3]==board[9]==mark):
        return True
    
    if ((board[4]==board[2]==board[9]==mark) or (board[7]==board[2]==board[6]==mark)):
        return True

def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'player_1'
    else:
        return 'player_2'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board, position):
        position = (int)(input("enter the correct position from 1 to 9"))
    return position

def replay():
    choice = input("play game again? Y or N")
    return choice


# we need a while loop to keep running the game
#break out of while loop with replay function
print("Welcome to Tic Tac Toe") 
while True:
    board = [' ']*10
    oneMarker, twoMarker = enterInputs()
    turn = choose_first()
    
    print(turn+"will go first")
    play_game = input("Want to play? Y or N : ")
    
    if play_game=='Y':
        gameOn= True
    else:
        gameOn=False
    
    while gameOn:
        if turn == 'player_1':
            
            #player 1 turn
            display(board)
            pos = player_choice(board)
            placeMarker(board,oneMarker,pos)
            
            if winGame(board,oneMarker):
               display(board)
               print ("Player 1 won")
               gameOn = False
            else:
                if full_board_check(board):
                    display(board)
                    print("TIE")
                    gameOn = False
                else:
                    turn = 'player_2'
              
             
             
            
            
            
        else:
            #player 2 turn
            
            display(board)
            pos = player_choice(board)
            placeMarker(board,twoMarker,pos)
            
            if winGame(board,twoMarker):
               display(board)
               print ("Player 2 won")
               gameOn = False
            else:
                if full_board_check(board):
                    display(board)
                    print("TIE")
                    gameOn = False
                else:
                    turn = 'player_1'
            
    
    
    if not replay():
        break
    
    
    
        
        
    



                                                                       


    

    

