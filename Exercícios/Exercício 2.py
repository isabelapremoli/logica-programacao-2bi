#INICIO - Mensagem de boas-vindas e cardápio

print('Bem-vindo à Loja de Gelatos da Isabela Premoli')
print('--------------------CARDÁPIO---------------------')
print('-------------------------------------------------')
print('---|  TAMANHO  |  CUPUAÇU (CP)  |  AÇAÍ (AC) |---')
print('---|     P     |    R$  9,00    |  R$ 11,00  |---')
print('---|     M     |    R$ 14,00    |  R$ 16,00  |---')
print('---|     G     |    R$ 18,00    |  R$ 20,00  |---')
print('-------------------------------------------------')

#Tradutor das siglas CP e AC
sabores_dicio = {'CP': 'Cupuaçu', 'cp': 'Cupuaçu', 'AC': 'Açaí', 'ac': 'Açaí'}


#Acumulador
soma = 0

#Entrada para a escolha do sabor
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor not in ('CP','cp','ac','AC'):
        print('Sabor inválido. Tente novamente.')
        continue

    #Entrada para a escolha do tamanho
    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    if tamanho not in ('P','p','m','M','g','G'):
        print('Tamanho inválido. Tente novamente.')
        continue
       
    #Definição do preço baseado no sabor e tamanho
    if sabor in ('CP', 'cp'):
        if tamanho in ('P','p'):
            preco = 9
        elif tamanho in ('M','m'):
            preco = 14
        else:
            preco = 18
    
    #Se sabor for 'AC' ou 'ac'
    else:  
        if tamanho in ('P','p'):
            preco = 11
        elif tamanho in ('M','m'):
            preco = 16
        else:
            preco = 20


    #Exibir apenas 1 pedido
    print(f'Você pediu um {sabores_dicio[sabor]} no tamanho {tamanho}: R$ {preco},00')

    #Acumular o valor do pedido
    soma += preco

    maisPedido = input('Deseja mais alguma coisa? (S/N): ')
    if maisPedido in ('N','n'):
        break

print(f'O valor total a ser pago: R$ {soma},00')

#FIM