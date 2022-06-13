from assets.funcoes import cabecario
import time

while True:
    desafiante = input('Desafiente: ')
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

palavra = input('digite a palavra: ')
arquivoPL = open('players.txt', 'w')
arquivoPL.write(f'DESAFIANTE > {desafiante}')
arquivoPL.write('\n')
arquivoPL.write(F'COMPETIDOR > {competidor}')
arquivoPL.write('\n')
arquivoPL.write(f'PALAVRA > {palavra}')
arquivoPL.write('\n')
arquivoPL.close()


def jogo():
   
    dica1 = input('digite a dica 1: ')
    dica2 = input('digite a dica 2: ')
    dica3 = input('digite a dica 3: ')

    digitados = []
    chance = 6

    while True:

        print('(1) jogar')
        print('(2) pedir uma dica')
        print('(3) dar um chute: ')
        lol = input()
        if lol =='1':
            letra = input('Competidor, digite uma letra: ')
            
            if len(letra) > 1:
                print('ERROR, Digitar mais que uma letra não pode campeão!!!')
                continue
            
            digitados.append(letra)
            secreto_temp = ''
            for letra_secre in palavra:
                if letra_secre in digitados:
                    secreto_temp += letra_secre
                else:
                    secreto_temp += '*'

            if secreto_temp == palavra:
                print('PARABÉNS, O COMPETIDOR GANHAOU !!!')
                break
            else:
                print(f'Palavra secreta: {secreto_temp}')
            
            if letra not in palavra:
                chance -= 1
            
            if chance <= 0:
                print('NÃO FOI DESSA VEZ, O DESAFIANTE GANHOU!!!')
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
                print(dica1)
            elif dicaEscolida == '2':
                print(dica2)
            elif dicaEscolida == '3':
                print(dica3)
            time.sleep(4)
        elif lol == '3':
            chuteR = input('de o seu chute: ')
            if chuteR == palavra:
                print(f'PARABÉNS, O COMPETIDOR {competidor} GANHOU!!!')   
                break 
            elif chuteR != palavra:
                print(f'NÃO FOI DESSA VEZ, O DESAFIANTE {desafiante} GANHOU!!!')
                break


jogo()