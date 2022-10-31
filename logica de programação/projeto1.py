'''
1 . Quais são os dados de entrada necessários?
número
2. O que devo fazer com estes dados?
eu devo calcular o fatorial do numero que for passado para o meu programa e o exibir na tela.
3. Quais são as restrições deste problema?
- O número deve ser um valor positivo
- O número deve ser um valor inteiro
4. Qual é o resultado esperado?
- O resultado esperado é que o fatorial do número providenciado seja exibido.
5. Qual é sequencia de passos a ser feita para chegar ao resultado esperado?

input numero
if numero > 0 
if numero = inteiro
fatorial = 1 
loop de 1 a numero
    fatorial = fatorial * numero 
print fatorial
'''

numero = int(input('Digite o numero: '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero +1):
        fatorial = fatorial * item
    print(fatorial)