
import random
from time import sleep

#lembrar de tirar as repetições na parte dos ifs ali de escolha_configuracoes

def menu_principal(escolha_configuracoes,pontos,fichas):
    print("━━━━︳ MENU ︳━━━━┑")
    print("1.JOGAR          ︳")
    print("2.REGRAS/SOBRE   ︳")
    print("3.CONFIGURAÇÕES  ︳")
    print("4.SAIR           ︳")
    escolha_menu = input("ESCOLHA : ")
    escolha_menu = int(escolha_menu)

    for i in range(1, 100):
        print()

    pontos_do_jogador = 0
    pontos_do_dealer = 0
    escolha = 1
    if escolha_menu == 1:

        #PARTIDAS ISOLADAS

        if escolha_configuracoes == 1:
            while escolha == 1:
                if escolha == 1:
                    jogador_vs_dealer()
                    print("1. JOGAR NOVAMENTE")
                    print("2. MENU PRINCIPAL")
                    escolha = int(input())
                if escolha == 2:
                    menu_principal(escolha_configuracoes,pontos,fichas)
                else:
                    print("Digite 1 ou 2.")
                    escolha = 1

        #PLACAR CASUAL

        if escolha_configuracoes == 2:
            while escolha == 1:
                    if escolha == 1:
                        casual(pontos)
                        print()
                        print("1. JOGAR OUTRA SÉRIE")
                        print("2. MENU PRINCIPAL")
                        escolha = int(input())
                        print()
                    if escolha == 2:
                        menu_principal(escolha_configuracoes,pontos,fichas)
                    else:
                        print("POR FAVOR, DIGITE 1 OU 2.")
                        escolha = 1

       #PLACAR CASSINO

        if escolha_configuracoes == 3:
            while escolha == 1:
                if escolha == 1:
                    cassino(fichas)
                    print()
                    print("1. JOGAR OUTRA PARTIDA")
                    print("2. MENU PRINCIPAL")
                    escolha = int(input())
                    print()
                if escolha == 2:
                    menu_principal(escolha_configuracoes, pontos, fichas)
                else:
                    print("POR FAVOR, DIGITE 1 OU 2.")
                    escolha = 1


    elif escolha_menu == 2:
        print("REGRAS: ")
        print("")
        print("                JOGO                                       "
              "\n⬤ Se ultrapassar os 21 pontos, você perde INSTÂNTANEAMENTE."
              "\n⬤ Quem fizer 21 pontos ganha instantaneamente, a não ser que os dois façam ao mesmo tempo."
              "\n⬤ Caso ninguem faça 21 pontos, quem chegar mais próximo de 21 ganha."
              "\n⬤ Voçê poderá ver apenas 1 das cartas do dealer ao iniciar o jogo.")
        print(""
              "\n                CONFIGURAÇÕES"
              "\nAqui você pode escolher qual sistema de pontos desejar, ou seja,"
              "\nescolhendo 2 você vai definir o sistema de pontos para casual. Lembrando"
              "\nque o jogo vem com a configuração PADRÃO ao iniciar."
              "\n"
              "\n⬤ PADRÃO: Tendo apenas uma partida isolada(sem contagem de pontos)."
              "\n   Ganha quem marcar ou chegar mais perto do 21."
              "\n⬤ CASUAL: Aqui você vai escolher quantos pontos você vai disputar contra o dealer"
              "\n   contendo um sistema de contagem de pontos."
              "\n   Ganha quem tiver mais pontos ao se encerrar."
              "\n⬤ CASSINO: Na opção cassino você poderá escolher quantas fichas desejar começar,"
              "\n   aqui existe um sistema de apostas ao qual você apostará contra o dealer. "
              "\n   Você que dirá quanto ganhou, ou seja, se saiu no lucro ou deseja apostar mais.  ")
        print()
        print("Digite qualquer coisa para sair: ")
        sair = input()
        menu_principal(escolha_configuracoes,pontos,fichas)

    elif escolha_menu == 3:
        print("CONFIGURAÇÕES: ")
        print("SISTEMA DE PONTOS")
        print("1. PADRÃO")
        print("2. CASUAL")
        print("3. CASSINO")
        print("ATUAL: ",escolha_configuracoes)
        escolha_configuracoes = int(input("ESCOLHA: "))

        if escolha_configuracoes == 2:
            print("DIGITE A QUANTIDADE DE PONTOS PARA ACABAR A SÉRIE: ")
            print("ATUAL: ",pontos)
            pontos = int(input())

        if escolha_configuracoes == 3:
            print("DIGITE A QUANTIDADE DE FICHAS QUE VOCÊ COMEÇA: ")
            print("ATUAL: ",fichas)
            fichas = int(input())

        menu_principal(escolha_configuracoes,pontos,fichas)


