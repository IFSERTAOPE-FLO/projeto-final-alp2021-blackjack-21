import sys
import random
from time import sleep

def menu_principal(escolha_configuracoes,pontos,fichas):

    #MENU PRINCIPAL

    limpar_tela()

    print("━━━━︳ MENU ︳━━━━┑")
    print("1.JOGAR          ︳")
    print("2.REGRAS/SOBRE   ︳")
    print("3.CONFIGURAÇÕES  ︳")
    print("4.SAIR           ︳")
    escolha_menu = input("ESCOLHA : ")

    limpar_tela()

    escolha = 1

    #1.JOGAR

    if escolha_menu == "1":

        #PARTIDAS ISOLADAS

        if escolha_configuracoes == "1":
            while escolha == 1:
                if escolha == 1:
                    print("PARTIDA ÚNICA")
                    sleep(1)
                    jogador_vs_dealer()
                escolha = jogar_novamente(escolha_configuracoes,pontos,fichas)

        #PARTIDAS CASUAL

        if escolha_configuracoes == "2":
            while escolha == 1:
                    if escolha == 1:
                        print("PARTIDA CASUAL")
                        sleep(1)
                        casual(pontos)
                    escolha = jogar_novamente(escolha_configuracoes,pontos,fichas)

       #PARTIDAS CASSINO

        if escolha_configuracoes == "3":
            while escolha == 1:
                if escolha == 1:
                    print("BEM-VINDO AO CASSINO")
                    sleep(1)
                    cassino(fichas)
                escolha = jogar_novamente(escolha_configuracoes, pontos, fichas)


    #2.REGRAS/SOBRE

    elif escolha_menu == "2":
        regras(escolha_configuracoes,pontos,fichas)

    #3.CONFIGURAÇÕES

    elif escolha_menu == "3":

        print()
        print("CONFIGURAÇÕES: ")
        print("SISTEMA DE PONTOS")
        print("1. PADRÃO")
        print("2. CASUAL")
        print("3. CASSINO")
        print("ATUAL: ",escolha_configuracoes)
        escolha_configuracoes = input("ESCOLHA: ")
        print()

        #CONFIGURAÇÕES CASUAL

        if escolha_configuracoes == "2":
            print("DIGITE A QUANTIDADE DE PONTOS PARA ACABAR A SÉRIE: ")
            print("ATUAL: ",pontos)
            pontos = int(input())

        #CONFIGURAÇÕES CASSINO

        if escolha_configuracoes == "3":
            print("DIGITE A QUANTIDADE DE FICHAS QUE VOCÊ COMEÇA: ")
            print("ATUAL: ",fichas)
            fichas = int(input())

        menu_principal(escolha_configuracoes,pontos,fichas)

    #4.SAIR

    elif escolha_menu == "4":
        print("VOCÊ TEM CERTEZA QUE QUER SAIR? ")
        print("1. SIM")
        print("2. NÃO")
        sair_agora = input()
        if sair_agora == "1":
            sys.exit()
        elif sair_agora != "1":
            menu_principal(escolha_configuracoes,pontos,fichas)


