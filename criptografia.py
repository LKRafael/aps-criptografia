print("---------- APS: Criptografia (Cifra de César) ----------")

while True:     # Loop para reiniciar o programa caso o usuário queira

    while True:     # Laço de repetição para forçar uma entrada válida de mensagem

        mensagem = input("Digite a mensagem que deseja processar (até 128 caracteres): ") 

        if len(mensagem) <= 128:    # Uso de 'len' para a contagem de caracteres dentro da mensagem
            break   # sai do loop
        else:
            print("Mensagem muito longa! Digite no máximo 128 caracteres")


    while True:     # Loop para forçar o usuário a escolher apenas as opções dadas
        
        acao = input("Digite a ação que deseja realizar ('c' para criptografar e 'd' para descriptografar): ").lower()
        # Uso de 'lower' para aceitar caso o usuário digite 'c' ou 'd' em maiúsculo

        if acao == "c" or acao == "d":
            break
        else:
            print("Ação inválida! digite apenas 'c' ou 'd' para continuar")

    while True:     # Loop para forçar uma entrada de chave válida

        try:    # Tratamento de erro para o uso de algo que não seja número inteiro

            chave = int(input("Digite a chave (1 a 25): "))
            
            if 1 <= chave <= 25:
                break
            else:
                print("Chave inválida! Digite um número entre 1 e 25")

        except ValueError:
            print("Entrada inválida, utilize apenas números")

    resultado = ""      # Variável vazia que vai acumular os caracteres da mensagem

    for c in mensagem:      # Loop que percorre cada caractere da mensagem

        if c.isupper():       # Verifica se o caractere  é maiúsculo
            resultado += c    # Adiciona caractere

        elif c.islower():     # Verifica se o caractere é minúsculo
            resultado += c

        else:       # Para outros tipos de caracteres (espaço, número, pontuação, etc)
            resultado += c
            