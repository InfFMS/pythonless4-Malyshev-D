# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
m = []
def delit(a):
    d = a
    for i in range(a, 1,-1):
        if a % i == 0:
            d = i
    m.append(d)
    if a//d > 1:
        a = a // d
        delit(a)
x = int(input())
delit(x)
print(*m, sep='*')