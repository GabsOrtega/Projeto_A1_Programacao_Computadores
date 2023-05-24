from time import sleep

print('+=' * 30)
print("Seja Bem vindo ao Projeto A1 de Programação de Computadores!")
print('+=' * 30)
print()

while True:
    print('+=' * 30)
    print('MENU')
    print('+='* 30)
    opcao = int(input('''Escolha a opção de sua preferência:
[ 1 ] - Conversão para decimal para as bases binário e octadecimal
[ 2 ] - Conversão das bases binário e octadecimal para decimal
[ 3 ] - Calculadora aritmética de binários, que contemple as operações de soma e subtração
[ 4 ] - Sair do Programa
[ 5 ] - Integrantes do grupo (extra) 
'''))

    if opcao == 1:
        print("Você escolheu a opção [ 1 ] Conversão para decimal para as bases binário e octadecimal")
        print('PROCESSANDO...')
        sleep(0.5)
    
        decimal = int(input("Digite um número inteiro decimal: "))
        print('PROCESSANDO...')
        binario = bin(decimal)
        octal = oct(decimal)
        sleep(1)
        
        print(f'A conversão do número decimal {decimal} para binário é igual a {binario[2:]}')
        print(f'A conversão do número decimal {decimal} para a octadecimal é igual a {octal[2:]}')
        sleep(1)
        
    elif opcao == 2:
         print("Você escolheu a opção [ 2 ] - Conversão das bases binário e octadecimal para decimal")
         print('PROCESSANDO...')
         sleep(0.5)
         
         binario = int(input("Digite um número em binário: "))
         octadecimal = int(input("Digite um número em octadecimal: "))
         
         
    
        
    elif opcao == 3:
        print()
        
    elif opcao == 4:
        break
    
    elif opcao == 5:
        print("Os integrantes do grupo são:")
        print('Gabriel Ortega')
        print('Isabelle Santini')
        sleep(1)
    
    

'''Opção 1: Conversão para decimal para as bases binário e octadecimal.
Opção 2: Conversão das bases binário e octadecimal para decimal.
Opção 3: Calculadora aritmética de binários, que contemple as operações de soma e subtração.
Opção 4: Sair do programa'''
