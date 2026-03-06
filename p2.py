class Students:
    def __init__(self,fullname,marks,grade):
        self.name=fullname
        self.marks=marks
        self.grade=grade
        print("adding new students")

    def department( self):
        print("they all belong to cs")   
    def getmarks(self):
        return self.marks 
       
obj1=Students("farhan",67,'A')
print(obj1.name,obj1.marks,obj1.grade)
obj1.department()
obj1.getmarks()
obj2=Students("aijaz",80,'B')
print(obj2.name,obj2.marks,obj2.grade)
obj3=Students("moiz",90,'C')
print(obj3.name,obj3.marks,obj3.grade)
