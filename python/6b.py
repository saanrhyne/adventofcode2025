# Highkey forgot about AoC for a few days

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()

  count = 0
  listy = []

  for line in lines:
    line = list(line)
    listy.append(line)
  
  # parsing operators
  operators = listy[-1]
  listy.pop(-1)
  operators = [i for i in operators if i.strip()]

  
  newlines = []
  for i in range(len(listy[0])):
    working = ""
    for j in range(len(listy)):
      working += listy[j][i]
    newlines.append(working)
  
  op = 0
  sum = 1

  for i in newlines:
    if i.strip() == "":
      if operators[op] == "+":
        count += sum - 1
      else:
        count += sum
      op += 1
      sum = 1
    else:
      if operators[op] == "+":
        sum += int(i.strip())
      else:
        sum *= int(i.strip())
    
  print(count)

# attempt 1: 10194584711842, it's correct yay!
