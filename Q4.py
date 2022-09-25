'''Desenvolver um programa para verificar a maior do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e, 
assim calcular o total de acertos e a maior (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:

a. Maior e Menor Acerto;

b. Total de Alunos que utilizaram o sistema;

c. A Média das Notas da Turma.

Gabarito da Prova: 
01 - A 
02 - B 
03 - C 
04 - D 
05 - E 
06 - E 
07 - D 
08 - C 
09 - B 
10 – A

Após concluir isto você poderia incrementar o programa permitindo que o professor
digite o gabarito da prova antes dos alunos usarem o programa. '''

gab = []
alun = acertos = total_acerto = maior = menor = cont = 0
aux = []
for x in range(10):
    prof = input(f"DIGITE O GABARITO DA PROVA >>> QUESTÃO {x+1}: ").upper()
    gab.append(prof)
while True:
    alun += 1
    for i in range(10):
        prova = input("\nDIGITE SEU GABARITO >>> QUESTÃO " + str(i+1) + ": ").upper()
        aux.append(prova)
    for j, nt in enumerate(aux):
        if nt == gab[j]:
            acertos += 1
            total_acerto += 1
    cont += 1
    if acertos > maior:
        maior = acertos
    if (acertos < menor) or (cont == 1):
        menor = acertos

    perg = int(input("\nDIGITE [1] SE NINGUEM MAIS FOR USAR OU [2] SE OUTRO ALUNO FOR UTILIZAR: "))
    if perg == 1:
        break
    elif perg == 2:
        acertos = 0
        aux.clear()

media = (total_acerto / alun)
print('\n')
print('-='*30)
print(f"MAIOR NOTA: {maior:.1f}")
print(f"MENOR NOTA: {menor:.1f}")
print(f"TOTAL DE ALUNOS: {alun}")
print(f"MÉDIA DA TURMA: {media:.1f}")
print('-='*30)