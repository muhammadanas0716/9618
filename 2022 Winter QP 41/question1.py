DataArray = [0 for i in range(100)]


def ReadFile():
    try:
        fileToBeRead = open("IntegerData.txt", "r")
        for line in range(100):
            DataArray[line] = int(fileToBeRead.readline().strip())

        fileToBeRead.close()
    
    except FileNotFoundError:
        print("File not found.")


def FindValues():
    value = int(input("Enter the number you want to search for: "))
    while value < 1 or value > 100:
        value = int(input("Enter the number you want to search for: "))
    
    counter = 0
    for number in DataArray:
        if value == number:
            counter += 1
        
    return counter


ReadFile()
print(f"The number of times the number requested is: {FindValues()}")

def BubbleSort():
    lenOfArray = len(DataArray)

    for i in range(lenOfArray - 1):
        for j in range(lenOfArray - 1 - i):
            if DataArray[j] > DataArray[j + 1]:
                DataArray[j], DataArray[j+1] = DataArray[j+1], DataArray[j]

BubbleSort()
print(DataArray)


# 23 / 23