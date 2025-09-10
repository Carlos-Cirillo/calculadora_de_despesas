import math

x = float(input('Digite o valor do cateto: '))
y = float(input('Digite o valor do adjacente: '))

msg = math.hypot(x, y)

print(f'A hipotenusa vai medir {msg:.2f}')