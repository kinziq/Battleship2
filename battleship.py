#Name: Kinz
#Date: 06/09/23
#Purpose: Battleship...
#Plan: Game will be in a 5x5 grid. AI will place their ship randomly in that grid with 2 square length ships 5 times.
#There will be a minimum of 10 incorrect guesses.
#There will be four array's, one for the player's moves, another for the AI's placement and the last is for counting guesses


begin = (input("Welcome to Battleship. Please type in 'y' when you are ready to start: "))
rulesmessage =("This game will be seperated into a 5x5 grid. The AI will random place their own ships as this will be a one way. You will get 10 incorrect tries after which the game will end.") 
if rulesmessage("y"):
    print(f"{rulesmessage}")
else:
    print(f"{rulesmessage}")