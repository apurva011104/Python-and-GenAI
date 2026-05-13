class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s = Student("Alex")
s.set_marks(85)
print(s.get_marks())