#INICIO

#Boas vindas e escolha do serviço  
while True:
    print('Bem vindo a Copiadora da Isabela Premoli')
    print('Entre com o tipo de serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')

    escolha_servico = input('>>')
    
    if escolha_servico in ['DIG', 'ICO', 'IPB', 'FOT', 'dig', 'ico', 'ipb', 'fot']:
        break
    else:
        print('Escolha inválida, entre com o tipo do serviço novamente')
        continue      

#Entrada da quantidade de páginas
while True:
    try:
        num_paginas = int(input("Entre com o número de páginas: "))

        if num_paginas < 20:
            desconto = 0

        elif 20 <= num_paginas < 200:
            desconto = 0.15 #valor já convertido - valor do desconto (15) dividido por 100 (%) 

        elif 200 <= num_paginas < 2000:
            desconto = 0.20 #valor já convertido - valor do desconto (20) dividido por 100 (%)

        elif 2000 <= num_paginas < 20000:
            desconto = 0.25 #valor já convertido - valor do desconto (25) dividido por 100 (%)

        else:
            print('Não aceitamos tantas páginas de uma vez.')
            print('Por favor, entre com o número de páginas novamente.')
            continue
        break
    except ValueError:
        break

#Serviço Adicional
while True:
    print ('Deseja adicionar algum serviço?')
    print ('1 - Encadernação Simples - R$ 15,00')
    print ('2 - Encadernação Capa Dura - R$ 40,00')
    print ('0 - Não desejo mais nada')

    servico_extra = input('>>')

    if servico_extra in ['1', '2', '0']:
        break
    else:
        print('Escolha inválida. Tente novamente!')
        continue

if escolha_servico in ['DIG', 'dig']:
    valor_servico = 1.10
elif escolha_servico in ['ICO', 'ico']:
    valor_servico = 1.00
elif escolha_servico in ['IPB', 'ipb']:
    valor_servico = 0.40
elif escolha_servico in ['FOT', 'fot']:
    valor_servico = 0.20

valor_desconto = num_paginas * desconto
paginas_com_desconto = num_paginas - valor_desconto

if servico_extra == '1':
    valor_extra = 15.00
elif servico_extra == '2':
    valor_extra = 40.00
else:
    valor_extra = 0.00

total = (valor_servico * paginas_com_desconto) + valor_extra

#Resultado final da compra
print(f"Total: R$ {total} (serviço: {valor_servico} * páginas: {paginas_com_desconto} + extra: {valor_extra})")

#FIM