k = int(input())
line = input()
lin = line.split()
try:
   waste = int(lin[len(lin)-1])
   r = [int(i) for i in lin]
except:
   lin.reverse()
   waste = lin.pop(0)
   lin.reverse()
   r = [int(i) for i in lin]
dic = {}
for i in r:
   dic[i] = dic.get(i , 0) + 1
for key,value in dic.items():
   if value < k:
      ans = key
print(ans)