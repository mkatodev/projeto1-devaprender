'''programa que gera um valor aleatório de 1 - 10 e permite que o usuario chute o 
numero aleatorio e dizer se o chute é maior menor ou igual ao valor aleatorio.'''

import random

valor_aleaorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleaorio:
        print('Chute foi maior que o valor gerado')
    elif chute < valor_aleaorio:
        print('Chute foi menor que o valor gerado')
    elif chute == valor_aleaorio:
        acertou = True
        print('voce acertou!')