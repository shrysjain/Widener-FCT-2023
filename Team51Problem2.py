n = int(input())
if str(n*n)[-len(str(n)):] == str(n): print("automorphic")
else: print("not automorphic")