c = 0
n = input().lower()
vowel = "aeiou"
for i in range(len(n)-1):
  if n[i] in vowel and n[i+1] in vowel: c += 1
print(c)