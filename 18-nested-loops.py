# nested loop means adding one loop inside another loop
# for example: 
# you can easily generate a list of (x,y) coordinates 

for x in range(6):
   for y in range(3):
       print(f'({x},{y})')

# result shows:
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
# (2,0)
# (2,1)
# (2,2)
# (3,0)
# (3,1)
# (3,2)
# (4,0)
# (4,1)
# (4,2)
# (5,0)
# (5,1)
# (5,2)

# challenge :
# make an f shape with x's

# xxxxx
# xx
# xxxxx
# xx
# xx

numbers= [5,2,5,2,2]

for num in numbers:
    # can do print('x' * num)
    output= ""
    for count in range(num):
        output += 'x'
    print(output)

# print an L with x's 
shape = [2,2,2,2,7]

for x_count in shape:
    ans = ""
    for val in range(x_count):
        ans += "x"
    print(ans)

# Explanation
# Line 1: We create a list of numbers.
# Line 2: We create a for loop to iterate over each of the items
#  in the list, using the variable x_count.
# Line 3: We define a variable ans and initially set it as an empty string.
# Line 4: We create an inner loop using the range() function to 
#  generate a sequence of numbers, starting from 0 to x_count. In the first iteration,
#  x_count is 7, so the range of 2 will generate the numbers 0 and 1. This means that this inner 
#  loop will be executed two times and that is exactly what x_count represents.
# Line 5: From the iteration in line 4, we append an x to our ans variable.
# Line 6: We print the ans. This means, that for the first iteration, 
#  we simply print our two x’s on the first row, then we go to the second 
#  iteration of our outer loop in line 2. Here x_count is 2. Now, we go back to line 3, since the ans
#  variable was set to an empty string. Python goes over to our inner loop, where it will append two x’s 
#  (the value of x_count is 2) to the ans variable, and then print.


