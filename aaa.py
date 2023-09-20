print(f'{"MENU INICIAL":^40}\n\nDigite um número para escolher alguma das opções a baixo:\n\n1. Listar\n2. Adicionar\n3. Alterar\n4. Excluir')
menu_escolha=str(input("\nDigite a opção escolhida aqui e de enter: "))
if menu_escolha=="1":
    print("\nVocê digitou: 1. Listar\n")
    print(f'{"CATEGORIA":^15}|{"NOME DO FILME":^30}|{"GÊNERO":^14}')
    print(f'{"Filme":^15}|{"O esquadrão do mau":^30}|{"Ação":^14}')
    print(f'{"Serie":^15}|{"Vikings":^30}|{"Romance":^14}')
    print(f'{"Anime":^15}|{"Deaf note":^30}|{"Suspense":^14}')
    #listar tudo, ou filtrar por coisas filme em nota fiscal categoria 
elif menu_escolha=="2": 
    print("\nVocê digitou: 2. Adicionar\n")
    categoria=input("Digite a categoria (S)Serie/(F)Filme/(A)Amime) aqui: ")
    input(f"Digite o gênero do(a) {categoria} aqui: ")
    nome_filme=input(f"Digite o nome do(a) {categoria} aqui: ")
    print(f"\n{nome_filme} foi adicionado a Lista de ", categoria)
    #A pessoa tem q escrever serie e genero valido(caso deseje ver categorias digitar tal coisa)
elif menu_escolha=="3":
    print("\nVocê digitou: 3. Alterar\n")
    print("Digite o nome do vídeo que deseja alterar")
    #Cada filme é uma letra ou numero?
elif menu_escolha=="4":
    print("\nVocê digitou: 4. Excluir\n")
    deletar=input("Digite qual vídeo você gostaria de deletar: ")
    comando_deletar=input(f"Você escolheu: {deletar}\n Para confirmar digite:(S)\nPara cancelar digite:(N)\nDigite S/N:")
    if comando_deletar in ["S","s", "Sim", "sim"]:
        print(deletar, "deletado")
    elif comando_deletar in ["N", "n", "nao", "não", "Não", "Nao"]:
        print("voltando")
    else: 
        print("Teste")    
#te, certeza q quer deletar? digite s/n
else:
     print(f"{menu_escolha} não é um caracteri reconhecido")
