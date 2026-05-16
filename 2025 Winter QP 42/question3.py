TreeArray = []

for x in range(50):
    TreeArray.append([-1,-1,-1])

RootPointer = -1
FreeNode = 0

def AddNode(value):
    pass

try:
    File= open("TreeData.txt")
    for Line in File:
        AddNode(int(Line.strip()))
    File.close()
except:
    print("Error cannot open file")


def WriteAllToFile():
    try:
        File = open("Tree.txt", "w")

        for x in range(50):
            File.write(f"{TreeArray[x][0]},{TreeArray[x][1]},{TreeArray[x][2]}\n")

        File.close()

    except IOError:
        print("Cannot write to file")


# 12 / 21