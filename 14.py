from string import ascii_lowercase
alp = '0123456789' + ascii_lowercase
for x in alp:
    try:
        num1 = int(f'11353{x}12', 25)
        num2 = int(f'135{x}21', 25)
        if (num1 + num2) % 24 == 0:
            print(x, (num1 + num2) // 24)
    except:
        break