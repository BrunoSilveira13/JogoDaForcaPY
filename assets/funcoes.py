import os 
import time
def cabecario():
    print('-=' * 20 )
    print('        JOGO DA FORCA')
    print('-=' * 20 )
def limparTela():
    os.system('cls')
def caveiraPerderdor():
    print("\033[1;31m              _______________         ")
    print("             /               \       ")
    print("            /                 \      ")
    print("          //                   \/\  ")
    print("          \|   XXXX     XXXX   | /   ")
    print("           |   XXXX     XXXX   |/     ")
    print("           |   XXX       XXX   |      ")
    print("           |                   |      ")
    print("           \__      XXX      __/     ")
    print("             |\     XXX     /|       ")
    print("             | |           | |        ")
    print("             | I I I I I I I |        ")
    print("             |  I I I I I I  |        ")
    print("             \_             _/       ")
    print("               \_         _/         ")
    print("                 \_______/    \033[m  ")
def trofeuGanhador():
    print("\033[1;33m       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \033[m")
def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |       |\   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |        \   ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")
        
    print(" |            ")
    print("_|___         ")
    print()
def forcaSozinha():
    print("  _______     ")
    print(" |/      |    ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print("_|___         ")
    print()
