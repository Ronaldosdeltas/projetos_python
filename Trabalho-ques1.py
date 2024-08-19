print('Bem vindo a loja do ronaldoss') # enuciado de boas vindas ao cliente.
valor_unico = float(input('Entre com o valor do produto:'))# Valor interio do produto
quantidade = int(input('Entre com a quantidade do produto:'))# Quantidade do produto
valor_sem_desconto = valor_unico * quantidade #Calculo do valor interio do produto * a quantidade do produto
#forma para calcular os descontos dos produtos
if valor_sem_desconto <2500:
    desconto = 0
#Calculo do valor do produto * a porcentagem
elif  2500<= valor_sem_desconto <6000:
    desconto = (valor_sem_desconto * 0.96)

elif   6000<= valor_sem_desconto <10000:
    desconto =  (valor_sem_desconto * 0.93)

else:
    desconto =  (valor_sem_desconto * 0.89)

#saida dos valores totais sem e com descontos
print (f'valor_SEM_desconto:{valor_sem_desconto}')
print (f'valor_COM_desconto:{desconto}')