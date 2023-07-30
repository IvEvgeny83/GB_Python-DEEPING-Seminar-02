'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
'''

num = int(input("\nВведите число: "))
print(f"Значение перевода для проверки - {hex(num)}")

NUM_SYS = 16
res_num = ''

while num > 0:
    hex_num = num % NUM_SYS
    
    match hex_num:
        case 10:
            hex_num = 'A'
        case 11:
            hex_num = 'B'
        case 12:
            hex_num = 'C'
        case 13:
            hex_num = 'D'
        case 14:
            hex_num = 'E'
        case 15:
            hex_num = 'F'

    res_num += str(hex_num)
    num //= NUM_SYS

print(f"Результат перевода введенного число в шестнадцатиричный вид: {res_num[::-1]}")