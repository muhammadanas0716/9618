global QueueHead
global QueueTail
global QueueData

QueueHead, QueueTail = -1, -1
QueueData = ["" for i in range(20)]


def Enqueue(Value: str):
    global QueueHead
    global QueueTail
    global QueueData

    if QueueHead == -1:
        QueueHead = 0
        QueueTail += 1
        QueueData[QueueTail] = Value
        return True
    else:
        if QueueTail == 19:
            return False
        else:
            QueueTail += 1
            QueueData[QueueTail] = Value
            return True

def Dequeue():
    global QueueHead
    global QueueTail
    global QueueData

    if QueueHead == -1:
        return "false"
    
    temp = QueueData[QueueHead]

    if QueueHead == QueueTail:
        QueueHead = -1
        QueueTail = -1
    else:
        QueueHead += 1
    
    return temp