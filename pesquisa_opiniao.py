# Pesquisa de satisfação da empresa TudoWeb

TOTAL_ENTREVISTADOS = 10  # Após os testes, altere para 50

quantidade_excelente = 0
quantidade_ruim = 0

print("PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("Opções de avaliação:")
print("1 - EXCELENTE")
print("2 - BOM")
print("3 - RUIM")
print()

for numero in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"Entrevistado {numero} de {TOTAL_ENTREVISTADOS}")

    nome = input("Digite o nome do entrevistado: ").strip()

    # Validação da idade
    while True:
        try:
            idade = int(input("Digite a idade do entrevistado: "))

            if idade > 0:
                break

            print("A idade deve ser maior que zero.")
        except ValueError:
            print("Digite uma idade válida usando somente números inteiros.")

    # Validação da opinião
    while True:
        try:
            opiniao = int(
                input("Digite a opinião (1 - EXCELENTE, 2 - BOM, 3 - RUIM): ")
            )

            if opiniao in (1, 2, 3):
                break

            print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite somente 1, 2 ou 3.")

    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        quantidade_excelente += 1
        avaliacao = "EXCELENTE"
    elif opiniao == 2:
        avaliacao = "BOM"
    else:
        quantidade_ruim += 1
        avaliacao = "RUIM"

    print(f"Resposta registrada: {avaliacao}")
    print()

# Exibição dos resultados
print("=" * 40)
print("RESULTADO DA PESQUISA")
print("=" * 40)
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f'Quantidade de respostas "EXCELENTE": {quantidade_excelente}')
print(f'Quantidade de respostas "RUIM": {quantidade_ruim}')