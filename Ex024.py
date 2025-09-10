msg = input('Em que cidade você nasceu? ').strip()  # tira espaços extras
palavras = msg.split()  # divide a resposta em palavras
primeira = palavras[0]  # pega só a primeira palavra

if primeira.lower() == 'são':  # compara em minúsculo pra evitar erro
    print(True)
else:
    print(False)
