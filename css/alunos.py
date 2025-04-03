#  def fibonacci(limit):
#     sequence = [0, 1]
#     while sequence[-1] + sequence[-2] <= limit:
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence

# # Solicita ao usuário um número limite
# try:
#     num = int(input("Informe um número limite para a sequência de Fibonacci: "))
#     if num < 0:
#         print("Por favor, informe um número inteiro positivo.")
#     else:
#         print("Sequência de Fibonacci até", num, ":", fibonacci(num))
# except ValueError:
#     print("Entrada inválida! Informe um número inteiro.")

---------------------------------------------------------------------------------

#fib

def fib(n):
    print(f"fib de {n}:")
    if _name_ == '_main_':
