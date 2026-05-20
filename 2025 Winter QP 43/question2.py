# DECLARE Queue: ARRAY[0:100] OF STRING
# DECLARE QueueHead: INTEGER
# DECLARE QueueTail: INTEGER
# DECLARE NumberItems: INTEGER

global Queue, QueueHead, QueueTail, NumberItems
Queue = ["" for _ in range(100)]
QueueHead = -1
QueueTail = -1
NumberItems = 0


def Enqueue(value):
    global Queue, QueueHead, QueueTail, NumberItems

    if NumberItems == 100:
        return False
    
    if QueueHead == -1:
        QueueHead = 0
    
    QueueTail += 1
    Queue[QueueTail] = value
    NumberItems += 1

    return True

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems

    if NumberItems == 0:
        return "False"
    
    temp = Queue[QueueHead]
    QueueHead += 1 
    NumberItems -= 1

    return temp

def ReadData():
    lines = 0
    try:
        file = open("BinaryData.txt", "r")
        for line in file:
            if lines >= 100:
                break
            else:
                digit = line.strip()
                Enqueue(digit)
                lines += 1
        file.close()
    
    except IOError:
        print("Some error occured.")


def Compress():
    global NewString

    NewString = ""

    current = Dequeue()
    count = 1

    while NumberItems > 0:
        nextDigit = Dequeue()

        if nextDigit == current:
            count += 1
        else:
            NewString = NewString + current + str(count)
            current = nextDigit
            count = 1

    NewString = NewString + current + str(count)

# 19 / 24