# Seems pretty easy ngl, just make a grid

count = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as file:
  lines = file.readlines()

  for i in range(len(lines)):
    lines[i] = list(lines[i].strip())
    lines[i].append("")
    lines[i].insert(0, "")
  
  temp = []
  for i in range(len(lines[0])):
    temp.append("")
  lines.append(temp)
  lines.insert(0, temp)

  for i in range(1, len(lines)):
    for j in range(1, len(lines[i])):
      if lines[i][j] == '@':
        r = 0

        if lines[i][j + 1] == '@': r += 1
        if lines[i][j - 1] == '@': r += 1
        if lines[i + 1][j] == '@': r += 1
        if lines[i + 1][j + 1] == '@': r += 1
        if lines[i + 1][j - 1] == '@': r += 1
        if lines[i - 1][j] == '@': r += 1
        if lines[i - 1][j - 1] == '@': r += 1
        if lines[i - 1][j + 1] == '@': r += 1

        if r < 4:
          count += 1

print(count)

# Attempt 1: 1451, correct
