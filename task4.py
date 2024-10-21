# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def nod(a, b):
    d = [1]
    for i in range(min(a, b), 1, -1):
        if max(a,b) % i == 0 and min(a, b) % i == 0: d.append(i)
    print('НОД:', max(d))
a = int(input())
b = int(input())
nod(a, b)