def jogador_vs_dealer():

    #ARMAZENAMENTO

    ganhou = 0
    cartas_do_dealer = []
    cartas_do_jogador = []

    #DEALER

    print("Essa é a carta do dealer: ")

    #GERA AS CARTAS DO DEALER (FUNÇÃO CARTA RETORNA UMA LISTA)

    carta1_do_dealer = carta()
    carta2_do_dealer = carta()

    #JUNTA AS DUAS LISTAS COM AS CARTAS EM SÓ UMA LISTA E ARMAZENA ESSA LISTA UMA VARIAVEL AUXILIAR

    cartas_do_dealer = carta1_do_dealer + carta2_do_dealer
    cartas_do_dealer_aux = cartas_do_dealer

    #SEPARA OS NUMERAIS DOS NAIPES E PRINTA O DESENHO DA CARTA

    cartas_do_dealer = separador(cartas_do_dealer,0)
    desenho_da_carta(carta1_do_dealer)
    print()


    #JOGADOR

    print("Essas são suas cartas:")

    #GERA AS CARTAS DO JOGADOR (FUNÇÃO CARTA RETORNA UMA LISTA)

    carta1_do_jogador = carta()
    carta2_do_jogador = carta()

    #JUNTA AS DUAS LISTAS COM AS CARTAS EM SÓ UMA LISTA E ARMAZENA ESSA LISTA EM UMA VARIAVEL AUXILIAR

    cartas_do_jogador = carta1_do_jogador + carta2_do_jogador
    cartas_do_jogador_aux = cartas_do_jogador

    #SEPARA OS NUMERAIS DOS NAIPES E PRINTA O DESENHO DA CARTA

    cartas_do_jogador = separador(cartas_do_jogador,0)
    desenho_da_carta(cartas_do_jogador_aux)
    print()

    #COM OS NUMERAIS SEPARADO DOS NAIPES, SEPARA CADA NUMERAL EM UMA VARIAVEL

        #DEALER

    carta1_do_dealer = cartas_do_dealer[0]
    carta2_do_dealer = cartas_do_dealer[1]
    soma_do_dealer = soma(cartas_do_dealer)
        #JOGADOR

    carta1_do_jogador = cartas_do_jogador[0]
    carta2_do_jogador = cartas_do_jogador[1]
    soma_do_jogador = soma(cartas_do_jogador)

    #VERIFICA SE HÁ UM BLACKJACK

    if blackjack(carta1_do_jogador, carta2_do_jogador) == True:
        print("BlackJack!!")
    elif blackjack(cartas_do_dealer, carta2_do_dealer) == True:
        print("BlackJack!!")

    #CASO NÃO HAJA UM BLACKJACK CHAMA AS FUNÇÕES PARA COMPRAS DE CARTAS

    else:

        #JOGADOR

        cartas_do_jogador = escolha_do_jogador(cartas_do_jogador_aux, cartas_do_jogador)
        cartas_do_jogador_aux = cartas_do_jogador
        cartas_do_jogador = separador(cartas_do_jogador,0)
        soma_do_jogador = soma(cartas_do_jogador)
        limpar_tela()

        #DEALER (CASO O JOGADOR NÃO TENHA ESTOURADO)

        if soma_do_jogador < 21:
            cartas_do_dealer = escolha_do_dealer(cartas_do_dealer_aux, cartas_do_dealer)
            cartas_do_dealer_aux = cartas_do_dealer
            cartas_do_dealer = separador(cartas_do_dealer,0)
            soma_do_dealer = soma(cartas_do_dealer)


    #VERIFICA QUEM VENCEU

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

    print("digite qualquer coisa para continuar")
    nada = input()

    #MOSTRA TODAS AS CARTAS DO DEALER E JOGADOR

    print()
    print()
    print("Suas cartas:")
    desenho_da_carta(cartas_do_jogador_aux)
    print("(",soma_do_jogador,")")

    sleep(1)

    print()
    print("Cartas do dealer:")
    desenho_da_carta(cartas_do_dealer_aux)
    print("(",soma_do_dealer,")")
    print()

    return ganhou

def escolha_do_jogador(cartas_aux, cartas):

    #FUNÇÃO RECEBE DUAS LISTAS

    #SOMA OS VALORES DE UMA LISTA E MOSTRA A SOMA

    soma_das_cartas = soma(cartas)
    print("(", soma_das_cartas, ")")

    #ARMAZENAMENTO

    cartass = []
    escolha = "1"

    #COMPRAS

    while escolha == "1" and soma_das_cartas < 21:

        print()
        print("Digite: ")
        print("1 - COMPRAR")
        print("2 - PARAR")
        escolha = input()
        print()

        #1. COMPRAR

        if escolha == "1":

            #GERA A CARTA COMPRADA JUNTA ESSA CARTA COM AS OUTRAS E ARMAZENA EM UMA VARIAVEL AUXILIAR

            carta_comprada = carta()
            cartass = cartas_aux + carta_comprada
            cartas_aux = cartass

            #DESENHA A CARTA COMPRADA

            print()
            print("Sua compra: ")
            desenho_da_carta(carta_comprada)

            #SEPARA OS NUMERAIS DOS NAIPES, SOMA AS CARTAS, DEVOLVE O VALOR E VERIFICA SE NÃO PASSOU DO LIMITE

            cartass = separador(cartass,0)
            soma_das_cartas = soma(cartass)

            print("(", soma_das_cartas, ")")
            print()

            if soma_das_cartas > 21:
                nada = 0

        #2.PARAR

        elif escolha == "2":
            print("VOCÊ ESCOLHEU PARAR")

        #VALOR INVALIDO

        else:
            print("POR FAVOR DIGITE 1 OU 2")
            escolha = "1"

    return cartas_aux


def escolha_do_dealer(cartas_aux, cartas):

    #FUNÇÃO RECEBE DUAS LISTAS

    #SOMA OS VALORES DA LISTA

    soma_das_cartas = soma(cartas)

    #DEALER SÓ COMPRA CARTA SE O VALOR DAS CARTAS FOR MENOR QUE 17

    if soma_das_cartas < 17:

        #COMPRAS

        print("Compras do dealer: ")
        while soma_das_cartas < 17:

            ##GERA A CARTA COMPRADA JUNTA ESSA CARTA COM AS OUTRAS E ARMAZENA EM UMA VARIAVEL AUXILIAR

            carta_comprada = carta()
            cartass = cartas_aux + carta_comprada
            cartas_aux = cartass

            #DESENHA A CARTA COMPRADA, SEPARA OS NUMERAIS DOS NAIPES E SOMA AS CARTAS

            desenho_da_carta(carta_comprada)

            cartass = separador(cartass, 0)
            soma_das_cartas = soma(cartass)

        #NÃO COMPROU
    else:
        print("O dealer manteve sua mão.")


    print("(", soma_das_cartas, ")")

    return cartas_aux

