class Vehicle:
    def __init__(self, ID, MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition):
        # PRIVATE ID: STRING
        # PRIVATE MaxSpeed: INTEGER
        # PRIVATE CurrentSpeed: INTEGER
        # PRIVATE IncreaseAmount: INTEGER
        # PRIVATE HorizontalPosition: INTEGER

        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = 0

    
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self, speedValue):
        self.__CurrentSpeed = speedValue
    
    def SetHorizontalPosition(self, newHorizontalPos):
        self.__HorizontalPosition = newHorizontalPos


    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount

        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed
    
class Helicopter(Vehicle):
    # PRIVATE VerticalPosition: INTEGER
    # PRIVATE VerticalChange: INTEGER
    # PRIVATE MaxHeight: INTEGER

    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount) # pyright: ignore[reportCallIssue]
        self.__VertChange = 0
        self.__MaxHeight = 0
    
