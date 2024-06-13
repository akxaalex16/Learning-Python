# use dictionaries for key value pairs
# use curly braces
# the keys need to be unique
# the vaules can be a string, boolean, number/int, float, lists, etc.

customer ={"name" : "Akxa Alex",
           "age" : 30,
           "is_verified" : True
           }

# to access items in the dictionary, we use square brackets
# variable[key]
print(customer["name"])

# if you pass a key that doesnt exist or is not written 
# the exact way it is found in the dictionary then 
# you get a KeyError
# print(customer["birthdate"])
# print(customer["Name"])

# to get around the key error you can use the get method
# if you use a key that doesnt exist, it doesnt yell at us with an error
print(customer.get("birthdate"))
# it just returns None, which means the absence of a value

# we can also supply a default value if the dictionary doesnt have a certain key
print(customer.get("birthdate", "June 1 1994"))

# you can update any value in the dictionary
customer["name"] = "Sean Hupe"
print(customer["name"])

# we can also add a new key value pair
customer["birthdate"] = "Sep 1 1975"
print(customer["birthdate"])

# challenge
phone_number = input("Phone: ")

digits_mapping = {
             "1": "One",
             "2" : "Two",
             "3" : "Three"
             }
output = ""
for item in phone_number:
   output += digits_mapping.get(item, "!") + " "
print(output)