import json

def salvar(data, file_name):
    with open(file_name + '.json', 'w') as f:
        json.dump(data, f, indent = 4)

def carregar(file_name):
    try:
        with open(file_name + '.json', 'r') as f:
            data = json.load(f)
            f.close()
    except FileNotFoundError:
        data = []
    return data
        
def add(tipo):
    
    while True:
        if tipo == "estudantes":
            data = carregar(tipo)
            achou = False
            try:
                cod = int(input("Digite o código do estudante: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            for i in data:
                if i['codigo_estudante'] == cod:
                    achou = True
                    continue
            if achou:
                input("Código do estudante já existe. Pressione ENTER para continuar.")
                continue
        
            nome = input("Digite o nome do estudante: ")
            matricula = input("Digite a matrícula do estudante: ")
            pessoa = {"codigo_estudante": cod, "nome": nome, "matricula": matricula}
            data.append(pessoa)
            salvar(data, tipo)
            input("Estudante adicionado, precione ENTER para continuar.")
            break

        if tipo == "professores":
            data = carregar(tipo)
            try:
                cod = int(input("Digite o código do professor: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            for i in data:
                if i['codigo_professor'] == cod:
                    achou = True
                    continue
            if achou:
                input("Código do professor já existe. Pressione ENTER para continuar.")
                continue
            nome = input("Digite o nome do professor: ")
            cpf = input("Digite o CPF do professor: ")
            pessoa = {"codigo_professor": cod, "nome": nome, "cpf": cpf}
            data.append(pessoa)
            salvar(data, tipo)
            input("Professor adicionado, precione ENTER para continuar.")
            break
        if tipo == "disciplinas":
            data = carregar(tipo)
            try:
                cod = int(input("Digite o código da disciplina: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            for i in data:
                if i['codigo_professor'] == cod:
                    achou = True
                    continue
            if achou:
                input("Código do professor já existe. Pressione ENTER para continuar.")
                continue
            nome = input("Digite o nome da disciplinas: ")
            pessoa = {"codigo_disciplina": cod, "nome": nome}
            data.append(pessoa)
            salvar(data, tipo)
            input("Disciplina adicionado, precione ENTER para continuar.") 
            break 
        if tipo == "turmas":
            data = carregar(tipo)
            professores = carregar("professores")
            disciplinas = carregar("disciplinas")
            try:
                cod = int(input("Digite o código da turma: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            for i in data:
                if i['codigo_professor'] == cod:
                    achou = True
                    continue
            if achou:
                input("Código do professor já existe. Pressione ENTER para continuar.")
                continue
            try:
                cod_1 = int(input("Digite o código da professor: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            try:
                cod_2 = int(input("Digite o código da disciplina: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            encontrado = False
            
            for professor in professores:
                if professor['codigo_professor'] == cod_1:
                    encontrado = True
            encontrado_2 = False
            for disciplina in disciplinas:
                if disciplina['codigo_disciplina'] == cod_2:
                    encontrado_2 = True
            if encontrado and encontrado_2 == True:
                pessoa = {"codigo_turma": cod, "codigo_professor": cod_1, "codigo_disciplina": cod_2}
                data.append(pessoa)
                salvar(data, tipo)
                input("Turma adicionada, precione ENTER para continuar.")
                break
            else:
                input("Você digitou algo errado, digite ENTER para voltar")
                break                 
        if tipo == "matriculas":
            data = carregar(tipo)
            turmas = carregar("turmas")
            estudantes = carregar("estudantes")
            try:
                cod = int(input("Digite o código da turma: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            try:
                cod_1 = int(input("Digite o código do estudante: "))
            except ValueError:
                input("Digite apenas números, ENTER para continuar")
                continue
            encontrado = False
            
            for turma in turmas:
                if turma['codigo_turma'] == cod:
                    encontrado = True
            encontrado_2 = False
            for estudante in estudantes:
                if estudante['codigo_estudante'] == cod_1:
                    encontrado_2 = True
            if encontrado and encontrado_2 == True:
                pessoa = {"codigo_turma": cod, "codigo_estudante": cod_1}
                data.append(pessoa)
                salvar(data, tipo)
                print("Matricula adicionada com sucesso!")
                break
            else:
                input("Você digitou algo errado, digite ENTER para voltar")
                break

def lista(tipo):
    
    if tipo == "estudantes":
        estudantes = carregar(tipo)
        if not estudantes:
            print("---LISTA---")
            print("...lista vazia...")
        else:
            print("---LISTA---")
            for i in estudantes:
                print(f"CÓDIGO: {i['codigo_estudante']} | NOME: {i['nome']} | MATRÍCULA: {i['matricula']}")
    if tipo == "professores":
        professores = carregar(tipo)
        if not professores:
            print("---LISTA---")
            print("...lista vazia...")
        else:
            print("---LISTA---")
            for i in professores:
                print(f"CÓDIGO: {i['codigo_professor']} | NOME: {i['nome']} | MATRÍCULA: {i['cpf']}")
    if tipo == "disciplinas":
        disciplinas = carregar(tipo)
        if not disciplinas:
            print("---LISTA---")
            print("...lista vazia...")
        else:
            print("---LISTA---")
            for i in disciplinas:
                print(f"CÓDIGO: {i['codigo_disciplina']} | NOME: {i['nome']}")
    if tipo == "turmas":
        turmas = carregar(tipo)
        if not turmas:
            print("---LISTA---")
            print("...lista vazia...")
        else:
            print("---LISTA---")
            for i in turmas:
                print(f"CÓDIGO DE TURMA: {i['codigo_turma']} | CÓDIGO DE PROFESSOR: {i['codigo_professor']} | CÓDIGO DE DISCIPLINA: {i['codigo_disciplina']}")
    if tipo == "matriculas":
        matriculas = carregar(tipo)
        if not matriculas:
            print("---LISTA---")
            print("...lista vazia...")
        else:
            print("---LISTA---")
            for i in matriculas:
                print(f"CÓDIGO DE TURMA: {i['codigo_turma']} | CÓDIGO DE ESTUDANTE: {i['codigo_estudante']}")
 
def excluir(tipo,dado):
    if tipo == "estudantes":
        data = carregar(tipo)
        achou = False
        for i in data:
            if i['codigo_estudante'] == dado:
                data.remove(i)
                print("Estudante removido")
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")
    if tipo == "professores":
        data = carregar(tipo)   
        achou = False
        for i in data:
            if i['codigo_professor'] == dado:
                data.remove(i)
                print("Professor removido")
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")   
    if tipo == "disciplinas":
        data = carregar(tipo)
        achou = False
        for i in data:
            if i['codigo_disciplina'] == dado:
                data.remove(i)
                print("Disciplina removida")
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")
    if tipo == "turmas":
        data = carregar(tipo)
        achou = False
        for i in data:
            if i['codigo_turma'] == dado:
                data.remove(i)
                print("Turma removida")
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")
    if tipo == "matriculas":
        data = carregar(tipo)
        achou = False
        for i in data:
            if i['codigo_turma'] == dado:
                data.remove(i)
                print("Matricula removida")
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")
#mostrar que foi alterado e mostrar na parte das duas ultimas oq esta incorreto
def editar(tipo,dado):
    if tipo == "estudantes":
        data = carregar(tipo)
        achou = False
        for i in data:
            if i['codigo_estudante'] == dado:
                print(f"CÓDIGO : {dado} encontrado, informe os novos dados do estudante a baixo: ")
                try:
                    cod = int(input("Digite o código do estudante: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                nome = input("Digite o novo nome do estudante: ")
                matricula = input("Digite a nova matrícula do estudante: ")

                i['codigo_estudante'] = cod
                i['nome'] = nome
                i['matricula'] = matricula
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")
    if tipo == "professores":
        data = carregar(tipo)   
        achou = False
        for i in data:
            if i['codigo_professor'] == dado:
                try:
                    cod = int(input("Digite o novo código do professor: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                nome = input("Digite o novo nome do professor: ")
                cpf = input("Digite o novo CPF do professor: ")

                i['codigo_professor'] = cod
                i['nome'] = nome
                i['cpf'] = cpf
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")   
    if tipo == "disciplinas":
        data = carregar(tipo)
        achou = False
        for i in data:
            if i['codigo_disciplina'] == dado:
                try:
                    cod = int(input("Digite o novo código da disciplina: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                nome = input("Digite o novo nome da disciplina: ")
                
                i['codigo_disciplina'] = cod
                i['nome'] = nome
                salvar(data, tipo)
                achou = True
                break
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")
    if tipo == "turmas":
        data = carregar(tipo)
        professores = carregar("professores")
        disciplinas = carregar("disciplinas")
        achou = False
        for i in data:
            if i['codigo_turma'] == dado:
                try:
                    cod = int(input("Digite o novo código da turma: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                try:
                    cod_1 = int(input("Digite o novo código da professor: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                try:
                    cod_2 = int(input("Digite o novo código da disciplina: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                for professor in professores:
                    if professor['codigo_professor'] == cod_1:
                        encontrado = True
                encontrado_2 = False
                for disciplina in disciplinas:
                    if disciplina['codigo_disciplina'] == cod_2:
                        encontrado_2 = True
                if encontrado and encontrado_2 == True:

                    i['codigo_turma'] = cod
                    i['codigo_professor'] = cod_1
                    i['codigo_disciplina'] = cod_2
                    salvar(data, tipo)
                    achou = True
                    break
                else:
                    input("Algum dos dados está incorreto, digite ENTER para voltar")
                    break
                
            if not achou:
                print(f"{dado} Não encontrado, rever lista.")
    if tipo == "matriculas":
        data = carregar(tipo)
        turmas = carregar("turmas")
        estudantes = carregar("estudantes")
        achou = False
        for i in data:
            if i['codigo_turma'] == dado:
                try:
                    cod = int(input("Digite o novo código da turma: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                try:
                    cod_1 = int(input("Digite o novo código do estudante: "))
                except ValueError:
                    input("Digite apenas números, ENTER para continuar")
                    continue
                encontrado = False
                for turma in turmas:
                    if turma['codigo_turma'] == cod:
                        encontrado = True
                encontrado_2 = False
                for estudante in estudantes:
                    if estudante['codigo_estudante'] == cod_1:
                        encontrado_2 = True
                if encontrado and encontrado_2 == True:
                    
                    i['codigo_turma'] = cod
                    i['codigo_estudante'] = cod_1
                    salvar(data, tipo)
                    achou = True
                    break
                else:
                    input("Você digitou algo errado, digite ENTER para voltar")
                    break
                        
        if not achou:
            print(f"{dado} Não encontrado, rever lista.")

    


def menu():
    op = "-1"
    while op != "0":
        op = input("""

---MENU PRINCIPAL---


1) Gerenciar estudantes.
2) Gerenciar professores.
3) Gerenciar disciplinas.
4) Gerenciar turmas.
5) Gerenciar matriculas.
0) Sair

Digite a opção aqui: """)
        if op =="1":
            menu_2("estudantes")
        if op =="2":
            menu_2("professores")
        if op =="3":
            menu_2("disciplinas")
        if op =="4":
            menu_2("turmas")
        if op =="5":
            menu_2("matriculas")
        if op =="0":
            break
        else:
            print(f"'{op}' Não é um comando valido.")

def menu_2(tipo):
    while True:
        op_2 = input(f"""

---GERENCIAMENTO DE {tipo.upper()}---

1) Listar
2) Adicionar
3) Alterar
4) Excluir
5) Voltar ao Menu

Digite a opção desejada aqui: """)
        if op_2 == "1":
            lista(tipo)
        if op_2 == "2":
            add(tipo)
        if op_2 == "3":
            try:
                dado = int(input(f"Digite o codigo do(a) {tipo}: "))
                editar(tipo,dado)  
            except ValueError:
                print("Digite um número.")
        if op_2 == "4":
            try:
                dado = int(input(f"Digite o codigo do(a) {tipo}: "))
                excluir(tipo,dado)
            except ValueError:
                print("Digite um número.")
        if op_2 == "5":
            break




menu()