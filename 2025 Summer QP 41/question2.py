def ReadData(fileName):
    array = []
    try:
        fileReading = open(fileName, "r")
        while True:
            line = fileReading.readline().strip()
            if line != "":
                array.append(line)
            else:
                break

        fileReading.close()
    except IOError:
        print(f"File {fileName} not found")

    return array

def SplitData(DataArray):
    RedArray = []
    GreenArray = []
    BlueArray = []
    OrangeArray = []
    YellowArray = []
    PinkArray = []

    for string in DataArray:
        temp = string.split(",")
        if temp[1] == "red":
            RedArray.append(int(temp[0]))
        elif temp[1] == "green":
            GreenArray.append(int(temp[0]))
        elif temp[1] == "blue":
            BlueArray.append(int(temp[0]))
        elif temp[1] == "orange":
            OrangeArray.append(int(temp[0]))
        elif temp[1] == "yellow":
            YellowArray.append(int(temp[0]))
        elif temp[1] == "pink":
            PinkArray.append(int(temp[0]))

    StoreData(RedArray, "Red.txt")
    StoreData(GreenArray, "Green.txt")
    StoreData(BlueArray, "Blue.txt")
    StoreData(OrangeArray, "Orange.txt")
    StoreData(YellowArray, "Yellow.txt")
    StoreData(PinkArray, "Pink.txt")


def StoreData(DataToStore, fileName):
    try:
        FileToBeRead = open(fileName, "w")
        for item in DataToStore:
            FileToBeRead.write(f"{str(item)}\n")
        
        FileToBeRead.close()
    
    except IOError:
        print("File cannot be loaded")



array = ReadData("TheData.txt")
SplitData(array)

# 25 / 25