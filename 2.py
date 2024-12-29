def F(x, y, z, w):
    l1 = not((not x or y) and (not w))
    l2 = not(z and (not(y and w)))
    return int(l1 or l2)

print('x y z w | F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if F(x, y, z, w) == 0:
                    print(x, y, z, w, '|', F(x, y, z, w))