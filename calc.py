# Função Restart, reiniciará a calc quando o usuário solicitar
def restart():
    calc_restart = input('''
    Você deseja calcular algo novamente?
    Digite S para Sim e N para Não
    ''')

    # Condicional do Sim
    try:
        if calc_restart == 'S' or calc_restart == 's':
            print (calc_restart)
            calculadora()
        # Condicional do Senão SE1
        elif calc_restart == 'N' or calc_restart == 'n':
            print("OK, até breve.")
        # Senão
        else:
            restart()
    except:
        print('Insira um valor válido, S para Sim e N para Não')
        restart()

# Função Calculadora, onde realiza as operações
def calculadora():
    operation = input('''
    Por favor, digite um número para realizar um calculo
    1 -> Para Soma
    2 -> Para Subtração
    3 -> Para Divisão
    4 -> Para Multiplicação
    ''') # Neste passo estamos interagindo com o usuário e aguardando um dos números acima

    n1 = int(input('Digite o primeiro número: ')) #Entrada do primeiro numero
    n2 = int(input('Digite o segundo numero: ')) #Entrada do segundo número

    # Calculo de Soma
    if operation == '1':
        print ('{} + {} = '.format(n1,n2))
        print (n1 + n2)
    elif operation == '2':
        # Calculo de Subtração
        print ('{} - {} = '.format(n1,n2))
        print (n1 - n2)
    elif operation == '3':
        # Tratamento de erro, divisão por 0
        try:
            # Calculo de Divisão
            print ('{} / {} = '.format(n1,n2))
            print (n1 / n2)
        except ZeroDivisionError:
            print ('Não é possivel dividir por zero')
    elif operation == '4':
        # Calculo de Multiplicação
        print ('{} * {} = '.format(n1,n2))
        print (n1 * n2)
    else:
        print('O valor digitado não é valido, reinicie a calculadora.')

    restart()

calculadora()

# Função de boas vindas
def bemvindo():
    print('''
     Bem-Vindo a Calculadora
     ''')
bemvindo()
calculadora()