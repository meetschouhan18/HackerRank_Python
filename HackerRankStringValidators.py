#String Validators
#checking every element of string 


s = input("Enter String :- ")
alnum1 = 0
alpha1 = 0
digit1 = 0
lower1 = 0
upper1 = 0
for i in s:
    if i.isalnum():
        alnum1 = 1
    if i.isalpha():
        alpha1 = 1
    if i.isdigit():
        digit1 = 1
    if i.islower():
        lower1 = 1
    if i.isupper():
        upper1 = 1
if alnum1 == 1:
    print("True")
else:
    print("False")
if alpha1 == 1:
    print("True")
else:
    print("False")
if digit1 == 1:
    print("True")
else:
    print("False")
if lower1 == 1:
    print("True")
else:
    print("False")
if upper1 == 1:
    print("True")
else:
    print("False")