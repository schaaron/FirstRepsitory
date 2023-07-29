real=float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar= real / 5.04
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))