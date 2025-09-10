a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Triangulo formado')

else:
     print('Não da para forma triangulo')
