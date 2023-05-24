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
        sleep(1)
    
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
         sleep(1)
    
                 
         def octdecimal(octal):
             conversao = 0
             tamanho = len(octal) - 1
             pos = 0
             while tamanho >= 0:
                 digito = octal[pos]
                 conversao += int(digito) * (8 ** tamanho)
                 pos += 1
                 tamanho -= 1
             return conversao
                 
                 
         def bindecimal(binary):
             conversao = 0
             tamanho = len(binary) - 1
             pos = 0
             while tamanho >= 0:
                 digito = binary[pos]
                 conversao += int(digito) * (2 ** tamanho)
                 pos += 1
                 tamanho -= 1
             return conversao
         
         
         sumOct = octdecimal(input("Digite um número em octadecimal: "))
         print(sumOct)
         sumDec = bindecimal(input("Digite um número em binário: "))
         print(sumDec)
         
         
    elif opcao == 3:
         print("Você escolheu a opção [ 3 ] - Calculadora aritmética de binários, que contemple as operações de soma e subtração")
         print('PROCESSANDO...')
         sleep(0.5)
         
         while True:
            calculadora = int(input('''
[ 1 ] - Soma binária
[ 2 ] - Subtração binária
[ 3 ] - Sair da calculadora binária'''))
            
            if calculadora == 1:
                print("Você escolheu a opção [ 1 ] - Soma binária")
                print('PROCESSANDO...')
                sleep(1)


                def somaBinaria(numBin1, numBin2):
                    numBin1 = int(numBin1, 2)
                    numBin2 = int(numBin2, 2)

                    resultado = bin(numBin1 + numBin2)[2:]

                    return resultado
                
                binario = somaBinaria(input("Digite o primeiro número binário: "), input("Digite o segundo número binário: "))
                print(binario)

            elif calculadora == 2:
                print("Você escolheu a opção [ 2 ] - Subtração binária")
                print('PROCESSANDO...')
                sleep(1)

                def subtracaoBinaria(numBin1, numBin2):
                    numBin1 = int(numBin1, 2)
                    numBin2 = int(numBin2, 2)

                    resultado = bin(numBin1 - numBin2)[2:]

                    return resultado
                
                binario = subtracaoBinaria(input("Digite o primeiro número binário: "), input("Digite o segundo número binário: "))
                print(binario)
            
                
                
            elif calculadora == 3:
                break
         
         
         
         
        
    elif opcao == 4:
        break
    
    elif opcao == 5:
        print("Os integrantes do grupo são:")
        print('Gabriel Ortega')
        print('Isabelle Santini')
        sleep(1)
    
    else:
        print('Opção inválida! Escolha dentre as opções pré-existentes do menu!')
    
    

'''Opção 1: Conversão para decimal para as bases binário e octadecimal.
Opção 2: Conversão das bases binário e octadecimal para decimal.
Opção 3: Calculadora aritmética de binários, que contemple as operações de soma e subtração.
Opção 4: Sair do programa'''
