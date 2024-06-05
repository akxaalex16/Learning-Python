course ="Python's course for beginners"
course2= 'Python for "beginners"'
email='''Hi John,

Here is our first email to you

Thank you,
The support team
'''
print(course)
print(course2)
print(email)

msg="Hello Bean, eeeeeee!"
# the index of the first character in this string is zero
print(msg[0]) 
# shows H in terminal

print(msg[-1])
# shows the last character of !
# -1 is the index of the last character


# to extract more than 1 character from the string
print(msg[0:3])
# [starts at 0: number of characters]
# shows Hel

# shows the whole message
print(msg[0:])
print(msg[:])

# makes a copy of msg variable 
copy_msg= msg[:]
print(copy_msg)


# starts from the second letter and then shows the rest of the message
print(msg[1:])

# has a default start value of zero
# shows Hello
print(msg[:5])


# example: name="Jennifer"
#          print(name[1:-1])
name="Akxa Alex"
print(name[1:-1])
# shows kxa Ale