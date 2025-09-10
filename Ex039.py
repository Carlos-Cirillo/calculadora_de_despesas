ano_nascido = int(input('Qual ano você nasceu? '))

idade = 2025 - ano_nascido

if idade < 18:
    msg = 18 - idade
    print(f'Ainda vai se alistar, faltam {msg}')
elif idade == 18:
    print(f'Hora de se alistar agora')
elif idade > 18:
    msg = idade - 18
    print(f'Já passou do tempo de alistamento, você está {msg} anos atrasado')