velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('TÁ MALUCO CARA?!?!? O LIMITE DE VELOCIDADE É 80Km/h!!! PARA ESSE CARRO AÍ')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tá devagar, filho. Se manda daqui')