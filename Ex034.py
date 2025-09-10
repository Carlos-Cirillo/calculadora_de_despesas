salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 2000:
    aumento = salario * 1.15
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')
else:
    aumento= salario * 1.10
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')