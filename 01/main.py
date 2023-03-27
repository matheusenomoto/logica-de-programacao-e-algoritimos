# Regras de negócio
# Quantidades	Desconto
# Até 9	0% na unidade
# Entre 10 e 99	5% na unidade
# Entre 100 e 999	10% na unidade
# De 1000 para mais	15% na unidade

# Apresentação padrão
def introduction():
    print('----------------------------------')
    print('Aluno: Matheus Lopes Enomoto')
    print('RU: 3687178')
    print('----------------------------------')
    print('Software de Automação de Descontos')
    print('----------------------------------')

# Realiza a leitura do valor do produto e retorna o mesmo, sem aferição da leitura
def productValue():
    value = float(input('Entre com o valor do produto:'))
    return value

# Realiza a leitura da quantidade do produto e retorna o mesmo, sem aferição da leitura
def productQty():
    quantity = int(input('Entre com a quantidade do produto:'))
    return quantity

# Verifica a condição de desconto aplicável ao quantitativo do produto, sem aferição da leitura
def checkDiscount(qty):
    qty = qty
    discount = 0

    if (qty >= 0 and qty <= 9):
        discount = 0.00
    elif (qty >= 10 and qty <= 99):
        discount = 0.05
    elif (qty >= 100 and qty <= 999):
        discount = 0.10
    elif (qty >= 1000):
        discount = 0.15
    else:
        print('Nenhum desconto será aplicado')

    return discount

# Apresenta os valores totais sem e com desconto
def showCart(value, qty, discount):
    value = value
    qty = qty
    discount = discount
    percentual = discount*100

    total = value * qty
    totalDiscount = value *(1-discount) * qty

    print('Valor SEM desconto: R$ {:.2f}'.format(total))
    print('Valor COM desconto para essa quantidade: R$ {:.2f} (desconto de {}%)'.format(totalDiscount, percentual))

introduction()
value = productValue()
qty = productQty()
discount = checkDiscount(qty)
showCart(value, qty, discount)
