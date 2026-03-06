class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Farhan", 90)
s1.show()

class Student_info:
    def  show_info(self,section,university,gpa):
        self.section=section
        self.university=university
        self.gpa=gpa
        return self.university,self.section,self.gpa

obj1=Student_info()
data=obj1.show_info('A',"Air",'3.3')
#print(obj1.section)
#print(obj1.university)
#print(obj1.gpa)
print(data)

class Calculator:
    def add(self,a,b):
        return a+b
    
obj2=Calculator()
result=obj2.add(23,34)
print(result)