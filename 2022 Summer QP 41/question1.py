FileData = [["", 0] * 2 for i in range(11)] # string

def ReadHighScores():
    try:
        file = open(f"HighScore.txt", "r")
        
        for i in range(10):
            playerName = file.readline().strip()
            playerScore = int(file.readline().strip())

            FileData[i][0] = playerName
            FileData[i][1] = playerScore

        file.close()
    except FileNotFoundError:
        print("File not found.")

def OutputHighScores():
    counter = 0
    while FileData[counter][0] != "":
        print(f"{FileData[counter][0]} {FileData[counter][1]}")
        counter += 1

ReadHighScores()
OutputHighScores()


username = input("Enter your Username: ")
while len(username) != 3:
    username = input("Enter your Username: ")

score = int(input("Enter score: ")) 

while score < 1 or score > 100000:
    score = int(input("Enter score: ")) 

def addPlayer(username=username, score=score):
    if FileData[-1][0] != "":
        print(f"List is full")
    
    else:
        # Check if added value is smallest or not
        for item in FileData:
            if item[1] > score:
                continue


# 23 / 33