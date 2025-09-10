distancia = int(input('Digite a distancia da sua viagem em KM: '))

if distancia <= 200: 
    valor_km = distancia * 0.50
    print('Nós cobramos R$0,50 centavos por KM utilizado.')
    print(f'O valor da sua viagem será de: {valor_km}')
else:
    valor_km2 = distancia * 0.45
    print(f'O valor da sua viagem acima de 200km ficara por R$0,45 centavos por km, te damos um desconto.')
    print(f'Com o desconto sua viagem fica no valor de {valor_km2}')
