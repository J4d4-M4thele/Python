my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

#this doesn't work
friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice-cream')

print("My friend's favourite foods are:")
print(friends_foods)