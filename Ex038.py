primeiro = int(input('Primeiro número:'))
segundo = int(input('Segundo número:'))

if primeiro > segundo: 
    print(f'O primerio numero é o maior, {primeiro} é maior que {segundo}')
elif primeiro < segundo:
    print(f'O segundo numero é o maior, {segundo} é maior que {primeiro}')
elif primeiro == segundo:
    print('Os dois valores são iguais')

# OU utilizar o ELSE
#  else:
#   print('Os dois valores são iguais')