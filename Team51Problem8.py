n = input().split(" ")

w = n[0][::-1] # word
t = list(n[1][::-1]) # target
t1 = "".join(t.copy()) 
e = ""

for i in w:
  if i in t[1:] and i != t[0]:
    print("NO")
    break
  if i == t[0]:
    e += i
    t.pop(0)
    if e == t1:
      print("YES")
      break

# extra = ""
# word = n[1]
# for i in n[0][::-1]:
#   if i == word[-1] and :
