frase = str(input('Digite uma frase: ')).strip()
contador = frase.lower().count('a')
posicao_inicio = frase.lower().find('a') + 1
posicao_ultima = frase.lower().rfind('a') + 1
print(f'A letra A aparece {contador} vezes na frase'  )
print(f'A primeira letra A aparece na posição: {posicao_inicio}')
print(f'A última letra A aparece na posição: {posicao_ultima}')