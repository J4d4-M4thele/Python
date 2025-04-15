from pathlib import Path

path = Path('alice.txt')
# contents = path.read_text(encoding='utf-8')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} doesn't exist.") 
else:
    #Count approximate no. of words in file
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")    