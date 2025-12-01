# yeah idk
import math

pos = 50
count = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as lines:
  for line in lines:
    val = int(line[1:])
    if line[0] == "R":
      if pos + val % 100 > 99: count += 1
      count += val // 100
      pos = (pos + val) % 100
    else:
      if val % 100 > 0 and val % 100 > pos: count += 1
      count += val // 100
      pos = (pos - val) % 100

print(count)

# test 1: 7426, not right, now I have to wait 10 whole minutes
# test 2: 6967, but I know that's not right from before
