first_set = set()
second_set = set()
n = int(input())
first_line = input()
first_num = first_line.split()
for i in first_num:
    first_set.add(int(i))
m = int(input())
second_line = input()
second_num = second_line.split()
for i in second_num:
    second_set.add(int(i))
total = first_set.symmetric_difference(second_set)
print(len(total))
