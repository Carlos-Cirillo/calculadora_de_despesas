nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + nota2) / 2 

if media >= 7: 
    print(f'Se tua nota foi {nota1} e {nota2} então você está APROVADO')
elif media >= 5 and media < 7:
    print(f'Se tua nota foi {nota1} e {nota2} então você está de RECUPERAÇÃO')
else:
    print(f'Se tua nota foi {nota1} e {nota2} então você está REPROVADO')