import re

# Define the file path
file_path = "input.txt"

# Define the varibles
count = 0

# RegEx to find the pattern mul(x, y)
pattern = r"mul\(\s*([+-]?\d*\.?\d+)\s*,\s*([+-]?\d*\.?\d+)\s*\)"

# RegEx to remove content between "don't()" and "do()" with ""
removepattern = r"don't\(\).*?do\(\)"

# Open and read the file
with open(file_path, "r") as file:
    content = file.read()

# Replace characters between don't() and do() with an empty string
updated_content = re.sub(removepattern, "", content, flags=re.DOTALL)

#print(updated_content)

# Find all matches
matches = re.findall(pattern, updated_content)

# Print results
if matches:
    for match in matches:
        x, y = match
        count = count + int (x) * int (y)
else:
    print("No occurrences of mul(x, y) found.")

print(f"Total: {count}")
