"""
Anonymous Function (function without name) is called lambda function.
Useful if the function expresion is small also if we are not gonna use it multiple times

"""


# What we do normally

def square(num):
    return num ** 2

result = square(5)
print(result)


# Above example using lambda function

fun = lambda num : num ** 2
result = fun(4)
print(result)
