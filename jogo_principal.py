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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto



vdd=True
jogando=True
inedita=[]
frota={}
conta=4
tamanho=4
frota_oponente = {
            'porta-aviões': [
                [[9, 1], [9, 2], [9, 3], [9, 4]]
            ],
            'navio-tanque': [
                [[6, 0], [6, 1], [6, 2]],
                [[4, 3], [5, 3], [6, 3]]
            ],
            'contratorpedeiro': [
                [[1, 6], [1, 7]],
                [[0, 5], [1, 5]],
                [[3, 6], [3, 7]]
            ],
            'submarino': [
                [[2, 7]],
                [[0, 6]],
                [[9, 7]],
                [[7, 6]]
            ]
        }
tabuleiro_oponente= posiciona_frota(frota_oponente)
repeticao=True
afundado=0
navio="porta-aviões"
while jogando:
    while vdd:
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
        continuar=True
        continuar2=True
        while continuar:
            linha=int (input('Linha:'))

            if linha >=0 and linha <=9:
                continuar=False
            else:
                print('Linha inválida!')

        while continuar2:
            coluna=int (input('Coluna:'))
            if coluna >=0 and coluna <=9:
                continuar2=False
            else:
                print('Coluna inválida!')
        
        if navio != "submarino":
            orientacao=int(input ('[1] Vertical [2] Horizontal >'))
        if orientacao==1:
            orientacao="vertical"
        elif orientacao==2:
            orientacao= "horizontal"
        
        

        valida=posicao_valida(frota, linha, coluna, orientacao, tamanho)
        if valida == True:
            if conta==4:
                prenchefrota= preenche_frota(frota, "porta-aviões", linha, coluna, orientacao, tamanho)
                conta+=3
                navio="navio-tanque"
                tamanho=3
                
            elif conta == 7:
                navio="navio-tanque"
                prenchefrota= preenche_frota(frota, "navio-tanque", linha, coluna, orientacao, tamanho)
                tamanho=3
                conta+=3
            elif conta==10:
                navio="contratorpedeiro"
                prenchefrota= preenche_frota(frota, "navio-tanque", linha, coluna, orientacao, tamanho)
                tamanho=2
                conta+=2
            elif conta== 12:
                navio="contratorpedeiro"
                prenchefrota= preenche_frota(frota, "contratorpedeiro", linha, coluna, orientacao, tamanho)
                tamanho=2
                conta+=2
            elif conta== 14:
                navio="contratorpedeiro"
                prenchefrota= preenche_frota(frota, "contratorpedeiro", linha, coluna, orientacao, tamanho)
                tamanho=2
                conta+=2
            elif conta==16:
                navio="submarino"
                prenchefrota= preenche_frota(frota, "contratorpedeiro", linha, coluna, orientacao, tamanho)
                tamanho=1
                conta+=1
            elif conta==17 or conta == 18 or conta == 19 or conta==20:
                navio="submarino"
                prenchefrota= preenche_frota(frota, "submarino", linha, coluna, 'horizontal', tamanho)
                tamanho=1
                conta+=1
            
            
        else:
            print("Esta posição não está válida!")

        tabuleiro_jogador= posiciona_frota(frota)
        
        if conta> 20:
            vdd= False
    

    while repeticao:
        linhaj= int(input("linha jogada"))
        colunaj= int(input("coluna jogada"))
        if [linhaj,colunaj] not in inedita:
            inedita.append([linhaj,colunaj])
        else:
            print ("A posição linha LINHA e coluna COLUNA já foi informada anteriormente")
        
        monta_tabu= monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente)
        print(monta_tabu)
        fazjogada= faz_jogada(tabuleiro_oponente,linhaj,colunaj)
        afundado+= afundados(frota,tabuleiro_oponente)
    
        if afundado == 10:
            repeticao=False
    jogando = False
print('Parabéns! Você derrubou todos os navios do seu oponente!')
