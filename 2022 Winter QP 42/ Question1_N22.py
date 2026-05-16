# DECLARE Jobs: ARRAY[0:99, 0:1] OF INTEGER
# DECLARE GLOBAL NumberOfJobs: INTEGER


def Initialise():
    global Jobs, NumberOfJobs

    Jobs = [[-1, -1] for i in range(100)]
    NumberOfJobs = 0

def AddJob(jobNumber, priorityNumber):
    global NumberOfJobs

    added = False
    for i in range(len(Jobs)):
        if Jobs[i][0] == -1 and Jobs[i][1] == -1:
            Jobs[i][0] = jobNumber
            Jobs[i][1] = priorityNumber
            print("Added")
            added = True
            NumberOfJobs += 1
        
            break
    
    if added == False:
        print("Not added")


def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(0, NumberOfJobs):
        print(str(Jobs[i][0]), " priority ", str(Jobs[i][1]))


Initialise() # To setup the arrays
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

def InsertionSort():
    # Assume first element is sorted
    sorted = False
    ix = 0
    while not sorted or ix == 99:
        sortedElement = Jobs[ix][1]
        if ix <= 98:
            temp = Jobs[ix+1][1]
            if sortedElement > temp:
                Jobs[ix+1][1] = sortedElement
                sortedElement = temp
            
            ix += 1

InsertionSort()
print(Jobs)