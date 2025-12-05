# Wow this one seems easy

count = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()
  ranges = []
  ingredients = []

  for line in lines:
    line = line.strip()
    if line == "":
      pass
    elif "-" not in line:
      ingredients.append(line)
    else:
      ranges.append(line)
  
  for i in ingredients:
    for r in ranges:
      start = int(r[:r.index("-")])
      end = int(r[r.index("-") + 1:])
      if int(i) >= start and int(i) <= end:
        count += 1
        break
    

print(count)

# attempt 1: 761, I feel like I'm getting better at these!
