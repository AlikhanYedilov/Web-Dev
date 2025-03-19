print("Task: sleep_in")
def sleep_in(weekday, vacation):
    return not weekday or vacation

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))


print("Task: monkey_trouble")
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))


print("Task: sum_double")
def sum_double(a, b):
    return 2 * (a + b) if a == b else a + b

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))


print("Task: diff21")
def diff21(n):
    return 2 * abs(n - 21) if n > 21 else abs(n - 21)

print(diff21(19))
print(diff21(10))
print(diff21(21))


print("Task: parrot_trouble")
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))


print("Task: makes10")
def makes10(a, b):
    return a == 10 or b == 10 or (a + b == 10)

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))


print("Task: string_times")
def string_times(string, n):
    return string * n

print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))


print("Task: front_times")
def front_times(string, n):
    front = string[:3]
    return front * n

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))


print("Task: string_bits")
def string_bits(string):
    return string[::2]

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))


print("Task: string_splosion")
def string_splosion(string):
    result = ""
    for i in range(len(string) + 1):
        result += string[:i]
    return result

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))


print("Task: last2")
def last2(string):
    if len(string) < 2:
        return 0
    last_2 = string[-2:]
    count = 0
    for i in range(len(string) - 2):
        if string[i:i+2] == last_2:
            count += 1
    return count

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))


print("Task: array_count9")
def array_count9(nums):
    return nums.count(9)

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))
