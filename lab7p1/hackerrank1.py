print("Hello , World")
###
n = int(input())
if n % 2 != 0: print("weird")
elif (n % 2 == 0) and (2 <= n <= 5): print("not weird")
elif (n % 2 == 0) and (6 <= n <= 20): print("weird")
elif (n % 2 == 0) and (n > 20): print("not weird")
###
a = int(input())
b = int(input())
print(a//b)
print(a/b)
###
print(a + b)
print(a - b)
print(a * b)
###
n1 = int(input())
for i in range(n1):
    print(i * i)
###
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("TRue")
else:
    print("FAlse")
###
x = int(input())
y = int(input())
z = int(input())
t = int(input())
list1 = [[i , j , k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != t]
print(list1)
###
max1 = 0
prev = 0
r = int(input())
for _ in range(r):
    i = int(input())
    if i > max1:
        prev = max1
        max1 = i
    elif i > prev:
        prev = i
print(prev)
###
st = int(input())
students = {}
for _ in range(st):
    name, m1, m2, m3 = input().split()
    students[name] = (int(m1) + int(m2) + int(m3)) / 3
print(students[input()])
