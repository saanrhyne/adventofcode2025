# Doesn't seem too bad

sum = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as lines:
  listy = lines.readlines()

  for line in listy:
    listi = list(line.strip())

    val = max(listi)
    ind = listi.index(max(listi))

    if ind != len(listi) - 1:
      sublisti = listi[ind + 1:]
      val2 = max(sublisti)
      sum += int(val + val2)
    else:
      listi[listi.index(max(listi))] = '0'
      val2 = max(listi)
      sum += int(val2 + val)

print(sum)

# attempt 1: 17196, first try lets goo
