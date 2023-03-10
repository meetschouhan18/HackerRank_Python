#Text Wrap
#break string at a given index everytime and print the sub-string

string = input("")
width = int(input(""))
c = 0
l = []

while c < len(string):
    s = string[c:c + width]
    c = c + width
    l.append(s + '\n')

st = "".join(l)
print(st)
