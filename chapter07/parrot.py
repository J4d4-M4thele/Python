# message = input("Tell me something, and I'll repeat it back to you: ")
# print(message)

# letting user quit when they want to 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

# while message != 'quit':
#     message = input(prompt)
#     print(message)

# using a flag
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message) 