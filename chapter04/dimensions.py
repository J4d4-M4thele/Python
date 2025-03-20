dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# for d in dimensions:
#     print(d)

#throws an error
#dimensions[0] = 250 #values can't be changed

# #looping through all values in a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)    