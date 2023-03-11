def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    a = []
    b = []
    n = sentence.split()
    n.reverse()
    
    for i in n:
        for j in i:
            if j.isupper():
                j = j.lower()
            else:
                j = j.upper()
            a.append(j)
        b.append("".join(a))
        a.clear()    
    return " ".join(b)

if __name__ == '__main__':
    sentence = input()
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
