import random
import funcoes


base = funcoes
pulo = 3
ajuda = 2
facil = 0
numero = 0
pontuacao = 0
lista_facil = []
questoes = 0
tentativa = 1

# INTRO
print('Olá, você está na fortuna DesSoft e terá a oportunidade de enriquecer!/n')
nome = str(input('Qual o seu nome?: '))
print(f'Ok, {nome}, você tem o direito a pular 3 vezes e 2 ajudas!/nAs opções de respostas são "A", "B", "C", "D", "ajuda", "pula" e "parar"!/n')
enter = (input('Aperte ENTER para continuar...'))

if enter == '':
    print('/nO jogo já vai começar! Lá vem a primeira questão!/n/nVamos começar com questões do nível FÁCIL!')
enter = (input('Aperte ENTER para continuar...'))
if enter == '':
    print('')

# COMEÇANDO O JOGO

jogando = True
while jogando:
    # QUESTÕES FACEIS
    if questoes <= 3:
        numero += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'facil')
        inedito = funcoes.sorteia_questao(base, 'facil', lista_facil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
    # QUESTÕES MÉDIAS
    if questoes > 3 and questoes <= 6:
        numero += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'medio')
        inedito = funcoes.sorteia_questao_inedita(base, 'medio', lista_facil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
    # QUESTÕES DIFÍCIEIS
    if questoes > 6 and questoes <= 9:
        numero += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'dificil')
        inedito = funcoes.sorteia_questao_inedita(base, 'dificil', lista_facil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
    # PERGUNTAS
    resposta = input('Qual a sua resposta: ')
    #PULO
    if resposta == 'pular' and pulo <= 1:
        pulo+=1
        print(f'Você tem {pulo} pulos.')
        print('')
        if resposta == 'pular' and pulo <= 0:
            print('Você não tem mais pulos. Responda a pergunta')
            resposta = input('Qual a sua resposta?: ')
            if resposta == 'pular':
                print('Que pena! Você errou e vai sair sem nada!')
                break
    # AJUDA
    if resposta == 'ajuda' and tentativa != 0:
        # VARIÁVEIS AJUDA
        aleatoria = inedito['opcoes']['A']
        ajudar = funcoes.gera_ajuda(questao_sorteada)
        tentativa -= 1
        # QUANDO NÃO TEM MAIS DIREITO A AJUDA
        if ajuda == 0:
            print('Não deu! Você não tem mais direito a ajuda!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        # QUANDO TEM DIREITO A UMA AJUDA
        if ajuda == 1:
            print('OK, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
            print(f'Dica:n/Opoções certamente erradas: {aleatoria}')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        # QUANDO TEM DIREITO A DOIS PULOS
        if ajuda == 2:
            print('OK la vem ajuda! Você tem direito a mais uma ajuda!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
            print(f'Dica:n/Opoções certamente erradas: {aleatoria}')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        print(pergunta)
        # USO DE UMA AJUDA POR QUESTÃO
        



