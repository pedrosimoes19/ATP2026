from matplotlib import pyplot as plt

def medias(tabMeteo):
    res = []
    for data, tmin, tmax, _ in tabMeteo:
        media = (tmin + tmax) / 2
        res.append((data, media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}|\n")
    file.close()

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        linha_limpa = line.strip()
        if linha_limpa != "":
            partes = linha_limpa.split("|")
            ano, mes, dia = partes[0].split("-")
            data = (int(ano), int(mes), int(dia))
            tmin = float(partes[1])
            tmax = float(partes[2])
            prec = float(partes[3])
            res.append((data, tmin, tmax, prec))
    file.close()
    return res

def minMin(tabMeteo):
    tbaixa = None
    if len(tabMeteo) > 0:
        tbaixa = tabMeteo[0][1]
        for _, tmin, _, _ in tabMeteo:
            if tmin < tbaixa:
                tbaixa = tmin
    return tbaixa

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, _ in tabMeteo:
        res.append((data, tmax - tmin))
    return res

def maxChuva(tabMeteo):
    resultado = None
    if len(tabMeteo) > 0:
        max_data = tabMeteo[0][0]
        max_prec = tabMeteo[0][3]
        for data, _, _, prec in tabMeteo:
            if prec > max_prec:
                max_prec = prec
                max_data = data
        resultado = (max_data, max_prec)
    return resultado

def diasChuvosos(tabMeteo, p):
    res = []
    for data, _, _, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res

def maxPeriodoCalor(tabMeteo, p):
    consecutivo = 0
    max_dias = 0
    for _, _, _, prec in tabMeteo:
        if prec < p:
            consecutivo = consecutivo + 1
            if consecutivo > max_dias:
                max_dias = consecutivo
        else:
            consecutivo = 0
    return max_dias

def grafTabMeteo(t):
    if len(t) == 0:
        print("A tabela está vazia!")
    else:
        x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
        y_min = [tmin for _, tmin, _, _ in t]
        y_max = [tmax for _, _, tmax, _ in t]
        y_prec = [prec for _, _, _, prec in t]

        plt.figure()
        plt.plot(x, y_min, color="blue", marker="o", label="Tmin ºC")
        plt.plot(x, y_max, color="red", marker="o", label="Tmax ºC")
        plt.title("Temperaturas Mínima e Máxima")
        plt.xlabel("Data (AAAA-MM-DD)")
        plt.ylabel("Temperatura (ºC)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.bar(x, y_prec, color="skyblue", label="Precipitação (mm)")
        plt.title("Precipitação Diária")
        plt.xlabel("Data (AAAA-MM-DD)")
        plt.ylabel("Precipitação (mm)")
        plt.legend()
        plt.grid(axis='y')
        plt.show()

def menu():
    print("""\nGestão de dados meteorológicos:
1. Adicionar registo de dia à tabela
2. Listar registos da tabela atual
3. Calcular temperatura média de cada dia
4. Calcular a temperatura mínima mais baixa
5. Calcular a amplitude térmica de cada dia
6. Determinar o dia de precipitação máxima
7. Listar dias com precipitação superior a um limite
8. Maior sequência de dias com precipitação abaixo de um limite
9. Desenhar gráficos meteorológicos
10. Guardar tabela num ficheiro de texto
11. Carregar tabela de um ficheiro de texto
0. Sair""")
    opçao = input("Escolhe uma opção: ")
    return opçao

def iniciar():
    tabMeteo = []
    executar = True

    while executar:
        opçao = menu()

        if opçao == "1":
            ano = int(input("Ano (ex: 2026): "))
            mes = int(input("Mês (1-12): "))
            dia = int(input("Dia (1-31): "))
            tmin = float(input("Temperatura Mínima (ºC): "))
            tmax = float(input("Temperatura Máxima (ºC): "))
            prec = float(input("Precipitação (mm): "))
            registo = ((ano, mes, dia), tmin, tmax, prec)
            tabMeteo.append(registo)
            print("Registo inserido com sucesso!")

        elif opçao == "2":
            if len(tabMeteo) == 0:
                print("A tabela está vazia!")
            else:
                print("\nData (A-M-D) | Tmin (ºC) | Tmax (ºC) | Prec (mm)")
                print("-" * 45)
                for data, tmin, tmax, prec in tabMeteo:
                    print(f"{data[0]}-{data[1]:02d}-{data[2]:02d}   | {tmin:<9} | {tmax:<9} | {prec}")

        elif opçao == "3":
            if len(tabMeteo) == 0:
                print("A tabela está vazia!")
            else:
                res = medias(tabMeteo)
                for data, m in res:
                    print(f"Data: {data[0]}-{data[1]:02d}-{data[2]:02d} -> Média: {m:.2f} ºC")

        elif opçao == "4":
            if len(tabMeteo) == 0:
                print("A tabela está vazia!")
            else:
                resultado = minMin(tabMeteo)
                print(f"Temperatura mínima mais baixa: {resultado} ºC")

        elif opçao == "5":
            if len(tabMeteo) == 0:
                print("A tabela está vazia!")
            else:
                res = amplTerm(tabMeteo)
                for data, amp in res:
                    print(f"Data: {data[0]}-{data[1]:02d}-{data[2]:02d} -> Amplitude: {amp:.2f} ºC")

        elif opçao == "6":
            if len(tabMeteo) == 0:
                print("A tabela está vazia!")
            else:
                res = maxChuva(tabMeteo)
                data = res[0]
                valor = res[1]
                print(f"Maior precipitação foi de {valor} mm no dia {data[0]}-{data[1]:02d}-{data[2]:02d}.")

        elif opçao == "7":
            if len(tabMeteo) == 0:
                print("A tabela está vazia.")
            else:
                limite = float(input("Insere o limite de precipitação (mm): "))
                res = diasChuvosos(tabMeteo, limite)
                if len(res) == 0:
                    print(f"Não existem dias com precipitação superior a {limite} mm.")
                else:
                    for data, p in res:
                        print(f"Data: {data[0]}-{data[1]:02d}-{data[2]:02d} -> {p} mm")

        elif opçao == "8":
            if len(tabMeteo) == 0:
                print("A tabela está vazia!")
            else:
                limite = float(input("Insere o limite de precipitação (mm): "))
                seq = maxPeriodoCalor(tabMeteo, limite)
                print(f"Maior sequência de dias com precipitação < {limite} mm: {seq} dia(s).")

        elif opçao == "9":
            grafTabMeteo(tabMeteo)

        elif opçao == "10":
            if len(tabMeteo) == 0:
                print("A tabela atual está vazia!")
            fnome = input("Nome do ficheiro para guardar: ")
            guardaTabMeteo(tabMeteo, fnome)
            print(f"Dados guardados com sucesso em '{fnome}'.")

        elif opçao == "11":
            fnome = input("Nome do ficheiro a carregar: ")
            tabMeteo = carregaTabMeteo(fnome)
            print("Dados carregados com sucesso!")

        elif opçao == "0":
            executar = False
            print("Programa terminado!")

        else:
            print("Opção inválida, tenta novamente.")

iniciar()