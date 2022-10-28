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
    print('{cad: ^22} {alt: ^22} {apa: ^22}'.format(cad=cadastrar, alt=alterar, apa=apagar))
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

    # recomeçando
    mostrarTela()


# função para o cadastro dos produtos
def cadastrarProd():
    cod = len(lista_produto) + 1
    produto = input('Nome do produto: ')
    preco = input('Preço do produto: ')
    lista_produto.append([cod, produto, preco])


mostrarTela()
