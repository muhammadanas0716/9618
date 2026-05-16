class Employee:
    # self.__HourlyPay single
    # self.__EmployeeNumber string
    # self.__JobTitle string

    def __init__(self, EmpNumP, PayP, JobP):
        self.__HourlyPay = PayP
        self.__EmployeeNumber = EmpNumP
        self.__JobTitle = JobP
        self.__PayYear2022 = [] # ARRAY [0:51]

        for x in range(52):
            self.__PayYear2022.append(0.00)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    

    def SetPay(self, weekNo, NoOfHours):
        pay = weekNo * NoOfHours
        self.__PayYear2022[weekNo - 1] = pay # Since week starts from 1

    def GetTotalPay(self):
        totalPay = 0
        for pay in self.__PayYear2022:
            totalPay += pay

        return totalPay
    

class Manager(Employee):
    def __init__(self, EmpNumP, PayP, JobP, BonusP):
        super().__init__(EmpNumP, PayP, JobP)
        self.__BonusValue = BonusP
    
    def SetPay(self, weekNo, NoOfHours):
        NoOfHoursUpdated = NoOfHours * (1 + self.__BonusValue / 100)

        super().SetPay(weekNo, NoOfHoursUpdated)



global EmployeeArray
EmployeeArray = []

try:
    employeeFile = open("Employees.txt", "r")

    for i in range(8):
        hourlyPay = float(employeeFile.readline().strip())
        employeeNumber = employeeFile.readline().strip()
        temp = employeeFile.readline().strip()

        try:
            if type(float(temp)) == float:
                bonusValue = float(temp)
                jobTitle = employeeFile.readline().strip()

                tempObj = Manager(EmpNumP=employeeNumber, PayP=hourlyPay, JobP=jobTitle, BonusP=bonusValue)
                EmployeeArray.append(tempObj)
        except ValueError:
            jobTitle = temp
            tempObj = Employee(EmpNumP=employeeNumber, PayP=hourlyPay, JobP=jobTitle)
            EmployeeArray.append(tempObj)



    employeeFile.close()
except FileNotFoundError:
    print("File not found")
