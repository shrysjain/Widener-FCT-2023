m = []
while True:
  temp = input()
  if temp == ".":
    break
  m.append(temp)

d= {}
for i in m[0].split(" "):
  d[i] = {}

for i in m[0].split(" "):
  for j in m[0].split(" "):
    d[i][j] = 0

hold = m[0].split(" ")
m.pop(0)

for i in m:
  temp = i.split(" ")
  temp1 = hold.copy()
  for j in range(len(temp)):
    temp1.remove(temp[j])
    for k in temp1:
      d[temp[j]][k] += 1

n1 = 0
ni = ""
n2 = 0
flag = False
f2 = False
for i in d.keys():
  temp1 = hold.copy()
  temp1.remove(i)
  flag = False
  for j in temp1:
    if flag:
      continue
    if d[i][j] <= d[j][i]:
      flag = True
  if flag:
    continue
  n1 = i
  print(n1)
  f2 = True
  break

if not(f2):
  print(0)