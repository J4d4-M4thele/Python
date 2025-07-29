#modifying list elements
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

#appending elements to end of the list
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

#inserting elements into list
# motorcycles.insert(1, 'ducati')
# print(motorcycles)

#removing elements from list
# del motorcycles[0]
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

#popping items from any position
# popped_motorcycle = motorcycles.pop() #removes from the back by default
# print(motorcycles)
# print(popped_motorcycle)

#removing items by value
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

# #removing an an item by value
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")

#index errors
# ---out of range error---
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])

#---printing last item in list---
print(motorcycles[-1])

motorcycles = []
print(motorcycles[-1])
