class Bird:
    def __init__(self, SpeciesP, DistancePerHourP):
        self.__Species = SpeciesP
        self.__DistancePerHour = DistancePerHourP
        self.__XPosition = 500.0 # Horizontal
        self.__YPosition = 500.0 # Vertical
    
    def GetPosition(self):
        return f"X = {self.__XPosition} Y = {self.__YPosition}"

    def GetSpecies(self):
        return self.__Species

    def Move(self, direction, NoOfMinutesFlying):
        minutes = int(NoOfMinutesFlying)
        distanceTravelled = (self.__DistancePerHour  / 60) * minutes

        if direction == "N":
            self.__YPosition += distanceTravelled
        elif direction == "S":
            self.__YPosition -= distanceTravelled
        elif direction == "E":
            self.__XPosition += distanceTravelled
        elif direction == "W":
            self.__XPosition -= distanceTravelled

Bird1 = Bird("Cockatiel", 71.0)
Bird2 = Bird("Macaw", 56.0)

print(f"""
Bird One: {Bird1.GetSpecies()} - {Bird1.GetPosition()}
Bird Two: {Bird2.GetSpecies()} - {Bird2.GetPosition()}
""")

while True:
    bird = input("Enter either 1 or 2 to choose a bird: ")
    if bird == "1" or bird == "2":
        break

    print(f"Please choose a correct value")

while True:
    directionTravelled = input("Enter the direction the bird has been travelling in: N, S, W, E")
    if directionTravelled in ["N", "S", "W", "E"]:
        break

    print(f"Please choose a correct value")

while True:
    mintsTravelled = int(input("Enter the time: 0 to 500"))
    if mintsTravelled >= 0 and mintsTravelled <= 500:
        break
    
    print(f"Please choose a correct value")

if bird == "1":
    Bird1.Move(directionTravelled, mintsTravelled)
else:
    Bird2.Move(directionTravelled, mintsTravelled)

        
# 25 / 27




