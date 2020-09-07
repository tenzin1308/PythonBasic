"""
Function in Python

Syntax:

def function_name(arguments):
    {do something in body}
    return
"""


# Example

def person(name, age):
    print(name, age)


person("Tenzin", 22)


# Using Default value


def person(name="John Doe", age=18):
    print(name, age)


person("Elizabeth")

# Using Keywords

person(age=21)
