i=1
# where we initiate the loop

# while loop with condition
while i <= 5:
    print(i)
    i = i + 1
    # if we dont add this line then it would be an infinite loop
    # because i equal to 1 would always be less than 5
    # we need to increment the i value so that once i = 6,
    # then the condition is false and we can terminate the loop
print("Done")

j= 1
while j <= 5:
    print("*" * j)
    j= j + 1
print("Done")