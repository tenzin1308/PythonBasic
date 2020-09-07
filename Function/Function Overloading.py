
"""
Python doesn't support Function Overloading.
So to overload a function we can use the concept of Variable length argument or Keyword variable length argument
"""


# Example of Function overloading

def sum(a, b):
    return a + b


def sum(a, b, c):
    return a + b + c

# Uncomment to see the error
#print(f'Sum = {sum(4, 5)}') # We get error because python overwrites the first function (of 2 argument) by the second function (of 3 argument)

print(f'Sum 2 = {sum(4, 5, 1)}')


# Using Variable length argument

def sum(a, *b): # b is Tuples here
    print(a)
    print(b)
    total = a
    for i in b:
        total += i
    return total


print(f'Sum 3 = {sum(1,2,3,6,8,100)}')


# Using Keyword variable length argument

def person(**b): # It's a good practice to use argument name kwargs and it's in dic format
    print(b)
    for k, v in b.items():
        print(f"{k} : {v}")

print('Person info :-"')
person(name="Tenzin", age=22, address="Queens", phone=6461234567)

