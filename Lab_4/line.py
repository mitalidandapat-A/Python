# Accept multiple lines of input
print("Enter multiple lines of text. Press Enter on an empty line to finish.")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# Process each line to make all characters uppercase
capitalized_lines = [line.upper() for line in lines]

# Print each capitalized line
for line in capitalized_lines:
    print(line)
