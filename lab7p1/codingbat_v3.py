print("Task: cigar_party")
def cigar_party(cigars, is_weekend):
    return cigars >= 40 if is_weekend else 40 <= cigars <= 60

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))


print("Task: date_fashion")
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))


print("Task: squirrel_play")
def squirrel_play(temp, is_summer):
    return 60 <= temp <= (100 if is_summer else 90)

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))


print("Task: caught_speeding")
def caught_speeding(speed, is_birthday):
    allowance = 5 if is_birthday else 0
    if speed <= 60 + allowance:
        return 0
    if speed <= 80 + allowance:
        return 1
    return 2

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))


print("Task: sorta_sum")
def sorta_sum(a, b):
    return 20 if 10 <= a + b <= 19 else a + b

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))


print("Task: make_bricks")
def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))


print("Task: lone_sum")
def lone_sum(a, b, c):
    return sum(x for x in (a, b, c) if (a, b, c).count(x) == 1)

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))


print("Task: lucky_sum")
def lucky_sum(a, b, c):
    for n in (a, b, c):
        if n == 13:
            return sum(x for x in (a, b, c) if x != 13)
    return a + b + c

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))


print("Task: no_teen_sum")
def fix_teen(n):
    return 0 if 13 <= n <= 19 and n not in (15, 16) else n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


print("Task: round_sum")
def round10(num):
    return num + (10 - num % 10) if num % 10 >= 5 else num - num % 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))


print("Task: close_far")
def close_far(a, b, c):
    close = abs(a - b) <= 1 or abs(a - c) <= 1
    far = abs(a - b) >= 2 and abs(b - c) >= 2 or abs(a - c) >= 2 and abs(b - c) >= 2
    return close and far

print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
