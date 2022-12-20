############################################
#                  TASK 1
############################################
lst = [1, 2, 3, 4, 5, 6, 7, "ofek", False]
ele = 4
print(ele in lst)

############################################
#                  TASK 2
############################################
l = ['Ben', 'Noa', 'Banana']
for word in l:
    if 'a' in word:
        print(word)
        break

############################################
#                  TASK 3
############################################
line = input()
i = int(input())
print(line.split(" ")[i - 1])

############################################
#                  TASK 4
############################################
l = [22, 5, 4, 8, 2, 10]
min = l[0]
for num in l:
    if num < min:
        min = num
print(min)

############################################
#                  TASK 5
############################################
n1 = int(input())
n2 = int(input())
s = 0
for i in range(min(n1, n2) + 1, max(n1, n2)):
    if i % 2 != 0:
        s += i
print(s)

############################################
#                  TASK 6
############################################
l1 = [1, 2, 3]
l2 = [5, 6, 7, 8, 9, 0]
new_lst = []
min_length = min(len(l1), len(l2))

for i in range(min_length):
    new_lst.append(l1[i])
    new_lst.append(l2[i])

new_lst += l1[min_length:] + l2[min_length:]
print(new_lst)

############################################
#                  Challenge
############################################
lst = []
n = int(input())
while n >= 0:
    lst.append(n)
    n = int(input())

if n % 2 ==0:
    print(lst[::2])
else:
    print(sorted(lst[1::2]))



