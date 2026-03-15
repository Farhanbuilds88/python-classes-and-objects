class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = Student("Ali", 85)
print("Marks:", s1.get_marks())
s1.set_marks(90)
print("Updated Marks:", s1.get_marks())