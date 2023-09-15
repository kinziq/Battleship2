#Name: Kinz
#Date: 06/09/23
#Purpose: Battleship
#Plan: Game will be in a 5x5 grid. AI will place their ship randomly in that grid with 2 square length ships 5 times.
#There will be a minimum of 10 incorrect guesses.
import os
import random
from time import sleep

os.system("cls")

board=["o"]*25
answers=["o"]*25
#if num ==1:
    


(input("Welcome to Battleship. Please type in any character on your keyboard when you are ready to start: "))

rulesmessage =("This game will be seperated into a 5x5 grid. The AI will random place their own ships as this will be a one way. You will get 10 incorrect tries after which the game will end. The board will now generate soon.")
print(f"{rulesmessage}")


#board
print("  A B C D E")
print( f'1 {board[0]} {board[1]} {board[2]} {board[3]} {board[4]}')
print( f'2 {board[5]} {board[6]} {board[7]} {board[8]} {board[9]}')
print( f'3 {board[10]} {board[11]} {board[12]} {board[13]} {board[14]}')
print( f'4 {board[15]} {board[16]} {board[17]} {board[18]} {board[19]}')
print( f'5 {board[20]} {board[21]} {board[22]} {board[23]} {board[24]}')


shipguess = dict({"A":0, "B":1, "C":2, "D":3, "E":4}) 
guess = input("Please input your guess (A2, B2, D3 etc): ")
if len(guess) == 2:
  letter = guess[0]
  row = int(guess[1])
spot = shipguess[letter] + (row-1)*5
if spot == 9:
    answers[9] == "x"
print(f'{answers[9]}')
