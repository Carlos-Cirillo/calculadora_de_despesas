despesas = [
    {"nome": "Mercado", "valor": 120.50},

]

while True:
    print("\n[1] Adicionar despesa")
    print("[2] Lista despesas")
    print("[3] Mostrar total")
    print("[4] Sair\n")

    opcao = int(input('Escolha a opção desejada:'))

    if opcao == 1:
        nome_despesa = input('Qual nome da despesa? ')
        valor_despesa = input('Valor gasto: ')

    #Trocar virgula por ponto e transformar em número
        valor_despesa = float(valor_despesa.replace(',', '.'))

    #Salvar o nome e valor na lista
        despesas.append({
            "nome": nome_despesa,
            "valor": valor_despesa
        })

        print('\n✅ Despesa adicionada com sucesso!')
        input('Pressione ENTER para voltar ao menu...')
    
    elif opcao == 2:
        if despesas:
            print('\n📌 Lista de despesas:')
            for despesa in despesas:
                print(f"- {despesa['nome']}: R$ {despesa['valor']:.2f}")
        else:
            print('\nNenhum gasto adicionado.')
        input('Pressione ENTER para voltar ao menu...')
    
    elif opcao == 3:
        valor = sum(d['valor'] for d in despesas)
        print(f"\n💰 Total gasto: R$ {valor:.2f}")
        input('Pressione ENTER para voltar ao menu...')

    elif opcao == 4:
        print("\n👋 Saindo do programa...")
        break

    else: 
        print("\n❌ Opção inválida, tente novamente.")
