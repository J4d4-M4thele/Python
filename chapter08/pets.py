# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("tortoise", "junior")    
# # multiple functions
# describe_pet("dog", "tyson")

# # keyboard arguments
# describe_pet(animal_type='tortoise', pet_name='junior')
# describe_pet(animal_type='dog', pet_name='tyson')

# # default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='willie', animal_type="lizard")

# # equivalent function calls
# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# # argument errors
describe_pet()