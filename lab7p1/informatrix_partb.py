a1 = int(input())
b1 = int(input())
print(max(a1, b1))

year = int(input())
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):print("YES")
else:print("NO")

correct = int(input())
student = int(input())
print("YES" if correct == student else "NO")

x = int(input())
print(1 if x > 0 else -1 if x < 0 else 0)

a = int(input())
b = int(input())
print(1 if a > b else 2 if b > a else 0)
