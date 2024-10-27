def fibonacci(numero):
    fib = [0, 1]
    
    while fib[-1] < numero:
        fib.append(fib[-1] + fib[-2])

    if numero in fib:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

try:
    num = int(input("Informe um número: "))
    print(fibonacci(num))
except ValueError:
    print("Por favor, insira um número inteiro válido.")
