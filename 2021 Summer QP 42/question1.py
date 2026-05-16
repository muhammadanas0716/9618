class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


# DECLARE linkedList[0:9] OF node
linkedList = []

linkedList.append(Node(1, 1))
linkedList.append(Node(5, 4))
linkedList.append(Node(6, 7))
linkedList.append(Node(7, -1))
linkedList.append(Node(2, 2))
linkedList.append(Node(0, 6))
linkedList.append(Node(0, 8))
linkedList.append(Node(56, 3))
linkedList.append(Node(0, 9))
linkedList.append(Node(0, -1))

# DECLARE pointers
startPointer = 0 # INTEGER
emptyList = 5 # INTEGER


def outputNodes(array):
    currentPointer = startPointer
    while currentPointer != -1:
        print(array[currentPointer].data)
        currentPointer = array[currentPointer].nextNode


def addNode(array, startPointer=0, emptyList=5):
    value = int(input("Enter the number you want to add: "))

    if emptyList == -1:
        return False

    currentPointer = startPointer
    linkedList[emptyList].data = value
    emptyList = linkedList[emptyList].nextNode
    



outputNodes(linkedList)
addingNode = addNode(linkedList, startPointer, emptyList)
if addingNode == True:
    print("Data was added.")
else:
    print("Data was not added")
outputNodes(linkedList)

