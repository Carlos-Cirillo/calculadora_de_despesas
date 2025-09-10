import random  # importa a biblioteca random, que permite fazer sorteios

# pede para o usuário digitar 4 nomes
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

# cria uma lista com todos os nomes digitados
lista_nomes = [nome1, nome2, nome3, nome4]

# embaralha a lista diretamente
random.shuffle(lista_nomes)

# mostra a lista embaralhada
print(lista_nomes)
