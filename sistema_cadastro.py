# lista dos produtos
lista_produto = []

def mostrarTela():
    print()
    print(f'{"LOJA TEM DE TUDO":-^30}')
    print()

    # variáveis do título
    alterar = 'Alterar Produtos[2]  |'
    cadastrar = 'Cadastrar Produtos[1] |'
    apagar = 'Apagar produto[3]'


    # menu
    print(67 * '-')
    print('{cad: ^22} {alt: ^22} {apa: ^22}'.format(cad=cadastrar,
                                                    alt=alterar, apa=apagar))
    print(67 * '-')
    
    # tabela dos produtos
    print()
    print(67 * '-')
    print(f'{"ID": ^20} {"PRODUTO": ^20} {"PREÇO": ^20}')
    print(67 * '-')
    
    # verificando se tem produtos na lista
    if len(lista_produto) == 0:
        ...
    else:
        # listando produtos
        for i in lista_produto:
            for j in i:
                print(f'{j: ^20}', end=' ')
            print()
            print(67 * '-')
            
    print()
    print()
    
    # escolha da função desejada
    escolha = input('Digite a opção que você deseja: ')

    # verificando a função escolhida
    if escolha.isnumeric():
        if escolha == '1':
            cadastrarProd()
        elif escolha == '3':
            excluirProd()
        elif escolha == '2':
            atualizarProd()

    # recomeçando
    mostrarTela()


# função para o cadastro dos produtos
def cadastrarProd():
    cod = len(lista_produto) + 1
    produto = input('Nome do produto: ')
    preco = input('Preço do produto: ')

    if '.' in preco:
        preco.replace('.', ',')
        lista_produto.append([cod, produto, preco])
    else:
        lista_produto.append([cod, produto, preco])

# função para excluir produto
def excluirProd():
    cod = int(input('Informe o ID do produto para excluir: '))
    for i in lista_produto:
        if i[0] == cod:
            lista_produto.remove(i)
            break

# função para atular dados
def atualizarProd():
    global lista_produto
    cont = 0
    
    cod = input('Qual o código do produto que deseja atualizar? ')
    valor = input('O que deseja atulizar, nome (1) ou preço (2)? ')

    if cod.isnumeric():
        if valor.isnumeric():
            if valor == '1':
                dado = input('digite o novo nome: ')
                for i in lista_produto:
                    for j in i:
                        if str(j) == cod:
                            lista_produto[cont][1] = dado
                            break
                    cont += 1
            else:
                dado = input('digite o novo preço: ')
                for i in lista_produto:
                    for j in i:
                        if str(j) == cod:
                            lista_produto[cont][2] = dado
                            break
                    cont += 1
        else:
            print('Opção inválida!')
    else:
        print('Código inválido!')

        
mostrarTela()
