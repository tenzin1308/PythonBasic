
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.age)

    class laptop:

        def __init__(self):
            self.brand = "HP"
            self.year = 2019
            self.cpu = "i7"

        def show(self):
            print(self.brand, self.year, self.cpu)

s1 = Student("James", 19)
s1.show()
print(s1.lap.brand)

lab2 = Student.laptop()
lab2.show()