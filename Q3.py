'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

◦ 1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc) 
5 - Voto Nulo 
6 - Voto em Branco

Faça um programa que calcule e mostre:

◦ O total de votos para cada candidato;

◦ O total de votos nulos;

◦ O total de votos em branco;

◦ A percentagem de votos nulos sobre o total de votos;

◦ A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. '''

C1 = C2 = C3 = C4 = NULO = BRANCO = 0
list = ['AMANDA', 'BIA', 'CARLOS', 'DANIEL', 'VOTO NULO', 'VOTO EM BRANCO']
while True:
    print('\n\t1 - AMANDA\n\t2 - BIA\n\t3 - CARLOS\n\t4 - DANIEL\n\t5 - VOTO NULO\n\t6 - VOTO EM BRANCO\n')
    voto = int(input("\nESCOLHA O SEU CANDIDATO CONFORME A TABELA ACIMA: "))
    if voto == 0:
        break
    elif voto == 1:
        C1 += 1
    elif voto == 2:
        C2 += 1
    elif voto == 3:
        C3 += 1
    elif voto == 4:
        C4 += 1
    elif voto == 5:
        NULO += 1
    elif voto == 6:
        BRANCO += 1
TOTAL_VOTO = C1 + C2 + C3 + C4 + NULO + BRANCO
PERC_NULO = (NULO / TOTAL_VOTO)*100
PERC_BRANCO = (BRANCO / TOTAL_VOTO)*100

print(f'\n\t{list[0]}: {C1} voto(s)')
print(f'\t{list[1]}: {C2} voto(s)')
print(f'\t{list[2]}: {C3} voto(s)')
print(f'\t{list[3]}: {C4} voto(s)')
print(f'\t{list[4]}: {NULO} voto(s)')
print(f'\t{list[5]}: {BRANCO} voto(s)')
print(f'\tNº TOTAL DE VOTOS: {TOTAL_VOTO} voto(s)')
print(f'\n\tPERCENTUAL DE VOTOS NULO: {PERC_NULO:.1f}%')
print(f'\tPERCENTUAL DE VOTOS EM BRANCO: {PERC_BRANCO:.1f}%')