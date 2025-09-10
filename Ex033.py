a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

maior = a
menor = a

# Verifica b
if b > maior:
    maior = b
if b < menor:
    menor = b

# Verifica c
if c > maior:
    maior = c
if c < menor:
    menor = c

# Descobre o meio
if a != maior and a != menor:
    meio = a
elif b != maior and b != menor:
    meio = b
else:
    meio = c

print(f'O número maior é: {maior}, o menor é: {menor}, e o do meio é: {meio}')
