preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco*5/100)
print('O valor do produto que era {:.2f} agora com o desconto de 5% ficou {:.2f}'.format(preco, novo))
