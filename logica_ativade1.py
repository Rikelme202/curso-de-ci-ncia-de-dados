'''1. Verificador de Par ou Ímpar. Peça ao usuário um número inteiro e diga se ele
é par ou ímpar'''

'''print("seja bem vindo ao programa de par ou impar")
numero = int(input("digite um numero: "))
if numero % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")'''

'''2. Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como
"Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso"
(65 anos ou mais)'''

'''print("bem vindo ao programa de classificação de idade")
idade = int(input("digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("você e uma Criança")
elif idade >= 13 and idade <= 17:
    print("você e um Adolescente")
elif idade >= 18 and idade <= 64:
    print("você e um Adulto")
else:
    print("você e um Idoso")'''

'''3. Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher
entre as operações de soma, subtração, multiplicação e divisão. Peça dois
números e a operação desejada. Imprima o resultado.'''

'''print('bem vindo a calculadora, selecione a operação desejada')
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
usuario = int(input('digite o numero da operação desejada: '))
if usuario == 1: 
    numero1 = int(input('digite o primeiro numero: '))
    numero2 = int(input('digite o segundo numero: '))
    resultado = numero1 + numero2
    print(f'o resultado da soma é {resultado}')
elif usuario == 2:
    numero1 = int(input('digite o primeiro numero: '))
    numero2 = int(input('digite o segundo numero: '))
    resultado = numero1 - numero2
    print(f'o resultado da subtração é {resultado}')
elif usuario == 3:
    numero1 = int(input('digite o primeiro numero: '))
    numero2 = int(input('digite o segundo numero: '))
    resultado = numero1 * numero2
    print(f'o resultado da multiplicação é {resultado}')
elif usuario == 4:  
    numero1 = int(input('digite o primeiro numero: '))
    numero2 = int(input('digite o segundo numero: '))
    if numero2 == 0:
        print('não é possível dividir por zero')
    else:
        resultado = numero1 / numero2
        print(f'o resultado da divisão é {resultado}')
else:
    print('operação inválida')'''

'''4. Classificador de Triângulos. Peça ao usuário para digitar o comprimento de
três lados de um triângulo. Determine se os lados formam um triângulo válido
e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno.
Regras'''

'''print('bem vindo ao programa de classificação de triângulos')
lado1 = float(input('digite o valor do primeiro lado: '))
lado2 = float(input('digite o valor do segundo lado: '))
lado3 = float(input('digite o valor do terceiro lado: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print('o triangulo e equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('o triângulo é isósceles')
    else:
        print('o triângulo é escaleno')
else:
    print('os lados não formam um triângulo válido')'''

'''5. Solicite os coeficientes a, b e c de uma equação do segundo grau (ax² + bx + c
= 0). Determine e mostre o número de raízes reais distintas que a equação
possui. Regra: O número de raízes reais depende do discriminante (delta)'''

'''print('===bem vindo ao programa de equação do segundo grau===')
a = float(input('digite o valor de a:'))
b = float(input('digite o valor de b:'))
c = float(input('digite o valor de c:'))
delta = b**2 - 4*a*c
if delta > 0:
    print('a equação possui duas raízes reais distintas')
elif delta == 0:
    print('a equação possui uma raiz real')
else:
    print('a equação não possui raízes reais,raizes complexas')'''

'''6. Peça ao usuário a temperatura da água (em graus Celsius). Determine o
estado físico da água (sólido, líquido ou gasoso). Regras:'''

"""print('===bem vindo ao programa de estado físico da água===')
temperatura = float(input('digite a temperatura da água em graus Celsius: '))
if temperatura <= 0:
    print('a água está no estado sólido (gelo)')
elif 0 < temperatura < 100:
    print('a água está no estado líquido')
else:
    print('a água está no estado gasoso (vapor)')"""

"""7. Uma empresa de vendas possui corretores. A empresa paga ao corretor uma
comissão calculada de acordo com o valor de suas vendas"""

"""print('===bem vindo ao programa de comissão de vendas===')
nome = input("digite o seu nome: ")
vendas = float(input("digite o valor total da venda: "))
if vendas < 500:
    comissao = vendas * 0.06
    print(f"{nome}, sua comissao é de R$ {comissao:.2f}")
elif 500 <= vendas < 700:
    comissao = vendas * 0.085
    print(f"{nome}, sua comissao é de R$ {comissao:.2f}")
elif 700 <= vendas < 1000:
    comissao = vendas * 0.10
    print(f"{nome}, sua comissao é de R$ {comissao:.2f}")
elif vendas >= 1000:
    comissao = vendas * 0.12
    print(f"{nome}, sua comissao é de R$ {comissao:.2f}")
else:
    print("valor de venda inválido")"""

"""8. Ajude um hotel da cidade a calcular o valor da hospedagem"""

print('===bem vindo ao programa de cálculo de hospedagem===')
dia = int(input('digite a quantidade de dias de hospedagem: '))
diaria = dia * 290
if dia > 7:
    valor = dia * 6.50
    total = valor + diaria
    print(f'o valor total da hospedagem é R$ {total:.2f}')
elif dia == 7:
    valor = dia * 12
    total = valor + diaria
    print(f'o valor total da hospedagem é R$ {total:.2f}')
else:
    valor = dia * 16.50 
    total = valor + diaria
    print(f'o valor total da hospedagem é R$ {total:.2f}')