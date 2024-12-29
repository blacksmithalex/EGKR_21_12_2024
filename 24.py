file = open('24_19254.txt')
a = file.readline().replace('FSRQ', '*')
file.close()

inds = [i for i in range(len(a)) if a[i] == '*']
mcount = inds[80] + 80 * 3 + 3
for i in range(len(inds) - 81):
    count = inds[i + 81] - inds[i] - 1 + 80 * 3 + 6
    mcount = max(count, mcount)
count = len(a) - inds[-80] - 1 + 80 * 3 + 3
mcount = max(count, mcount)
print(mcount)



