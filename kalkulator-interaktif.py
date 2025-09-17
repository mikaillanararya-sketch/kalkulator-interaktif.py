name = input('Haloo! Selamat datang di kalkulator interaktif, nama kamu siapa?')
print (f'senang bertemu dengan kamu, {name}! Selamat datang di kalkulator interaktif!!')

operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
num1 = float(input('Masukkan nomor pertama: '))
num2 = float(input('Masukkan nomor kedua: '))

if operator == '+':
    result = num1 + num2
    print (f'Hasil {num1} + {num2} = {result}')
    operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
    num1 = float(input('Masukkan nomor pertama: '))
    num2 = float(input('Masukkan nomor kedua: '))
elif operator == '-':
    result = num1 - num2
    print (f'Hasil {num1} - {num2} = {result}')
    operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
    num1 = float(input('Masukkan nomor pertama: '))
    num2 = float(input('Masukkan nomor kedua: '))
elif operator == '*':
    result = num1 * num2
    print (f'Hasil {num1} * {num2} = {result}')
    operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
    num1 = float(input('Masukkan nomor pertama: '))
    num2 = float(input('Masukkan nomor kedua: '))
elif operator == '/':
    result = num1 / num2
    print (f'Hasil {num1} / {num2} = {result}')
    operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
    num1 = float(input('Masukkan nomor pertama: '))
    num2 = float(input('Masukkan nomor kedua: '))
else:
    print(f'Yahh maaf, {operator} tidak valid')
    operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
    num1 = float(input('Masukkan nomor pertama: '))
    num2 = float(input('Masukkan nomor kedua: '))