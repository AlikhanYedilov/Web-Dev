#63
n_63 = int(input())
arr_63 = list(map(int, input().split()))
for i in range(n_63):
    if i % 2 == 0:
        print(arr_63[i], end=" ")
print()

#64
n_64 = int(input())
arr_64 = list(map(int, input().split()))
for num in arr_64:
    if num % 2 == 0:
        print(num, end=" ")
print()

#65
n_65 = int(input())
arr_65 = list(map(int, input().split()))
count_65 = 0
for num in arr_65:
    if num > 0:
        count_65 += 1
print(count_65)

#66
n_66 = int(input())
arr_66 = list(map(int, input().split()))
count_66 = 0
for i in range(1, n_66):
    if arr_66[i] > arr_66[i - 1]:
        count_66 += 1
print(count_66)

#67
n_67 = int(input())
arr_67 = list(map(int, input().split()))
found_67 = False
for i in range(1, n_67):
    if arr_67[i] > 0 and arr_67[i - 1] > 0 or arr_67[i] < 0 and arr_67[i - 1] < 0:
        found_67 = True
if found_67:
    print("YES")
else:
    print("NO")

#68
n_68 = int(input())
arr_68 = list(map(int, input().split()))
count_68 = 0
for i in range(1, n_68 - 1):
    if arr_68[i] > arr_68[i - 1] and arr_68[i] > arr_68[i + 1]:
        count_68 += 1
print(count_68)

#69
n_69 = int(input())
arr_69 = list(map(int, input().split()))
for i in range(n_69 // 2):
    arr_69[i], arr_69[n_69 - i - 1] = arr_69[n_69 - i - 1], arr_69[i]
print(*arr_69)