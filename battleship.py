#Name: Kinz
#Date: 06/09/23
#Purpose: Battleship
#Plan: Game will be in a 5x5 grid. AI will place their ship randomly in that grid with 2 square length ships 5 times.
#There will be a minimum of 10 incorrect guesses.
#There will be four array's, one for the player's moves, another for the AI's placement and the last is for counting guesses
import random
from time import sleep

(input("Welcome to Battleship. Please type in any character on your keyboard when you are ready to start: "))

rulesmessage =("This game will be seperated into a 5x5 grid. The AI will random place their own ships as this will be a one way. You will get 10 incorrect tries after which the game will end. The board will now generate soon.")
print(f"{rulesmessage}")
sleep(4)

grid  = [" | 1 | 2 | 3 | 4 | 5 |"]
gridA = ["A| x | x | x | x | x |"]
gridB = ["B| x | x | x | x | x |"]
gridC = ["C| x | x | x | x | x |"]
gridD = ["D| x | x | x | x | x |"]
gridE = ["E| x | x | x | x | x |"]
print(f"{grid}")
print(f"{gridA}")
print(f"{gridB}")
print(f"{gridC}")
print(f"{gridD}")
print(f"{gridE}")