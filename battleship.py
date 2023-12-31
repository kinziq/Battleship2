#Name: Kinz
#Date: 06/09/23
#Purpose: Battleship
#Plan: Game will be in a 5x5 grid. AI will place their ship randomly in that grid with 2 square length ships 5 times.
#There will be a minimum of 10 incorrect guesses.
import os
import random

os.system("cls")

board=["o"]*25
answers=["xooooxoxoxooxoxxxooo"]
guessed_spots = []

(input("Welcome to Battleship. Please type in any character on your keyboard when you are ready to start: "))

print("This game will be seperated into a 5x5 grid. The AI will random place their own ships as this will be a one way. You will get 10 incorrect tries after which the game will end. The board will now generate soon.")


#board
def boardlayout():
  print("  A B C D E")
  print( f'1 {board[0]} {board[1]} {board[2]} {board[3]} {board[4]}')
  print( f'2 {board[5]} {board[6]} {board[7]} {board[8]} {board[9]}')
  print( f'3 {board[10]} {board[11]} {board[12]} {board[13]} {board[14]}')
  print( f'4 {board[15]} {board[16]} {board[17]} {board[18]} {board[19]}')
  print( f'5 {board[20]} {board[21]} {board[22]} {board[23]} {board[24]}')

boardlayout()
turns = 0
leftturns = 10
shipguess = dict({"A":0, "B":1, "C":2, "D":3, "E":4}) 


run = True
while run:
  guess = str.upper(input("Please input your guess (A2, B2, D3 etc): "))
  os.system("cls")
  if len(guess) != 2:
        print("Invalid Guess! Please enter a valid guess!\n")
  if len(guess) == 2:
    
    #Will add a turn counter if the length of the characters are equal to two to the variable turns. This will also include how many left turns there are.
    
    letter = guess[0]
    row = int(guess[1])
    spot = shipguess[letter] + (row-1)*5
    
     # Check if the spot has already been guessed
    if spot in guessed_spots:
            print("You already guessed this spot. Try again.")
            continue  # Skip the rest of the loop and ask for input again
        
        # Add the guessed spot to the set
    guessed_spots.append(spot)
    
    board[spot] = ('x')
  boardlayout()

  check_ships = [0, 5, 7, 9, 12, 14, 15, 16, 18, 23]
  
  for hit in check_ships:
    if board[hit] == ("x"):
      os.system("cls")
      print(f"Nice! You hit a ship at spot {(hit)+1}.\n")
      boardlayout()
      print(f"You have guessed wrong {turns} times. You have {leftturns} incorrect guesses left.")      

  check_bad_ships = [1, 2, 3, 4, 6, 8, 10, 11, 13, 17, 18, 19, 20, 21, 22, 24]
  
  for bad_hits in check_bad_ships:
    if board[bad_hits] == ("x"):
        os.system("cls")
        print("Good try!\n")
        boardlayout()
        turns+=1
        leftturns-=1
        print(f"You have guessed the ships wrong {turns} times. You have {leftturns} turns left.")
  
  if turns == 10:
    run = False
    print("Game Over.")
    
