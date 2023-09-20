opcao = -1

while opcao !="2":
    opcao = input("""

    1) Calcular o IMC
    2) Sair

    Digite a opção desejada:
    """)

    if opcao == "1":
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        calcular = peso / (altura * altura)
        calcular2 = peso / (altura **2)
        print(f"Seu indice é de {calcular, calcular2}")