# DECLARE QueueArray : ARRAY[0:9] OF STRING
QueueArray = [""] * 10

HeadPointer = 0
TailPointer = 0
NumberItems = 0


def Enqueue(InputData: str):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberItems

    if NumberItems > 9:
        return False
    else:
        QueueArray[TailPointer] = InputData

    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1

    NumberItems += 1
    return True


def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberItems

    if NumberItems == 0:
        return "FALSE"
    else:
        value = QueueArray[HeadPointer]
        HeadPointer += 1

        if HeadPointer > 9:
            HeadPointer = 0

        NumberItems -= 1
        return f"Item removed: {value}"


print(
    f"TailPointer: {TailPointer}, HeadPointer: {HeadPointer}, NumberItems: {NumberItems}"
)

Enqueue("Anas")
Enqueue("Talha")
Enqueue("Amena")
Enqueue("Hadia")
Enqueue("Haider")
Enqueue("Faizan")
Enqueue("Samueal")
Enqueue("Emaan Fatima")
Enqueue("Mukhtar")
Enqueue("Ali")
print(Dequeue())
Enqueue("Dua")
print(Dequeue())
print(Dequeue())
print(Dequeue())
Enqueue("Aliya")
Enqueue("Amigo")
Enqueue("Warda")
print(Dequeue())
print(Dequeue())


print(
    f"TailPointer: {TailPointer}, HeadPointer: {HeadPointer}, NumberItems: {NumberItems}"
)
print(f"QueueArray: {QueueArray}")
