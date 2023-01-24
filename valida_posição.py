def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    define=define_posicoes(linha,coluna,orientacao,tamanho)
    
    for listinha in define:
        if listinha[0]>9 or listinha[1]>9:
            return False


    for posicoes in frota.values():
        for linha in posicoes:
            for par in linha:
                for par2 in define:
                    if par[0] == par2[0] and par[1] == par2[1]:
                        return False
    return True