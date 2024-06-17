# each file is a module and makes it more organized, and you can use that module in other files 
# just import this file to any other file that you want to use these methods
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


# challenge
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
