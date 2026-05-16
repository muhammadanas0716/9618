class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = 0 
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        if self.__CurrentSpeed + self.__IncreaseAmount >= self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
            self.__HorizontalPosition = self.__CurrentSpeed
        else:
            self.__CurrentSpeed += self.__IncreaseAmount
            self.__HorizontalPosition += self.__CurrentSpeed

    def OutputCurrentPosition(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID=ID, MaxSpeed=MaxSpeed, IncreaseAmount=IncreaseAmount)
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight
        self.__VerticalPosition = 0

    def GetVerticalPosition(self):
        return self.__VerticalPosition
    
    def IncreaseSpeed(self):
        if self.__VerticalPosition + self.__VerticalChange >= self.__MaxHeight:
            self.__VerticalPosition += self.__MaxHeight
        else:
            self.__VerticalPosition += self.__VerticalChange
        
        super().IncreaseSpeed()


    def OutputCurrentPosition(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))
        print("Current verticalposition = ", self.__VerticalPosition)

#main
Car = Vehicle("Tiger", 100, 20)
Heli1 = Helicopter("Lion", 350, 40, 3, 100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputCurrentPosition()
print("")
Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.OutputCurrentPosition()