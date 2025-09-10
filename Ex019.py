import random  # importa a biblioteca random, que permite fazer sorteios

# pede para o usuário digitar 4 nomes
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

# cria uma lista com todos os nomes digitados
lista_nomes = [nome1, nome2, nome3, nome4]

# usa random.choice() para sortear 1 item aleatório da lista
sorteio = random.choice(lista_nomes)

# mostra na tela o nome sorteado
print(sorteio)

