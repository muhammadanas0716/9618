from random import randint

randomArray = [[0] * 10 for i in range(10)]

def OutputArray():
    global randomArray

    for row in randomArray:
        rowOut = ""
        for i in range(10):
            rowOut = rowOut + f"{row[i]} "
        
        print(rowOut)

for i in range(10):
    for j in range(10):
        randomInt = randint(1, 100)
        randomArray[i][j] = randomInt

OutputArray()
print("\n\n########################################################")
print("########################################################")
print("########################################################\n\n")


arrayLength = 10
for X in range(len(randomArray) - 1):
    for Y in range(len(randomArray) - 2):
        for Z in range(len(randomArray) - Y - 2):
            if randomArray[X][Z] > randomArray[X][Z + 1]:
                TempValue = randomArray[X][Z]
                randomArray[X][Z] =  randomArray[X][Z+1]
                randomArray[X][Z + 1] = TempValue


OutputArray()

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1,SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
            
    return -1
            

# 21 / 23
    