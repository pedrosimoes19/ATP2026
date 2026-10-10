import random
def menu():
    lista = []
    opcao = ""
    while opcao != "0":
        print("Este é o menu: ")
        print("(1) Criar lista")
        print("(2) Ler lista")
        print("(3) Soma")
        print("(4) Média")
        print("(5) Maior")
        print("(6) Menor")
        print("(7) Está ordenada por ordem crescente")
        print("(8) Está ordenada por ordem decrescente")
        print("(9) Procura um elemento")
        print("(0) Sair")

        opcao = input("Escolhe uma opção de 0 a 9: ")

        if opcao in ["3", "4", "5", "6", "7", "8", "9"] and len(lista) == 0:
            print("A lista está vazia! Escolhe primeiro a opção 1 ou a 2.")
        
        elif opcao == "1":
            nde = int(input("Insere o número de elementos da lista: "))                 #nde --> número de elementos
            lista = []
            for i in range(nde):
                elemento = random.randint(1, 100)
                lista.append(elemento)
            print(f"Lista gerada: {lista}")
        
        elif opcao == "2":
            nde = int(input("Insere o número de elementos da lista: "))
            lista = []
            contador = 0
            while contador < nde:
                elemento = int(input(f"Insere o {contador + 1}º elemento da lista: "))
                contador = contador + 1
                lista.append(elemento)
            print(f"Lista gerada: {lista}")
        
        elif opcao == "3":
            print("Será calculada a soma dos elementos da lista: ")
            total = 0
            for elemento in lista:
                total = total + elemento
            print(f"A soma é {total}.")

        elif opcao == "4":
            print("Será calculada a média dos elementos da lista: ")
            soma = 0
            for elemento in lista:
                soma = soma + elemento
            media = soma / nde
            print(f"A média é {media}.")

        elif opcao == "5":
            print("Será calculado o maior elemento da lista: ")
            maior = lista[0]
            for elemento in lista:
                if elemento > maior:
                    maior = elemento
            print(f"O maior elemento da lista é {maior}.")
        
        elif opcao == "6":
            print("Será calculado o menor elemento da lista: ")
            menor = lista[0]
            for elemento in lista:
                if elemento < menor:
                    menor = elemento
            print(f"O menor elemento da lista é {menor}.")
        
        elif opcao == "7":
            print("Será que a lista está ordenada por ordem crescente?")
            ordenada = True
            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    ordenada = False
            if ordenada:
                print("Sim")
            else:
                print("Não")

        elif opcao == "8":
            print("Será que a lista está ordenada por ordem decrescente?")
            ordenada = True
            for i in range(len(lista) - 1):
                if lista[i] < lista[i + 1]:
                    ordenada = False
            if ordenada:
                print("Sim")
            else:
                print("Não")

        elif opcao == "9":
            ee = int(input("Seleciona o elemento que queres encontrar: "))                #ee --> elemento a encontrar
            posicoes = []
            for i in range(len(lista)):
                if lista[i] == ee:
                    posicoes.append(i)
            if posicoes == []:
                print(-1)
            else:
                print(posicoes)
        elif opcao == "0":
            pass

        else:
            print("Opção inválida! Por favor escolhe uma opção de 0 a 9.")

    if opcao == "0":
        print(f"Aplicação terminada. Lista final: {lista}.")

menu()

                


