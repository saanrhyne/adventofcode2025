# numpy euclidean distance

import numpy

with open("C:/Users/saanv/Downloads/input.txt", "r") as input:
  lines = input.readlines()

lines = [line.strip().split(",") for line in lines]

pairs = []
distances = []

for i in range(len(lines)):
  for j in range(i + 1, len(lines)):

    a = numpy.array([int(x) for x in lines[i]])
    b = numpy.array([int(x) for x in lines[j]])

    distances.append(float(numpy.linalg.norm(a - b)))
    pairs.append([lines[i], lines[j]])

top = []

for i in range(10):
  ind = distances.index(min(distances))
  top.append(pairs[ind])
  pairs.pop(ind)
  distances.pop(ind)

circuits = []

for i in range(len(top)):
  for j in range(i, len(top)):
    if top[i][0] in top[j]:
      if top[i][0] == top[j][0]:
        circuits.append([top[i][0], top[i][1], top[j][1]])
      else:
        circuits.append([top[i][0], top[i][1], top[j][0]])
