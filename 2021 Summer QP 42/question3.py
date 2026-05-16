class TreasureChest:
    def __init__(self, QuestionP: str, AnswerP: int, PointsP: int):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Points = PointsP

    def getQuestion(self):
        return self.__Question
    
    def checkAnswer(self, UserAnswer):
        if UserAnswer ==  self.__Answer:
            return True
        else:
            return False
        

    def getPoints(self, NoOfAttempts):
        if NoOfAttempts == 1:
            return self.__Points
        elif NoOfAttempts == 2:
            return self.__Points // 2
        elif NoOfAttempts == 3 or NoOfAttempts == 4:
            return self.__Points // 4
        else:
            return 0
        
        


# DECLARE arrayTreasure [0:4] OF TreasureChest
arrayTreasure = []

def readData():
    try:
        ChestDataFile = open("TreasureChestData.txt", "r")

        for _ in range(5):
            question = ChestDataFile.readline().strip()
            answer = int(ChestDataFile.readline().strip())
            points = int(ChestDataFile.readline().strip())

            tempObj = TreasureChest(question, answer, points)
            arrayTreasure.append(tempObj)

        ChestDataFile.close()

    except FileNotFoundError:
        print("File not found")


readData()
quetionNo = int(input("Enter a question no. 1-5: "))
print(f"Question is: {arrayTreasure[quetionNo - 1].getQuestion()}")

solved = False
count = 0
while solved != True:
    answerUser = int(input("Enter your answer: "))
    output = arrayTreasure[quetionNo - 1].checkAnswer(answerUser)

    if output:
        solved = True
    
    count += 1

print(f"Your points: {arrayTreasure[quetionNo - 1].getPoints(count)}")


# 31 / 31