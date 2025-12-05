# Again this doesn't seem bad, pretty mathy

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()

  count = 0
  ranges = []
  fresh = []

  for line in lines:
    line = line.strip()
    if "-" in line:
      start, end = map(int, line.split("-"))
      ranges.append((start, end))
  
  ranges.sort()
  last = (0, 0)

  for s, e in ranges:
    if (s, e) != last and last[1] < s:
      last = (s, e)
      count += (e - s) + 1
    elif last[1] >= s and last[1] < e:
      s = last[1] + 1
      last = (s, e)
      count += (e - s) + 1

print(count)

# attempt 1: 345755049374932, I don't think this is gonna be right though, NO WAY IT'S RIGHT
