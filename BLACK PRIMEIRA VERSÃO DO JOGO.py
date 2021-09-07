import random

def comparacao():

    # gera cartas do dealer

    print("Essa é a carta do dealer: ")

    carta1_do_dealer = conversao(carta(1))

    carta2_do_dealer = conversao(carta(2))

    # gera cartas do jogador

    print("Essas são suas cartas:")

    carta1_do_jogador = conversao(carta(1))

    carta2_do_jogador = conversao(carta(1))

    #armazenamento

    soma_do_jogador = 0
    soma_do_dealer = 0

    #comparando se há um black jack

    if (carta1_do_jogador == "A" and (carta2_do_jogador == "K" or carta2_do_jogador == "Q" or carta2_do_jogador == "J")) or (carta2_do_jogador == "A" and (carta1_do_jogador == "K" or carta1_do_jogador == "Q" or carta1_do_jogador == "J")):
        soma_do_jogador = 21
    elif (carta1_do_dealer == "A" and (carta2_do_dealer == "K" or carta2_do_dealer == "Q" or carta2_do_dealer == "J")) or (carta2_do_dealer == "A" and (carta1_do_dealer == "K" or carta1_do_dealer == "Q" or carta1_do_dealer == "J")):
        soma_do_dealer = 21

    #chama as funções que executam as jogadas

    else:
        soma_do_jogador = escolha_do_jogador(carta1_do_jogador,carta2_do_jogador)
        if soma_do_jogador < 21:
            soma_do_dealer = escolha_do_dealer(carta1_do_dealer,carta2_do_dealer)

    #compara as soma das cartas de ambos e diz quem venceu

    if soma_do_jogador == soma_do_dealer:
        print("Empate!")
    elif soma_do_jogador > 21 or (soma_do_dealer > soma_do_jogador and soma_do_dealer < 21):
        print("Você perdeu!")
    elif soma_do_dealer > 21 or soma_do_jogador > soma_do_dealer:
        print("Você venceu!")




def escolha_do_jogador(carta1,carta2):

        soma_das_cartas = carta1 + carta2

        if soma_das_cartas < 21:
            escolha = 1
            while escolha == 1 and soma_das_cartas < 21:

                print("Digite: ")
                print("1 - pegar mais uma carta")
                print("2 - parar")
                escolha = int(input())
                if escolha == 1:
                    carta_comprada = conversao(carta(1))
                    soma_das_cartas = soma_das_cartas + carta_comprada
                    print("(", soma_das_cartas, ")")
                if escolha != 1 and escolha != 2:
                    print("Por favor, digite 1 ou 2.")
                    escolha = 1

        return soma_das_cartas

def escolha_do_dealer(carta1,carta2):
    soma_das_cartas = carta1 + carta2
    if soma_das_cartas < 17:
        print("Compras do dealer: ")
    else:
        print("O dealer manteve sua mão.")
        print("(",soma_das_cartas,")")

    while soma_das_cartas < 17:
        carta_comprada = conversao(carta(1))
        soma_das_cartas = soma_das_cartas + carta_comprada
    print("(",soma_das_cartas,")")
    return soma_das_cartas

def desenho_da_carta(c,n):

    print()
    print("|",c,"      |")
    print("|",n,"      |")
    print("|   ",n,"   |")
    print("|     ",n," |")
    print("|     ",c," |")
    print()

def carta(verif):

    numerais = ["A",2,3,4,5,6,7,8,9,10,"K","Q","J"]
    naipes = ["♥", "♦", "♣", "♠"]

    carta = random.choice(numerais)
    naipe = random.choice(naipes)
    if verif == 1:
        desenho_da_carta(carta,naipe)

    return carta

def conversao(carta):
    if carta == "K" or carta == "Q" or carta == "J":
        carta = 10
    if carta == "A":
        carta = 1
    return carta

comparacao()