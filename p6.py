#student method 
class Student:
    @staticmethod
    def hellow():
        print("hellow")

Student.hellow()

class Country:
    @staticmethod
    def cities():
        print("there are 34 cities")
Country.cities()
class Marks:
    def display(self,marks1,marks2):
        self.marks1=marks1
        self.marks2=marks2
        print("marks1 is:",self.marks1," and marks2 is:",self.marks2)
s1=Marks()
s1.display(12,34)

class Calcalator:
    def add(a,b):
        return a+b
result=Calcalator.add(12,23)
print("the sum of the two number is :",result)

class NumberCheck:

    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

NumberCheck.is_even(8)