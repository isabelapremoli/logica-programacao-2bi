#INICIO

print("Bem vindo a Loja da Isabela Premoli")

vp = float(input("Entre com o valor do produto: ")) #Valor do produto para inserir
qtd = int(input("Entre com a quantidade do produto: ")) #Quantidade de produto para inserir
valorTotal = vp * qtd #Valor da compra SEM desconto

if(valorTotal < 2500): 
    desconto = 0
    print('Você não teve nenhum desconto.')

elif(2500 >= valorTotal < 6000):
    desconto = 4
    print('Você recebeu um desconto de 4%.')

elif(6000 >= valorTotal < 10000):
    desconto = 7
    print('Você recebeu um desconto de 7%.')

else:
    desconto = 11
    print('Você recebeu um desconto de 11%.')


valorComDesconto = valorTotal - valorTotal * (desconto/100) #Valor da compra COM o desconto aplicado

print('O valor SEM desconto é de R$ {} reais'.format(valorTotal))

print('O valor COM desconto é de R$ {} reais'.format(valorComDesconto, desconto))

#FIM