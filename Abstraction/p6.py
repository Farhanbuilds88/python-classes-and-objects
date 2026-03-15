class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


emp1 = Employee("Farhan", 50000)

print("Salary:", emp1.get_salary())

emp1.set_salary(60000)

print("Updated Salary:", emp1.get_salary())