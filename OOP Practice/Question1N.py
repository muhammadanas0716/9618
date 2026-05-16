class EventItem:
    def __init__(self, EventNameP, TypeP, DifficultyP):
        self.__EventName = EventNameP
        self.__Type = TypeP
        self.__Difficulty = DifficultyP

    def GetName(self):
        return self.__EventName
    
    def GetEventType(self):
        return self.__Type
    
    def GetDifficulty(self):
        return self.__Difficulty
    

# DECLARE GROUP: ARRAY OF EventItem
Group = []

Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))


class Character:
    def __init__(self, CharacterNameP, JumpP, SwimP, RunP, DriveP):
        self.__CharacterName = CharacterNameP
        self.__Jump = JumpP
        self.__Swim = SwimP
        self.__Run = RunP
        self.__Drive = DriveP

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, TypeOfEvent, DifficultyOfEvent):
        # Pass e.g run # Diff. mention
        chance = 100

        if TypeOfEvent == "jump":
            if self.__Jump >= DifficultyOfEvent:
                chance = 100
            elif DifficultyOfEvent - self.__Jump == 1:
                chance = 80
            elif DifficultyOfEvent - self.__Jump == 2:
                chance = 60
            elif DifficultyOfEvent - self.__Jump == 3:
                chance = 40
            elif DifficultyOfEvent - self.__Jump == 4:
                chance = 20
        if TypeOfEvent == "swim":
            if self.__Swim >= DifficultyOfEvent:
                chance = 100
            elif DifficultyOfEvent - self.__Swim == 1:
                chance = 80
            elif DifficultyOfEvent - self.__Swim == 2:
                chance = 60
            elif DifficultyOfEvent - self.__Swim == 3:
                chance = 40
            elif DifficultyOfEvent - self.__Swim == 4:
                chance = 20
        if TypeOfEvent == "run":
            if self.__Run >= DifficultyOfEvent:
                chance = 100
            elif DifficultyOfEvent - self.__Run == 1:
                chance = 80
            elif DifficultyOfEvent - self.__Run == 2:
                chance = 60
            elif DifficultyOfEvent - self.__Run == 3:
                chance = 40
            elif DifficultyOfEvent - self.__Run == 4:
                chance = 20
        if TypeOfEvent == "drive":
            if self.__Drive >= DifficultyOfEvent:
                chance = 100
            elif DifficultyOfEvent - self.__Drive == 1:
                chance = 80
            elif DifficultyOfEvent - self.__Drive == 2:
                chance = 60
            elif DifficultyOfEvent - self.__Drive == 3:
                chance = 40
            elif DifficultyOfEvent - self.__Drive == 4:
                chance = 20

        return chance



Character1 = Character("Tarz", 5,3,5,1)
Character2 = Character("Geni", 2,2,3,4)

points1 = 0
points2 = 0

for event in Group:
    score1 = Character1.CalculateScore(event.GetEventType(), event.GetDifficulty())
    score2 = Character2.CalculateScore(event.GetEventType(), event.GetDifficulty())

    if score1 == score2:
        print("This event is a draw")
    elif score1 > score2:
        points1 += 1
        print(f"Player 1: {Character1.GetName()} has won the game")
    else:
        points2 += 1
        print(f"Player 2: {Character2.GetName()} has won the game")


if points1 == points2:
    print("This group was a draw.")
elif points1 > points2:
    print(f"Player 1: with {points1} has won the game")
else:
    print(f"Player 2: with {points2} has won the game")   

