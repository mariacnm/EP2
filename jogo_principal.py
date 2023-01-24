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
cont3=True
cont4=True
print("Insira as informações referentes ao navio porta-aviões que possui tamanho 4")

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
#define1= (define_posicoes(porta_aviões_linha,porta_aviões_coluna,porta_aviões_orientação,4))
frota1=(preenche_frota({},'porta-aviões',porta_aviões_linha,porta_aviões_coluna,porta_aviões_orientação,4))

soma1=0
i=1
while cont2:
    print("Insira as informações referentes ao navio navio-tanque que possui tamanho 3")
    navio_tanque_linha = int (input('Linha:'))
    navio_tanque_coluna = int (input('Coluna:'))
    navio_tanque_orientacao = int (input ('Orientação'))
    if navio_tanque_orientacao == 1 :
        navio_tanque_orientacao='vertical'
    if navio_tanque_orientacao == 2:
        navio_tanque_orientacao = 'horizontal'
    valida_pa=posicao_valida({},navio_tanque_linha,navio_tanque_coluna,navio_tanque_orientacao,3)
    if valida_pa== False:
        soma1+=1
        print("Esta posição não está válida!")
        if i>soma1:
            i-=1
    if i>=2:
        cont2=False
    i+=1
#define2= (define_posicoes(navio_tanque_linha,navio_tanque_coluna,navio_tanque_orientacao,3))
frota2=(preenche_frota(frota1,'navio-tanque',navio_tanque_linha,navio_tanque_coluna,navio_tanque_orientacao,3))

j=1
soma2=0
while cont3:
    print("Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2")
    navio_contratorpedeiro_linha = int (input('Linha:'))
    navio_contratorpedeiro_coluna = int (input('Coluna:'))
    navio_contratorpedeiro_orientacao = int (input ('Orientação'))
    if navio_contratorpedeiro_orientacao == 1 :
        navio_contratorpedeiro_orientacao='vertical'
    if navio_contratorpedeiro_orientacao == 2:
        navio_contratorpedeiro_orientacao = 'horizontal'
    valida_pa=posicao_valida({},navio_contratorpedeiro_linha,navio_contratorpedeiro_coluna,navio_contratorpedeiro_orientacao,2)
    if valida_pa== False:
        soma2+=1
        print("Esta posição não está válida!")
        if j>soma2:
            j-=1
    if j>=3:
        cont3=False
    j+=1
#define3= (define_posicoes(navio_contratorpedeiro_linha,navio_contratorpedeiro_coluna,navio_contratorpedeiro_orientacao,2))
frota3=(preenche_frota(frota2,'contratorpedeiro',navio_contratorpedeiro_linha,navio_contratorpedeiro_coluna,navio_contratorpedeiro_orientacao,2))
m=1
soma3=0
while cont4:
    print("Insira as informações referentes ao navio submarino que possui tamanho 1")
    submarino_linha = int (input('Linha:'))
    submarino_coluna = int (input('Coluna:'))
    valida_pa=posicao_valida({},submarino_linha,submarino_coluna,'horizontal',1)
    if valida_pa== False:
        soma3+=1
        print("Esta posição não está válida!")
        if i>soma3:
            i-=1
    if m>=4:
        cont4=False
    m+=1
#define4= (define_posicoes(navio_contratorpedeiro_linha,navio_contratorpedeiro_coluna,navio_contratorpedeiro_orientacao,2))
frota4=(preenche_frota(frota3,'contratorpedeiro',submarino_linha,submarino_coluna,'horizontal',1))
print(frota4)






 