def jogador_vs_dealer():
    # armazenamento

    ganhou = 0
    cartas_do_dealer = []
    cartas_do_jogador = []
    soma_do_jogador = 0
    soma_do_dealer = 0

    # 1.gera cartas do jogador 2. junta as duas listas em uma (a função carta retorna uma lista)
    # 3. armazena as cartas em uma variavel auxiliar 4. chama a funçao "separador" que remove o naipe deixando só o numerador

    print("Essa é a carta do dealer: ")

    carta1_do_dealer = carta()
    carta2_do_dealer = carta()

    cartas_do_dealer = carta1_do_dealer + carta2_do_dealer

    cartas_do_dealer_aux = cartas_do_dealer
    cartas_do_dealer = separador(cartas_do_dealer,0)

    desenho_da_carta(carta1_do_dealer)
    print()
    # gera as cartas do dealer e faz o mesmo processo acima

    print("Essas são suas cartas:")

    carta1_do_jogador = carta()
    carta2_do_jogador = carta()

    cartas_do_jogador = carta1_do_jogador + carta2_do_jogador

    cartas_do_jogador_aux = cartas_do_jogador
    cartas_do_jogador = separador(cartas_do_jogador,0)

    desenho_da_carta(cartas_do_jogador_aux)
    print()
    carta1_do_jogador = cartas_do_jogador[0]
    carta2_do_jogador = cartas_do_jogador[1]

    carta1_do_dealer = cartas_do_dealer[0]
    carta2_do_dealer = cartas_do_dealer[1]

    # compara se há um blackjack senão tiver chama as funçoes que executam as jogadas

    if blackjack(carta1_do_jogador, carta2_do_jogador) == True:
        soma_do_jogador = soma(cartas_do_jogador)
    elif blackjack(cartas_do_dealer, carta2_do_dealer) == True:
        soma_do_dealer = soma(cartas_do_dealer)

    else:
        cartas_do_jogador = escolha_do_jogador(cartas_do_jogador_aux, cartas_do_jogador)
        cartas_do_jogador_aux = cartas_do_jogador
        cartas_do_jogador = separador(cartas_do_jogador,0)
        soma_do_jogador = soma(cartas_do_jogador)
        if soma_do_jogador < 21:
            cartas_do_dealer = escolha_do_dealer(cartas_do_dealer_aux, cartas_do_dealer)
            cartas_do_dealer_aux = cartas_do_dealer
            cartas_do_dealer = separador(cartas_do_dealer,0)
            soma_do_dealer = soma(cartas_do_dealer)

    # compara as soma das cartas de ambos e diz quem venceu
    print()
    if soma_do_jogador == soma_do_dealer:
        print("Empate!")
        ganhou = 0
    elif soma_do_jogador > 21 or (soma_do_dealer > soma_do_jogador and soma_do_dealer <= 21):
        print("Você perdeu!")
        ganhou = 2
    elif soma_do_dealer > 21 or (soma_do_jogador > soma_do_dealer and soma_do_jogador <= 21):
        print("Você venceu!")
        ganhou = 1
    sleep(2)

    print()
    print()
    print("Suas cartas:")
    desenho_da_carta(cartas_do_jogador_aux)
    print("(",soma_do_jogador,")")
    print()
    print("Cartas do dealer:")
    desenho_da_carta(cartas_do_dealer_aux)
    print("(",soma_do_dealer,")")
    print()

    return ganhou

def escolha_do_jogador(cartas_aux, cartas):
    soma_das_cartas = soma(cartas)
    print("(", soma_das_cartas, ")")
    cartass = []
    if soma_das_cartas < 21:
        escolha = 1
        while escolha == 1 and soma_das_cartas < 21:

            print("Digite: ")
            print("1 - pegar mais uma carta")
            print("2 - parar")
            escolha = int(input())
            if escolha == 1:
                carta_comprada = carta()
                cartass = cartas_aux + carta_comprada
                cartas_aux = cartass
                print()
                print("Sua compra: ")
                desenho_da_carta(carta_comprada)
                cartass = separador(cartass,0)
                soma_das_cartas = soma(cartass)
                print("(", soma_das_cartas, ")")
                print()
            if soma_das_cartas > 21:
                print("ESTOUROU!!")
            if escolha != 1 and escolha != 2:
                print("Por favor, digite 1 ou 2.")
                escolha = 1

    return cartas_aux


def escolha_do_dealer(cartas_aux, cartas):
    soma_das_cartas = soma(cartas)
    if soma_das_cartas < 17:
        print("Compras do dealer: ")
    else:
        print("O dealer manteve sua mão.")

    while soma_das_cartas < 17:
        carta_comprada = carta()
        cartass = cartas_aux + carta_comprada
        cartas_aux = cartass
        desenho_da_carta(carta_comprada)
        cartass = separador(cartass,0)
        soma_das_cartas = soma(cartass)
    print("(", soma_das_cartas, ")")
    return cartas_aux


