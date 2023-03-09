def print_formatted(number):
    # your code goes here
    l = []
    m = number
    while m > 1:
        r = m%2
        m = m//2
        l.append(str(r))
    l.reverse()
    s = "".join(l)
    w = len(s)
    indent1 = w
    indent2 = w + 1
    indent3 = w + 1
    indent4 = w + 1
    for i in range(1 , number+1):
        #Decimal
        result1 = i
        
        #Octal
        l = []
        m = i
        while m > 7:
            r = m%8
            m = m//8
            l.append(str(r))
        
        l.reverse()
        s = "".join(l)
        result2 = str(m) + str(s)
        x = len(result2)
        
        #Hexa
        l = []
        m = i
        n = i
        if i < number+1:
            if m == 10:
                result3 = 'A'
            if m == 11:
                result3 = 'B'
            if m == 12:
                result3 = 'C'
            if m == 13:
                result3 = 'D'
            if m == 14:
                result3 = 'E'
            if m == 15:
                result3 = 'F'
            while m > 15:
                r = m%16
                if r == 10:
                    r = 'A'
                if r == 11:
                    r = 'B'
                if r == 12:
                    r = 'C'
                if r == 13:
                    r = 'D'
                if r == 14:
                    r = 'E'
                if r == 15:
                    r = 'F'
                m = m//16
                l.append(str(r))
            if n < 10 or n > 15:
                l.reverse()
                s = "".join(l)
                result3 = str(m) + str(s)
                y = len(result3)
        
        #Binary
        l = []
        m = i
        while m > 1:
            r = m%2
            m = m//2
            l.append(str(r))
        l.reverse()
        s = "".join(l)
        result4 = str(m) + str(s)
        z = len(result4)
        if result1 > 9:
            indent1 = w - 1
        if x == 2:
            indent2 = w
        if x == 3:
            indent2 = w - 1
        if y == 2:
            indent3 = w
        if z == 2:
            indent4 = w
        if z == 3:
            indent4 = w - 1
        if z == 4:
            indent4 = w - 2
        if z == 5:
            indent4 = w - 3
        if z == 6:
            indent4 = w - 4
        if z == 7:
            indent4 = w - 5
        print(" "*indent1 + str(result1) + " "*indent2 + str(result2) + " "*indent3 + str(result3) + " "*indent4 + str(result4))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    
    
#OR


#n = int(input())
#w = len("{0:b}".format(n))
#for i in range(1,n+1):
#  print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))

#n inside ()of format is sended inside {}
#then integer n is converted into binary (since "b" is mentioned)
#then if n = 17 then {0:b}.format(n) = 10001 (binary form of 17) then w = len(10001) = 5
