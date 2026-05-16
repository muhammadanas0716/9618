class node:
    #PUBLIC Data : INTEGER
    #PUBLIC nextNode : INTEGER

    def __init__(self, DataP, nextP):
        self.Data = DataP
        self.nextNode = nextP
    

linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), 
              node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
currentPointer = startPointer
previousPointer = 0
emptyListPointer = 5

def deleteNode(item):
    # Find the node and the previous node
    global startPointer, currentPointer, previousPointer, emptyListPointer

    while currentPointer != -1 and linkedList[currentPointer].Data != item:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode

    if currentPointer == -1:
        print("No item as such was found in the linked list.")
        return False
    
    if startPointer == currentPointer:
        startPointer = linkedList[startPointer].nextNode
    else:
        linkedList[previousPointer].nextNode = linkedList[currentPointer].nextNode

    # Back to free list
    linkedList[currentPointer].Data = 0
    linkedList[currentPointer].nextNode = emptyListPointer # Point the removed node from the linked list to the freelist pointer (first node atm there)

    emptyListPointer = currentPointer # change the emptylist start pointer to this current pointer which alr is pointing towards the next free node which prev was first node of the free list
    return True