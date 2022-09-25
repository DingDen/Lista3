'''Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e 
depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente 
Nota: 9.9 
Nota: 7.5 
Nota: 9.5 
Nota: 8.5 
Nota: 9.0
Nota: 8.5 
Nota: 9.7 
Resultado final: 
Atleta: Aparecido Parente 
Melhor nota: 9.9 
Pior nota: 7.5 
Média: 9,04 '''

notas = []
atletas = []
cont = melhor = pior = 0
while True:
    cont += 1
    atleta = input("DIGITE O NOME DO ATLETA OU APERTE [ENTER] PARA ENCERRAR O PROGRAMA: ").upper()
    atletas.append(atleta)

    if atleta == '':
        cont -= 1
        break
    
    for i in range(7):
        nota = float(input(f"NOTA DO JURADO {i+1}: "))
        notas.append(nota)
        notas.sort()

    melhor = notas[6]
    pior = notas[0]
    media = (notas[1] + notas[2] + notas[3] + notas[4] + notas[5]) / 5

for j in range(cont):
    print('-='*30)
    print("\n\tNOME DO ATLETA: ", atletas[j])
    print(f"\tNOTA: {notas[0]}")
    print(f"\tNOTA: {notas[1]}")
    print(f"\tNOTA: {notas[2]}")
    print(f"\tNOTA: {notas[3]}")
    print(f"\tNOTA: {notas[4]}")
    print(f"\tNOTA: {notas[5]}")
    print(f"\tNOTA: {notas[6]}")
    print("\n\tRESULTADO FINAl: ")
    print("\tNOME DO ATLETA: ", atletas[j])
    print(f"\tMELHOR NOTA: {melhor}")
    print(f"\tPIOR NOTA: {pior}")
    print(f"\tMÉDIA: {media:.2f}")
    print('-='*30)
