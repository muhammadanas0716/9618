class Lesson:
    def __init__(self, lessonID, subject, teacher, room, period, day):
        self.__lessonID = lessonID # STRING
        self.__subject = subject # STRING
        self.__teacher = teacher # STRING
        self.__room = room # STRING
        self.__period = period # INTEGER
        self.__day = day # STRING

    def GetLessonID(self):
        return self.__lessonID
    
    def GetSubject(self):
        return self.__subject
    
    def GetTeacher(self):
        return self.__teacher
    
    def GetRoom(self):
        return self.__room
    
    def GetPeriod(self):
        return self.__period
    
    def GetDay(self):
        return self.__day
    



def LoadTimetable(file="files/TimeTable.txt"):
    lessonsArray = []
    
    try:
        file = open(file, "r")
        for line in file:
            items = line.strip().split(",")
            lessonID = items[0]
            subject = items[1]
            teacher = items[2]
            room = items[3]
            period = int(items[4])
            day = items[5]
            lessonsArray.append(Lesson(lessonID, subject, teacher, room, period, day))
        file.close()

    except IOError:
        return "File not found."
    
    return lessonsArray
        



