import os

palavra_secreta = input('Qual é a Palavra da Forca ?')
letras_acertadas = ''
tentativas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma Letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        palavra_secreta = input('Qual é a Palavra da Forca ?')
        letras_acertadas = ''
        tentativas = ''
        palavra_formada = ''
        palavra_secreta = ''