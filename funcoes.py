def transforma_base(lista_questoes):
    dic = {}
    i = 0
    if lista_questoes == []:
        return {}
    for i in range(0, len(lista_questoes)):
        questao = lista_questoes[i]
        if questao['nivel'] not in dic.keys():
            dic[questao['nivel']] = []
        dic[questao['nivel']].append(questao)
    i += 1

    return dic

def valida_questao(questao):
    problemas = {}

# regra 1    
    
    if not 'titulo' in questao:
        problemas['titulo'] = "nao_encontrado"
    if not 'nivel' in questao:
        problemas['nivel'] = "nao_encontrado"
    if not 'opcoes' in questao:
        problemas['opcoes'] = "nao_encontrado"
    if not 'correta' in questao:
        problemas['correta'] = "nao_encontrado"

# regra 2
    
    soma = 0
    for chave in questao:
        soma+=1
    if soma < 4 or soma > 4:
        problemas['outro'] = 'numero_chaves_invalido'

# regra 3
    
    if 'titulo' in questao:
        if len(questao['titulo'].strip()) == 0:
            problemas['titulo'] = 'vazio'
    
    if 'nivel' in questao:
        if questao['nivel'] == 0:
            problemas['nivel'] = 'valor_errado'
    if 'nivel' in questao.keys() and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        problemas['nivel'] = 'valor_errado'
    if 'opcoes' in questao:
        s = 0
        for chave in questao['opcoes']:
            s+=1
        if s < 4 or s > 4:
            problemas['opcoes'] = 'tamanho_invalido'
    if 'opcoes' in questao and s == 4:
        lista = []
        for valor in questao['opcoes']:
            lista_correta = ['A','B','C','D']
            if valor == 'A' or valor == 'B' or valor == 'C' or valor == 'D':
                lista.append(valor)
        if lista == lista_correta:
            if 'opcoes' not in problemas.keys():
                opcoes = {}
            for resposta in questao['opcoes']:
                if len(questao['opcoes'][resposta].strip()) == 0:
                    opcoes[resposta] = 'vazia'
                if len(opcoes) > 0:
                    problemas['opcoes'] = opcoes
    if 'correta' in questao.keys():
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            problemas['correta'] = 'valor_errado'

            
    return problemas


def valida_questoes(lista_questoes):
    lista_problemas = []
    for questao in lista_questoes:
        problemas = {}
        if not 'titulo' in questao:
            problemas['titulo'] = "nao_encontrado"
        if not 'nivel' in questao:
            problemas['nivel'] = "nao_encontrado"
        if not 'opcoes' in questao:
            problemas['opcoes'] = "nao_encontrado"
        if not 'correta' in questao:
            problemas['correta'] = "nao_encontrado"

# regra 2
    
        soma = 0
        for chave in questao:
            soma+=1
        if soma < 4 or soma > 4:
            problemas['outro'] = 'numero_chaves_invalido'

# regra 3
    
        if 'titulo' in questao:
            if len(questao['titulo'].strip()) == 0:
                problemas['titulo'] = 'vazio'
    
        if 'nivel' in questao:
            if questao['nivel'] == 0:
                problemas['nivel'] = 'valor_errado'
        if 'nivel' in questao.keys() and questao['nivel'] not in ['facil', 'medio', 'dificil']:
            problemas['nivel'] = 'valor_errado'
        if 'opcoes' in questao:
            s = 0
            for chave in questao['opcoes']:
                s+=1
            if s < 4 or s > 4:
                problemas['opcoes'] = 'tamanho_invalido'
        if 'opcoes' in questao and s == 4:
            lista = []
            for valor in questao['opcoes']:
                lista_correta = ['A','B','C','D']
                if valor == 'A' or valor == 'B' or valor == 'C' or valor == 'D':
                    lista.append(valor)
            if lista == lista_correta:
                if 'opcoes' not in problemas.keys():
                    opcoes = {}
                for resposta in questao['opcoes']:
                    if len(questao['opcoes'][resposta].strip()) == 0:
                        opcoes[resposta] = 'vazia'
                    if len(opcoes) > 0:
                        problemas['opcoes'] = opcoes
        if 'correta' in questao.keys():
            if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
                problemas['correta'] = 'valor_errado'

        lista_problemas.append(problemas)
    
    return lista_problemas
 

import random

def sorteia_questao(questoes, nivel):
    sorteia = random.choice(questoes[nivel])
    return sorteia


import random

def sorteia_questao(questoes, nivel):
    sorteia = random.choice(questoes[nivel])
    return sorteia

def sorteia_questao_inedita(dic, nivel, lista):

    while True:
        questao = sorteia_questao(dic, nivel)
        if questao not in lista:
            lista.append(questao)
            return questao

def questao_para_texto(questao, num):
    divisoria = '----------------------------------------'
    NUMERO = (f'QUESTAO {num}')
    TITULO = questao['titulo']
    TEXTO = divisoria + '\n' + NUMERO + '\n\n' + TITULO + '\n\n' + 'RESPOSTAS:' + '\n'
    for alternativa, resposta in questao['opcoes'].items():
        TEXTO += f'{alternativa}: {resposta}' + '\n' 
    return TEXTO
    

import random

def gera_ajuda(questao):
  d = '''DICA:
Opções certamente erradas: '''
  l = []
  for k, valor in questao['opcoes'].items():
    if k != questao['correta']:
      l.append(valor)
  numero = random.randint(1, 2)
  sorteio = random.sample(l, k=numero)
  d += ' | '.join(sorteio)
  return d



