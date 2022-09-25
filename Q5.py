'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo 
Primeiro Salto: 6.5 m 
Segundo Salto: 6.1 m 
Terceiro Salto: 6.2 m 
Quarto Salto: 5.4 m 
Quinto Salto: 5.3 m 
Melhor salto: 6.5 m 
Pior salto: 5.3 m 
Média dos demais saltos: 5.9 m 
Resultado final: 
Rodrigo Curvêllo: 5.9 m '''


saltos = [] 
atletas = []
melhor = pior = cont = 0
'''quant = int(input("DIGITE QUANTOS ATLETAS PARTICIPARÃO DO PROGRAMA: "))'''
while True:
    cont += 1
    atleta = input("NOME DO ATLETA (se quiser encerrar o programa, aperte apenas [ENTER]): ").upper() 
    atletas.append(atleta)

    if atleta == '':
       cont -= 1
       break
    
    for i in range(5):
        salto = float(input(f"DIGITE OS VALORES DE CADA SALTO (METROS) >>> SALTO {i+1}: "))
        saltos.append(salto)
        saltos.sort()
        
    pior = saltos[0]
    melhor = saltos[4]
    media = (saltos[0] + saltos[1] + saltos[2] + saltos[3] + saltos[4] - (melhor + pior)) / 3
    
for x in range(cont):
    print('-='*30)
    print("\n\tNOME DO ATLETA: ", atletas[x])
    print(f"\tPRIMEIRO SALTO: {saltos[0]} m")
    print(f"\tSEGUNDO SALTO: {saltos[1]} m")
    print(f"\tTERCEIRO SALTO: {saltos[2]} m")
    print(f"\tQUARTO SALTO: {saltos[3]} m")
    print(f"\tQUINTO SALTO: {saltos[4]} m")
    print(f"\tMELHOR SALTO: {saltos[4]} m")
    print(f"\tPIOR SALTO: {saltos[0]} m")
    print(f"\tMÉDIA DOS SALTOS: {media:.1f} m")
    print("\n\tRESULTADO FINAl: ")
    print(f"\t{atletas[x]}: {media:.1f} m")
    print('-='*30)