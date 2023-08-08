from random import randint
from time import sleep
computador = randint(0,5) #faz o computador sortear um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #Jogador tentando adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, VOCÊ VENCEU')
else:
    print('GANHEI, eu pensei no número  {} e não no {}.'.format(computador, jogador))