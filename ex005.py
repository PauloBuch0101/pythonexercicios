real = float(input('Quanto você tem na sua carteira? R$'))
dolar = real / 5.16
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))