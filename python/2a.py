# so just make a list from the input and separate it

with open("C:/Users/saanv/Downloads/input.txt", "r") as line:
  ids = line.readline().strip().split(",")

sum = 0

for id in ids:
  start = int(id[:id.find("-")])
  stop = int(id[id.find("-") + 1:])
  for i in range(start, stop + 1): # iterate through each number in the ranges
    if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
      sum += i

print(sum)

# test 1: 20223751392, answer is too low, the range wasn't inclusive of the stop number
# test 2: 20223751480, got it!
