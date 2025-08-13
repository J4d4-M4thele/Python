from pathlib import Path

# reading a text file 
path = Path('pi_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

# accessing a file's lines
contents = path.read_text()
# print(contents)
lines = contents.splitlines()
for line in lines:
    print(line)
 