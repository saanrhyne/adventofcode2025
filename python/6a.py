# Stayed up until midnight for this one, it better be good

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()

  count = 0
  overall = []

  for line in lines:
    line = line.strip()
    working = line.split(" ")
    while ("") in working:
      working.remove("")
    overall.append(working)
  

  for i in range(len(overall[0])): # columns
    sum = 1
    for j in range(len(overall) - 1): # rows
      if overall[-1][i] == "+":
        sum += int(overall[j][i])
      else:
        sum *= int(overall[j][i])
  
    if overall[-1][i] == "+": sum -= 1

    count += sum
    

print(count)

# attempt 1: 5782351442566, YAY I GOT IT
