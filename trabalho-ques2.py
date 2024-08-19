print("    seja bem vindo(a) a loja de Gelados do Ronaldoss")# Messagem de boas vindas da loja ao clients
card = 'Caradápio'
# forma para acrescentar as linhas ao redor e abaixo do nome cardápio
meio = card.center(48,'-')
print(meio)
line = ('-'* 48)
print(line)
#Enunciado do caradápio para o cliente
print('---| Tamanho |  Cupuaçu (CP) |   Açaí (AC)  |---')
print('---|    P    |    R$  9.00   |   R$ 11.00   |---')
print('---|    M    |    R$  14.00  |   R$ 16.00   |---')
print('---|    G    |    R$  18.00  |   R$ 20.00   |---')
linee = ('-'* 48)
print(linee)

total_val = 0 # valor total das compras

while True:#Laço de repetição, para em caso de error do cliente na entrada do sabor desejado
    sabor = input('Entre com o sabor que deseja (CP / AC ):').upper() #Entre com o sabor
    if sabor not in ('CP','AC' ):
     print('Sabor invalido. Por favor, tente novamente.')# Messagem de retorno em caso de error do cliente na entrada do sabor
     print('')
     continue

    tamanho = input('Entre com o tamanho (P/M/G):').upper() #Messagem para entradada com o tamanho do sabor
    if tamanho not in ('P','M','G'):
     print('Tamanho invalido. Por favor, tente novamente.') 
     print('')
     continue
    #Aqui fazemos o uso do IF/ELIF/ELSE para calculo do valor e tamanho do sabor
    if sabor == 'CP':
      product_name = 'Capuaçu'
    else: product_name = 'Açaí'

    if sabor == 'CP':
      if tamanho == 'P':
        valor_product = 9.00
      elif tamanho == 'M':
        valor_product =14.00
      else: valor_product = 18.00

    else:
      if sabor == 'AC':
       if tamanho == 'P':
        valor_product = 11.00
       elif tamanho == 'M':
        valor_product = 16.00
       else: valor_product = 20.00
    
    total_val += valor_product # Soma do valor total mais o valor do produto

      #Messagem de saída com valor, tamanho e valor a ser pago do do produto
    print (f'Você pediu um {product_name} do tamanho {tamanho} no valor de: R${valor_product}')
    
    continuee = input('Deseja algo mais? S/N:').upper()#Messagem de entrada para compra de mais sabores
    if continuee == 'S':
      continue #Aqui usamos o laço de repetição continue caso digite 'S'
    else:
     print (f'Valor total a pagar: R${total_val}') # mesagem de saída com o valor total que o client deve pagar
     break





