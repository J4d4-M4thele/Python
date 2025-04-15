# zero division error
# print(5/0)

# using try-catch block
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# # using exceptions
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    # else block
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

    # answer = int(first_number) / int(second_number)
    # print(answer)

