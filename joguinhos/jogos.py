import forca, adivinhacao, par_ou_impar

def escolhe_jogo():
    print("*******************************************")
    print("*********** Escolha o seu jogo! ***********")
    print("*******************************************")

    print("(1) Forca (2) Adivinhação (3) Par ou Impar")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print()
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print()
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print()
        print("Jogando par ou impar")
        par_ou_impar.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
