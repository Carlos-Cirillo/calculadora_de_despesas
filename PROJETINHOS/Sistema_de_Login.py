# 1. Criar um dicionário vazio para armazenar os usuários
import getpass

usuarios = {}

# 2. Loop principal do sistema
while True:
    print("\n[1] Criar conta")
    print("[2] Fazer login")
    print("[3] Manutenção (Usuários cadastrados)")
    print("[4] Sair")

    opcao_str = input("Digite a opção desejada: ")

    # Verifica se a entrada é numérica
    if not opcao_str.isdigit():
        print("Opção inválida, digite um número.")
        continue

    opcao = int(opcao_str)

    # Verifica se o número está dentro das opções válidas
    if opcao not in [1, 2, 3, 4]:
        print("Opção inválida, tente novamente.")
        continue

    # Criar conta
    if opcao == 1:
        while True:
            user = input('Digite o seu nome de usuário: ')

            if user in usuarios:
                print("Usuário já existe, escolha outro nome.")
            else:
                senha = getpass.getpass('Digite a senha desejada: ')
                usuarios[user] = senha
                print("Usuário criado com sucesso!")
                break

    # Fazer login
    elif opcao == 2:
        while True:
            user = input('Digite seu usuário (ou 0 para voltar ao menu): ')

            if user == '0':
                break  # volta para o menu principal

            if user in usuarios:
                senha = getpass.getpass('Digite sua senha: ')
                print()
                if senha == usuarios[user]:
                    print(f'Bem-vindo {user}!\n')
                    break  # login realizado, sai do loop
                else:
                    print('Senha incorreta, tente novamente.')
            else:
                print('Usuário não encontrado, verifique seu nome.')

    # Manutenção (listar usuários)
    elif opcao == 3:
        senha_admin = getpass.getpass('Digite a senha para acessar área de manutenção: ')
        if senha_admin == 'admin123':
            print('\nAcesso concedido\n')
            if usuarios:
                print('Usuários cadastrados:')
                for user in usuarios.keys():
                    print(f"- {user}")
            else:
                print("Nenhum usuário cadastrado ainda.")
        else:
            print("Acesso NEGADO")

    # Sair
    elif opcao == 4:
        print("Saindo do sistema...")
        break
