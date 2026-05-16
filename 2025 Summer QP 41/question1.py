# DECLARE Queue : ARRAY[0:19] OF INTEGER
# DECLARE HeadPointer : INTEGER
# DECLARE TailPointer : INTEGER
# DECLARE NumberItems : INTEGER

global Queue, HeadPointer, TailPointer, NumberItems

Queue = [-1 for i in range(20)]
HeadPointer = -1
TailPointer = -1
NumberItems = 0


def Enqueue(Value):
    global Queue, HeadPointer, TailPointer, NumberItems

    # Check if full
    if NumberItems >= 20:
        return False

    # If queue empty
    if NumberItems == 0:
        HeadPointer = 0
        TailPointer = 0

    else:
        TailPointer += 1

        # Circular queue wrap
        if TailPointer == 20:
            TailPointer = 0

    Queue[TailPointer] = Value
    NumberItems += 1

    return True


for X in range(1, 26):
    ReturnValue = Enqueue(X)

    if ReturnValue == True:
        print(X, "Successful")

    else:
        print(X, "Unsuccessful")


def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems

    # Check if empty
    if NumberItems == 0:
        return -1

    Value = Queue[HeadPointer]

    HeadPointer += 1

    # Circular queue wrap
    if HeadPointer == 20:
        HeadPointer = 0

    NumberItems -= 1

    # Reset pointers if queue empty
    if NumberItems == 0:
        HeadPointer = -1
        TailPointer = -1

    return Value


# 13 / 20