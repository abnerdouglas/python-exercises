def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Informe um número: "))
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

'''
Explicação: A função fibonacci gera a sequência até encontrar um valor maior ou igual ao número informado. 
Se o número for encontrado na sequência, ele pertence à sequência de Fibonacci.
'''