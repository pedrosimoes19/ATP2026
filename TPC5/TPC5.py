def ler_nota(texto):
    nota = float(input(texto))
    while nota < 0 or nota > 20:
        print("Nota inválida! A nota deve ser entre 0 e 20.")
        nota = float(input(texto))
    return nota

def menu():
    turma = []
    opçao = ""
    while opçao != "0":
        print("""Este é o menu:
(1) Criar turma
(2) Inserir um aluno na turma
(3) Listar a turma
(4) Consultar um aluno por id
(5) Guardar a turma em ficheiro
(6) Carregar uma turma dum ficheiro
(0) Sair""")

        opçao = input("Escolhe uma opção de 0 a 6: ")

        if opçao in ["2", "3", "4", "5"] and len(turma) == 0:
                        print("A turma está vazia! Escolhe primeiro a opção 1 ou a 6.")

        elif opçao == "1":
            nda = int(input("Insere o número de alunos da turma: "))            #nda --> número de alunos
            turma = []
            for i in range(nda):
                nome = input(f"Insere o nome do aluno {i + 1}: ")
                id = input(f"Insere o id do aluno {i + 1}: ")
                notaTPC = ler_nota("Nota do TPC: ")
                notaProj = ler_nota("Nota do projeto: ")
                notaTeste = ler_nota("Nota do teste: ")
                aluno = (nome, id, [notaTPC, notaProj, notaTeste])
                turma.append(aluno)
            print(f"Turma criada: {turma}")

        elif opçao == "2":
            nome = input("Insere o nome do aluno: ")
            id = input("Insere o id do aluno: ")
            notaTPC = ler_nota("Nota do TPC: ")
            notaProj = ler_nota("Nota do projeto: ")
            notaTeste = ler_nota("Nota do teste: ")
            aluno = (nome, id, [notaTPC, notaProj, notaTeste])
            turma.append(aluno)

        elif opçao == "3":
            for nome, id, notas in turma:
                print(f"Nome: {nome}, id: {id}, nota do TPC: {notas[0]}, nota do projeto: {notas[1]}, nota do teste: {notas[2]}.")

        elif opçao == "4":
            encontrado = False
            while encontrado == False:
                id = input("Insere o id do aluno a consultar: ")
                for nome, id_aluno, notas in turma:
                    if id == id_aluno:
                        print(f"Nome: {nome}, id: {id_aluno}, nota do TPC: {notas[0]}, nota do projeto: {notas[1]}, nota do teste: {notas[2]}.")
                        encontrado = True
                if encontrado == False:
                    print("id inválido! Tenta novamente.")

        elif opçao == "5":
            ndf = input("Insere o nome do ficheiro: ")           #ndf --> nome do ficheiro
            f = open(f"{ndf}.txt", "w")                                   #f --> ficheiro
            for nome, id, notas in turma:
                f.write(f"{nome}|{id}|{notas[0]}|{notas[1]}|{notas[2]}\n")
            f.close()
            print("A turma foi guardada em ficheiro!")

        elif opçao == "6":
            ndf = input("Insere o nome do ficheiro: ")
            f = open(f"{ndf}.txt", "r")
            turma = []
            for linha in f:
                linha_limpa = linha.strip()
                dados = linha_limpa.split("|")
                notas = [float(dados[2]), float(dados[3]), float(dados[4])]
                turma.append((dados[0], dados[1], notas))
            f.close()
            print("A turma foi carregada!")
                
        elif opçao == "0":
            print(f"Aplicação terminada.")
            
        else:
            print("Opção inválida! Por favor escolhe uma opção de 0 a 6.")
            
menu()                                                             