file = open('17_19249.txt')
a = [int(x) for x in file]
file.close()

m43 = -float('inf')
for x in a:
    if abs(x) % 100 == 43 and len(str(abs(x))) == 5 and x > m43:
        m43 = x

count, sm = 0, float('inf')
for i in range(len(a) - 2):
    rule1 = abs(a[i]) % 100 == 43 and len(str(abs(a[i]))) == 5
    rule2 = abs(a[i + 1]) % 100 == 43 and len(str(abs(a[i + 1]))) == 5
    rule3 = abs(a[i + 2]) % 100 == 43 and len(str(abs(a[i + 2]))) == 5
    rule4 = a[i]**2 + a[i + 1]**2 + a[i + 2]**2 <= m43**2
    if (rule1 or rule2 or rule3) and rule4:
        count += 1
        sm = min(sm, a[i]**2 + a[i + 1]**2 + a[i + 2]**2)
print(count, sm)