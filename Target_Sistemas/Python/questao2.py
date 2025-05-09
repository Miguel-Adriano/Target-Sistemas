# Questão 2: Verificar se número pertence à sequência de Fibonacci

def verificar_fibonacci(numero):
    a, b = 0, 1
    if numero == 0 or numero == 1:
        return True
    while b < numero:
        a, b = b, a + b
    return b == numero

# Recebe o número a ser verificado
numero = int(input("Digite um número: "))

if verificar_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} NÃO pertence à sequência de Fibonacci.")
