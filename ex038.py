# Variáveis "n1" e "n2"
n1: int = int(input('Digite um número: '))
n2: int = int(input(('Digite outro número: ')))

# Caso n1 seja maior que n2, n1 será o maior
if n1 > n2:
    print('O primeiro valor é maior que o segundo')
    print('O segundo valor é menor que o primeiro')

# Caso n1 e n2 sejam iguais
elif n1 < n2:
    print('O segundo valor é maior que o primeiro')
    print('O primeiro valor é menor que o segundo')

# Caso n2 seja maior que n1, n2 será maior
else:
    print('Os dois valores são iguais')

