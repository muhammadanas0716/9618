class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.nextnode = pointer


linkedList = [
    Node(1, 1),
    Node(5, 4),
    Node(6, 7),
    Node(7, -1),  # last node of actual linked list
    Node(2, 2),
    Node(0, 6),  # FREE
    Node(0, 8),  # FREE
    Node(56, 3),
    Node(0, 9),  # FREE
    Node(0, -1),  # FREE (last node of free list)
]

startPointer = 0
freeListPointer = 5


def addNode():
    global startPointer
    global freeListPointer

    dataInput = int(input("Enter your number: "))

    # Step 1: check if free list is empty
    if freeListPointer == -1:
        print("Linked list is full. Sorry.")
        return False

    # Step 2: take first free node
    newNodePointer = freeListPointer

    # Step 3: move freeListPointer to next free node
    freeListPointer = linkedList[newNodePointer].nextnode

    # Step 4: store data in new node
    linkedList[newNodePointer].data = dataInput
    linkedList[newNodePointer].nextnode = -1

    # Step 5: if actual linked list is empty
    if startPointer == -1:
        startPointer = newNodePointer
        return True

    # Step 6: traverse actual linked list to find last node
    currentPointer = startPointer
    while linkedList[currentPointer].nextnode != -1:
        currentPointer = linkedList[currentPointer].nextnode

    # Step 7: connect last node to new node
    linkedList[currentPointer].nextnode = newNodePointer

    return True
