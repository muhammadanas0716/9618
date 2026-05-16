HighScores = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

def ReadData():
    try:
        HighScoresFile = open("HighScoreTable.txt", "r")

        for i in range(7):
            playerID = HighScoresFile.readline().strip()
            gameLevel = HighScoresFile.readline().strip()
            score = HighScoresFile.readline().strip()

            HighScores[i][0] = playerID
            HighScores[i][1] = gameLevel
            HighScores[i][2] = score

        HighScoresFile.close()

        return HighScores
    except FileNotFoundError:
        print("File not found.")

ReadData()

def OutputHighScores(array: list):
    for player in array:
        print(f"{player[0]} reached level {player[1]} with a score of {player[2]}")

# OutputHighScores(HighScores)

def SortScores():
    # Sort by Game level
    n = len(HighScores)

    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if HighScores[j+1][1] > HighScores[j][1]:
                HighScores[j+1], HighScores[j] = HighScores[j], HighScores[j+1]
                swapped = True
            
        if not swapped:
            break
    
    return HighScores


print(SortScores())