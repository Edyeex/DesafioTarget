def fibonacci(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        seq = [0, 1]
        while seq[-1] < n:
            seq.append(seq[-1] + seq[-2])
        return seq

def verifica_na_sequencia(num):
    seq = fibonacci(num)
    if num in seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
print(verifica_na_sequencia(num))
