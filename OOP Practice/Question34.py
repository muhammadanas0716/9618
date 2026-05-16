class MaintenanceRecord:
    def __init__(self, RecordIDP, DateP, DescriptionP, CostP):
        self.__RecordID = RecordIDP
        self.__Date = DateP
        self.__Description = DescriptionP
        self.__Cost = CostP

    def GetRecordID(self):
        return self.__RecordID

    def GetDate(self):
        return self.__Date

    def GetDescription(self):
        return self.__Description
    
    def GetCost(self):
        return self.__Cost


class FleetVehicle:
    def __init__(self, VehicleRegP, MakeP, ModelP, YearP):
        self.__VehicleReg = VehicleRegP
        self.__Make = MakeP
        self.__Model = ModelP
        self.__Year = YearP
        self.__Records = []
        self.__RecordCount = 0

    def GetVehicleReg(self):
        return self.__VehicleReg
    
    def GetMake(self):
        return self.__Make
    
    def GetModel(self):
        return self.__Model
    
    def GetYear(self):
        return self.__Year
    
    def AddRecord(self, RecordP):
        self.__Records.append(RecordP)
        self.__RecordCount += 1

    def GetTotalMaintenanceCost(self):
        totalCost = 0

        for record in self.__Records:
            totalCost += record.GetCost()
        
        return totalCost
    
    def GetRecordsByDate(self, Date):
        dateRecords = []

        for record in self.__Records:
            if record.GetDate() == Date:
                dateRecords.append(record)

        return dateRecords

    def GetVehicleSummary(self):
        print("Registration:", self.__VehicleReg)
        print("Make:", self.__Make)
        print("Model:", self.__Model)
        print("Year:", self.__Year)
        print("Total Maintenance Cost:", self.GetTotalMaintenanceCost())



vehicle1 = FleetVehicle("ABC-123", "Toyota", "Corolla", 2020)

record1 = MaintenanceRecord("R001", "15/01/2025", "Oil Change", 5000)
record2 = MaintenanceRecord("R002", "15/01/2025", "Tyre Replacement", 12000)
record3 = MaintenanceRecord("R003", "20/03/2025", "Brake Inspection", 3000)

vehicle1.AddRecord(record1)
vehicle1.AddRecord(record2)
vehicle1.AddRecord(record3)

vehicle1.GetVehicleSummary()

janRecords = vehicle1.GetRecordsByDate("15/01/2025")
print("Records on 15/01/2025:", len(janRecords))

def FindMostExpensiveVehicle(FleetVehicleObjs: list):
    maxVehicle = FleetVehicleObjs[0]
    
    for vehicle in FleetVehicleObjs:
        if vehicle.GetTotalMaintenanceCost() > maxVehicle.GetTotalMaintenanceCost():
            maxVehicle = vehicle
    
    return maxVehicle


