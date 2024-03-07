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
