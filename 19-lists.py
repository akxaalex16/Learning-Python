# list of names
names =['akxa','alex','sean','hupe','baby luv','jovi','bambi']
print(names)
# shows the whole list

# access specific vaules by their index
print(names[2])
# shows sean

# acccess last item in list
print(names[-1])
# shows bambi

# accessing second value from the end of the list
print(names[-2]) 
# shows jovi

# use a colon to select a range of items 
print(names[2:])
# this gets all the items starting from the index of 2
# shows: ['sean', 'hupe', 'baby luv', 'jovi', 'bambi']

# can also add an end index
# doesnt include the item at that index of 4, the 5th
# element does not get returned 
print(names[2:4])
# shows:['sean', 'hupe']

# this assumes 0 as the default index
# it returns everything
print(names[:])

# can modify any item in list
names[4] = 'baby'
print(names)


# challenge: write a program to find the largest number in a list
numbers=[2,3,6,9,16]
max= numbers[0]
# this variable holds the largest number
# we want to assume that the first item in this list 
# is the largest number

for num in numbers:
    if num > max:
        max = num
print(max)