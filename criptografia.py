print("---------- APS: Criptografia (Cifra de César) ----------")

while True:     # Loop para reiniciar o programa caso o usuário queira

    while True:     # Laço de repetição para forçar uma entrada válida de mensagem

        mensagem = input("Digite a mensagem que deseja processar (até 128 caracteres): ") 

        if len(mensagem) <= 128:    # Uso de 'len' para a contagem de caracteres dentro da mensagem
            break   # sai do loop
        else:
            print("Mensagem muito longa! Digite no máximo 128 caracteres")


    while True:     # Loop para forçar o usuário a escolher apenas as opções dadas
        
        acao = input('Digite a ação que deseja realizar ("c" para criptografar e "d" para descriptografar): ').lower()
        # Uso de 'lower' para aceitar caso o usuário digite 'c' ou 'd' em maiúsculo

        if acao == "c" or acao == "d":
            break
        else:
            print('Ação inválida! digite apenas "c" ou "d" para continuar')

    while True:     # Loop para forçar uma entrada de chave válida

        try:    # Tratamento de erro para o uso de algo que não seja número inteiro

            chave = int(input("Digite a chave (1 a 25): "))
            
            if 1 <= chave <= 25:
                break
            else:
                print("Chave inválida! Digite um número entre 1 e 25")

        except ValueError:
            print("Entrada inválida, utilize apenas números")

    resultado = ""      # Variável vazia que vai acumular os caracteres da mensagem (1 por vez)

    for c in mensagem:      # Loop que percorre cada caractere da mensagem

        if c.isupper():       # Verifica se o caractere  é maiúsculo
            base = ord('A')     # Se o caractere for maiúsculo, a variável "base" vai usar a letra A da tabela ASCII como base
            if acao == "c":
                resultado += chr((ord(c) - base + chave) % 26 + base)      # Criptografar
# Transforma o caractere em número da tabela ASCII, subtrai pela variável "base" para a base ficar em um valor de 0 a 25,
# depois soma (para criptografar) ou subtrai (para descriptografar) a chave. Então o uso de "% 26" (resto de divisão)
# para garantir que o caractere vai se manter dentro das 26 letras do alfabeto, por conseguinte a soma da base novamente
# para voltar ao padrão da tabela ASCII. Assim temos o uso de "chr" para transformar o valor de número para letras
# de volta e "+=" para adicionar caracteres ao resultado
            else:
                resultado += chr((ord(c) - base - chave) % 26 + base)      # Descriptografar

# Nota do Luska: caracteres maiúsculos e minúsculos tem valores diferentes na tabela ASCII, por isso
# a verificação e também o valor da "base" ser alternado para cada um dos casos
    
        elif c.islower():     # Verifica se o caractere é minúsculo
            base = ord('a')
            if acao == "c":
                resultado += chr((ord(c) - base + chave) % 26 + base)
            else:
                resultado += chr((ord(c) - base - chave) % 26 + base)

        else:       # Para outros tipos de caracteres (espaço, número, pontuação, etc)
            resultado += c      # Adiciona mais caractere a variável
    
    print(f"A mensagem processada é: {resultado}")

    while True:     # Loop para forçar uma entrada válida
        continuar = input('Deseja processar outra mensagem? Digite "S" para reiniciar ou "N" para encerrar: ').lower()
        if continuar in ("s", "n"):     # Percorre a 'tupla' para comparar o valor #amopython
            break   # Sai do loop depois de receber a entrada esperada
        else:
            print('Opção inválida! Digite apenas "S" ou "N"')

    if continuar == "n":
        print("Encerrando o programa...")
        break
