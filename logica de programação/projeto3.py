velocidade = int(input('Digite a sua velocidade: '))
velocidade_max = 80
if velocidade < velocidade_max:
    print('Não levou multa!')
elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
    print('multa leve!')
elif velocidade > velocidade_max + 11 and velocidade <= velocidade_max + 20:
    print('multa grave')
elif velocidade > velocidade_max + 20:
    print('multa gravissiva')