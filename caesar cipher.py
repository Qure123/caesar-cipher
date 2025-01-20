def encrypt(n,m,l):
    if l != 'r':
        for c in m:
            if c.isalpha():
                if c.isupper():
                    print(const_upper_en[(const_upper_en.find(c) + n) % 26], end = '')
                else:
                    print(const_lower_en[(const_lower_en.find(c) + n) % 26], end = '')
            else:
                print(c, end = '')
    else:
        for c in m:
            if c.isalpha():
                if c.isupper():
                    print(const_upper_rus[(const_upper_rus.find(c) + n) % 32], end = '')
                else:
                    print(const_lower_rus[(const_lower_rus.find(c) + n) % 32], end = '')
            else:
                print(c, end = '')
def decrypt(n,m,l):
    if l != 'r':
            for c in m:
                if c.isalpha():
                    if c.isupper():
                        print(const_upper_en[(const_upper_en.find(c) - n) % 26], end = '')
                    else:
                        print(const_lower_en[(const_lower_en.find(c) - n) % 26], end = '')
                else:
                    print(c, end = '')
            print()
    else:
            for c in m:
                if c.isalpha():
                    if c.isupper():
                        print(const_upper_rus[(const_upper_rus.find(c) - n) % 32], end = '')
                    else:
                        print(const_lower_rus[(const_lower_rus.find(c) - n) % 32], end = '')
                else:
                    print(c, end = '')
k = input('Вам нужно расшифровать или зашифровать (р/decr - расшифровка, з/encr - зашифровка):\n')
n= int(input('Введите шаг:\n'))
m = input('Введите фразу:\n')
l = input('Ведите язык (r - рус, e - англ):\n')
const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные eng буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные eng буквы
const_upper_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'# Прописные eng буквы
const_lower_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'# Строчные eng буквы
if k != 'decr':
    encrypt(n,m,l)
else:
    decrypt(m,l)
#Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!