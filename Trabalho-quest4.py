#Fazendo a implementação da função cadastro_livros
def cadastro_livros(id):
          
    books = {'id': id,'nome':'','autor':'', 'editora':''}
    print (f' ID do Livro: {id}')
    books ['nome'] = input('Digite o nome do livro:')
    books ['autor'] = input('Digite o nome do autor do livro:')
    books['editora'] = input('Digite o nome da editora do livro:')

    lista_livro.append(books)
    print('Livro cadastrado com sucesso!')

#Fazendo a implementação da função consulta_livros
def consulta_livro():
    print ('Escolha a opção que deseja:')
    menuConsulta = ('1- Consultar todos','2- Consultar por Id', '3- Consultar por autor', '4- Retornar',)

    for i in range(len(menuConsulta)):
      print(menuConsulta[i])
#Uso do try/except para caso aja erro do cliente
    try:
       option = int(input('>>'))
    except ValueError:
      print('Opção invalida. Tente novamente.')
    if option < 1 or option > 4:
      print('Opção invalida. Tente novamente.')

#Uso do if/for/elif para a implementação da consulta

    if option == 1: # consultar todos
      for i in lista_livro:
        for j, k in i.items():
          print(f'{j}:{k}')

    elif option == 2: # consulta por id
        try:
         idConsulta = int(input('Digite o id do livro:'))
        except ValueError:
          print('Opção invalida. Tente novamente.')

        print('-'*30)
        for i in lista_livro:
          if idConsulta == int(i['id']):
            for j, k in i . items () :
              print(f'{j}:{k}')

    elif option == 3: # consulta por autor
      autor = input('Digite o nome do autor do livro:')
      for i in lista_livro:
        if autor == i['autor']:
          for j, k in i . items () :
            print(f'{j} {k}')

    else: return 1  

#Fazendo a implementação da função remover_livros
def remover_livro():
  idRemover = input('Digite o Id do livro que deseja remover:')
  for i in range(len(lista_livro)):
    if int((lista_livro[i])['id'])== int(idRemover):
      print('Livro removido com sucesso!')
      
      del lista_livro[i]
      break

# implementação do MAIN do menu principal
print ('   Bem vindo(a) a Livraria do Ronaldoss Martins')


lista_livro = []; id_global = 0
menu =('1. Cadastrar Livro', '2. Consultar Livros', '3. Remover Livros', '4. Sair')

while True:
    print("-"*20,"MENU PRINCIPAL",'-'*20,)
    for i in menu:
     print(i)
    try: 
     option = int(input('>>'))
    except ValueError:
     print('Opção invalida. Tente novamente.')
    if option < 1 or option > 4:
      print('Opção invalida. Tente novamente.')
      continue
    if option == 1:
      print('-'*20,"MENU CADASTRAR LIVRO", '-'*20,)
      id_global += 1
      cadastro_livros(id_global)
      continue
    elif option == 2:
      print('-'*20,"MENU CONSULTAR LIVRO", '-'*20,)
      consulta_livro()
      continue
    elif option == 3:
      print('-'*20,"MENU REMOVE LIVRO", '-'*20,)
      remover_livro()
      continue
    else:
      break

  
  
     


 
        


