
print('Bem vindo a copiadora do Ronaldoss ') # Messagem de boas vindas
 #Enunciado dos serviços da copiadora
print('Escolha o tipo de serviço')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão preto e branco')
print('FOT - Fotocópia')
def escolha_service():# aplicação da função def
   while True: # laço de repetição na função
    service_name = ('DIG', 'ICO', 'IPB, FOT')
    service_name = input('') #Entrada do pedido

    if service_name not in ('DIG', 'ICO', 'IPB', 'FOT'): # Entrada do nome do service
     print('Messagem invalida. Tente novamente.') # message de valor invalido
     continue
     #Calculo dos valores do serviço
    if service_name == 'DIG':
     return float(0.10)
    elif service_name == 'ICO':
      return float(1.0)
    elif service_name == 'IPB':
      return float (0.40)
    elif service_name == 'FOT':
      return float (0.20)
    

def numero_de_folhas():# Inciando a função def numero de folhas
    while True:# laço de repetição na função
        try:
           numero_de_folhas = int(input('Entre com número de páginas:')) # Entrada do número de páginas

           if numero_de_folhas <20:# Fazendo o uso do if para Calculo dos numeros de paginas
              return numero_de_folhas
           
           elif  20 <= numero_de_folhas < 200:
                return int(numero_de_folhas* 0.85) #Retorno do numero de paginas vezes a porcentagem
           
           elif   200<= numero_de_folhas <2000:
                return int(numero_de_folhas * 0.8) #Retorno do numero de paginas vezes a porcentagem
           
           elif   2000<= numero_de_folhas <20000:
                return int(numero_de_folhas * 0.75) #Retorno do numero de paginas vezes a porcentagem
           else:
              print('Não aceitamos tantas páginas de uma só vez.')
              print('Por favor, entrar com o numero de paginas mais uma vez.')

        except ValueError: #Uso de try/except para entrada de valores não numericos
         print('Por favor, Digite um valor numerico.')
        print('')
        continue


def servico_extra():#Iniciando a função servico_extra
    while True: # laço de repetição na função_extra
        try:
            #Entrada de servico_extra com nome do servico_extra e o seu valore
            extra_service = int(input('Deseja adicionar um serviço extra?\n1-  Encadernação simples - R$ 15.00\n2-  Encadernação capa dura - R$ 40.00\n0-  Nada mais a desejar\n>>'))  
        
            if extra_service != 0 and extra_service!= 1 and extra_service != 2: # Uso so IF para o calculo na função
              continue
            else:
        
             if extra_service == 0:
              return float(0) #Retorno do valor so servico
        
             if extra_service == 1:
              return float(15.0) #Retorno do valor so servico
        
             else:
              return float(40.0) #Retorno do valor so servico
        
        except ValueError: #Uso de try/except para entrada de valores não numericos
          print('Por favor, Digite navamente...')
          continue
          


servico = escolha_service()

pages = numero_de_folhas()

extra = servico_extra()
#Calculo do valor total de todos os serviços
total = (servico * pages) + extra 
print(f'Total:R${total} (escolha_service: {servico} * {pages} + extra: {extra})')

 

        
        
       

     

 







