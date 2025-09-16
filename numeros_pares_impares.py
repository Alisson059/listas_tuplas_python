"""

O programa pede ao usuário para digitar 10 números inteiros,
guarda esses números em uma lista e depois converte para uma tupla.
Durante a digitação, ele conta quantos números são pares e quantos são ímpares.
Depois, permite que o usuário escolha um número específico para verificar quantas vezes
ele aparece na tupla e em quais posições. Por fim, mostra também a quantidade
total de números pares e ímpares digitados.

"""



# Lista para guardar os números digitados
list_temp = []

# Contadores para números pares e ímpares
pares = 0
impares = 0

print("Digite os 10 primerio numeros")

# Loop para receber os 10 números do usuário
for i in range(10):
    num = int(input(f"Digite o {i + 1}º numero: "))
    list_temp.append(num)

    # Verifica se o número é par ou ímpar e atualiza os contadores
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Ordena a lista em ordem crescente
list_temp.sort()

# Converte a lista para uma tupla (imutável)
numeros = tuple(list_temp)

# Pergunta ao usuário qual número deseja consultar
cont = int(input("Qual número você deseja ver quantas vezes digitou?"))

# Verifica se o número está na tupla
if cont in numeros:
    # Conta quantas vezes o número aparece
    vezes = numeros.count(cont)

    # Encontra todas as posições do número (começando em 1)
    posicoes = [i + 1 for i, v in enumerate(numeros) if v == cont]

    # Mostra os resultados
    print(f"O número {cont} aparece {vezes} vezes na tupla.")
    print(f"o número {cont} aparece nas posições: {posicoes}")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números impares: {impares}")

# Caso o número não tenha sido digitado
else:
    print(f"O número {cont} não foi digitado nenhuma vez.")

