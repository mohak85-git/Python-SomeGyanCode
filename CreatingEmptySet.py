numbers = {}    # creates an empty dictionary instead of an empty set
print(numbers, type(numbers))

numbers = {*{}}  # creates an empty set by unpacking an empty dictionary
print(numbers, type(numbers))
# similarly an empty set can be created using empty string, list

numbers = {*""}  # creates an empty set by unpacking an empty string
print(numbers, type(numbers))

numbers = {*[]}  # creates an empty set by unpacking an empty list
print(numbers, type(numbers))

numbers = {*()}  # creates an empty set by unpacking an empty tuple
print(numbers, type(numbers))

numbers = set()  # creates an empty set by calling set constructor
print(numbers, type(numbers))
