import funcoes
import random
import perguntas
from perguntas import quest

base = funcoes.transforma_base(quest)
pulo = 3
ajuda = 2
facil = 0
premio = 0
lista = []
num = 0
questoes = 0
tentativa = 1
continuar_jogando = ''
# INTRO
print('Olá, você está na fortuna DesSoft e terá a oportunidade de enriquecer!')
nome = str(input('Qual o seu nome?: '))
print(f'Ok, {nome}, você tem o direito a pular 3 vezes e 2 ajudas!/nAs opções de respostas são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
enter = (input('Aperte ENTER para continuar...'))

if enter == '':
    print('O jogo já vai começar! Lá vem a primeira questão!/n/nVamos começar com questões do nível FÁCIL!')
enter = (input('Aperte ENTER para continuar...'))
if enter == '':
    print('')

# COMEÇANDO O JOGO

jogando = True
while jogando:
    # QUESTÕES FACEIS
    if questoes <= 3:
        num += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'facil')
        nova = funcoes.sorteia_questao_inedita(base, 'facil', lista)
        pergunta = funcoes.questao_para_texto(nova, num)
        print(pergunta)
    # QUESTÕES MÉDIAS
    if questoes > 3 and questoes <= 6:
        num += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'medio')
        nova = funcoes.sorteia_questao_inedita(base, 'medio', lista)
        pergunta = funcoes.questao_para_texto(nova, num)
        print(pergunta)
    # QUESTÕES DIFÍCIEIS
    if questoes > 6 and questoes <= 9:
        num += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'dificil')
        nova = funcoes.sorteia_questao_inedita(base, 'dificil', lista)
        pergunta = funcoes.questao_para_texto(nova, num)
        print(pergunta)
    # PERGUNTAS
    resposta = input('Qual a sua resposta: ')
    #PULO
    if resposta == 'pula' and pulo >= 1:
        pulo-=1
        print(f'Você tem {pulo} pulos.')
        print('')
        if resposta == 'pula' and pulo <= 0:
            print('Você não tem mais pulos. Responda a pergunta')
            resposta = input('Qual a sua resposta?: ')
            if resposta == 'pula':
                print('Que pena! Você errou e vai sair sem nada!')
                break
    # AJUDA
    if resposta == 'ajuda' and tentativa != 0:
        aleatoria = nova['opcoes']['A']
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
            print(f'Dica: n/ Opções certamente erradas: {aleatoria}')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        # QUANDO TEM DIREITO A DOIS PULOS
        if ajuda == 2:
            ajuda -= 1
            print('OK lá vem ajuda! Você tem direito a mais uma ajuda!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
            print(f'Dica: n/ Opções certamente erradas: {aleatoria}')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        ajuda -= 1
        print(pergunta)
        # AJUDA POR QUESTÃO
        if tentativa == 0:
            print('Você não tem direito a mais ajuda(s). Responda a pergunta:')
            resposta = (input('Qual é a sua resposta?'))
            if resposta == 'ajuda':
                print('Que pena! Você errou e vai sair sem nada')
                break



# CORRETO

    if resposta == nova['correta']:
        questoes += 1
        if questoes == 1:
            premio = 1000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 2:
            premio = 5000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 3:
            premio = 10000
            print('HEY! Você passou para o nível MEDIO!')
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 4:
            premio = 30000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 5:
            premio = 50000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 6:
            premio = 100000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
            print('HEY! Você passou para o nível DIFICIL!')
        elif questoes == 7:
            premio = 300000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 8:
            premio = 500000
            print(f'Você acertou! Seu prêmio atual é de R$ {premio}')
        elif questoes == 9:
            print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais! ')
            premio = 1000000
            print(f'Voce acertou!! Seu premio atual e de R$ {premio}')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')

# ERRADA
    if resposta != 'ajuda' and resposta != nova['correta'] and resposta != 'pula':
        print('Que pena! Voce errou e vai sair sem nada.')
        continuar_jogando = input('Quer jogar novamente?')
        if continuar_jogando == 'sim':
            jogando = True
        break
    
    facil += 1