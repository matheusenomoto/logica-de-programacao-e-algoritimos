# Regras de negócio
# código do produto desejado
# Se o cliente quer pedir mais alguma coisa (se sim repetir o passo item 2.  Caso contrário ir para próximo passo
# Encerre a conta do cliente com o valor total
# Código	Descrição	Valor(R$)
# 100	Cachorro-Quente	9,00
# 101	Cachorro-Quente Duplo	11,00
# 102	X-Egg	12,00
# 103	X-Salada	13,00
# 104	X-Bacon	14,00
# 105	X-Tudo	17,00
# 200	Refrigerante Lata	5,00
# 201	Chá Gelado	4,00
# requisitos
# if, elif e else
# Se a pessoa digitar um NÚMERO diferente dos da tabela printar na tela: ‘opção inválida’ e voltar para o menu
# Deve-se utilizar while, break, continue

# Apresentação padrão
def introduction():
    print('----------------------------------')
    print('Aluno: Matheus Lopes Enomoto')
    print('RU: 3687178')
    print('----------------------------------')
    print('Software Lanchonete')
    print('----------------------------------')

# Apresentação do cardápio com as opções de código, Descrição e Valor
def showMenu():
    menu = """
         -----------------------------------------------------------------------
        |				CARDÁPIO				|
        |-----------------------------------------------------------------------|
        |	Código	|	Descrição		|	Valor(R$)	|
        |---------------|-------------------------------|-----------------------|
        |	100	|	Cachorro-Quente		|	9,00		|
        |	101	|	Cachorro-Quente Duplo	|	11,00		|
        |	102	|	X-Egg			|	12,00		|
        |	103	|	X-Salada		|	13,00		|
        |	104	|	X-Bacon			|	14,00		|
        |	105	|	X-Tudo			|	17,00		|
        |	200	|	Refrigerante Lata	|	5,00		|
        |	201	|	Chá Gelado		|	4,00		|
         -----------------------------------------------------------------------
    """
    print(menu)


# solicita o código do ítem desejado
def mayIHelpYou():
    cod = int(input('Qual o código do produto que você gostaria? '))
    return cod


# verifica o código digitado
def checkCod(cod):
    cod = cod
    while True:
        if cod == 100:
            return cod
        elif cod == 101:
            return cod
        elif cod == 102:
            return cod
        elif cod == 103:
            return cod
        elif cod == 104:
            return cod
        elif cod == 105:
            return cod
        elif cod == 200:
            return cod
        elif cod == 201:
            return cod
        else:
            print('Opção Inválida!')
            cod = int(input('digite uma opção novamente: '))
            continue

    return cod


# Lista de produtos do menu
menuProducts = [
    {'cod': 100, 'desc': 'Cachorro-Quente', 'price': 9},
    {'cod': 101,  'desc': 'Cachorro-Quente Duplo', 'price': 11},
    {'cod': 102, 'desc': 'X-Egg', 'price': 12},
    {'cod': 103, 'desc': 'X-Salada', 'price': 13},
    {'cod': 104, 'desc': 'X-Bacon', 'price': 14},
    {'cod': 105, 'desc': 'X-Tudo', 'price': 17},
    {'cod': 200, 'desc': 'Refrigerante Lata', 'price': 5},
    {'cod': 201, 'desc': 'Chá Gelado', 'price': 4},
    ]


# Soma o valor dos itens
def calculateCart(list):
    list = list
    finalValue = 0

    for subItem in list:
        finalValue += subItem['price']

    return finalValue


# Apresenta o carrinho
def showCart(cart):
    cart = cart
    listOfProducts = []

    # Loop para verificar quais itens foram adicionados e coleta-os do menuProducts
    for item in cart:
        for i in menuProducts:
            if item == i['cod']:
                # Adiciona os itens no carrinho à lista para cálculo
                listOfProducts.append(i)

    # Lista individualmente os itens do pedido
    print('Seu pedido:')
    for i in listOfProducts:
        print('{} Subtotal: R$: {}'.format(i['desc'], i['price']))

    # Apresenta o valor somado de todos os itens
    total = calculateCart(listOfProducts)
    print('Total: R$ {}'.format(total))

# mostra o que já foi escolhido enquanto o cliente decide se quer mais alguma coisa
def partialCart(cart):
    cart = cart
    partialCartProducts = []

    print('Até o momento o seu pedido é:')
    for item in cart:
        for i in menuProducts:
            if item == i['cod']:
                partialCartProducts.append(i)

    for i in partialCartProducts:
        print('{} Subtotal: R$: {}'.format(i['desc'], i['price']))


# verifica o código digitado
def checkMoreOptions():

    moreOptions = int(input("""
    Você gostaria de mais alguma coisa?
    0 - Não
    1 - Sim
    """))
    if(moreOptions == 0):
        return False
    elif(moreOptions == 1):
        return True

introduction()

while True:

    showMenu()
    cart = []

    cod = mayIHelpYou()
    checkedCod = checkCod(cod)
    cart.append(checkedCod)

    while True:
        partialCart(cart)
        moreOptions = checkMoreOptions()
        if moreOptions:
            cod = mayIHelpYou()
            checkedCod = checkCod(cod)
            cart.append(checkedCod)
        else:
            break

    showCart(cart)

