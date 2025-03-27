# Microatividade 1: Estruturas de Condição if e else

temperatura = 29
if temperatura < 30:
    print('A temperatura hoje está amena')
else:
    print('Hoje está fazendo calor')

temperatura = 31
if temperatura < 30:
    print('A temperatura hoje está amena')
else:
    print('Hoje está fazendo calor')

# Microatividade 2: Estrutura de Condição elif

tempoExperiencia = 5
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')

tempoExperiencia = 1
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')

tempoExperiencia = 3
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')

# Microatividade 3: Estrutura de Repetição while

entrada_idade = ''
while str(entrada_idade) != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    print(f'Número digitado: {entrada_idade}')

# Microatividade 4: Estrutura de Repetição for

texto = 'Olá, laço for.'
for item in texto:
    print(f'Caractere: {item}')

for num in range(1, 11):
    print(f'Número do intervalo: {num}')

# Microatividade 5: Funções em Python

def imprimir_variavel():
    texto = 'Olá, funções em Python'
    print(texto)

imprimir_variavel()

# Microatividade 6: Argumentos de Funções

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')

# Trabalho Prático: Calculadora

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
