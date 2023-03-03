line = input()
n = int(input())
c = 0
a = 0
line = line + " "
b = str()
words = []
for i in line:
    a = a + 1
    if c != n:
        b = b + i
        c = c + 1
    else:
        c = 1
        words.append(b)
        b = i
p = len(line) - a
if n > p:
    words.append(b)
if (len(line) - 1)%n == 0:
    words.remove(" ")
    print(words)
else:
    last_ele = words.pop(n-1)
    last_ele = last_ele[:len(last_ele)-1]
    words.append(last_ele)
    print(words)
b = str()
final = []
for i in words:
    for j in i:
        if j not in b:
            b = b + j
    final.append(b)
    b = str()
print("\n".join(final))    