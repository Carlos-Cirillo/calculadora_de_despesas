salario = float(input('Digite aqui seu salario atual: R$ '))
ajuste = salario * 0.15
salario_novo = ajuste + salario

print(f'Seu salario de {salario} teve um ajuste de 15% sendo assim o salario novo será R$ {salario_novo:.6}')