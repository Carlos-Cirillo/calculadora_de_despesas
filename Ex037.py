numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

escolha = int(input('Sua opção: '))

if escolha == 1:
    binario = bin(numero)
    print(f'{numero} convertido para BINÁRIO é igual {binario}')
elif escolha == 2:
    octal = oct(numero)
    print(f'{numero} convertido para OCTAL é igual {octal}')
elif escolha == 3:
    hexa = hex(numero)
    print(f'{numero} convertido para HEXADECIMAL é igual {hexa}')
else:
    print('Opção invalida')