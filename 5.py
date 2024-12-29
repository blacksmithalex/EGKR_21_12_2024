def to3(N):
    res = ''
    while N != 0:
        res += str(N % 3)
        N //= 3
    return res[::-1]
def f(N):
    N3 = to3(N)
    if N % 3 == 0:
        N3 += N3[-2:]
    else:
        s = sum([int(x) for x in N3])
        N3 += to3(s)
    return int(N3, 3)

res = []
for N in range(1, 200):
    R = f(N)
    if R > 220 and R % 2 == 0:
        res.append(R)
print(min(res))
