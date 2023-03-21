def average(array):
    # your code goes here
    
    total = set()
    sum = 0
    num = array
    for i in num:
        total.add(int(i))
    
    for i in total:
        sum = sum + int(i)
    
    avg = sum/len(total)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    result = average(arr)
    print(result)
