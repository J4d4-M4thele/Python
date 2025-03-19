dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#throws an error
dimensions[0] = 250

#looping through all values in a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)    