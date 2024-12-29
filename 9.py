file = open('9_19241.txt')
n = 1
for line in file:
    line = [int(x) for x in line.split()]
    freq1, freq3 = [], []
    for x in line:
        if line.count(x) == 1:
            freq1.append(x)
        elif line.count(x) == 3:
            freq3.append(x)
    if len(freq3) == 6 and len(freq1) == 1:
        avg = sum(freq3) / 6
        if avg < freq1[0]:
            print(n)
    n += 1
