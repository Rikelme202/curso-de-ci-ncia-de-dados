'''numero fatorial'''

'''num = int(input('qual o seu numero?: '))
resultado = 1 
for i in range(1,num + 1):
    resultado *=i
print(f'o resultado do numero em fatorial e de {resultado }')'''


'''questao 2'''

'''cida1 = 90000
cida2 = 200000
tax_cid1 = 0.05
tax_cid2 = 0.015
anos = 0
while cida2 >= cida1:
    cida1 = cida1 * (1 + tax_cid1)
    cida2 = cida2 * (1 + tax_cid2)
    anos += 1
print(f' anos necessarios para isso acontecer {anos} anos')
print(f'a população da cidade 1 e de {cida1:.0f}')
print(f'a população da cidade 2 e de {cida2:.0f}')'''

'''3. Resumo estatístico de notas de um curso'''
'''notas = []
reprovados = 0
aprovados = 0
recuperação = 0
while True:
    conti = input('deseja adicionar uma nota? (sim/sair): ')
    if conti == 'sair':
        break
    else:
        try:
            nota = float(input('digite sua nota: '))
        except ValueError:
            print('opção invalida, digite uma nota entre 0 e 10')
            continue
        if nota < 0 or nota > 10:
            print('opção invalida, digite uma nota entre 0 e 10')
            continue
        notas.append(nota)

        if nota >= 7:
            aprovados += 1
        elif nota > 5 and nota < 7:
            recuperação += 1
        elif nota <= 5 and nota >= 0:
            reprovados += 1

qnotas = len(notas)
if qnotas > 0:
    por_apro = (aprovados / qnotas) * 100
    por_re = (reprovados/ qnotas) * 100 
    por_rec = (recuperação / qnotas) * 100
    medi = (sum(notas) / qnotas)
    print(f'total de notas analisadas {qnotas}')
    print(f'aprovados: {aprovados} com porcentagem de ({por_apro:.0f} %)')
    print(f'Reprovados: {reprovados} com porcentagem de ({por_re:.0f} %)')
    print(f'Recuperação: {recuperação} com porcentagem de ({por_rec:.0f} %)')
    print(f'media da turma: {medi:.2f}')
    if por_apro >= 70:
        print('desempenho satifatorio')
    else:
        print('desempenho baixo')
'''
 
'''4. Seleção de atributos para um modelo'''

'''n = int(input("Informe o número total de atributos (n): "))
r = int(input("Informe o número de atributos a selecionar (r): "))

if n < 0 or r < 0 or r > n:
    print("Parâmetros inválidos: é necessário que 0 <= r <= n.")
else:
    fatorial_n = 1
    for i in range(1, n + 1):
        fatorial_n *= i

    fatorial_r = 1
    for i in range(1, r + 1):
        fatorial_r *= i

    fatorial_nr = 1
    for i in range(1, n - r + 1):
        fatorial_nr *= i

    combinacoes = fatorial_n // (fatorial_r * fatorial_nr)

    print(f"Número de subconjuntos possíveis: {combinacoes}")

    if combinacoes <= 10000:
        print("Viabilidade: busca exaustiva viável.")
    else:
        print("Viabilidade: busca exaustiva inviável.")'''

'''5. Uma população inicial de 2727 indivíduos cresce a uma taxa de 4% ao ano'''

'''pop_ini = 2727
taxa = 0.04
for ano in range(1, 6):
    pop_ini = pop_ini * (1 + taxa)
    print(f'Ano {ano}: {pop_ini:.0f} indivíduos')'''


'''6. Probabilidade experimental de um número par'''
'''pares = 0 
total = 20
for i in range(total):
    resultado = int(input(f"informe o {i+1}º numero: "))
    if resultado % 2 == 0:
        pares += 1
        propabilidade = pares / total


print(f"Quantidade de números pares: {pares}")
print(f"Probabilidade experimental de número par: {probabilidade:.2f}")'''