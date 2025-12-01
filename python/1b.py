# now just need to modify with another check... but also my lovely solution of modding 100 won't work 🥀
import math

pos = 50
count = 0

with open("C:/Users/saanv/Downloads/input.txt", "r") as lines:
  for line in lines:

    if int(line[1:]) > 99:
      count += math.floor(float(line[1:]) / 100) # so like it'll cycle if we take out the 100s
      count -= 1 # one of these checks is redundant because of the count += 1 later

    val = int(line[1:]) % 100
    if line[0] == "L":
      if pos - val < 0:
        pos = 100 - abs(pos - val)
        count += 1
      else:
        pos -= val
    else:
      if pos + val > 99:
        pos = 0 + abs(100 - (pos + val))
        count += 1
      else:
        pos += val

print(count)

# test 0: so unfortunately running the test case got 19, which is a lot more than 6, fixing some things gets 9, I think that the if pos == 0 at the end is redundant? yes this seems to work
# test 1: 7885, nooooooooooo its too high, removing check for vals over 100 I guess
# test 2: 2398, so we need the check but there's something wrong with it, I think it cycles one too many times
# test 3: 7877, I did not fix the cycling, it was too high
# test 4: 7420, now its locking me out for five minutes, but I know why I'm wrong - sometimes it would round up with the > 100 values cycling, need to use floor instead
# test 5: 6967, six seven!!! now I must wait 2m 27s to submit this. NOOOOOOOOOOOOOOOOOOOOOOOOOOO it's not right I'm going to crash out
# test 6: 6049, if this does not work I'm going to play zelda or do my chem work. it's incorrect, gg
