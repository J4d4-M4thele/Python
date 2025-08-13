from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line

# print(pi_string)
# print(len(pi_string))

# path = Path('pi_digits.txt')
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

# working with file contents
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

# print(f"PI: {pi_string}")
print(f"PI: {pi_string[:52]}...")
print(f"PI length: {len(pi_string)}")