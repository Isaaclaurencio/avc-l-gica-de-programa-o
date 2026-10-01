'''tem 3 variaves de cuso da passagem ônibus, metrõ/term e trilho (nessa mesma ordem)acredito ver uma forma de descartar os que não vão ser usados (isaac rocha)'''

taronibus = 5,00
tarmetro = 5,40
tartrilho = 8,90

'''try serve como se fosse uma rede de segurança e com o except ele segura o programa sem dar erro usei para caso coloque lera ao inves de número não dar erro e parar o sistema (isaac rocha) '''


try:
    diaTrabalhados = int(input("Digite uantos dias você trabalha: "))
    salario = float(input("Digite seu  salário bruto use '.' (ponto) como divisor de milhar: "))
    qtdconduçõesdia = int(input("Digite quantas conduções você pega por dia: "))
except ValueError:
    print("Digite somente números")

