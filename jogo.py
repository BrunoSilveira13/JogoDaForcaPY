from assets.funcoes import cabecario, limparTela, mudarCor
import time
mudarCor()
limparTela()
cabecario()
while True:
    desafiante = input('Desafiante: ')
    if len(desafiante) < 1:
        print("O nome do desafiante não pode conter menos de uma caractere! ")
    else:
        break
while True:
    competidor = input('Competidor: ')
    if len(competidor) < 1:
        print("O nome do competidor não pode conter menos de uma caractere! ")
    else:
        break
limparTela()
cabecario()
palavra = input('digite a palavra: ')

palavraS = ' *' * len(palavra)

while True:
    dica1 = input('digite a dica 1: ')
    if len(dica1) < 1:
        print('A dica deve conter no minimo uma caractere!')
    else:
        break
while True:
    dica2 = input('digite a dica 2: ')
    if len(dica2) < 1:
        print('A dica deve conter no minimo uma caractere!')
    else:
        break
while True:
    dica3 = input('digite a dica 3: ')
    if len(dica3) < 1:
        print('A dica deve conter no minimo uma caractere!')
    else:
        break

digitados = []
chance = 6
limparTela()
cabecario()
print('Palavra secreta:', palavraS)
print(f'O competidor ainda tem {chance} chances. ')
while True:
    print('(1) jogar')
    print('(2) pedir uma dica')
    print('(3) dar um chute: ')
    lol = input()
    limparTela()
    cabecario()
    if lol =='1':
        letra = input('Competidor, digite uma letra: ')
        limparTela()
        cabecario()
        
        if len(letra) > 1:
            print('ERROR, Digitar mais que uma letra não pode campeão!!!')
            continue
        
        digitados.append(letra)
        secreto_temp = ''
        for letra_secre in palavra:
            if letra_secre in digitados:
                secreto_temp += letra_secre
            else:
                secreto_temp += ' *'
        
        if secreto_temp == palavra:
            print('Parabéns, o competidor GANHAOU !!!')
            vencedor = (f'\nCompetidor VENCEDOR > {competidor}\nDesafiante PERDEDOR > {desafiante}\nPalavra > {palavra}\n')
            break
        else:
            print(f'Palavra secreta: {secreto_temp}')
        
        if letra not in palavra:
            chance -= 1
        # if not letra in letra_secre:
        #     print('Você ja chutou essa letra')
        #     continue

        if chance <= 0:
            print(f'Não foi dessa vez, o desafiante {desafiante} ganhou!')
            vencedor = (f'\nDesafiante VENCEDOR > {competidor}\nCompetidor PERDEDOR > {desafiante}\nPalavra > {palavra}\n')
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
        chuteR = input('De o seu chute: ')
        if chuteR == palavra:
            print('Parabéns, o competidor GANHOU !!!')
            vencedor = (f'\nDesafiante PERDEDOR > {desafiante}\nCompetidor VENCEDOR > {competidor}\nPalavra > {palavra}\n') 
            input()  
            break 
        elif chuteR != palavra:
            chance -= 1
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
                
                    


