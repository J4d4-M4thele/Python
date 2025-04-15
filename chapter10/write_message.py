from pathlib import Path

# writing multiple lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
# path.write_text("I love programming.")

path.write_text(contents)