preco = float(input('Digite o valor do produto: '))

desconto = preco * 0.12
valor_desconto = preco - desconto

print(f'Você pegou o produto com valor {preco} porem você ganhou 5% de desconto nessa compra, sendo assim você teve um desconto do valor {valor_desconto:.5}')