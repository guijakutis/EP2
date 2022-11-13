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