class MediaItem:
    #PRIVATE Title : STRING
    #PRIVATE Artist : STRING
    #PRIVATE Duration : INTEGER
    #PRIVATE PlayCount : INTEGER
    def __init__(self, TitleP, ArtistP, DurationP):
        self.__Title = TitleP
        self.__Artist = ArtistP
        self.__Duration = DurationP
        self.__PlayCount = 0

    def GetTitle(self):
        return self.__Title
    def GetArtist(self):
        return self.__Artist
    def GetDuration(self):
        return self.__Duration
    def GetPlayCount(self):
        return self.__PlayCount
    
    def Play(self):
        self.__PlayCount += 1
        return self.__Duration
    
    def GetDurationFormatted(self):
        minutes = self.__Duration // 60
        seconds = self.__Duration - (minutes*60)

        return f"{minutes} minutes {seconds} seconds"
    
class Podcast(MediaItem):
    def __init__(self, TitleP, ArtistP, DurationP, EpisodeNumberP, IsExplicitP):
        super().__init__(TitleP, ArtistP, DurationP)
        self.__EpisodeNumber = EpisodeNumberP
        self.__IsExplicit = IsExplicitP
        self.__ListenedTo = 0

    def GetEpisodeNumber(self):
        return self.__EpisodeNumber
    def GetIsExplicit(self):
        return self.__IsExplicit
    
    def Play(self):
        super().Play()
        self.__ListenedTo = 100
    
    def Resume(self, Position):
        if Position <= 0 or Position >= 100:
            return False
        else:
            super().Play()
            self.__ListenedTo = Position
            return True
        
    def GetDurationFormatted(self):
        return f"Ep [Number]: {super().GetDurationFormatted()}"

podcast1 = Podcast("Tech Talk", "Ali", 1800, 5, False)
media1 = MediaItem("Summer Song", "Sara", 210)
podcast1.Play()
media1.Play()
print(podcast1.GetDurationFormatted())
print(media1.GetDurationFormatted())
print("Podcast play count:", podcast1.GetPlayCount())
print("Media play count:", media1.GetPlayCount())