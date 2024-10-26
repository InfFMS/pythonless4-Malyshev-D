def rev(a):
    ans = 0
    l = len(str(a))
    for i in range(l):
        j = l-1-i
        ans += (a % 10) * 10**j
        a -= a % 10
        a = a // 10
    return ans
print(rev(int(input())))