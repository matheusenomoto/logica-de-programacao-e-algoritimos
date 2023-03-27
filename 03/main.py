# Apresentação padrão
def introduction():
    print('----------------------------------')
    print('Aluno: Matheus Lopes Enomoto')
    print('RU: 3687178')
    print('----------------------------------')
    print('Software Logística - eLog')
    print('----------------------------------')


# calcula o volume do objeto
def getVolume(dimensions):
    dimensions = dimensions
    vol = 1

    for i in dimensions:
        vol *= i

    return vol

# Verifica o volume necessário e devolve o R$
def checkVolume (vol):
    vol = vol

    if vol < 1000:
        volPrice = 10
        return volPrice
    elif 1000 <= vol < 10000:
        volPrice = 20
        return volPrice
    elif 10000 <= vol < 30000:
        volPrice = 30
        return volPrice
    elif 30000 <= vol < 100000:
        volPrice = 50
        return volPrice
    elif vol >= 100000:
        return False


# Retorna o valor em R$ conforme dimensões escolhidas
def dimensoesObjeto():

    # loop para retornar a tarifa do volume
    while True:
        dimensions = []

        # loops das dimensões
        # loop da altura
        while True:
            try:
                height = float(input('Insira a altura do objeto [cm]: '))
                dimensions.append(height)
            except:
                print('Você digitou um valor não numérico, insira novamente')
                continue
            break
        # loop do comprimento
        while True:
            try:
                length = float(input('Insira o comprimento do objeto [cm]: '))
                dimensions.append(length)
            except:
                print('Você digitou um valor não numérico, insira novamente')
                continue
            break
        # loop da largura
        while True:
            try:
                width = float(input('Insira a largura do objeto [cm]: '))
                dimensions.append(width)
            except:
                print('Você digitou um valor não numérico, insira novamente')
                continue
            break

        # Calcula o volume com as dimensões recebidas
        vol = getVolume(dimensions)
        print('O objeto possui {:.2f} cm³'.format(vol))

        # Verifica qual a tarifa referente ao volume calculado
        volPrice = checkVolume(vol)

        if volPrice == False:
            print('Desculpe, Esse volume está acima do que conseguimos transportar, tente inserir um novo volume')
            continue

        return volPrice

# Verifica o peso e retorna o multiplicador dessa variável
def checkWeight(weight):
    weight = weight

    # Nesse ponto da tabela 2 do exercício existe uma inconsistência nos requisitos que possuem multiplicador de 1.0 e 1.5
    # Ambos contém o valor exato de peso <= 1, considerei o primeiro multiplicador apenas < 1
    if weight < 0.1:
        weightValue = 1
        return weightValue
    elif 0.1 <= weight < 1:
        weightValue = 1.5
        return weightValue
    elif 1 <= weight < 10:
        weightValue = 2
        return weightValue
    elif 10 <= weight < 30:
        weightValue = 3
        return weightValue
    elif weight >= 30:
        return False

# Retorna o multiplicador em conforme peso
def pesoObjeto():

    while True:
        weight = 0
        # loop para receber o peso
        while True:
            try:
                weight = float(input('Digite o peso do objeto [kg]: '))
            except:
                print('Você digitou um valor não numérico, insira novamente')
                continue
            break


        print('O objeto possui {:.2f} kg'.format(weight))

        weightValue = checkWeight(weight)

        if weightValue == False:
            print('Desculpe, Esse objeto está acima do que conseguimos transportar, tente inserir o peso novamente')
            continue

        return weightValue

# rotas disponíveis
routes = [
    {'cod': 'RS', 'route': 'RS - De Rio de Janeiro até São Paulo', 'fee': 1},
    {'cod': 'SR', 'route': 'SR - De São Paulo até Rio de Janeiro', 'fee': 1},
    {'cod': 'BS', 'route': 'BS - De Brasília até São Paulo', 'fee': 1.2},
    {'cod': 'SB', 'route': 'SB - De São Paulo até Brasília', 'fee': 1.2},
    {'cod': 'BR', 'route': 'BR - De Brasília até Rio de Janeiro', 'fee': 1.5},
    {'cod': 'RB', 'route': 'RS - De Rio de Janeiro até Brasília', 'fee': 1.5},
]

# Retorna o multiplicador conforme rota escolhida
def rotaObjeto():

    while True:

        route = ''
        routeValue = 0

        print ('Selecione a rota desejada: ')
        for i in routes:
            print(i['route'])

        route = input('Selecione a rota: ')

        if route =='RS':
            routeValue =1
            return routeValue
        elif route =='SR':
            routeValue = 1
            return routeValue
        elif route =='BS':
            routeValue = 1.2
            return routeValue
        elif route =='SB':
            routeValue = 1.2
            return routeValue
        elif route =='BR':
            routeValue = 1.5
            return routeValue
        elif route =='RB':
            routeValue = 1.5
            return routeValue
        else:
            print('Você digitou uma rota que não existe, ou que ainda não realizamos, tente novamente.')
            continue


# Calcula o valor total
def getTotal(volume, weight, route):
    total = volume * weight * route
    return total

introduction()
volumePrice = dimensoesObjeto()
weightValue = pesoObjeto()
routeValue = rotaObjeto()
total = getTotal(volumePrice, weightValue, routeValue)

print('''
Total = Tarifa_Volume * Tarifa_Peso * Tarifa_Rota
Total: {} * {} * {}
Total de R$ {:.2f}
'''.format(volumePrice, weightValue, routeValue, total))
