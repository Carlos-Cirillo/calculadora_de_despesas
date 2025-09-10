# Exercício 22 - Curso em Vídeo (Python)
# Manipulando cadeias de caracteres (strings)

# Pede o nome completo do usuário
nome = input('Digite seu nome completo: ').strip()  # strip() remove espaços extras do começo e do fim

# Mostra o nome com todas as letras maiúsculas
print('Nome em maiúsculas:', nome.upper())

# Mostra o nome com todas as letras minúsculas
print('Nome em minúsculas:', nome.lower())

# Conta quantas letras tem no nome (sem contar espaços)
print('Quantidade de letras (sem espaços):', len(nome.replace(' ', '')))

# Mostra quantas letras tem o primeiro nome
primeiro_nome = nome.split()[0]  # split() separa o nome em partes (lista de palavras), pegamos a primeira
print('Quantidade de letras no primeiro nome:', len(primeiro_nome))
