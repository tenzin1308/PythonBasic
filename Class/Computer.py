"""
Class is a blueprint of something.

It contain Attributes ----> Variables (instances Variable)
           Behaviour  ----> Methods(Function)
           
"""


class Computer:
    def config(self):
        print("i9, 32 Gb, 2 TB")


comp1 = Computer()
print(type(comp1))

comp1.config()

Computer.config(comp1)
