print('Введите число (от 3 до 20) для подбора пароля: ')
x = int(input())
pass_ = []
for i in range (1, 20):
    for j in range (1, 20):
        if i > j:
            continue
        if i == j:
            continue
        if x < (i + j):
            continue
        if x % (i + j) == 0:
            pass_.append(i)
            pass_.append(j)
print('Комбинация для пароля: ', pass_)