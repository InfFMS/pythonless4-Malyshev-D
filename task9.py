# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
import math
def f(a):
    if a == 1:
        print('YES')
    elif a % 2 != 0:
        print('NO')
    else:
        a = a//2
        f(a)
a=int(input())
f(a)