alp = sorted('ЯНВАРЬ')
n = 1
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    if a1 != 'Я' and a.count('Ь') <= 1 and 'ЯЯ' not in a:
                        print(n, a)
                    n += 1