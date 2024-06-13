message = input("> ")
words = message.split(" ")

emojis =  {
    ":(" : "😞",
    ":)" : "😊"
           }

output= ""
for item in words:
    output += emojis.get(item, item) + " "
print(output)
