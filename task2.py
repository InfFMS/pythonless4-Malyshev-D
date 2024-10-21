e = ['один','два','три','четыре','пять','шесть','семь','восемь','девять']
d = ['','','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
o = ['десять', 'надцать']
def number_to_words(num):
    if (num <=9) or (num >=20):
        print(d[num//10], e[num%10-1])
    elif num==10: print(o[0])
    elif num==11 or num==13:
        print(e[num%10-1], o[1], sep='')
    elif (num >=14) and (num <= 19):
        print(e[num%10-1][:-1], o[1], sep='')
    else: print('двенадцать')
number_to_words(int(input()))