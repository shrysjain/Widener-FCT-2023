import math

n = int(input())
L = [int(i) for i in input().split()]
c = 0
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      if math.gcd(L[i], L[j], L[k]) == 1:
        c += 1
print(c)