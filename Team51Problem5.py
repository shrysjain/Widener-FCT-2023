goal = int(input())
M = int(input())
L = int(input())
maxc = goal // L+3
maxm = goal // M+3
close = [[goal,0,0]]
for i in range(maxc):
  for j in range(maxm):
    check = abs(i * L + j * M - goal)
    if check < close[0][0]:
      close = [[check, i, j]]
    elif check == close[0][0]:
      close.append([check, i, j])

newlist = []
for i in close:
  if i not in newlist:
    newlist.append(i)

for i in newlist:
  print(i[2], i[1])

