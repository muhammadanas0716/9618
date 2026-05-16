class NewRecord:
    def __init__(self, KeyP, Item1P, Item2P):
        self.__Key = KeyP
        self.__Item1 = Item1P
        self.__Item2 = Item2P

    def GetKey(self):
        return self.__Key

    def GetItem1(self):
        return self.__Item1

    def GetItem2(self):
        return self.__Item2


global HashTable, Spare

def Initialise():
    global HashTable, Spare

    EmptyRecord = NewRecord(-1, -1, -1)

    HashTable = []
    Spare = []

    for _ in range(200):
        HashTable.append(EmptyRecord)

    for _ in range(100):
        Spare.append(EmptyRecord)


def CalculateHash(Key):
    return Key % 200


def InsertIntoHash(TheRecord):
    global HashTable, Spare

    HashValue = CalculateHash(TheRecord.GetKey())

    if HashTable[HashValue].GetKey() == -1:
        HashTable[HashValue] = TheRecord
    else:
        for x in range(100):
            if Spare[x].GetKey() == -1:
                Spare[x] = TheRecord
                break


def CreateHashTable():
    try:
        File = open("HashData.txt", "r")

        for Line in File:
            Line = Line.strip()
            Data = Line.split(",")

            TempRecord = NewRecord(
                int(Data[0]),
                int(Data[1]),
                int(Data[2])
            )

            InsertIntoHash(TempRecord)

        File.close()

    except IOError:
        print("File not found")


Initialise()
CreateHashTable()

# 18 / 22