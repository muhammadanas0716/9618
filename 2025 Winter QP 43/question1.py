class BoardObject:
    def __init__(self, CodeP, StringP):
        # DECLARE Code: INTEGER
        # DECLARE String: CHAR

        self.__Code = CodeP
        self.__String = StringP
    
    def GetCode(self):
        return self.__Code

    def GetString(self):
        return self.__String


object1 = BoardObject("A", 2)
object2 = BoardObject("B", 3)
object3 = BoardObject("C", 5)
object4 = BoardObject("D", 2)
object5 = BoardObject("E", 7)

class Board:
    # DECLARE PRIVATE TheBoard : ARRAY[0:9, 0:9] OF BoardObject
    def __init__(self):
        self.__TheBoard = [[BoardObject("-", 0) for _ in range(10)] for _ in range(10)]
    
    def GetObject(self, row, col):
        return self.__TheBoard[row][col]

    def SetObject(self, BoardObj, row, col):
        self.__TheBoard[row][col] = BoardObj
    
    def DisplayBoard(self):
        for i in range(10):
            myList = ""
            for j in range(10):
                myList +=  f"{str(self.GetObject(i, j).GetCode())} "
            
            print(myList)

MyBoard = Board()
MyBoard.SetObject(object1, 0, 0)
MyBoard.SetObject(object2, 9, 9)
MyBoard.SetObject(object3, 4, 5)
MyBoard.SetObject(object4, 2, 2)
MyBoard.SetObject(object5, 8, 7)

MyBoard.DisplayBoard()

# Get row
row = int(input("Enter row no. plz: "))
while row < 0 or row > 9:
    row = int(input("Enter row no. plz: "))

# Get col
col = int(input("Enter col no. plz: "))
while col < 0 or col > 9:
    col = int(input("Enter col no. plz: "))

obj = MyBoard.GetObject(row, col)
if obj.GetCode() == 0 and obj.GetString() == "-":
    print("Miss")
else:
    print(f"The code for this object is: {obj.GetCode()}")
    print(f"The string for this object is: {obj.GetString()}")
          
# 31 / 31