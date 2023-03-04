#Mutation
#inserting element at desired location in a string

i = input("Enter String :- ")
j = input("Enter position and character you want to insert :- ")
a = j.split()
pos = int(a[0])
char = str(a[1])
string = i[:pos] + char + i[pos+1:]
print(string)