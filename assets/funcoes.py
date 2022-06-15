import os 
def cabecario():
    print('-=' * 20 )
    print('        JOGO DA FORCA')
    print('-=' * 20 )
def limparTela():
    os.system('cls')
def mudarCor():
    os.system('color 2')
def erroPalavra(palavra):
    while not palavra.isalpha():
        print('Apenas letras são permitidadas!')
        palavra = input('digite a palavra: ')
    return palavra.upper()
def inicializaLetras(palavra):
    return ["*" for letra in palavra]

def caveiraPerderdor():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def trofeuGanhador():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def desenhaForca(cima):
    print("  _______     ")
    print(" |/      |    ")
def cabeca():
    print(" |      (_)   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")