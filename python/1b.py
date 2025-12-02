# This is the bane of my existence btw 

pos = 50
count = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as lines:
  for line in lines:
    val = int(line[1:])
    if line[0] == "R":
      for i in range(val):
        pos += 1
        if pos == 100:
          pos = 0
          count += 1
    else:
      for i in range(val):
        pos -= 1
        if pos == -1:
          pos = 99
        if pos == 0:
          count += 1

print(count)

# attempt 1: 7004, it's not right, I think I was adding 1 to the range but that's actually not right
# attempt 2: 6932, I've never got that value before, but I still have to wait 3 mins 3 seconds, IT'S RIGHT LETS GOOOOOOOOO
