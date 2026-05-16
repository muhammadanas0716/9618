class Balloon():
    def __init__(self, colourP, DefenceItemP):
        self.__health = 100
        self.__colour = colourP
        self.__DefenceItem = DefenceItemP

    def ChangeHealth(self, Value):
        self.__health += Value

    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False
        
    def GetHealth(self):
        return self.__health
        
defenceItem = input("Enter your defence item: ")
color = input("Enter the color for your baloon: ")
Baloon1 = Balloon(color, defenceItem)


def Defend(balloonObj):
    opponentStrength = int(input("Enter opp. strength: "))
    balloonObj.ChangeHealth(int(-opponentStrength))
    print(f"Defence Object: {balloonObj.GetDefenceItem()}")
    health = balloonObj.CheckHealth()
    if health == True:
        print(f"No health left: {balloonObj.GetHealth()}")
    else:
        print(f"Health left: {balloonObj.GetHealth()}")
    
    return balloonObj


print(Defend(Baloon1))



# 25 / 25