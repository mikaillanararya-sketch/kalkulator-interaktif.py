# Project Title

Kalkulator Interaktif

## Description

Program sederhana ini adalah sebuah kalkulator yang dibangun menggunakan bahasa pemrograman Python. Program ini berinteraksi dengan pengguna melalui terminal atau command prompt untuk menerima input angka dan operasi sederhana matematika, kemudian menampilkan hasil perhitungannya. Program ini memiliki fitur interaksi personal dengan pengguna dan dapat melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian.

## Getting Started

### Dependencies

* Python 3.13.7 (kompatibel dengan berbagai sistem operasi termasuk Windows 11, macOS, dan Linux)
* Tidak memerlukan library external tambahan

### Installing

* Download dan install Python dari website resmi: https://www.python.org/downloads/
* Menambah extension di file kalkulator-interaktif.py

### Executing program

* Buka terminal atau command promp
* Salin raw coding dan tempel di terminal Anda, lalu run
* Ikuti instruksi yang muncul di layar:
  1. Masukkan nama Anda
  2. Pilih operator matematika (+, -, *, /)
  3. Masukkan angka pertama
  4. Masukkan angka kedua
  5. Program akan menampilkan hasil perhitungan
```
name = input('Haloo! Selamat datang di kalkulator interaktif, nama kamu siapa?')
print(f'senang bertemu dengan kamu, {name}! Selamat datang di kalkulator interaktif!!')

operator = input('Masukkan tanda pengoperasian (+, -, *, /): ')
num1 = float(input('Masukkan nomor pertama: '))
num2 = float(input('Masukkan nomor kedua: '))

if operator == '+':
    result = num1 + num2
    print(f'Hasil {num1} + {num2} = {result}')
elif operator == '-':
    result = num1 - num2
    print(f'Hasil {num1} - {num2} = {result}')
elif operator == '*':
    result = num1 * num2
    print(f'Hasil {num1} * {num2} = {result}')
elif operator == '/':
    result = num1 / num2
    print(f'Hasil {num1} / {num2} = {result}')
else:
    print(f'Yahh maaf, {operator} tidak valid')
```

## Authors

Dibuat oleh Mikailla Khiva Nuandhe Nararya
