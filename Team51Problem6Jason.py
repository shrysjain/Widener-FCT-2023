p, d = [int(i) for i in input().split(" ")]

s = [int(i) for i in input().split(" ")]

c = []

for i in range(d):
  ns = []
  for j in s:
    ns.append(j + i)
  ns.append(9999999999)
  ws = []
  ps = []
  ms = []
  cday = d
  cst = 0
  for j in ns:
    if j <= cday: pass
    if j > cday:
      if j >= cday + d:
        ms.append(cst)
      else:
        cst += 1
        cday += d
  ps.append(max(ms)-1)
  ws.append(i)

w = max(ps)
print(w)
a = []

for i in range(len(ps)):
  if ps[i] == w:
    a.append(str(ws[i]))

print(" ".join(a))