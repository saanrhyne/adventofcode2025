# Ok so basically my goats said to just change this up

sum = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as file:
  lines = file.readlines()

  for line in lines:
    listy = list(line.strip())
    vals = []
    
    while len(vals) < 12:

      end = len(listy) - (11 - len(vals))

      vals.append(max(listy[:end]))
      listy = listy[listy.index(vals[-1]) + 1:]

    sum += int("".join(vals))
    

print(sum)

# answer: 171039099596062, I can't believe I got it this was so simple and I was being dumb
