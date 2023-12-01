m = []
while True:
  temp = input()
  if temp == ".":
    break
  m.append(temp)

d= {}
for i in m[0].split(" "):
  d[i] = 0

m.pop(0)

for i in m:
  temp = i.split(" ")
  for j in range(len(temp)):
    d[temp[j]] += len(d.keys()) - 1 - j

n1 = 0
ni = ""
n2 = 0
for i in d.keys():
  if d[i] > n1:
    n1 = d[i]
    ni = i
    
    
del d[ni]


for i in d.keys():
  if d[i] > n2:
    n2 = d[i]
 

if n1 == n2:
  print(0)
else:
  print(ni)

