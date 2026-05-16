class Picture:
    def __init__(self, DescriptionP, WidthP, HeightP, FrameColourP):
        self.__Description = DescriptionP
        self.__Width = WidthP
        self.__Height = HeightP
        self.__FrameColour = FrameColourP

    def GetDescription(self):
        return self.__Description
    
    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetFrameColour(self):
        return self.__FrameColour
    
    def SetDescription(self, newDescription):
        self.__Description = newDescription


    
# DECLARE PictureArray [0:99] OF Picture
PictureArray = []

def ReadData():
    count = 0

    try:
        file = open("Pictures.txt", "r")

        for i in range(100):
            description = file.readline().strip()
            width = file.readline().strip()
            height = file.readline().strip()
            frameColour = file.readline().strip()

            tempObj = Picture(description, width, height, frameColour)
            PictureArray.append(tempObj)

            if description != "" and frameColour != "":
                count += 1
            else:
                break
    
        file.close()

    except FileNotFoundError:
        print("File not found")
    
    return count


ReadData()

found = False
while not found:
    framecolor = input("Enter frame color: ")
    width = input("Enter frame width: ")
    height = input("Enter frame height: ")
    myObj = PictureArray[0]

    for object in PictureArray:
        if object.GetFrameColour().lower() == framecolor.lower() or object.GetWidth() == width or object.GetHeight() == height:
            myObj = object
            found = True
            break

    if found == True:
        print(f"""
        Picture Description: {myObj.GetDescription()}
        Picture Width: {myObj.GetWidth()}
        Picture Height: {myObj.GetHeight()}
        Picture FrameColor: {myObj.GetFrameColour()}
        """)
    else:
        print("Try Again")
        


# 22 / 30