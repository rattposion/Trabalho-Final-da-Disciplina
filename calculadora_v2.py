def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

def calculadora(num1, num2, operacao):
    if operacao in ('+', 'soma'):
        return adicao(num1, num2)
    elif operacao in ('-', 'subtracao'):
        return subtracao(num1, num2)
    elif operacao in ('*', 'multiplicacao'):
        return multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        return divisao(num1, num2)
    else:
        return 'Operação inválida'

saida = ''
while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (+, -, *, / ou o nome): ')
    resultado = calculadora(num1, num2, operacao)
    print(f'Resultado da operação: {resultado}')
    saida = input('Deseja continuar? (S/N): ')
