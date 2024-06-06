from random import randint
from time import sleep
pc = randint(0, 5) # Faz o PC "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número de 0 à 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...') # Aguarde uma resposta
sleep(1)
print('QUASE LÁ...') # Resposta quase chegando
sleep(2)
if jogador == pc:
    print('ACERTOU! Meus parabéns, meu nobre')
else:
    print('ERROU! Pensei no número {} e não no número {}. Tente novamente, seu paspalho.'.format(pc, jogador))
