# dictionary of similar objects
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
# 'erin': 'java'
}

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# looping through all key-value pairs
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# # looping through all keys (default behaviour of loop)
# for name in favorite_languages: 
#     print(name.title())

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# keys in a particular order
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

#looping through all values 
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# #lists inside of dictionaries
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")