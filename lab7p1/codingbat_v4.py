print("Task: double_char")
def double_char(s):
    return ''.join(c * 2 for c in s)

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))


print("Task: count_hi")
def count_hi(s):
    return s.count("hi")

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))


print("Task: cat_dog")
def cat_dog(s):
    return s.count("cat") == s.count("dog")

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))


print("Task: count_code")
import re
def count_code(s):
    return len(re.findall(r'co.e', s))

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))


print("Task: end_other")
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))


print("Task: xyz_there")
def xyz_there(s):
    return 'xyz' in s.replace('.xyz', '')

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))


print("Task: count_evens")
def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))


print("Task: big_diff")
def big_diff(nums):
    return max(nums) - min(nums)

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))


print("Task: centered_average")
def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))


print("Task: sum13")
def sum13(nums):
    total = 0
    skip = False
    for num in nums:
        if num == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += num
    return total

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))


print("Task: sum67")
def sum67(nums):
    total = 0
    ignore = False
    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total += num
    return total

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))


print("Task: has22")
def has22(nums):
    return any(nums[i] == 2 and nums[i + 1] == 2 for i in range(len(nums) - 1))

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
