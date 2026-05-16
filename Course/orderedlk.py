class node:
    # PUBLIC Data : INTEGER
    # PUBLIC nextNode : INTEGER

    def __init__(self, DataP, nextP):
        self.Data = DataP
        self.nextNode = nextP


# DECLARE linkedList : ARRAY[0:9] OF node
linkedList = [
    node(1, 1),
    node(5, 4),
    node(8, 7),
    node(70, -1),
    node(6, 2),
    node(0, 6),
    node(0, 8),
    node(56, 3),
    node(0, 9),
    node(0, -1),
]

startPointer = 0
emptyList = 5


def orderedinsertion(currentpointer):
    global linkedList
    global emptyList
    global startPointer

    datatoinsert = int(input("Enter the data to add: "))

    # STEP1 : Check if you have space in your linked list
    if emptyList < 0:
        return False
    else:
        # STEP2 : Make temp variable known as freelist
        freelist = emptyList
        # STEP3 : Increment emptylist
        emptyList = linkedList[emptyList].nextNode

        # STEP4 : Make a new node on freelist pointer
        newnode = node(datatoinsert, -1)
        linkedList[freelist] = newnode

        # STEP5 : Finding the correctposition
        previouspointer = 0
        while currentpointer != -1 and linkedList[currentpointer].Data < datatoinsert:
            previouspointer = currentpointer
            currentpointer = linkedList[currentpointer].nextNode

        # STEP6 : Making Connection. There are 2 cases
        # 1) Storing on the first position
        # 2) Storing in middle/end

        if currentpointer == startPointer:  # case 1
            linkedList[freelist].nextNode = startPointer
            startPointer = freelist
        else:
            # case 2
            linkedList[freelist].nextNode = linkedList[previouspointer].nextNode
            linkedList[previouspointer].nextNode = freelist

        return True


def Finditem(currentpointer, searchvalue):
    while currentpointer != -1:
        if linkedList[currentpointer].Data != searchvalue:
            currentpointer = linkedList[currentpointer].nextNode
        else:
            return currentpointer
    return -1
