# Apresentação padrão
def introduction():
    print('----------------------------------')
    print('Aluno: Matheus Lopes Enomoto')
    print('RU: 3687178')
    print('----------------------------------')
    print('Software de Estoque - Bicicletaria')
    print('----------------------------------')


# Variáveis Globais
# Variável de contagem de peças para utilização de código único
sku = 0
# Armazenamento das peças cadastradas
products = []


# Gera um sku de código unitário para cada peça
def generateSKU():
    global sku
    sku = sku + 1
    print(sku)
    return sku


# cadastra a peça com sku único
def cadastrarPeca (cod):

    global products

    print('''
    ---------------------------
    Cadastrar Peça
    ---------------------------
    ''')
    print('Você escolheu cadastrar uma peça.')

    # recebe um sku para o código
    cod = cod
    print('O código dessa peça será: {}'.format(cod))

    # nome da peça
    name = input('Digite o nome da peça que será cadastrada: ')

    # fabricante
    manufacturer = input('Digite o nome do fabricante da peça que será cadastrada: ')

    # valor
    value = float(input('Digite o valor da peça que será cadastrada: '))

    newProduct = {
        'cod': cod,
        'name': name,
        'manufacturer': manufacturer,
        'value': value,
    }

    print(newProduct)
    products.append(newProduct)

# Retorna todas as peças cadastradas
def getProductsAll():
    global products

    print('''
        ------------------------
        TODOS OS PRODUTOS
        ------------------------
    ''')

    for i in products:
        print('''
            ------------------------
            Código: {}
            Nome: {}
            Fabricante: {}
            Valor: R$ {}
            ------------------------
        '''.format(i['cod'], i['name'], i['manufacturer'], i['value']))

# Retorna a peça cadastrada com o código recebido
def getProductsByCod():
    global products

    cod = int(input('Digite o CÓDIGO da peça dejada: '))

    for i in products:
        if cod == i['cod']:
            print('''
            ------------------------
            Código: {}
            Nome: {}
            Fabricante: {}
            Valor: R$ {}
            ------------------------
        '''.format(i['cod'], i['name'], i['manufacturer'], i['value']))

# Retorna todas as peças cadastradas para o fabricante recebido
def getProductsByManufacturer():
    global products

    manufacturer = input('Digite o FABRICANTE das peças dejada: ')

    for i in products:
        if manufacturer == i['manufacturer']:
            print('''
                ------------------------
                Código: {}
                Nome: {}
                Fabricante: {}
                Valor: R$ {}
                ------------------------
            '''.format(i['cod'], i['name'], i['manufacturer'], i['value']))

#Retornar a opção de consulta de peças escolhida
def consultarPeca():

    print('''
    ---------------------------
    Consultar Peça
    ---------------------------
    Escolha a opção desejada: 
    1 - Consultar Todas As Peças
    2 - Consultar Peças Por Código
    3 - Consultar Peças Por Fabricante
    4 - Retornar
    ''')

    option = int(input(''))

    return option


def removerPeca ():

    global products

    print('Você selecionou REMOVER uma peça dos seus produtos cadastrados.')

    # Recebe o código que será excluído
    cod = int(input('Digite o CÓDIGO da peça que deseja remover: '))

    # Verifica qual item possui o mesmo código digitado e remove-o da lista
    for i in products:
        if cod == i['cod']:
            print('''
                        O item abaixo foi removido com sucesso
                            Código: {}
                            Nome: {}
                            Fabricante: {}
                            Valor: R$ {}
                        '''.format(i['cod'], i['name'], i['manufacturer'], i['value']))

            products.remove(i)



# Apresenta e trata o menu de opções
def showMainMenu():
    print('''
    ---------------------------
    Menu Principal
    ---------------------------
    Escolha a opção desejada: 
    1 - Cadastrar Peças
    2 - Consultar Peças
    3 - Remover Peças
    4 - Sair
    ''')

    option = int(input(''))

    return option



# Principal
introduction()

while True:
    mainMenuOption = showMainMenu()

    # Cadastrar peça
    if mainMenuOption == 1:
        cod = generateSKU()
        cadastrarPeca(cod)

    # Consultar peça
    elif mainMenuOption == 2:

        # loop de consulta de peças
        while True:
            listProductsOption = consultarPeca()
            if listProductsOption == 1:
                getProductsAll()
            elif listProductsOption == 2:
                getProductsByCod()
            elif listProductsOption == 3:
                getProductsByManufacturer()
            elif listProductsOption == 4:
                break
    # Remover peça
    elif mainMenuOption == 3:
        removerPeca()
    # Consultar peça
    elif mainMenuOption == 4:
        print('Obrigado por utilizar a nossa plataforma.')
        break
    else:
        continue

