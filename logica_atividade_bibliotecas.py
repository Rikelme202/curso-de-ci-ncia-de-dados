import random as rd 
import math
'''print("seja bem vindo ao jogo de adivinhação de numeros aleatorios") #1 Questão
numero = rd.randint(1,100)
palpites = []
while True:
    usuario = int(input("")) 
    try:
        palpite = int(usuario)
    except ValueError:
        print("Isso não é um número inteiro. Tente de novo.")
        continue
    
    if usuario < 1 or usuario > 100:
         print("O número precisa estar entre 1 e 100.")
         continue
    palpites.append(usuario)

    if usuario == numero:
        print("parabéns Você Acertou o numero")
        print(f"a quantidade de tentativas foi de {len(palpites)}")
        print(f"seus palpites foram {palpites}")
        break
    elif usuario > numero:
        print("o numero aleatorio e menor")
    else:
        print("o numero aleatorio e maior")'''

#QUESTÃO 2
def triangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    if base > 0 and altura > 0:
        area = (base * altura) / 2
        print(f"E um Triangulo. Area de : {area:.2f}")
    else:
        print("não e um trinagulo, os valores devem ser maiores que zero")
def quadrado():
    lado = float(input("Lado: "))
    if lado > 0 :
        area = math.pow(lado,2)
        print(f"A area do quadrado: {area:.2f}")
    else:
        print("Não forma um quadrado: o lado deve ser maior que zero.")
def losango():
    D = float(input("Diagonal maior (D): "))
    d = float(input("Diagonal menor (d): "))
    if D > 0 and d > 0 and D >=d:
        area = (D * d) / 2
        lado = math.sqtr(math.pow(D / 2, 2) + math.pow(d / 2, 2))
        print(f"Area: {area:.2f}")
    else:
        print("Valores invalidos. ")
def retangulo():
    b = float(input("Base: "))
    h = float(input("Altura: "))

    if b > 0 and h > 0:
        area = b * h
        print(f"Área do retângulo: {area:.2f}")
    else:
        print("Retângulo inválido: valores devem ser maiores que zero.")
def trapézio():
    B = float(input("Base maior (B): "))
    b = float(input("Base menor (b): "))
    h = float(input("Altura (h): "))

    if B > 0 and b > 0 and h > 0 and B >= b:
        area = ((B + b) * h) / 2
        print(f"Área do trapézio: {area:.2f}")
    else:
        print("Trapézio inválido: valores devem ser maiores que zero e B >= b.")
def circulo():
    r = float(input("Raio (r): "))
    if r > 0:
        area = math.pi * math.pow(r, 2)
        print(f"Área do círculo: {area:.2f}")
    else:
        print("Círculo inválido: o raio deve ser maior que zero.")

areas = ["Tringulo", " Quadrado", "Losango","Retangulo", "Trapezio", "Circulo"]
for i, areas in enumerate(areas, start=1):
    print(f"{i}. {areas}")
escolha = int(input("digire a opção que deseja calcular"))
if escolha == 1:
    triangulo()
elif escolha == 2:
    quadrado()
elif escolha == 3:
    losango()
elif escolha == 4:
    retangulo()
elif escolha == 5:
    trapézio()
elif escolha == 6:
    circulo()
else:
    print("escolha uma opção")
    escolha = int(input("digire a opção que deseja calcular"))

#QUESTÃO 3