from pathlib import Path

# reading a text file 
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

# accessing a file's lines
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

# working with file contents
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"PI: {pi_string}")
print(f"PI length: {len(pi_string)}") 