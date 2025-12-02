# so just make a list from the input and separate it

with open("C:/Users/saanv/Downloads/input.txt", "r") as line:
  ids = line.readline().strip().split(",")

sum = 0
dupes = []

for id in ids:
  start = int(id[:id.find("-")])
  stop = int(id[id.find("-") + 1:])
  for i in range(start, stop): # iterate through each number in the ranges
    if i not in dupes:
      for j in range(1, len(str(i))//2): # create the chunk size
        if i not in dupes:
          for k in range(1, len(str(i))//2): # iterate through each chunk
            if str(i)[k:k+j] == str(i)[k+j:k+j+j] and str(i)[k:k+j] != str(i)[k+j+j:k+j+j+j] and i not in dupes:
              dupes.append(i)
              sum += i

print(dupes)
#print(sum)
