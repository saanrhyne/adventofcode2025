# I think I accidentally solved this one when trying to do part 1

with open("C:/Users/saanv/Downloads/input.txt", "r") as line:
  ids = line.readline().strip().split(",")

sum = 0

for id in ids:
  start = int(id[:id.find("-")])
  stop = int(id[id.find("-") + 1:])
  for i in range(start, stop + 1): # iterate through each number in the ranges
    for j in range (1, len(str(i))//2 + 1): # test each possible chunk size
      if str(i) == str(i)[0:j] * (len(str(i))//j):
        sum += i
        break # prevent duplicates

print(sum)

# test 1: 30260171216, took a long time but we ball, NO WAY I GOT IT FIRST TRY
