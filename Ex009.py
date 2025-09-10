num = int(input('Digite um número para ver a tabuada dele: '))

print('-----------------------------')
print(f'*****Essa é a tabua número {num}*****')
for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i}')

print('-----------------------------')