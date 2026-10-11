# '''tem 3 variaves de cuso da passagem ônibus, metrõ/term e trilho (nessa mesma ordem)acredito ver uma forma de descartar os que não vão ser usados (isaac rocha)'''

# taronibus = 5,00
# tarmetro = 5,40
# tartrilho = 8,90

#DEIXE TUDO CADEADO NO PRIMEIRO WHILE NÃO PODE TER FORA DELE (ISAAC)

while True:
    print("SIMULADOR DE VALE-TRANSPORTE (VT)")
    print ("1 - Simular")
    print ("2 - Resumo")
    print ("3 - Encerrar")
    
    escolha = input("Escolha uma opção: ")

# Opção 1

    if escolha == '1' or escolha == 'simular':
        salario = float(input("Digite o salário: R$ "))
        dias = int(input("Dias trabalhados (1 a 26): "))
        conducoes = int(input("Conduções por dia (1 a 8): "))

        print("1 - Ônibus (R$ 5,00)")
        print("2 - Metrô/Trem (R$ 5,40)")
        print("3 - Integração (R$ 8,90)")

        tipo = input("Escolha o transporte: ")

        if tipo == "1":
            tarifa = 5.00
        elif tipo == "2":
            tarifa = 5.40
        elif tipo == "3":
            tarifa = 8.90
        else:
            print("Tipo de transporte inválido!")
# o código acima foi feito por Isaac