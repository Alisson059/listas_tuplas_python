"""
O programa permite ao usuário digitar uma quantidade de números, separa-os em pares e ímpares,
organiza em uma tupla, mostra estatísticas como maior, menor e quantidade de pares/ímpares,
e ainda permite verificar quantas vezes um número específico foi digitado e em quais posições ele aparece.
O loop principal continua até o usuário digitar "sair".
"""

# Loop principal que mantém o programa rodando até o usuário digitar "sair"
while True:

    usuario = input("Digite 'entra' para digitar números ou 'sair' para encerrar: ").lower()

    # Caso o usuário queira entrar com números
    if usuario == "entra":
        quantidade = int(input("Digite a quantidade de números que deseja informar: "))

        # Listas auxiliares para organizar os números
        list_temp = []  # lista principal com todos os números
        list_impar = [] # guarda apenas os números pares
        list_par = []   # guarda apenas os números ímpares
        pares = 0       # contador de números pares
        impares = 0     # contador de números ímpares

        # Entrada de números pelo usuário
        for i in range(quantidade):
            num = int(input(f"Digite {i+1} o numero: "))
            list_temp.append(num)

            # Verifica se o número é par ou ímpar e atualiza os contadores
            if num % 2 == 0:
                list_par.append(num)
                pares += 1

            else:
                list_impar.append(num)
                impares += 1

        # Ordena a lista principal e transforma em tupla
        list_temp.sort()
        numeros = tuple(list_temp)

        if numeros:

            # Mostra resultados gerais
            print("\n--- Resultados ---")
            print(f"Lista final: {numeros}")
            print(f"Maior número: {max(numeros)} | Menor número: {min(numeros)}")
            print(f"Números pares: {list_par} | Total de pares: {pares}")
            print(f"Números ímpares: {list_impar} | Total de ímpares: {impares}")

        # Consulta sobre a frequência de um número específico
        else:
            print("Nenhum número foi digitado.")

        # Pergunta ao usuário qual número deseja consultar
        cont = int(input("Digite um número para ver quantas vezes ele apareceu: "))

        # Verifica se o número está na tupla
        if cont in numeros:
            vezes = numeros.count(cont)
            posicoes = [i + 1 for i, v in enumerate(numeros) if v == cont]
            print(f"O número {cont} aparece {vezes} vezes, nas posições: {posicoes}")
        else:
            print(f"O número {cont} não foi digitado nenhuma vez.")

    # Caso o usuário queira encerrar o programa
    elif usuario == "sair":
        print("Encerrando o programa... Até mais!")
        break

    # Caso o usuário digite algo inválido
    else:
        print("Opção inválida! Digite 'entra' ou 'sair'.")