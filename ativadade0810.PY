#lista atividade di a08/10
#questao 1
"""idades = []
for x in range(10):
    x = float(input("adicione uma nota: "))
    idades.append(x)
qua = sum(idades) / len(idades)
ordenar = sorted(idades)
print(ordenar)
n = len(idades)
meio = n // 2
def median():
    if n % 2 == 1:
        mediana = ordenar[meio]
    else:
        mediana = (ordenar[meio - 1] + ordenar[meio]) / 2
    print(mediana)
median()"""

"""bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul","vermelha","verde","azul","vermelha"]
quant = len(bolas)
verm = bolas.count("vermelha")
prob = verm / quant
print(bolas)
print("")
print(f"A quantidade de bolhinhas e de {quant}")
print(f"Existe {verm} bolinhas vermelhas")
print(f"Fração:{verm}/{quant} de cair vermelha")
print(f"Probabilidade de cair uma vermelha e de {prob:.0%}")"""


"""alunos = [
["Ana", 7.5, 8.0, 9.0],
["Bruno", 6.0, 5.5, 7.0],
["Carlos", 9.0, 8.5, 10.0],
["Daniela", 5.0, 6.0, 4.5],
["Eduardo", 8.0, 7.5, 6.5]
]
notass = []
nomes = []
maior_med = 0
melhor_aluno = ""
menor_med = float("inf")
pior_aluno = ""
resu_apro = []
resu_repro = []
for sub in alunos:
    nomes.append(sub[0])
    nome = sub[0]
    notas = sub[1:]
    media = sum(notas) / len(notas)
    notass.extend(sub[1:])
    mediag = sum(notass) / len(notass)
    print(f"{nome}: {media:.2f}")
    if media >= 7:
        print("O aluno foi aprovado")
        print("")
        resu_apro.append("aprovado")
        
    else:
        print("aluno foi reprovado")
        print("")
        resu_repro.append("reprovado")
    if media > maior_med:
        maior_med = media
        melhor_aluno = nome
    if media < menor_med:
        menor_med = media
        pior_aluno = nome

print(f"Média geral da turma: {mediag:.2f}")
print(f"Maior média: {melhor_aluno} ({maior_med:.2f})")
print(f"Menor média: {pior_aluno} ({menor_med:.2f})")
print(f"Aprovados: {len(resu_apro)}")
print(f"Reprovados: {len(resu_repro)}")"""


"""precos = [50, 80, 120, 35, 200, 75]
novos_precos = [round(preco * 1.10, 2) for preco in precos]

print(novos_precos) """ 

"""placa = input("Qual o seu nome?: ") # muda esssa indetificar 
horas = float(input("Tempo de permanencia (em horas): "))
def calcular(horas):
    if horas <= 1:
        return 5.00
    elif horas <= 3:
        return 10.00
    elif horas <= 5:
        return 15.00
    else:
        return 20.00

valor = calcular(horas)
print(f"Nome: {placa}")
print(f"Tempo: {horas} hora(s)")
print(f"Valor a pagar: R$ {valor:.2f}")"""

""""def calcular_id():
    resul = ano_hoje - ano_nasc
    if mes_hoje < mes_nasc or (mes_hoje == mes_nasc and dia_hoje < dia_nasc):
        resul -= 1
    
    if resul >= 18:
        print("maior de idade")
    else:
        print("menor de idade")
    print(resul)
dia_nasc = int(input("Dia de nascimento: "))
mes_nasc = int(input("Mês de nascimento: "))
ano_nasc = int(input("Ano de nascimento: "))

dia_hoje = int(input("Dia de hoje: "))
mes_hoje = int(input("Mês de hoje: "))
ano_hoje = int(input("Ano de hoje: "))

calcular_id()"""

"""def losango():
    print("Você está calculando a área do losango")
    diagonal_maior = float(input("Medida da diagonal maior: "))
    diagonal_menor = float(input("Medida da diagonal menor: "))
    area = (diagonal_maior * diagonal_menor) / 2
    print(f"A área do losango é de: {area:.2f}")

def triangulo():
    print("Você está calculando a área do triângulo")
    base = float(input("Qual o valor da base?: "))
    altura = float(input("Qual o valor da altura?: "))
    area = (base * altura) / 2
    print(f"A área do triângulo é de: {area:.2f}")

def trapezio():
    print("Você está calculando a área do trapézio")
    base_maior = float(input("Qual o valor da base maior?: "))
    base_menor = float(input("Qual o valor da base menor?: "))
    altura = float(input("Qual o valor da altura?: "))
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é de: {area:.2f}")

while True:
    print("\n0 - Sair")
    print("1 - Losango")
    print("2 - Triângulo")
    print("3 - Trapézio")

    try:
        usu = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números")
        continue

    if usu == 1:
        losango()
    elif usu == 2:
        triangulo()
    elif usu == 3:
        trapezio()
    elif usu == 0:
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")"""
def validar_senha(senha):
    if len(senha) < 8:
        return False
    for caractere in senha:
        if caractere.isdigit():
            return True
    return False

while True:
    senha = input("Digite a senha: ")

    if validar_senha(senha):
        print("Senha válida")
        break
    print("Inválida: mínimo de 8 caracteres e pelo menos um número")