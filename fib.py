def F(n):
    if n <= 2:
        return 1
    else: return F(n-1) + F(n-2)
x = int(input())
print(F(x))