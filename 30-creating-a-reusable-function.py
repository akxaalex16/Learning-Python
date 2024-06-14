# each function should only be responsible for one task
def emoji_converter(message):
    words = message.split(" ")

    emojis =  {
    ":(" : "😞",
    ":)" : "😊"
           }

    output= ""
    for item in words:
        output += emojis.get(item, item) + " "
    return output
# add the return line at the end of the function

# the input is not in the function because in one program you 
# might get it from the terminal, in another program you might
# get it from a graphical user interface
message = input("> ")

# call the function and store it in a variable
result = emoji_converter(message)

# we shouldnt put the output in the function because what we do with it 
# is different from one program to another
# in this program we are printing the output, but in another 
# program we might send the output as an email or as a response in a chat application
print(result)

# your functions should not worry about the input or printing 
# so dont include those lines of code in the function