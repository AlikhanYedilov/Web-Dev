import math
a = int(input())
b = int(input())
print(math.sqrt(a**2 + b**2))

n = int(input())
print(f"The next number for the number {n} is {n + 1}.")
print(f"The previous number for the number {n} is {n - 1}.")

N, K = map(int, input().split())
print(K // N)

N1, K1 = map(int, input().split())
print(K1 % N1)

v, t = map(int, input().split())
print((v * t) % 109)
