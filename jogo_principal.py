def define_posicoes(linha,coluna,orientacao,tamanho):
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
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] ==1:
        tabuleiro[linha][coluna] = 'X'
        return tabuleiro
    else:
        tabuleiro[linha][coluna] = '-'
        return tabuleiro
def posiciona_frota(frota):
    tabuleiro=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    for pos in frota.values():
        for l in pos:
            for listaazul in l:
                x=listaazul[0]
                y= listaazul[1]
                tabuleiro[x][y]=1
    return tabuleiro
def afundados(frota,tabuleiro):
    soma=0
    for posicoes in frota.values():
        for linha in posicoes:
            ajuda=0
            for numeros in linha:
                y=numeros[0]
                x=numeros[1]
                if tabuleiro[y][x] == "X":
                    ajuda+=1
            if ajuda == len(linha):
                soma+=1
    return soma
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




cont1=True
cont2 = True
input("Insira as informações referentes ao navio porta-aviões que possui tamanho 4")

while cont1:
    porta_aviões_linha = int (input('Linha:'))
    porta_aviões_coluna = int (input('Coluna:'))
    porta_aviões_orientação = int (input ('Orientação'))
    if porta_aviões_orientação == 1 :
        porta_aviões_orientação='vertical'
    if porta_aviões_orientação == 2:
        porta_aviões_orientação = 'horizontal'
    valida_pa=posicao_valida({},porta_aviões_linha,porta_aviões_coluna,porta_aviões_orientação,4)
    if valida_pa== True:
        cont1=False
    else:
        valida_pa== False
        print("Esta posição não está válida!")
define= (define_posicoes(porta_aviões_linha,porta_aviões_coluna,porta_aviões_orientação,4))
frota=(preenche_frota({},'porta-aviões',porta_aviões_linha,porta_aviões_coluna,porta_aviões_orientação,4))

i=1

while cont2:
    input("Insira as informações referentes ao navio navio-tanque que possui tamanho 3")
    navio_tanque_linha = int (input('Linha:'))
    navio_tanque_coluna = int (input('Coluna:'))
    navio_tanque_orientacao = int (input ('Orientação'))
    if navio_tanque_orientacao == 1 :
        navio_tanque_orientacao='vertical'
    if navio_tanque_orientacao == 2:
        navio_tanque_orientacao = 'horizontal'
    valida_pa=posicao_valida({},navio_tanque_linha,navio_tanque_coluna,navio_tanque_orientacao,3)
    if valida_pa== False:
        print("Esta posição não está válida!")
    if i>=2:
        cont2=False
    i+=1









 