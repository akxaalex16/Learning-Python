coordinates =(1,2,3)
# this method below is not the best
coordinates[0] * coordinates[1] * coordinates[2]
# instead we want to store the coordinate values in a seperate variable
x= coordinates[0]
y= coordinates[1]
z= coordinates[2]

# easier way of doing it; unpacking
# have the vairiables equal to the tuple
x, y, z = coordinates

print(x)
print(y)
print(z)

# we can do this method of unpacking for lists too