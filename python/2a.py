# so just make a list from the input and separate it

with open("C:/Users/saanv/Downloads/input.txt", "r") as line:
  ids = line.readline().strip().split(",")

for id in ids:
  start = int(id[:id.find("-")])
  stop = int(id[id.find("-") + 1:])
  for i in range(start, stop):
    for j in range(len(i)):
      

print(ids)
