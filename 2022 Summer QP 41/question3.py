# DECLARE ARRAY [0:9] OF STRING
# DECLARE HeadPointer OF INTEGER
# DECLARE TailPointer OF INTEGER
# DECLARE NoOfItems OF INTEGER

QueueArray = ["" for i in range(10)]
HeadPointer : int = 0
TailPointer : int  = 0
NoOfItems : int  = 0


def Enqueue(DataToAdd: str):
    global QueueArray, HeadPointer, TailPointer, NoOfItems

    if NoOfItems == 10:
        return False
    
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NoOfItems += 1
    return True

print(Enqueue("hello"))
print(QueueArray)

def Dequeue():
    global QueueArray, HeadPointer, TailPointer, NoOfItems
    if NoOfItems == 0:
        return False

    temp = TailPointer
    TailPointer += 1
    NoOfItems -= 1
    
    return QueueArray[temp]


# 17 / 21