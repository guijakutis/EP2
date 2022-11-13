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

