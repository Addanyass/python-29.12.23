# def ex_1():
#     """ отображает на экран
# форматированный текст"""
#     return "\"“Don't let the noise of others' opinions\
# drown out your own inner voice.\"\n\t\t\t\t\t\t\t\t\t\t\t\t”Steve Jobs"

# def ex_2(a,b):
#     """функция, которая принимает два числа
# в качестве параметра и отображает все нечетные числа
# между ними"""
#     print(f"между числвми {a} и {b}, содержатся следующие нечетные числа")
#     for i in range(a,b + 1):
#         if i % 2 != 0:
#             print(i, end=" ")
# ex_2(1,10)


# def ex_3(dlina, napravlenie, simvol):
#     """Функция которая примает 3 значения в качетсве длины направления и символа"""
#     if napravlenie ==1:
#         for i in range(dlina):
#             print(simvol)
#     elif napravlenie == 0:
#         print (simvol * dlina)
# ex_3(2,1,5555)


# def ex_4(a,b,c,d):
#     """Функция которая принимает 4 значения в дальнейшей возвращает максимальное число"""
#     print(f"Между числами {a} {b} {c} {d} принимает максимальное")

#     return max(a,b,c,d)
# print(ex_4(1,2,3,4))

# def ex_5(a,b):
#     """Функция которая возвращает сумму чисел в указанном диапазоне"""
#     print(f"Диапазон чисел из {a} {b} , сумма который равна:")
#     sum = 0
#     for i in range(a,b):
#         sum += 1
#     return sum
# print(ex_5(20,50))


# def ex_6(a,b):
#     """Функция которая проверяет является ли число простым"""
#     print(f"Число {a}")
#     if a % 2 !=0:
#         return True
#     else:
#         return False
# print(ex_6(12,2))

# def ex_7(number):
#     """Функция которая проверяет является ли число счастливым"""
#     print(f"Число{number}")
#     str_number = str(number)
#     first = str_number[0:3]
#     second = str_number[3:]
#     sum_first = 0
#     sum_second = 0
#     for i in first:
#         sum_first += int(i)
#     for i in second:
#         sum_second += int(i)
#     if sum_first == sum_second:
#         return "Счастливое"
#     else: 
#         return "Не счастливое"
# print(ex_7(123321))


