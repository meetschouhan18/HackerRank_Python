#we have to count no. of times the sub string is present in the srring

st = input("Enter String :- ")
s = input("Enter another string(subpart of string inputted above) :- ")
length = len(s)
words = []
ans = 0
for n in range(0, len(st)):
  word = st[n:n+length]
  words.append(word)
for i in words:
  if i == s:
    ans += 1
print(ans)

#Done