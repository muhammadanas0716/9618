Names = [""] * 10
HeadPointer = -1
TailPointer = 0


def Enqueue(Value: str):
    global Names
    global HeadPointer
    global TailPointer

    if TailPointer < 10:
        Names[TailPointer] = Value
        TailPointer += 1

        if HeadPointer == -1:
            HeadPointer = 0
    else:
        print("Queue is full")


def Dequeue():
    global Names
    global HeadPointer
    global TailPointer

    if HeadPointer == -1:
        print("Q is full")
    else:
        item = Names[HeadPointer]
        print(item)
        HeadPointer += 1

    if HeadPointer == TailPointer:
        TailPointer = 0
        HeadPointer = -1
