def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:
        return 0
    
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements-1, DataToFind)
    else:
        return RecursiveCount(ArrayCopy[1:], NumberElements-1, DataToFind)
    
ArrayCopy = [0,5,1,2,5,9,9,6,5,0]
countResult = RecursiveCount(ArrayCopy, 10, 0)
print(countResult)
print("\n\n###########\n\n")

fancyString = "x=0;y=1;x=x+y;y++;"

def SplitData():
    codesArray = []
    line = ""
    for letter in fancyString:
        if letter != ";":
            line += letter
        else:
            codesArray.append(line)
            line = ""
        
    return codesArray

arrayOutputCodes = SplitData()
for line in arrayOutputCodes:
    print(line)


# 18/19