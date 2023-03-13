#using list print 2nd highest value


n = int(input('Enter no. of participants :- '))
a = input('Enter score :- ')
d = []
r = []
c = a.split()
for i in c:
    d.append(int(i))
    r.append(int(i))
e = max(r)
for i in r:
    if i == e:
        d.remove(i)
try:
    print(max(d))
except:
    print('Error')