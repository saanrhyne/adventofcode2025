# Why does this seem easy

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()

lines = [line.strip() for line in lines]

area = 0

for i in lines:
  for j in lines:
    area = max(area, (abs(int(i[:i.index(",")]) - int(j[:j.index(",")])) + 1) * (abs(int(i[i.index(",") + 1:]) - int(j[j.index(",") + 1:])) + 1))

print(area)

# attempt 1: 4749672288, why was it so easy today?? The last two days have been super hard.
