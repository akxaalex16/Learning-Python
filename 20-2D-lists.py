# matrix which is a rectangular arrray of numbers
# 2D list is where each item in that list is another list
matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matrix)

# how to access items or lists in matrix
print(matrix[0])
# this accesses the inner list
# shows [1,2,3]

# now to get an item within a list in the matrix
print(matrix[0][2])
# shows the number 3

# modify values in matrix
matrix[1][0] = 20
print(matrix[1][0]) 
# shows 20 instead of 4 
print(matrix)
# shows the modified matrix
# [[1, 2, 3], [20, 5, 6], [7, 8, 9]]

# we can use nested loops to iterate over 
# all the items in the matrix

for row in matrix:
    for item in row:
        print(item)