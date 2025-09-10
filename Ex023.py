# Exercício 23 - Separando dígitos de um número

# Solicita ao usuário que digite um número de 0 a 9999
num = int(input('Digite um número entre 0 e 9999: '))

# Calcula cada dígito do número
milhar = num // 1000  # extrai o dígito das milhar
centena = (num // 100) % 10  # extrai o dígito da centena
dezena = (num // 10) % 10  # extrai o dígito da dezena
unidade = num % 10  # extrai o dígito da unidade

# Exibe os resultados
print(f'Analisando o número {num}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
