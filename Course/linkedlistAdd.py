class node:
    #PUBLIC Data : INTEGER
    #PUBLIC nextNode : INTEGER

    def __init__(self, DataP, nextP):
        self.Data = DataP
        self.nextNode = nextP
    

linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), 
              node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
emptyListPointer = 5


def addNode(value: int):
    global emptyListPointer, startPointer

    if emptyListPointer == -1:
        return False

    freeNode = emptyListPointer
    emptyListPointer = linkedList[freeNode].nextNode

    linkedList[freeNode].Data = value
    linkedList[freeNode].nextNode = -1

    # OPTIONAL: ASSUMING LL CAN BE EMPTY
    if startPointer == -1:
        startPointer = freeNode
        return True

    currentPointer = startPointer
    while linkedList[currentPointer].nextNode != -1:
        currentPointer = linkedList[currentPointer].nextNode

    linkedList[currentPointer].nextNode = freeNode
    return True


