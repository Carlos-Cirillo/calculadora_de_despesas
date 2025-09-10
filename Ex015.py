dias = int(input('Digite quantos dias você ficou com o carro: '))
km = float(input('Digite quantos quilometros rodou com o carro: '))

calculo_de_dias = 60 * dias
calculo_de_km = km * 0.15 

calculo_total = calculo_de_dias + calculo_de_km

print(f'Você ficou com o carro {dias} dias, que da o valor total de diarias {calculo_de_dias}\n')
print(f'Você rodou {km:.1f} quilometros com o carro, conforme o contrato cobramos R$0.15 por km rodado\n')
print(f'Dessa forma total a pagar é R${calculo_total:.2f}')