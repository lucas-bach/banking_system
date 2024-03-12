import locale

saldo = 500

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def sacar():
    global saldo

    while True:
        valor_input = input('Digite o valor: ')
        if valor_input.isdigit():
            Saldo_disp = float(valor_input)
            break
        else:
            print('Insira apenas números.')

    if Saldo_disp <= saldo:
        saldo -= Saldo_disp
        print('Saldo disponível!')
        print(f'Você retirou: {locale.currency(Saldo_disp, grouping=True)}')
        print('Obrigado e volte sempre.')  
    else:
        print('Valor excede o saldo!')   

def depositar():
    global saldo 
    valor_deposito = float(input('Digite o valor de depósito: '))
    saldo += valor_deposito
    print(f'Você depositou: {locale.currency(valor_deposito, grouping=True)}')
    
    print('Transação efetuada com sucesso!') 


def mostrar_saldo():
    print(f'Saldo atual: {locale.currency(saldo, grouping=True)}')


sacar()
        
depositar()

mostrar_saldo()
