'''10. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
e identificar os usuários com maior espaço ocupado. 
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre                456123789 
anderson                 1245698456 
antonio                  123456456 
carlos                    91257581 
cesar                      987458 
rosemary                  789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, 
você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc. Uso do espaço em disco pelos usuários 
-------------------------------------------------------------------------------
Nr.      Usuário                 Espaço utilizado                    % do uso 
1       alexandre                    434,99 MB                        16,85% 
2        anderson                    1187,99 MB                       46,02% 
3        antonio                     117,73 MB                        4,56% 
4        carlos                      87,03 MB                         3,37% 
5         cesar                      0,94 MB                          0,04%
6       rosemary                     752,88 MB                        29,16% 

Espaço total ocupado: 2581,57 MB 
Espaço médio ocupado: 430,26 MB

O f de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
de forma a agilizar a execução do programa. 
A conversão do espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, 
que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, 
que será chamada pelo programa principal. '''

from asyncore import write

def byteMB(byte):
    conv = byte / (1024**2)
    return f'{conv:.2f}'

def usopercent(uso, tot):
    percent = (uso / tot)*100
    return f'{percent:.2f}'

usuarios = []
esp_utilizado = []
esp_total = Nr = 1
while True:
    usuario = input("DIGITE O USUARIO: ").lower()
    if usuario == '':
        break 
    else:
        usuarios.append(usuario)
    esp_entr = int(input("DIGITE O ESPAÇO: "))
    esp_utilizado.append(esp_entr)
for k in esp_utilizado:
    esp_total += k

media = esp_total / len(usuarios)

with open ("relat.txt", 'w') as f:
    f.write("ACME Inc. Uso do espaço em disco pelos usuários \n")
    f.write("---------------------------------------------------------------------------------\n")
    f.write("Nr.     Usuário                 Espaço utilizado                    % do uso\n")
    
    for ind, pessoa in enumerate(usuarios):
        f.write(f'{Nr}' + f'\t{pessoa}' + f'\t\t{byteMB(esp_utilizado[ind])} MB' + f'\t\t{usopercent(esp_utilizado[ind], esp_total)}%\n')
        Nr += 1

    f.write('\n\nEspaço Total Ocupado: ' + byteMB(esp_total) + ' MB\n')
    f.write('Espaço médio Ocupado: ' + byteMB(media) + ' MB')
    f.close()

with open ("relat.txt","r") as f:
   print(f.read())