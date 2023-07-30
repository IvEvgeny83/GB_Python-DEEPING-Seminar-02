'''
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
'''

import fractions


first_num = input("\nВведите первую дробь вида a/b: ").split('/')
second_num = input("Введите вторую дробь вида c/d: ").split('/')

numerator_sum = int(first_num[0]) * int(second_num[1]) + int(second_num[0]) * int(first_num[1])
denominator_sum = int(first_num[1]) * int(second_num[1])
sum_num = [numerator_sum, denominator_sum]

numerator_multi = int(first_num[0]) * int(second_num[0])
denominator_multi = int(first_num[1]) * int(second_num[1])
multi_num = [numerator_multi, denominator_multi]

a1, b1 = sum_num # поиск общего делителя для числителя и знаменателя простой дроби
while b1 != 0:
    a1, b1 = b1, a1 % b1

a2, b2 = multi_num
while b2 != 0:
    a2, b2 = b2, a2 % b2

#проверка сделанных вычислений
verif_num_1 = fractions.Fraction(f'{first_num[0]}/{first_num[1]}')
verif_num_2 = fractions.Fraction(f'{second_num[0]}/{second_num[1]}')

verif_sum = verif_num_1 + verif_num_2
verif_multi = verif_num_1 * verif_num_2

print(f"\nВычисленная сумма введенных дробей равна: {sum_num[0]//a1}/{sum_num[1]//a1}")
print(f"Значение для ПРОВЕРКИ: {verif_sum}")

print(f"\nВычисленное произведение введенных дробей равно: {multi_num[0]//a2}/{multi_num[1]//a2}")
print(f"Значение для ПРОВЕРКИ: {verif_multi}")