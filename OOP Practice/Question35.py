class Passenger():
    #PRIVATE PassportNumber : STRING
    #PRIVATE Name : STRING
    #PRIVATE SeatNumber : STRING
    #PRIVATE MealPreference : STRING
    def __init__(self, PassportNumberP, NameP):
        self.__PassportNumber = PassportNumberP
        self.__Name = NameP
        self.__SeatNumber = ""
        self.__MealPreference = "Standard"

    def GetPassportNumber(self):
        return self.__PassportNumber
    def GetName(self):
        return self.__Name
    def GetSeatNumber(self):
        return self.__SeatNumber
    def GetMealPreference(self):
        return self.__MealPreference
    
    def SetSeatNumber(self, SeatNumber):
        self.__SeatNumber = SeatNumber
    
    def SetMealPreference(self, Meal):
        if Meal in ["Standard", "Kosher", "Vegetarian", "Halal"]:
            self.__MealPreference = Meal
            return True
        else:
            return False
        

class Flight():
    #PRIVATE FlightNumber : STRING
    #PRIVATE Destination : STRING
    #PRIVATE MaxPassengers : INTEGER
    #PRIVATE Passengers : ARRAY OF Passenger
    #PRIVATE PassengerCount : INTEGER

    def __init__(self, FlightNumberP, DestinationP, MaxPassengersP):
        self.__FlightNumber = FlightNumberP
        self.__Destination = DestinationP
        self.__MaxPassengers = MaxPassengersP
        self.__Passengers = []
        self.__PassengerCount = 0

    def GetFlightNumber(self):
        return self.__FlightNumber
    
    def GetDestination(self):
        return self.__Destination
    
    def GetAvailableSeats(self):
        temp = self.__MaxPassengers - self.__PassengerCount
        return temp
    
    def AddPassenger(self, Passenger: Passenger):
        if self.__PassengerCount < self.__MaxPassengers:
            self.__Passengers.append(Passenger)
            self.__PassengerCount += 1
            return True
        else:
            return False
        
    def FindPassenger(self, PassportNum):
        for passenger in self.__Passengers:
            if passenger.GetPassportNumber() == PassportNum:
                return passenger
        
        return None
    
    def GetPassengerList(self):
        for passenger in self.__Passengers:
            name = passenger.GetName()
            passportNum = passenger.GetSeatNumber()
            seatNum = passenger.GetSeatNumber()
            mealPref = passenger.GetMealPreference()

            print(name, passportNum, seatNum, mealPref)


print("hello world")

# this is me coding 