'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo. '''

lista = []
int1 = int2 = int3 = int4 = 0
while True:
    num = int(input("Digite números inteiros positivos: "))
    if num >= 0:
        lista.append(num)
        if num < 26:
            int1 += 1
        elif 26 <= num < 51:
            int2 += 1
        elif 51 <= num < 76:
            int3 += 1
        elif 76 <= num < 101:
            int4 += 1
    else:
        break
print('\tA lista fica da seguinte forma: ', lista, end='\n')
print('\t[0-25]:', int1)
print('\t[26-50]:', int2)
print('\t[51-75]:', int3)
print('\t[76-100]:', int4)