# tuples are similar to lists but unlike list,
# we cant not modify tuples
# tuples are immutable, we cant mutate or change them
# two methods for tuples: count and index
numbers = (1, 2, 3, 3, 6, 9, 16)

# return number of occurrences of a value
print(numbers.count(3))
# shows 2

# returns first index of value
print(numbers.index(16))
# shows: 6

# can access individual items using square brackets
print(numbers[0])
# shows: 1

# if you try to change any of the items, then you will get an error
# you get type error 'tuple' object does not support item assignment
