real = float(input('Digite qual o valor em real que deseja converter: '))
dolar = real / 5.20

print(f'O valor de {real} convertido em USD é ${dolar:.5}')

dolar = float(input('Digite qual o valor em dolar que deseja converter: '))
real = dolar * 5.20

print(f'O valor de {dolar} convertido em reais é R${real}')