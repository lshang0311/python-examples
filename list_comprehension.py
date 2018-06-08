"""
Examples of list comprehension

Ref:
    https://www.datacamp.com/community/tutorials/python-list-comprehension
"""

# as an alternative to For Loops
numbers = range(10)
new_list = [n ** 2 for n in numbers if n % 2 == 0]
print(new_list)

# as an alternative to map() in Combination with Lambda Functions
kilometer = [39.2, 36.5, 37.3, 37.8]

"""
feet = map(lambda x: float(3280.8399) * x, kilometer)
print(list(feet))
"""

feet = [float(3280.8399) * x for x in kilometer]
print(feet)

# as an alternative to filter() in combination with Lambda Functions
"""
feet = list(map(int, feet))
uneven = filter(lambda x: x % 2, feet)
print(list(uneven))
"""

feet = [int(x) for x in feet]
print(feet)

# as alternative to reduce() in combination with Lambda Functions
"""
from functools import reduce
reduced_feet = reduce(lambda x, y: x + y, feet)
print(reduced_feet)
"""
reduced_feet = sum([x for x in feet])
print(reduced_feet)

# list comprehension with conditionals
divided = [x for x in range(30) if x % 2 == 0]
print(divided)

divided = [x for x in range(30) if x % 2 == 0 if x % 6 == 0]
print(divided)

# if-else conditions
print([x / 2.0 if x <= 2 else x for x in range(10)])

# nested list comprehension - flatten a list of lists
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]
print([y for x in list_of_list for y in x])

# nested list comprehension - matrix manipulation
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print([row[0] for row in matrix])
print([[row[i] for row in matrix] for i in range(3)])

# nested list comprehension - initialize a matrix
matrix = [[0 for col in range(4)] for row in range(3)]
print(matrix)
