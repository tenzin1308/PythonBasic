class Person:
    country = "USA" ## Static Variable
    def __init__(self, name="Jane Doe", age=18):
        self.name = name
        self.age = age
        self.address = None

    def print(self):
        print(f'Name : {self.name} \nAge : {self.age} \nAddress : {self.address}')

    def compare(self,other):
        if self.age > other.age:
            print(f'{self.name} is older than {other.name}')
        else:
            print(f'{other.name} is older than {self.name}')


P1 = Person()
P1.print()

P2 = Person(age=25, name="James")
P2.address = "NYC"
P2.print()

P1.compare(P2)
print(P1.country)
print(P2.country)
print(Person.country)
P1.country = "Canada" ## Because of namespace [ Class namespace & object/Instance namesapce ]
print(P2.country)