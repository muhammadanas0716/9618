class Record:
    def __init__(self, Key, Data):
        self.Key = Key # INTEGER
        self.Data = Data # STRING


# DECLARE Hashtable: ARRAY[0:9, 0:99] OF Record
global Hashtable
def InitialiseHashTable():
    global Hashtable

    Hashtable = [[Record(-1, "") for i in range(10)] for i in range(100)]

def Hash(keyField):
    hash = keyField % 100
    return hash

def InsertData(recordObj):
    hash = Hash(recordObj.Key)
    for i in range(10):
        if Hashtable[hash][i].Key == -1:
            ix = i
        else:
            continue
    
    Hashtable[hash][ix] = recordObj


def ReadData():
    try:
        MyFile = open("HashTableData.txt", "r")
        for line in MyFile:
            pair = line.strip().split(",")
            tempObj = Record(int(pair[0]), pair[1])
            InsertData(tempObj)
        MyFile.close()

    except IOError:
        print("Could not move on.")

def GetRecord(KeyField):
    hashValue = Hash(KeyField)
    for i in range(10):
        if Hashtable[hashValue][i].Key == KeyField:
            key = Hashtable[hashValue][i].Key
            data = Hashtable[hashValue][i].Data
            return f"Key: {key} | Data: {data}"
        else:
            continue
    
    return "Not found."

InitialiseHashTable()
ReadData()
for i in range(5):
    keyfield = int(input("Enter key field plz: "))
    result = GetRecord(keyfield)
    print(result)



# 21/23