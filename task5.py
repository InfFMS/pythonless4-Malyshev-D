def rev(a):
    m = [''] * len(a)
    for i in range(len(a)):
        m[-i-1] = s[i]
    print(*m, sep='')
s = list(input())
rev(s)
