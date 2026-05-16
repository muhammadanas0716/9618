# Part (a)
class Queue:
    def __init__(self, QueueArrayP: list, HeadpointerP: int, TailPointerP: int):
        self.QueueArray = QueueArrayP # ARRAY [0:99] OF INTEGER
        self.Headpointer= HeadpointerP # INTEGER
        self.TailPointer = TailPointerP # INTEGER


# Part (b)
TheQueue = Queue([-1 for i in range(100)], -1, 0)

# Part (c)
def Enqueue(AQueue: Queue, TheData: int):
    # Queue is empty - always check because the headpointer needs to be incremented to 0
    if AQueue.Headpointer == -1: 
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.Headpointer = 0
        AQueue.TailPointer = AQueue.TailPointer + 1
        return 1

    else:
        if AQueue.TailPointer > 99:
            return -1
        else:
            AQueue.QueueArray[AQueue.TailPointer] = TheData
            AQueue.TailPointer = AQueue.TailPointer + 1
            return 1


def ReturnAllData():
    string = ""

    for i in range(TheQueue.Headpointer, TheQueue.TailPointer):
        string += f"{str(TheQueue.QueueArray[i])} "
    
    return string


count = 0
while count < 10:
    Value = int(input("Enter a number please: "))
    if Value >= 0:
        comment = Enqueue(TheQueue, Value)
        
        if comment == -1:
            print("Queue is full")
        else:
            print("Item added to Queue")
            count += 1
    else:
        print("Enter value greater than 0")

print(ReturnAllData())

def Dequeue():
    if TheQueue.Headpointer == -1:
        return -1
    
    value = TheQueue.QueueArray[TheQueue.Headpointer]
    TheQueue.Headpointer += 1

    if TheQueue.Headpointer == TheQueue.TailPointer:
        TheQueue.Headpointer = -1
        TheQueue.TailPointer = 0
    
    return value

deq1 = Dequeue()
if deq1 == -1:
    print("Empty Queue")
else:
    print(f"{deq1}")

deq2 = Dequeue()
if deq2 == -1:
    print("Empty Queue")
else:
    print(f"{deq2}")

print(ReturnAllData())