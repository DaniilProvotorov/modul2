print('Введите первое число: ')
first = int(input())
print('Введите второе число: ')
second = int(input())
print('Введите третье число: ')
third = int(input())

if first == second == third:
    print('Количество совпадающих чисел 3')
elif first == second or first == third or second == third:
    print('Количество совпадающих чисел 2')
else: print('Количество совпадающих чисел 0')