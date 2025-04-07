# zero division error
print(5/0)

# using try-catch block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")