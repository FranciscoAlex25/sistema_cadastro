# lista dos produtos
lista_produto = []

def mostrarTela():
    print()
    print(f'{"LOJA TEM DE TUDO":-^30}')
    print()

    # variáveis do título
    listar = 'Listar Produtos'
    cadastrar = 'Cadastrar Produtos'
    apagar = 'Apagar produto'
    alterar = 'Alterar produto'

    # menu
    print('{cad:=^30}[1] {alt:=^30}[2]'.format(cad=cadastrar, alt=alterar))
    print('{apa:=^30}[3] {lis:=^30}[4]'.format(apa=apagar, lis=listar))

    # tabela dos produtos
    print()
    print(f'{"ID": ^20} {"PRODUTO": ^20} {"PREÇO": ^20}')
    
    # verificando se tem produtos na lista
    if len(lista_produto) == 0:
        ...
    else:
        # listando produtos
        for i in lista_produto:
            for j in i:
                print(f'{j: ^20}', end=' ')
            print()
            
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
