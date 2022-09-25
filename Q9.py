'''9. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, 
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles. 
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse e o tipo de defeito.

tipo de defeito:
· necessita da esfera;
· necessita de limpeza; necessita troca do cabo ou conector; quebrado ou inutilizado. Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100 
Situação                                Quantidade          Percentual 
1- necessita da esfera                      40                 40% 
2- necessita de limpeza                     30                 30% 
3- necessita troca do cabo ou conector      15                 15% 
4- quebrado ou inutilizado                  15                 15% '''

mouse = esf = limp = cabo = quebr = 0
while True:
    mouse += 1
    ident = int(input("\nNÚMERO DE IDENTIFICAÇÃO DO MOUSE: "))
    if ident == 0:
        mouse -= 1
        break
    defeito = int(input("\nDEFEITOS >>> [1] PARA ESFERA, [2] LIMPEZA, [3] TROCA DE CABO/CONECTOR, [4] QUEBRADO/INUTILIZADO: "))
    if defeito == 1:
        esf += 1
    elif defeito == 2:
        limp += 1
    elif defeito == 3:
        cabo += 1
    elif defeito:
        quebr += 1
    
perc_esf = (esf / mouse)*100
perc_limp = (limp / mouse)*100
perc_cabo = (cabo / mouse)*100
perc_quebr = (quebr / mouse)*100 
print(f"\nQUANTIDADE DE MOUSES: {mouse}")
print("SITUAÇÃO                                 QUANTIDADE              PERCENTUAL")
print(f"1-NECESSITA DA ESFERA                     {esf}                        {perc_esf:.1f}%")
print(f"2-NECESSITA DE LIMPEZA                    {limp}                        {perc_limp:.1f}%")
print(f"3-NECESSITA TROCA DO CABO OU CONECTOR     {cabo}                        {perc_cabo:.1f}%")
print(f"4-QUEBRADO OU INUTILIZADO                 {quebr}                        {perc_quebr:.1f}%")