n = int(input('Informe o número que deseja consultar: '))

prev = 0
atual = 1

while atual < n:
    prox = prev + atual
    prev = atual
    atual = prox
    
if atual == n:
    print(f'O número {n} pertence à sequência de Fibonacci.')
else:
    print(f'O número {n} não pertence à sequência de Fibonacci.')
