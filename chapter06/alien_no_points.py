alien_0 = {'color': 'green', 'speed': 'slow'}
#key error will be thrown
# print(alien_0['points'])

#adding points key
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)