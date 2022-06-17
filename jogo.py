from assets.funcoes import cabecario, limparTela, caveiraPerderdor, desenhaForca, trofeuGanhador
import time

limparTela()
cabecario()

while True:
    print('Desafiante:')
    desafiante = input('> ')
    if len(desafiante) < 1:
        print("\033[1;31mO nome do desafiante não pode conter menos de uma caractere! \033[m")
    else:
        break
while True:
    print('Competidor: ')
    competidor = input('> ')
    if len(competidor) < 1:
        print("\033[1;31mO nome do competidor não pode conter menos de uma caractere! \033[m")
    else:
        break
limparTela()
cabecario()
while True:
    print('digite a palavra: ')
    palavra = input('> ')
    if len(palavra) < 1:
        print('\033[1;31mA palavra não faz sentido!\033[m')
    else:
        break
palavraS = ' *' * len(palavra)
dicaErro = ('\033[1;31mA dica deve conter no minimo uma caractere!\033[m')
while True:
    dica1 = input('digite a dica 1: ')
    if len(dica1) < 1:
        print(dicaErro)
    else:
        break
while True:
    dica2 = input('digite a dica 2: ')
    if len(dica2) < 1:
        print(dicaErro)
    else:    
        break
while True:
    dica3 = input('digite a dica 3: ')
    if len(dica3) < 1:
        print(dicaErro)
    else:
        break

digitados = []
chance = 6
erros = 0
limparTela()
cabecario()

print('Palavra secreta:', palavraS)
print()
print(f'O competidor ainda tem {chance} chances. ')
print()
while True:
    print('(1) jogar')
    print('(2) pedir uma dica')
    print('(3) dar um chute: ')
    lol = input('>')
    limparTela()
    cabecario()
    secreto_temp = ''
    if lol =='1':
        letra = input('Competidor, digite uma letra: ')
        limparTela()
        cabecario()
        
        if len(letra) > 1:
            print('ERROR, Digitar mais que uma letra não pode campeão!!!')
            continue
        
        digitados.append(letra)
        
        for letra_secre in palavra:
            if letra_secre in digitados:
                secreto_temp += letra_secre
            else:
                secreto_temp += ' *'
        if secreto_temp == palavra:
            limparTela()
            print(f'Parabéns, o competidor {competidor} GANHOU !!!')
            print(f'A palavra era {palavra}')
            trofeuGanhador()
            vencedor = (f'\nDesafiante PERDEDOR > {competidor}\nCompetidor VENCEDOR > {desafiante}\nPalavra > {palavra}\n')
            print('Aperte ENTER pra sair')
            input() 
            break
        else:
            
            print(f'Palavra secreta: {secreto_temp}')
            print()

        if letra not in palavra:
            chance -= 1
            erros += 1
            desenhaForca(erros)
            print(f'Palavra secreta: {secreto_temp}')
            print('\033[1;31mVocê errou!       \033[m')

        if erros >= 6:
            limparTela()
            print(f'Não foi dessa vez, o desafiante {desafiante} ganhou!')
            print(f'A palavra era {palavra}\n')
            caveiraPerderdor()
            vencedor = (f'\nDesafiante VENCEDOR > {competidor}\nCompetidor PERDEDOR > {desafiante}\nPalavra > {palavra}\n')
            print('Aperte ENTER pra sair')
            input()
            break
        print(f'O competidor ainda tem {chance} chances. ')
        print()
    elif lol == '2':
        print('Escolha qual dica você quer:')
        print('(1) dica 01')
        print('(2) dica 02')
        print('(3) dica 03')
        dicaEscolida = input()
        if dicaEscolida == '1':
            print('A dica 01 é ', dica1)
        elif dicaEscolida == '2':
            print('A dica 02 é ', dica2)
        elif dicaEscolida == '3':
            print('A dica 03 é ', dica3)
        time.sleep(4)
        limparTela()
        cabecario()
    elif lol == '3':
        for letra_secre in palavra:
            if letra_secre in digitados:
                secreto_temp += letra_secre
            else:
                secreto_temp += ' *'
        chuteR = input('De o seu chute: ')
        if chuteR == palavra:
            limparTela()
            print(f'Parabéns, o competidor {competidor} GANHOU !!!')
            print(f'A palavra era {palavra}')
            trofeuGanhador()
            vencedor = (f'\nDesafiante PERDEDOR > {competidor}\nCompetidor VENCEDOR > {desafiante}\nPalavra > {palavra}\n')
            print('Aperte ENTER pra sair')
            input() 
            break 
        else:
            erros +=1
            chance -= 1
            desenhaForca(erros)
            print(f'Palavra secreta: {secreto_temp}')
            print('\033[1;31mVocê errou!       \033[m')
            print(f'O competidor ainda tem {chance} chances. ')
            continue

while True:
            limparTela()
            try:
                print("\n")
                arquivo = open('arquivo.txt','a')
                arquivo.write(vencedor + "\n")
                arquivo.close()

                arquivo = open('arquivo.txt','r')
                limparTela()
                print("Histórico de partidas:\n")
                for linha in arquivo:
                    linha = linha.rstrip()
                    print (linha)
                arquivo.close()
                print()
                break
            except:
                arquivo = open('arquivo.txt','w')
                arquivo.close()