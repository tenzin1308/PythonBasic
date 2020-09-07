"""
We have 3 types of Methods:
        a) Instances/Object Methods
        b) Class Methods
        c) Static Methods

"""


class Student:
    # Class/Static Variable
    school = "ABC School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instances/Object Methods
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class Methods
    @classmethod  ## Decorator
    def getSchool(cls):
        print(cls.school)

    # Static Methods
    @staticmethod
    def info():
        print("This is Static Method")

s1 = Student(67, 87, 76)
s2 = Student(98, 67, 78)

print(s1.avg())
print(s2.avg())
Student.getSchool()
Student.info()
