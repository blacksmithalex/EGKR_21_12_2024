def f(x, p):
    if x >= 132 and p == 3:
        return True
    if x < 132 and p == 3:
        return False
    elif x >= 132:
        return False
    else:
        if p % 2 == 0:
            return f(x + 3, p + 1) or f(x + 6, p + 1) or f(x * 3, p + 1)
        else:
            return f(x + 3, p + 1) and f(x + 6, p + 1) and f(x * 3, p + 1)

for S in range(1, 131 + 1):
    if f(S, 1):
        print(S)