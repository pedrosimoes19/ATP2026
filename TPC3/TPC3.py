import random
jogar_novamente = "s"
print("Sê bem-vindo ao jogo da corrida aos 100!")
print("O total começa em 0.")
print("Os dois jogadores somam alternadamente um número de 1 a 10 ao total.")
print("O jogador que atingir exatamente o número 100 vence!")
while jogar_novamente.lower() == "s":
    a = input ("Quem começa? (1- Utilizador / 2- Computador): ")
    while a != "1" and a != "2":
        print ("Escreve 1 ou 2: ")
        a = input ("Quem começa? (1- Utilizador / 2- Computador): ")
    if a == "1":
        total = 0
        print(f"O jogo começa agora! Total: {total}" )
        while total < 100:
            limite_u = min(10, 100 - total)
            nu = int(input(f"Soma um número de 1 a {limite_u} ao total: "))         #nu = número do utilizador
            while nu < 1 or nu > limite_u :
                print(f"O número tem de estar entre 1 e {limite_u}!")
                nu = int(input("Soma um número ao total: ")) 
            total = total + nu
            print(f"Total atual: {total}")
            if total == 100:
                print("Parabéns, chegaste aos 100 e venceste!")
            else:
                limite_c = min(10, 100 - total)
                nc = (12 - (total % 11)) % 11              #nc = número do computador
                if nc == 0 or nc > limite_c:
                    nc = random.randint(1, limite_c)               
                total = total + nc              
                print(f"Eu somo o número {nc} ao total. Total: {total}")
                if total == 100:
                    print("Cheguei aos 100, venci!")
    elif a == "2":
        total = 0
        print(f"O jogo começa agora! Total: {total}" )
        nc = 1
        total = total + nc
        print(f"Eu jogo {nc}")
        print(f"Total atual: {total}")
        while total < 100:
            limite_u = min(10, 100 - total)
            nu = int(input(f"Soma um número de 1 a {limite_u} ao total: "))
            while nu < 1 or nu > limite_u :
                print(f"O número tem de estar entre 1 e {limite_u}!")
                nu = int(input("Soma um número ao total: "))
            total = total + nu
            print(f"Total atual: {total}")
            if total == 100:
                print("Parabéns, chegaste aos 100 e venceste!")
            else:
                nc = 11 - nu
                if 100 - total <= 10:
                    nc = 100 - total
                total = total + nc
                print(f"Eu somo o número {nc} ao total. Total: {total}")
                if total == 100:
                    print("Cheguei aos 100, venci!")
    jogar_novamente = input("Queres jogar novamente? ( Sim - S / Não - qualquer outra tecla ) ")
