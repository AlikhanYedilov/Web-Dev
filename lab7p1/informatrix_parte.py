#306
def min_306(a, b, c, d):
    return min(a, b, c, d)

a_306, b_306, c_306, d_306 = map(int, input().split())
print(min_306(a_306, b_306, c_306, d_306))

#307
def power_307(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

a_307, n_307 = map(float, input().split())
n_307 = int(n_307)
print(power_307(a_307, n_307))

#308
def xor_308(x, y):
    return x != y

x_308, y_308 = map(int, input().split())
print(int(xor_308(x_308, y_308)))