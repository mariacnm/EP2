def  define_posicoes(linha,coluna,orientacao,tamanho):
    posicao=[0]*tamanho
    
    if orientacao== 'vertical':
        for i in range(len(posicao)):
            pos=[]
            pos.append(linha)
            pos.append(coluna)
            linha+=1
            posicao[i]=pos
        return posicao
    else:
        for i in range(len(posicao)):
            pos=[]
            pos.append(linha)
            pos.append(coluna)
            coluna+=1
            posicao[i]=pos
        return posicao


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    define=(define_posicoes(linha,coluna,orientacao,tamanho))
    if nome_navio not in frota:
        frota[nome_navio]=[define]
    else:
        frota[nome_navio].append(define)

    return frota


frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)