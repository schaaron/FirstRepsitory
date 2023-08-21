#dizer se o número é par ou ímpar

n = int(input('Me diga um número qualquer: '))
resultado = n % 2
if resultado == 0:
    print('Este número {} é PAR'.format(n))
else:
    print('Este número {} é ÍMPAR'.format(n))
