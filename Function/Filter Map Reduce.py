"""
filter(function, iterable) : Filter function is used to filter out the output (kick out unwanted data)
map(function, iterable) : Map function is used to change the value of variable
reduce(function, iterable) : Reduce function is used to reduce to single output

"""
from functools import reduce

nums = [10, 3, 33, 24, 45, 23, 54, 65, 22]

# Example of filter
evens = list(filter(lambda num: num % 2 == 0, nums))
print(evens)

# Example of map
double = list(map(lambda num: num * 2, nums))
print(double)

# Example of reduce
sum = reduce(lambda a, b: a + b, nums)
print(sum)