import math

n = input().split()
og = input().split()
solutions = []
biggest = 0

for i in range(int(n[1])):
  count = 0
  done = False
  for j in og:

    
    if math.floor(int(j) + int(i) / int(n[1])) != count and not done:
      print(math.floor(int(j) + int(i) / int(n[1])))
      print("count", count)
      if count == biggest:
        solutions.append(int(i))
      elif count > biggest:
        solutions = [int(i)]
        biggest = count
      done = True
    count += 1

print(biggest)

st = ""
for i in solutions:
  st += str(i) + " "

print(st)
