# so basically a for loop and you go - or + but then loop back around

pos = 50 # where the dial is
count = 0 # if 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as lines:
  for line in lines:
    val = int(line[1:]) % 100 # super tuff real line value
    if line[0] == "L":
      if pos - val < 0:
        pos = 100 - abs(pos - val)
      else:
        pos -= val
    else:
      if pos + val > 99:
        pos = 0 + abs(100 - (pos + val))
      else:
        pos += val
    if pos == 0:
      count += 1

print(count)

# answer 1: 16, but not right
# answer 2: 307, fixed logic on rotating right, but still too low?? the test case works tho so idk what i got wrong, it has to be smth with the nuance of 99 or 0
# answer 3: 1172, now I accounted for line values being above 100 thanks to the subreddit, it's correct yay!!!
