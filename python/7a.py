# This doesn't seem too bad, just mathy

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()

lines = [line.strip() for line in lines]
 
lines = [list(row) for row in zip(*lines)][::-1] # copied from Gemini when I googled "rotate a list in a list in python"
lines = ["".join(line) for line in lines]

count = 0

for i in range(len(lines)):
  for j in range(len(lines[i])):
    if "^" in lines[i][:j]:
      top = lines[i][:j]
      top = top.index("^")
      print(top)
    print(lines[i])
    #if lines[i][j] == "^" and ("^" not in lines[i][:j]):
    #  count += 1

# print(count)
