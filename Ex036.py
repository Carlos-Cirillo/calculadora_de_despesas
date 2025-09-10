valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos_financiado = int(input('Quantos anos de financimento?'))

prestacao = valor_casa / (anos_financiado * 12)

if prestacao > salario * 0.3:
    print(f'Para pagar seu financiamento de R${valor_casa:.2f} em {anos_financiado} a prestação será de R${prestacao:.2f}')
    print(f'EMPRÉSTIMO NEGADO')
else:
    print(f'Para pagar seu financiamento de R${valor_casa:.2f} em {anos_financiado} a prestação será de R${prestacao:.2f}. Dessa forma seu EMPRESTIMO foi aprovado')