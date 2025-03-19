n_square = int(input())
i_square = 1
while i_square * i_square <= n_square:
    print(i_square * i_square)
    i_square += 1



n_div = int(input())
for i_div in range(2, n_div + 1):
    if n_div % i_div == 0:
        print(i_div)
        break



n_power = int(input())
pwr = 1
while pwr <= n_power:
    print(pwr, end=" ")
    pwr *= 2
print()



n_check = int(input())
pwr_check = 1
while pwr_check < n_check:
    pwr_check *= 2
print("YES" if pwr_check == n_check else "NO")



n_min_power = int(input())
k_min = 0
pwr_min = 1
while pwr_min < n_min_power:
    pwr_min *= 2
    k_min += 1
print(k_min)
