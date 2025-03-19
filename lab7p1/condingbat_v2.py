print("Task: hello_name")
def hello_name(name):
    return "Hello " + name + "!"

print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))


print("Task: make_abba")
def make_abba(a, b):
    return a + b + b + a

print(make_abba('Hi', 'Bye'))
print(make_abba('Yo', 'Alice'))
print(make_abba('What', 'Up'))


print("Task: make_tags")
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))


print("Task: make_out_word")
def make_out_word(out, word):
    return out[:2] + word + out[2:]

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))


print("Task: extra_end")
def extra_end(string):
    return string[-2:] * 3

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))


print("Task: first_two")
def first_two(string):
    return string[:2]

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))


print("Task: first_last6")
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))


print("Task: same_first_last")
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))


print("Task: make_pi")
def make_pi():
    return [3, 1, 4]

print(make_pi())


print("Task: common_end")
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))


print("Task: sum3")
def sum3(nums):
    return sum(nums)

print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))


print("Task: rotate_left3")
def rotate_left3(nums):
    return nums[1:] + nums[:1]

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))
