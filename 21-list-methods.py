# operations that we can perform on a list 
numbers = [2,3,6,9,16]
print(numbers)

# append method adds the value to the end of the list
numbers.append(16)
print(numbers)
# shows: [2, 3, 6, 9, 16, 16]

# to add a value to the middle of the list
# use the insert method
# it takes two values: the index of where you want to insert new item,
# and the value you want to insert
numbers.insert(2,5)
print(numbers)
# shows: [2, 3, 5, 6, 9, 16, 16]

# to add to the beginning of the list, we use insert also
numbers.insert(0, 10)
print(numbers)
# shows: [10, 2, 3, 5, 6, 9, 16, 16]

# to remove a value from the list
numbers.remove(10)
print(numbers)
# shows : [2, 3, 5, 6, 9, 16, 16]

# use .pop() to remove last item in list
numbers.pop()
print(numbers)
# shows: [2, 3, 5, 6, 9, 16]

# call the index method to check for the existance of an item in a list 
# shows the index of the first occurrence of that value
print(numbers.index(2))
# shows 0
# if you check for a value that is not in the list,
# you will get a value error, showing that number is not in list

# another way to check for existance of an item in a list
# by using the in operator
# gives boolean value
print(16 in numbers)
# shows True

# to see how many times a certain number occurs
print(numbers.count(16))
# shows 1

# to sort your list
# doesnt take in any value
num=[3,16,6,9]
num.sort()
print(num)
# shows : [3, 6, 9, 16]

# to sort in descending order after it is already sorted
# use reverse method
num.reverse()
print(num)
# shows: [16, 9, 6, 3]

# to make copy of our list
# after making the copy and manipulating it, it wont
# affect the original list
num2 = num.copy()
num2.append(27)
print(num)
# shows : [16, 9, 6, 3]
print(num2)
# shows: [16, 9, 6, 3, 27]

# use .clear() method to empty list
print(num2.clear())
# shows None


# challenge: write a program to 
# remove the duplicates in a list

nums= [2, 2, 3, 6, 1, 1, 9, 16, 5, 5]
uniques= []

for value in nums:
    if value not in uniques:
        uniques.append(value)
print(uniques)
# shows: [2, 3, 6, 1, 9, 16, 5]