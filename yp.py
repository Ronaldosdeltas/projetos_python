def cadastro_livro(id):
        while True:
         global id_global

         nome_l = input('Digite o nome do livro:')
         autor_l = input('Digite o nome do autor do livro:')
         editora_l = input('Digite o nome da editora do livro:')
         id = {'id': id,'name': nome_l, 'autor': autor_l, 'editora': editora_l}
         print (f'Seu foi Livro cadastrado! ID: {id_global}')
         lista_livro.append(id)

#Iniciando a função para consulta do livro (consultar_livros)