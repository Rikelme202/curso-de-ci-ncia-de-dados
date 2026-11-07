import random as rd 
print("seja bem vindo ao jogo de adivinhação de numeros aleatorios") #1 Questão
print("")
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
        print("o numero aleatorio e maior")
        