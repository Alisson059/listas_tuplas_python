"""
O código pede para o usuário digitar 20 números inteiros, guarda esses números em uma lista,
organiza em ordem crescente e converte para uma tupla. Ele mostra todos os números digitados,
além do maior e do menor número. Depois, pergunta ao usuário um número específico e, se esse número estiver
na tupla, mostra quantas vezes ele aparece. Caso o número não tenha sido digitado, o programa avisa.

"""
# Lista temporária para armazenar os números digitados pelo usuário
list_temp = []

# Loop para receber 20 números do usuário
print("Digite os 20 primerio numeros: ")
for i in range(20):
    num = int(input(f"Digite o {i+1}º numero: "))
    list_temp.append(num)  # Adiciona cada número à lista

# Ordena a lista em ordem crescente
list_temp.sort()

# Converte a lista para tupla (imutável)
numeros = tuple(list_temp)

# Mostra todos os números digitados
print(f"\nVocê digitou os números: {numeros}")

# Mostra o maior e o menor número da tupla
print(f"O maior numero digitado foi: {max(numeros)}")
print(f"O menor numero digitado foi: {min(numeros)}")

# Pergunta ao usuário qual número ele quer verificar
cont = int(input("Qual número você deseja ver quantas vezes digitou? "))

# Verifica se o número está na tupla
if cont in numeros:
    # Conta quantas vezes o número aparece
    vezes = numeros.count(cont)

    # Encontra todas as posições do número (começando em 1 para o usuário)
    posicoes = [i + 1 for i, v in enumerate(numeros) if v == cont]

    # Mostra os resultados
    print(f"O número {cont} aparece {vezes} vezes na tupla.")
    print(f"o número {cont} aparece nas posições: {posicoes}")

else:
    # Mensagem caso o número não tenha sido digitado
    print(f"O número {cont} não foi digitado nenhuma vez.")
