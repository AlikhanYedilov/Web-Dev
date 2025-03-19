start_num, end_num = map(int, input().split())
for num_even in range(start_num, end_num + 1):
    if num_even % 2 == 0:
        print(num_even, end=" ")
print()


low_bound, up_bound, mod_rem, div_val = map(int, input().split())
for num_div in range(low_bound, up_bound + 1):
    if num_div % div_val == mod_rem:
        print(num_div, end=" ")
print()


square_min, square_max = map(int, input().split())
for square_num in range(square_min, square_max + 1):
    if int(square_num ** 0.5) ** 2 == square_num:
        print(square_num, end=" ")
print()


number_string, digit_count = input().split()
print(number_string.count(digit_count))


sum_number = input()
sum_result = 0
for digit_sum in sum_number:
    sum_result += int(digit_sum)
print(sum_result)


reverse_input = input()
print(int(reverse_input[::-1]))