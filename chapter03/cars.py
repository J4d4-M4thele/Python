#sort() to sort list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#or the other way
cars.sort(reverse=True)
print(cars)

#sorted() to sort list temporarily
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#printing list in reverse order
cars.reverse()
print(cars)

#finding list length
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)