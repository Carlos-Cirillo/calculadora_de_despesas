import random


print('JOGO DO ADIVINHA')

chute = int(input('Digite um numero de 0 a 5: '))

numero = random.randint(0, 5)

if chute == numero:
    print(f'Parabens você ganhou, seu numero da sorte é: {chute}')
elif chute > 5: 
    print('O numero digitado é maior que 5, escolha numeros do 0 ao 5')

else: 
    print(f'Você errou o numero correto é: {numero}')
