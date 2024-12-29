def f(x, y, A):
    return (x - 3 * y < A) or (y > 400) or (x > 56)

for A in range(100):
    flag = True
    for x in range(1, 600):
        for y in range(1, 600):
            if not f(x, y, A):
                flag = False
    if flag:
        print(A)
