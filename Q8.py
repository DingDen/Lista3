'''8. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, 
quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

· O modelo do modelo mais econômico;

· Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros 
e quanto isto custará, considerando que a gasolina custe R$ 2,25 o litro. 
Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa.

    Comparativo de Consumo de Combustível 
    Veículo 1 
    Nome: fusca
    Km por litro: 7 

    Veículo 2 
    Nome: gol 
    Km por litro: 10 
    
    Veículo 3 
    Nome: uno 
    Km por litro: 12.5 
    
    Veículo 4 
    Nome: Vectra 
    Km por litro: 9 
    
    Veículo 5 
    Nome: Peugeout 
    Km por litro: 14.5 
    
    Relatório Final 
    1 - fusca - 7.0 - 142.9 litros - R$ 321.43 
    2 - gol - 10.0 - 100.0 litros - R$ 225.00 
    3 - uno - 12.5 - 80.0 litros - R$ 180.00 
    4 - vectra - 9.0 - 111.1 litros - R$ 250.00 
    5 - peugeout - 14.5 - 69.0 litros - R$ 155.17 
    O menor consumo é do peugeout. '''

carros = []
consum_s = []
gas = 2.25
dist = 1000
print("\nCOMPARATIVO DE CONSUMO DE COMBUSTÍVEL")
for i in range(5):
    print(f'VEÍCULO {i+1}')
    modelo = input(f"NOME DO CARRO >>> VEICULO {i+1}: ").upper()
    consum = float(input("CONSUMO EM KM/L: "))
    carros.append(modelo)
    consum_s.append(consum)
    print('\n')
aux = []    #LISTA PARA GUARDAR OS VALORES E VERIFICAR QUAL MAIS ECONÔMICO
print('-='*30)
print("\t\t\tRELATÓRIO FINAL")
for km, carro in enumerate(carros) :
    if (km == 0) or (km == 1) or (km == 2) or (km == 3) or (km == 4):
        c_dist = dist / consum_s[km] 
        p_lit = c_dist*gas
        aux.append(c_dist)
        aux.sort()         #DESSA FORMA, O MENOR CONSUMO SERÁ O ITEM DE ÍNDICE ZERO
    print(f"{km+1} - {carro}    -    {consum_s[km]} KM/L    -    {c_dist:.1f} L    -    R${p_lit:.2f}")
for i, car in enumerate(carros):     
    if aux[0]*consum_s[i] == dist:
        print(f"O MENOR CONSUMO É DO {car}")
