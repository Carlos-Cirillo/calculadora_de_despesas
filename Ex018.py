import math  # importa a biblioteca de funções matemáticas

# pede apenas 1 valor (o ângulo em graus)
angulo = float(input('Digite um ângulo em graus: '))

# converte o valor em radianos (necessário para usar sin, cos e tan)
rad = math.radians(angulo)

# calcula seno, cosseno e tangente a partir do valor em radianos
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

# mostra os resultados formatados
print(f'O ângulo de {angulo}° tem SENO {seno:.2f}')
print(f'O ângulo de {angulo}° tem COSSENO {cosseno:.2f}')
print(f'O ângulo de {angulo}° tem TANGENTE {tangente:.2f}')
