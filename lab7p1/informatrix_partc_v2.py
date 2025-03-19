num_x = int(input())
for divisor in range(2, num_x + 1):
    if num_x % divisor == 0:
        print(divisor)
        break

div_x = int(input())
for div_num in range(1, div_x + 1):
    if div_x % div_num == 0:
        print(div_num, end=" ")
print()


count_x = int(input())
count_divisors = 0
for count_num in range(1, int(count_x ** 0.5) + 1):
    if count_x % count_num == 0:
        count_divisors += 1
        if count_num != count_x // count_num:
            count_divisors += 1
print(count_divisors)


sum_total = 0
for _ in range(100):
    sum_total += int(input())
print(sum_total)


sum_n = int(input())
sum_result = 0
for _ in range(sum_n):
    sum_result += int(input())
print(sum_result)


binary_input = input()
print(int(binary_input, 2))


n_count = int(input())
zero_count = 0
for _ in range(n_count):
    if int(input()) == 0:
        zero_count += 1
print(zero_count)
