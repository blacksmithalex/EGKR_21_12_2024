def f(a, b):
    if a < b or a == 24:
        return 0
    elif a == b:
        return 1
    else:
        return f(a - 1, b) + f(a - 6, b) + f(a // 2, b)

print(f(34, 29) * f(29, 19) * f(19, 6))