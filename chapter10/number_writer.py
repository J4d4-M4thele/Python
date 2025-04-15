from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
# convert data to JSON-format
contents = json.dumps(numbers)
# write contents to file
path.write_text(contents)