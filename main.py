from time import sleep

'''Nome: Gabriel Ortega - RGM: 34659293
   Nome: Isabelle Santini - RGM: 33955999
   Campus Paulista
'''
   
print('+=' * 30)
print("Seja Bem vindo ao Projeto A1 de Programação de Computadores!")
print('+=' * 30)
print()

while True:
    print('+=' * 16)
    print(f"{'MENU':^30}")
    print('+='* 16)
    print('''[ 1 ] - Conversão para decimal para as bases binário e octadecimal
[ 2 ] - Conversão das bases binário e octadecimal para decimal
[ 3 ] - Calculadora aritmética de binários, que contemple as operações de soma e subtração
[ 4 ] - Sair do Programa
''')
    opcao = int(input("Escolha uma opção: "))

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
         
         numOct = input("Digite um número em octadecimal: ")
         sumOct = octdecimal(numOct)
         print(f'A conversão do número octadecimal {numOct} para decimal é igual a {sumOct}')
         sleep(1)
         
         numBin = input("Digite um número em binário: ")
         sumDec = bindecimal(numBin)
         print(f'A conversão do número binário {numBin} para decimal é igual a {sumDec}')
         sleep(1)
         
         
    elif opcao == 3:
         print("Você escolheu a opção [ 3 ] - Calculadora aritmética de binários, que contemple as operações de soma e subtração")
         print('PROCESSANDO...')
         sleep(1)
         
         while True:
            calculadora = int(input('''
[ 1 ] - Soma binária
[ 2 ] - Subtração binária
[ 3 ] - Sair da calculadora binária
'''))
            
            if calculadora == 1:
                print("Você escolheu a opção [ 1 ] - Soma binária")
                print('PROCESSANDO...')
                sleep(1)


                def somaBinaria(BinaryI, BinaryII):
                    BinaryI = int(BinaryI, 2)
                    BinaryII = int(BinaryII, 2)

                    resultado = bin(BinaryI + BinaryII)[2:]

                    return resultado
                
                BinaryI = input("Digite o primeiro número binário: ")
                BinaryII = input("Digite o segundo número binário: ")
                binario = somaBinaria(BinaryI, BinaryII)
                print(f'A soma binária dos números {BinaryI} + {BinaryII} é igual a {binario}')
                sleep(1)

            elif calculadora == 2:
                print("Você escolheu a opção [ 2 ] - Subtração binária")
                print('PROCESSANDO...')
                sleep(1)

                def subtracaoBinaria(BinaryI, BinaryII):
                    BinaryI = int(BinaryI, 2)
                    BinaryII = int(BinaryII, 2)

                    resultado = bin(BinaryI - BinaryII)[2:]

                    return resultado
                
                BinaryI = input("Digite o primeiro número binário: ")
                BinaryII = input("Digite o segundo número binário: ")
                binario = subtracaoBinaria(BinaryI, BinaryII)
                print(f'A subtração binária dos números {BinaryI} - {BinaryII} é igual a {binario}')
                sleep(1)
            
                
                
            elif calculadora == 3:
                print('Saindo da calculadora binária...')
                sleep(1)
                break
            
            else:
                print('Opção inválida! Escolha dentre as opções pré-existentes do menu!')
                sleep(1)
                
         
         
         
         
        
    elif opcao == 4:
        print('Saindo do programa... Até mais!')
        sleep(1)
        break
    
    
    else:
        print('Opção inválida! Escolha dentre as opções pré-existentes do menu!')
        sleep(1)
    