def desenho_da_carta(lista):
    numeral = lista
    naipe = lista

    tamanho = len(lista)
    entra = tamanho
    for numerais in range(0, tamanho, 2):
        c_aux = separador(numeral,0)
        n_aux = separador(numeral,1)
        tamanho2 = len(c_aux)
        for qual in range(0,tamanho2):
            c = c_aux[qual]
            n = n_aux[qual]
            if entra !=0:
                print()
                if c == 10:
                    print(" _________ "
                          "\n|", c, "     |"
                          "\n|", n, "      |"
                          "\n|   ", n, "   |"
                          "\n|     ", n, " |"
                          "\n|     ", c, "|"
                          "\n —————————"
                          "\n")
                else:

                    print(" _________ "
                          "\n|", c, "      |"
                          "\n|", n, "      |"
                          "\n|   ", n, "   |"
                          "\n|     ", n, " |"
                          "\n|     ", c, " |"
                          "\n —————————")

                entra = entra - 2


def carta():
    cartas = []
    numerais = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
    naipes = ["♥", "♦", "♣", "♠"]

    carta = random.choice(numerais)
    naipe = random.choice(naipes)

    cartas.append(carta)
    cartas.append(naipe)

    return cartas


def conversao(carta):
    if carta == "K" or carta == "Q" or carta == "J":
        carta = 10
    if carta == "A":
        carta = 1
    return carta


def separador(cartas,qual):
    teste = len(cartas)
    lista = []

    for numeral in range(qual, teste, 2):
        lista.append(cartas[numeral])
    return lista


def soma(cartas):
    soma = 0
    for numerador in cartas:
        numerador = conversao(numerador)
        soma = soma + numerador
    return soma


def blackjack(carta1, carta2):
    if (carta1 == "A" and (carta2 == "K" or carta2 == "Q" or carta2 == "J")) or (carta1 == "A" and (carta2 == "K" or carta2 == "Q" or carta2 == "J")):
        return True
    return False

def casual(pontos):

    #armazenamento

    escolha = 1
    pontos_do_jogador = 0
    pontos_do_dealer = 0

    while pontos_do_jogador != pontos and pontos_do_dealer != pontos:
        ganhou = jogador_vs_dealer()
        if ganhou == 1:
            pontos_do_jogador = pontos_do_jogador + 1
        elif ganhou == 2:
            pontos_do_dealer = pontos_do_dealer + 1
        elif ganhou == 3:
            pontos_do_dealer = pontos_do_dealer
            pontos_do_jogador = pontos_do_jogador
        print("PLACAR: ")
        print("JOGADOR ", pontos_do_jogador, "x", pontos_do_dealer, "DEALER")
        if pontos_do_jogador != pontos and pontos_do_dealer != pontos:
            print("DIGITE QUALQUER COISA PARA INICIAR A PRÓXIMA RODADA")
            esperar = input()
        elif pontos_do_jogador == pontos:
            print("PARABÉNS!!!!"
                    "\nVOCÊ VENCEU A SÉRIE!!!")
        elif pontos_do_dealer == pontos:
            print("O DEALER VENCEU A SÉRIE!!")

def cassino(fichas):

    valor_inicial = fichas
    escolha = 1

    while fichas != 0 and escolha != 2:
        print("SUAS FICHAS: ", fichas)
        print("DIGITE QUANTAS FICHAS VOCÊ QUER APOSTAR: ")
        aposta = int(input())
        if aposta > fichas:
            print("VOCÊ NÃO PODE APOSTAR MAIS FICHAS DO QUE TEM.")
            print("SUAS FICHAS: ", fichas)
        ganhou = jogador_vs_dealer()
        if ganhou == 1:
            fichas = fichas + aposta
            print("+",aposta)
        elif ganhou == 2:
            fichas = fichas - aposta
            print("-",aposta)
        elif ganhou == 3:
            print("SUAS FICHAS FORAM DEVOLVIDAS PARA VOCÊ.")

        print("VOCÊ TEM",fichas,"FICHAS.")
        print()
        if fichas != 0:
            print("1. FAZER OUTRA APOSTA")
            print("2. PARAR")
            escolha = int(input("ESCOLHA: "))
        else:
            print("INFELIZMENTE, VOCÊ NÃO TEM MAIS FICHAS.")
            escolha = 2
    if fichas > valor_inicial:
        diferenca = fichas - valor_inicial
        print("VOCÊ SAIU GANHANDO",diferenca,"FICHAS.")
        print("TOTAL DE FICHAS: ",fichas)
    elif fichas < valor_inicial:
        diferenca = valor_inicial - fichas
        print("VOCÊ SAIU PERDENDO",diferenca,"FICHAS.")
        print("TOTAL DE FICHAS: ",fichas)
    else:
        print("VOCÊ PERDEU TODAS AS FICHAS!")






#padrão (1,2,100)
menu_principal(1,2,100)