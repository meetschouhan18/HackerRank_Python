#enter number of students then enter their name and marks in 3 subjects in a single line using space
#then print the avg marks of the student whose name is specified


e = {}
n = int(input("Enter N :- "))
for i in range (0 , n):
    a = input("Enter name :- ")
    b = a.find(' ')
    c = a.find(' ' , b+1)
    d = a.find(' ' , c+1)
    b1 = a[b+1:c]
    c1 = a[c+1:d]
    d1 = a[d+1:len(a)]
    f = float(b1) + float(c1) + float(d1)
    f = f/3
    f = '{:.2f}'.format(f)
    q = a[:b]
    e[q] = f
p = input('Enter name :- ')
print(e[p])