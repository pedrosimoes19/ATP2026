import random
print("Sê bem-vindo ao jogo dos números!")
a = input ("Quem vai jogar? (1-utilizador / 2-computador): ")
while a!="1" and a!="2":
    print ("Escreve 1 ou 2!")
    input ("Quem vai jogar? (1-utilizador / 2-computador): ")
if a=="1":
    numero = random.randint(0,100)
    resposta = int(input("Adivinha o número de 0 a 100: " ))
    tentativas = 1
    while resposta<0 or resposta>100:
        print("Tem de ser um número entre 0 e 100!")
        resposta = int(input ("Tenta novamente: "))
    while resposta != numero:
        if resposta < numero:
            print ("O número é maior!")
        elif resposta > numero:
            print ("O número é menor!")
        resposta = int(input("Tenta novamente: "))
        while resposta<0 or resposta>100:
                print("Tem de ser um número entre 0 e 100!")
                resposta = int(input ("Tenta novamente: "))
        tentativas = tentativas + 1
    else:
        print("Acertaste!")
    print (f"Precisaste de {tentativas} tentativas! ")
elif a=="2":
    print("Estás pronto?")
    print("Pensa num número!")
    minimo = 0
    maximo = 100
    palpite = (minimo + maximo) // 2
    tentativas = 1
    adivinha = input(f"O teu número é {palpite}? (1-Maior / 2-Menor / 3-Correto)")
    while adivinha!="1" and adivinha!="2" and adivinha!="3":
        print ("Escreve 1, 2 ou 3!")
        adivinha = input(f"O teu número é {palpite}? (1-Maior / 2-Menor / 3-Correto)")
    while adivinha == "1" or adivinha == "2":
        if adivinha == "1":
            minimo = palpite + 1
            palpite = (minimo + maximo) // 2
            adivinha = input(f"O teu número é {palpite}? (1-Maior / 2-Menor / 3-Correto)")
        elif adivinha == "2":
            maximo = palpite - 1
            palpite = (minimo + maximo) // 2
            adivinha = input(f"O teu número é {palpite}? (1-Maior / 2-Menor / 3-Correto)")
        tentativas = tentativas + 1
    print (f"O teu número era {palpite}! ")
    print (f"Precisei de {tentativas} tentativas!")