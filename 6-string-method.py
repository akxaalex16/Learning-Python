course = 'Python for Beginners'

# gets the length of the string, how many characters are in the string
# shows 20 
print(len(course))

print(course.upper())
# shows PYTHON FOR BEGGINNERS

print(course.lower())
# shows python for beginners

print(course.title())
# returns a string where the first character in every word is uppercase 

print(course)
# shows original string, was not affected by the 
# upper and lower methods used above

print(course.find('P'))
# gives the index value of the character
# shows 0

print(course.find('O'))
# the find method is case sensitive 
# if the character is not there then it shows -1

print(course.find('Beginners'))
# shows 11
# the index of where that word starts

print(course.replace('Beginners', 'absolute beginners'))
# .replace('the word you want to replace', 
# 'with the word(s) you want to replace it with')

# checking to see if a certain word or character is in the string
print('Python' in course)
# produces boolean value, true or false
# shows True

print('python' in course)
# shows False
# case sensitive