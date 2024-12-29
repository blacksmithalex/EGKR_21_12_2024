from sys import setrecursionlimit
setrecursionlimit(20000)
def F(n):
    if n < 5:
        return n
    return 2 * n * F(n - 4)

res = (F(13766) - 9 * F(13762)) / F(13758)
print(res)