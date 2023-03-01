n = int(input())
a = ['1','2','3','4','5','6','7','8','9']

for i in range(0 , n):
    line = input()
    char = line.split()
    char_1 = char[0]
    char_2 = char[1]

    try:
        if int(char_2) == 0:
            print("Error Code:","integer division or modulo by zero")
            continue
        div = int(char_1)/int(char_2)
        print(int(div))
    
    except:
        if char_1 in a:
            print("Error Code:","invalid literal for int() with base 10:","'"+char_2+"'")
        else:
            print("Error Code:","invalid literal for int() with base 10:","'"+char_1+"'")
