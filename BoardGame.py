# Homework 3 - Board Game System
# Name:Jenna Kramer
# Date:04/01/26

import random

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data

def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)

def updateTurn(data):
    #change player turn 
    playerTurn = data[0].split(": ")
    if "Player1" in playerTurn:
        playerTurn[1] = "Player2"
    else:
        playerTurn[1] = "Player1"
    result = ": ".join(playerTurn)
    data[0] = result

    return data 

def movePlayer(data):
    playerTurn = data[0].split()
    for x in range(1, len(data)):
        item = data[x]
        if playerTurn[1] in item:
            # Get current position of player
            splitItem = item.split(": ")
            position = int(splitItem[0])

            #Incrementing Current Position
            roll = random.randint(1,7)
            position += roll

            #Storing new position in data
            splitItem[0] = str(position)
            result = ": ".join(splitItem)
            data[x] = result

    return data

def checkPosition(data):
    playerTurn = data[0].split()
    if "Player1" in playerTurn:
        currPlayer = data[1].split(": ")
        position = int(currPlayer[0])
        if position == 12:
            position += 2
            print(f'{currPlayer[1]} has drank caffeine and moved two spaces ahead!')
        elif position == 8:
            position += 5
            print(f'{currPlayer[1]} has hopped on a lime scooter and moved five spaces ahead!')
        elif position == 5:
            position -= 1
            print(f'{currPlayer[1]} has gotten stuck behind a slower walker and moved one space behind.')
        elif position == 17:
            position -= 6
            print(f'{currPlayer[1]} has missed their shuttle and moved six spaces behind.')
        
        #Place the new position inside data
        currPlayer[0] = str(position)
        result = ": ".join(currPlayer)
        data[1] = result
        
    else:
        currPlayer = data[2].split(": ")
        position = int(currPlayer[0])
        if position == 12:
            position += 2
            print(f'{currPlayer[1]} has drank caffeine and moved two spaces ahead!')
        elif position == 8:
            position += 5
            print(f'{currPlayer[1]} has hopped on a lime scooter and moved five spaces ahead!')
        elif position == 5:
            position -= 1
            print(f'{currPlayer[1]} has gotten stuck behind a slower walker and moved one space behind.')
        elif position == 17:
            position -= 6
            print(f'{currPlayer[1]} has missed their shuttle and moved six spaces behind.')
            
        #Place the new position inside data
        currPlayer[0] = str(position)
        result = ": ".join(currPlayer)
        data[2] = result
        
    return data

def checkWin(data):
    playerTurn = data[0].split()
    if "Player1" in playerTurn:
        currPlayer = data[1].split(": ")
        position = int(currPlayer[0])
        if position >= 30:
            return 0, currPlayer[1]
    else:
        currPlayer = data[2].split(": ")
        position = int(currPlayer[0])
        if position >= 30:
            return 0, currPlayer[1]
    return 1, "N/A" 

def main():
    filename = "events.txt"   # Students can rename if needed

    finished = 1
    winner = ''

    gameData = loadGameData(filename)
    displayGame(gameData)
    print()
    while finished: 
        print(f'{gameData[0].split(": ")[1]}\'s Turn')
        choice = input("\nMove player? (y/n): ")
        if choice.lower() == "y":
            #move current player
            gameData = movePlayer(gameData)
            
            #Check Current Player's Position
            gameData = checkPosition(gameData)
            
            #check for a win
            finished, winner = checkWin(gameData)

            #Display New Game Data
            displayGame(gameData)
            
            # Move to next player's turn
            gameData = updateTurn(gameData)

    print(f'{winner} has won the game!! Congratulations!')

if __name__ == "__main__":
    main()
