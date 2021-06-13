class Employee():

    raiseAmount = 1.04
    
    def __init__(self,firstName,lastName,pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName+ "."+lastName + "@gmail.com"


    def fullPay(self):
        return str(self.pay * self.raiseAmount)

#Now you can modify values and iterate values directly from the class
#so that you will not be needing any instance of the class
    @classmethod
    def raiseAmountAfterAYear(cls,amount):
        cls.raiseAmount = amount

#µµµ-it is the right method (ALTERNATIVE CONSTRUCTOR)
    @classmethod
    def from_new_employee_string(cls,text_to_split):
        firstName , lastName, pay = text_to_split.split("-")
        return cls(firstName ,lastName, pay) #create a new object of the class
    
#so now let's consider that you wanna check if a day was a working day
    @staticmethod
    def is_workday(day):
        #monday = 0 , sunday = 6 , .weekday() is a method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

John = Employee("John","Snow",35000)
Jude = Employee("Jude","Grace",36000)
Jacob = Employee("Jacob","Carrey",34000)
print(Employee.raiseAmount)
print("John's full play : ",John.fullPay())


Employee.raiseAmountAfterAYear(1.06)
print("New raise amount after a year :")
print(Employee.raiseAmount)
print("John's full play after a year : ",John.fullPay())


#µµµ-consider now you have a list of employee that are separated by a "-" in a string format
#and you wanna create a list out of it
emp_1 = "Jake-Peterson-32000 "
emp_2 = " Julie-Roberts-37000 "
emp_3 = " Jade-Nickolson-40000 "

new_emp_listed_1 = Employee.from_new_employee_string(emp_1) #emp_1 = text to split
new_emp_listed_2 = Employee.from_new_employee_string(emp_2)
new_emp_listed_3 = Employee.from_new_employee_string(emp_3)

print(new_emp_listed_1.email)
print(new_emp_listed_1.lastName)


import datetime
my_date = datetime.date(2016, 7, 10) #it's a Sunday
my_date_2 = datetime.date(2016, 7, 11) #it's a Monday

print(Employee.is_workday(my_date))
print(Employee.is_workday(my_date_2))


    
