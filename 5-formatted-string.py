first = "Bean"
last = "Alex"

# how do we print: Bean [Alex] is a coder, on the terminal
message= first + ' [' + last + '] is a coder'
print(message)

# even though the above example is okay and it works,
# we should put it in a formatted string to make it easier
msg=f'{first} [{last}] is a coder'
print(msg)