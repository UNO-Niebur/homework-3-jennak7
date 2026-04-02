# Homework 3 - Board Game System
# Name:Jenna Kramer
# Date:04/01/26

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


def movePlayer(data):
    """Example function to simulate moving a player."""
    # print("\nMove player function not fully implemented.")
    # Students will modify this
    # print(data)
    playerTurn = data[0].split()
    for x in range(1, len(data)):
        item = data[x]
        if playerTurn[1] in item:
            splitItem = item.split(": ")
            position = int(splitItem[0])
            position += 1 
            splitItem[0] = str(position)
            result = ": ".join(splitItem)
            data[x] = result

    for line in data:
        print(line)

def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        movePlayer(gameData)


if __name__ == "__main__":
    main()