def casual(pontos):

    #ARMAZENAMENTO

    escolha = 1
    pontos_do_jogador = 0
    pontos_do_dealer = 0

    #FICA EM LOOP ATE ALGUEM ATINGIR UMA QUANTIDADE DE PONTOS DETERMINADA NAS CONFIG

    while pontos_do_jogador != pontos and pontos_do_dealer != pontos:

        #CHAMA A FUNÇÃO DO JOGO (FUNÇÃO RETORNA UM NÚMERO(1- VITORIA DO JOGADOR, 2- VITORIA DO DEALER, 3- EMPATE))

        ganhou = jogador_vs_dealer()

        #PEGA ESSE NUMERO E TESTA
        if ganhou == 1:
            pontos_do_jogador = pontos_do_jogador + 1
        elif ganhou == 2:
            pontos_do_dealer = pontos_do_dealer + 1
        elif ganhou == 3:
            pontos_do_dealer = pontos_do_dealer
            pontos_do_jogador = pontos_do_jogador

        #MOSTRA O PLACAR

        print("PLACAR: ")
        print("JOGADOR ", pontos_do_jogador, "x", pontos_do_dealer, "DEALER")

        #DIZ QUEM VENCEU (SE NÃO ACABOU AINDA NAO FAZ NADA)

        if pontos_do_jogador != pontos and pontos_do_dealer != pontos:
            print("DIGITE QUALQUER COISA PARA INICIAR A PRÓXIMA RODADA")
            esperar = input()

        #JOGADOR

        elif pontos_do_jogador == pontos:
            print()
            print("PARABÉNS!!!!"
                    "\nVOCÊ VENCEU A SÉRIE!!!")

        #DEALER

        elif pontos_do_dealer == pontos:
            print("O DEALER VENCEU A SÉRIE!!")

def cassino(fichas):

    #ARMAZENAMENTO

    valor_inicial = fichas
    escolha = 1

    limpar_tela()

    while fichas != 0 and escolha != 2:
        entra = 1
        if escolha == 1:

            #MOSTRA AS FICHAS

            print("SUAS FICHAS: ", fichas)
            print("DIGITE QUANTAS FICHAS VOCÊ QUER APOSTAR: ")
            aposta = int(input())
            limpar_tela()

            #CASO TENTE APOSTAR SEM SENTIDO

            if aposta > fichas:
                print("VOCÊ NÃO PODE APOSTAR MAIS FICHAS DO QUE TEM.")
                entra = 2
            elif aposta <= 0:
                print("APOSTE UM NÚMERO VÁLIDO.")
                entra = 2

            #EXECUTA A PARTIDA

            else:
                print("PARTIDA VALENDO",aposta,"FICHAS.")
                print()
                print()
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

            #OUTRA RODADA

        if fichas != 0 and entra == 1:
            print("1. FAZER OUTRA APOSTA")
            print("2. PARAR")
            escolha = input("ESCOLHA: ")
            limpar_tela()

            if escolha == "1":
                escolha = 1
            elif escolha == "2":
                escolha = 2
            else:
                print("POR FAVOR ESCOLHA 1 OU 2")
                print()
                escolha = 3

        elif fichas <= 0:
            print("INFELIZMENTE, VOCÊ NÃO TEM MAIS FICHAS.")
            escolha = 2


    #"PLACAR" FINAL

    if fichas == 0:
        print("VOLTE SEMPRE!")

    elif fichas > valor_inicial:
        diferenca = fichas - valor_inicial
        print("VOCÊ TERMINOU GANHANDO",diferenca,"FICHAS.")
        print("TOTAL DE FICHAS: ",fichas)


    elif fichas < valor_inicial:
        diferenca = valor_inicial - fichas
        print("VOCÊ TERMINOU PERDENDO",diferenca,"FICHAS.")
        print("TOTAL DE FICHAS: ",fichas)


    elif fichas == valor_inicial:
        print("VOCÊ TERMINOU COM A MESMA QUANTIDADE DE FICHAS")


def jogar_novamente(escolha_configuracoes,pontos,fichas):
    escolha = 3
    while escolha != 1 or escolha != 2:
        print()
        print("1. JOGAR NOVAMENTE")
        print("2. MENU PRINCIPAL")
        escolha = input()
        print()
        if escolha == "1":
            return 1
        elif escolha == "2":
            menu_principal(escolha_configuracoes,pontos,fichas)
        else:
            print("POR FAVOR, DIGITE 1 OU 2.")
            escolha = 3

def carta():
    cartas = []
    numerais = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
    naipes = ["♥", "♦", "♣", "♠"]

    carta = random.choice(numerais)
    naipe = random.choice(naipes)

    cartas.append(carta)
    cartas.append(naipe)

    return cartas

def blackjack(carta1, carta2):
    if (carta1 == "A" and (carta2 == "K" or carta2 == "Q" or carta2 == "J")) or (carta1 == "A" and (carta2 == "K" or carta2 == "Q" or carta2 == "J")):
        return True
    return False

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
                sleep(0.5)
                entra = entra - 2

def limpar_tela():
    for i in range(1, 100):
        print()

def regras(escolha_configuracoes, pontos, fichas):
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
    menu_principal(escolha_configuracoes, pontos, fichas)

#padrão ("1",2,100)
menu_principal("1",2,100)