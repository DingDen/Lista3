'''O cardápio de uma lanchonete é o seguinte:

◦ Especificação            Código               Preço 
Cachorro Quente             100                R$ 1,20 
Bauru Simples               101                R$ 1,30 
Bauru com ovo               102                R$ 1,50 
Hambúrguer                  103                R$ 1,20 
Cheeseburguer               104                R$ 1,30 
Refrigerante                105                R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado. '''

valor100 = valor101 = valor102 = valor103 = valor104 = valor105 = 0
while True:
    print('\tCACHORRO QUENTE:      R$1.20         CÓDIGO 100')
    print('\tBAURU SIMPLES:        R$1.30         CÓDIGO 101')
    print('\tBAURU COM OVO:        R$1.50         CÓDIGO 102')
    print('\tHAMBÚRGUER:           R$1.20         CÓDIGO 103')
    print('\tCHEESEBURGUER:        R$1.30         CÓDIGO 104')
    print('\tREFRIGERANTE:         R$1.00         CÓDIGO 105')
    cod = int(input("\nDIGITE O CÓDIGO DA ESPECIFICAÇÃO DO CARDÁPIO: "))
    quant = int(input("DIGITE A QUANTIDADE DESEJADA: "))
    ped = int(input("DIGITE [1] - ENCERRAR PEDIDO, [2] - NÃO ENCERRAR PEDIDO: "))
    if ped == 1:
        if cod == 100:
            valor_pago = 1.2*quant
            valor100 = valor100 + valor_pago
        elif cod == 101:
            valor_pago = 1.3*quant
            valor101 = valor101 + valor_pago
        elif cod == 102:
            valor_pago = 1.5*quant
            valor102 = valor102 + valor_pago
        elif cod == 103:
            valor_pago = 1.2*quant
            valor103 = valor103 + valor_pago
        elif cod == 104:
            valor_pago = 1.3*quant
            valor104 = valor104 + valor_pago
        elif cod == 105:
            valor_pago = quant
            valor105 = valor105 + valor_pago
        break

    elif ped == 2:
        if cod == 100:
            valor_pago = 1.2*quant
            valor100 = valor100 + valor_pago
        elif cod == 101:
            valor_pago = 1.3*quant
            valor101 = valor101 + valor_pago
        elif cod == 102:
            valor_pago = 1.5*quant
            valor102 = valor102 + valor_pago
        elif cod == 103:
            valor_pago = 1.2*quant
            valor103 = valor103 + valor_pago
        elif cod == 104:
            valor_pago = 1.3*quant
            valor104 = valor104 + valor_pago
        elif cod == 105:
            valor_pago = quant
            valor105 = valor105 + valor_pago
        
valor_total = valor100 + valor101 + valor102 + valor103 + valor104 + valor105

print('-='*30)
print(f'\tCACHORRO QUENTE         PREÇO: R${valor100:.2f}')
print(f'\n\tBAURU SIMPLES           PREÇO: R${valor101:.2f}')
print(f'\n\tBAURU COM OVO           PREÇO: R${valor102:.2f}')
print(f'\n\tHAMBÚRGUER              PREÇO: R${valor103:.2f}')
print(f'\n\tCHEESEBURGUER           PREÇO: R${valor104:.2f}')
print(f'\n\tREFRIGERANTE            PREÇO: R${valor105:.2f}')
print(f'\n\tPREÇO TOTAL A SER PAGO: R${valor_total:.2f}')
print('-='*30)