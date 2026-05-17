#======== 2º Trabalho de fundamentos de algoritimo =========
#== Automatização do processo de coleta de tíquetes do RU ==

#Nome --> Johnny Maia Fernandes   ra: 140363

#Primeira questão, linha 125
#Segunda questão, linha 426

from dataclasses import dataclass
@dataclass
class PaisMedalhaGenero:
    '''
    Armazena dados por país, medalha e gênero 
    '''
    pais: str
    medalha: str
    genero: str  

@dataclass
class PaisMedalhas:
    '''
    Armazena dados por país, quantidade de medalhas de ouro, prata e bronze
    '''
    pais: str
    ouro: int
    prata: int
    bronze: int
    total: int

@dataclass
class Espacamento:
    '''
    Armazena o espaçamento necessário, para o alinhamento da tabela 
    '''
    o : int
    p : int
    b : int
    t : int


import sys
sys. setrecursionlimit(2036)
def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])

    filtra_elementos(tabela)

    # TODO: computar e exibir o quadro de medalhas
    # FEITO
    computa_exibe_quadro_medalhas(tabela)

    # TODO: computar e exibir os países que tiverem apenas
    # atletas de um único gênero premiados
    # FEITO
    computa_exibe_paises_1genero(tabela)



def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.
    Por exemplo, se o conteúdo do arquivo for
    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995
    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)



#FILTRA ELEMENTOS E OS ARMAZENA EM UMA ESTRUTURA
def filtra_elementos(lista: list[list[str]]):
    '''
    Recebe a lista *tabela* e faz uma seleção de elementos necessários, cujos
    quais são: medalha, país e gênero. Se o gênero for 'O' ou 'X', ele armazena como None.
    Modificando desta maneira, *lista*.

    Exemplo

    >>> tabela = [['medal_type','medal_code','medal_date','name','gender','discipline','event','event_type','url_event','code','country_code','country','country_long'],
    ... ["Gold Medal","1","2024-07-27","Remco EVENEPOEL","M","Cycling Road","Men's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--","1903136","BEL","Belgium","Belgium"],
    ... ["Silver Medal","2","2024-07-27","Filippo GANNA","M","Cycling Road","Men's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--","1923520","ITA","Italy","Italy"]]
    >>> filtra_elementos(tabela)
    >>> tabela
    [PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='ITA', medalha='Silver Medal', genero='M')]

    >>> tabela = tabela = [['medal_type','medal_code','medal_date','name','gender','discipline','event','event_type','url_event','code','country_code','country','country_long'],
    ... ["Bronze Medal","1","2024-07-27","Remco EVENEPOEL","X","Cycling Road","Men's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--","1903136","BRA","Brazil","Brazil"]]
    >>> filtra_elementos(tabela)
    >>> tabela
    [PaisMedalhaGenero(pais='BRA', medalha='Bronze Medal', genero=None)]
    '''

    
    for linha in range(1, len(lista)):
        if lista[linha][4] == 'X' or lista[linha][4] == 'O':
            lista[linha][4] = None

        lista[linha -1] = PaisMedalhaGenero(lista[linha][10], lista[linha][0], lista[linha][4])
    lista.pop()



#QUADRO DE MEDALHAS 
def computa_exibe_quadro_medalhas(tabela: list[list[str]]):
    '''
    Recebe *tabela*, tipo list[list[str]], que possuí todas as informações dos ganhadores das 
    medalhas das olimpíadas. A função computa essa informação em 4 funções, 4 partes, e na última
    etapa ela imprime o quadro de medalhas

    Exemplos

    >>> computa_exibe_quadro_medalhas([PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='ITA', medalha='Silver Medal', genero='M'), 
    ... PaisMedalhaGenero(pais='BEL', medalha='Bronze Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W'), 
    ... PaisMedalhaGenero(pais='GBR', medalha='Silver Medal', genero='W')])
    País    Ouro   Prata   Bronze   Total
    BEL        1       0        1       2
    AUS        1       0        0       1
    GBR        0       1        0       1
    ITA        0       1        0       1

    >>> computa_exibe_quadro_medalhas([PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'), 
    ... PaisMedalhaGenero(pais='BRA', medalha='Bronze Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W')])
    País    Ouro   Prata   Bronze   Total
    BRA        1       0        1       2
    AUS        1       0        0       1

    >>> computa_exibe_quadro_medalhas([PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'), 
    ... PaisMedalhaGenero(pais='BRA', medalha='Bronze Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W'),
    ... PaisMedalhaGenero(pais='AUS', medalha='Silver Medal', genero='W')])
    País    Ouro   Prata   Bronze   Total
    AUS        1       1        0       2
    BRA        1       0        1       2

    >>> computa_exibe_quadro_medalhas([PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M'), 
    ... PaisMedalhaGenero(pais='BRA', medalha='Bronze Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W')])
    País    Ouro   Prata   Bronze   Total
    AUS        1       0        0       1
    BRA        0       1        1       2


    '''


    #Armazena os elementos desta lista em uma lista de tipo estruturado 
    primeira_parte = organiza_quadro_medalhas(tabela)

    #Organiza por ordem de classificação
    segunda_parte = organiza_por_classif(primeira_parte)

    #Imprime o quadro de medalhas
    imprime_quadro_medalhas(segunda_parte)



def organiza_quadro_medalhas(tabela: list[PaisMedalhaGenero]) -> list[PaisMedalhas]:
    '''
    Recebe o conteúdo *tabela*, soma a quantidade
    de medalhas de ouro, prata e bronze de um respectivo país, armazenando estes dados
    em uma lista de tipo estruturado e fazendo com que não repita dados na lista.
    Desta forma, retornando *lista_estruturada*, do tipo list[PaisMedalhas]

    Exemplos

    >>> organiza_quadro_medalhas([PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='ITA', medalha='Silver Medal', genero='M'), 
    ... PaisMedalhaGenero(pais='BEL', medalha='Bronze Medal', genero='M')])
    [PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='ITA', ouro=0, prata=1, bronze=0, total=1)]
   
    >>> organiza_quadro_medalhas([PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M')])
    [PaisMedalhas(pais='BRA', ouro=0, prata=1, bronze=0, total=1), PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=0, total=1)]

    >>> organiza_quadro_medalhas([PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M'),PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'),PaisMedalhaGenero(pais='BRA', medalha='Bronze Medal', genero='M')])
    [PaisMedalhas(pais='BRA', ouro=1, prata=1, bronze=1, total=3)]

    >>> organiza_quadro_medalhas([PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M'),PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M'),PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M')])
    [PaisMedalhas(pais='BRA', ouro=0, prata=3, bronze=0, total=3)]
    '''
  
    lista_estruturada: list[PaisMedalhas] = []

    for i in range(len(tabela)):
        G = 0 ; S = 0 ; B = 0    

        for b in range(len(tabela)):

            if tabela[i].pais == tabela[b].pais:      
                if tabela[b].medalha == 'Gold Medal':
                    G = G + 1 
                elif tabela[b].medalha == 'Silver Medal':
                    S = S + 1 
                elif tabela[b].medalha == 'Bronze Medal': 
                    B = B + 1
   
        estrutura = PaisMedalhas(tabela[i].pais, G, S, B, G + S + B)
        adiciona = se_adic_estrutura(lista_estruturada, estrutura)

        if adiciona == True:
            lista_estruturada.append(estrutura)  


    return lista_estruturada
        


def se_adic_estrutura(lista_estruturada: list[PaisMedalhas], estrutura: PaisMedalhas) -> bool:
    '''
    Recebe *lista_estruturada*, tipo list[PaisMedalhas], em que se está armazenado os dados
    dos países e das medalhas e recebe a estrutura do tipo PaisMedalhas. A função verifica se
    a estrutura já existe na lista_estruturada, retornando *adiciona*
    tipo PaisMedalhas

    Exemplos
    
    >>> se_adic_estrutura([PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2)], PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2))
    False

    >>> se_adic_estrutura([PaisMedalhas(pais='ITA', ouro=0, prata=1, bronze=1, total=2), PaisMedalhas(pais='HUN', ouro=0, prata=0, bronze=1, total=1)], 
    ... PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2))
    True

    >>> se_adic_estrutura([PaisMedalhas(pais='CHN', ouro=1, prata=0, bronze=0, total=1), PaisMedalhas(pais='KOR', ouro=1, prata=0, bronze=0, total=1), 
    ... PaisMedalhas(pais='TUN', ouro=0, prata=1, bronze=0, total=1), PaisMedalhas(pais='HGK', ouro=1, prata=0, bronze=0, total=1), 
    ... PaisMedalhas(pais='FRA', ouro=0, prata=1, bronze=0, total=1), PaisMedalhas(pais='HUN', ouro=0, prata=0, bronze=1, total=1)], 
    ... PaisMedalhas(pais='HGK', ouro=1, prata=0, bronze=1, total=2))
    False
    '''                                                 
    adiciona = True 
                            
    for p in lista_estruturada:
        if estrutura.pais == p.pais:
            adiciona = False
    return adiciona



def indice_menor_classif(lst: list[PaisMedalhas]) -> int:
    '''
    Recebe *lst*, tipo list[PaisMedalhas]. A função determina 
    qual o indice com menor classificação das olimpiadas, a classificação 
    é dada pelo maior número de medalhas de ouro, se houver empate, pelo maior
    número de medalhas de prata e se houver empate, pelo maior número de medalhas de bronze.
    Retornando, desta forma *imin*, tipo int.

    Exemplos

    >>> indice_menor_classif([PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='ITA', ouro=0, prata=1, bronze=1, total=2)])
    1

    >>> indice_menor_classif([PaisMedalhas(pais='ITA', ouro=0, prata=1, bronze=1, total=2),PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2)])
    0

    >>> indice_menor_classif([PaisMedalhas(pais='ITA', ouro=0, prata=1, bronze=1, total=2),PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), 
    ... PaisMedalhas(pais='BRA', ouro=0, prata=0, bronze=1, total=1)])
    2
    '''
    assert len(lst) != 0
    imin = 0
    for i in range(1, len(lst)):
        if lst[i].ouro == lst[imin].ouro and lst[i].prata == lst[imin].prata:
            
            if lst[i].bronze < lst[imin].bronze:
                imin = i
                
        if lst[i].ouro == lst[imin].ouro:
            if lst[i].prata < lst[imin].prata:
                imin = i
                
        if lst[i].ouro < lst[imin].ouro:
            imin = i          
    return imin



def organiza_por_classif(lista: list[PaisMedalhas]):
    '''
    Recebe *lista*, tipo list[PaisMedalhas], e à organiza em ordem decrescente, comparando
    a quantidade de ouro, de modo que, se empatar a quantidade de ouro, compara com
    a quantidade de prata, e se empatar também a quantidade de prata, compara com a quantidade
    de bronze. Retornando a própria *lista*, só que separada em ordem decrescente.
    
    Exemplos

    >>> organiza_por_classif([PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='BRA', ouro=1, prata=1, bronze=0, total=2)])
    [PaisMedalhas(pais='BRA', ouro=1, prata=1, bronze=0, total=2), PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2)]

    >>> organiza_por_classif([PaisMedalhas(pais='BEL', ouro=0, prata=0, bronze=1, total=1), PaisMedalhas(pais='BRA', ouro=0, prata=1, bronze=0, total=1)])
    [PaisMedalhas(pais='BRA', ouro=0, prata=1, bronze=0, total=1), PaisMedalhas(pais='BEL', ouro=0, prata=0, bronze=1, total=1)]

    >>> organiza_por_classif([PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='BRA', ouro=1, prata=1, bronze=0, total=2)])
    [PaisMedalhas(pais='BRA', ouro=1, prata=1, bronze=0, total=2), PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2)]

    >>> organiza_por_classif([PaisMedalhas(pais='BEL', ouro=0, prata=1, bronze=1, total=2), PaisMedalhas(pais='BRA', ouro=0, prata=1, bronze=0, total=1)])
    [PaisMedalhas(pais='BEL', ouro=0, prata=1, bronze=1, total=2), PaisMedalhas(pais='BRA', ouro=0, prata=1, bronze=0, total=1)]

    >>> organiza_por_classif([PaisMedalhas(pais='BEL', ouro=20, prata=10, bronze=1, total=31), PaisMedalhas(pais='BRA', ouro=19, prata=30, bronze=20, total=69)])
    [PaisMedalhas(pais='BEL', ouro=20, prata=10, bronze=1, total=31), PaisMedalhas(pais='BRA', ouro=19, prata=30, bronze=20, total=69)]
    '''
    j = len(lista)
    while j>1:
        imin = indice_menor_classif(lista[:j])
        aux = lista[imin]
        lista[imin] = lista[j -1]
        lista[j -1] = aux
        j = j -1

    return lista
   

      
def imprime_quadro_medalhas(lista: list[PaisMedalhas]):
    '''
    Efetua a impressão do quadro de medalhas, em que na primeira linha temos:
    país, ouro, prata, bronze e total, nas linhas respectivas temos: o país,
    a quantidade de medalhas de ouro, a quantidade de medalhas de prata, a quantidade
    de medalhas de bronze e a soma das medalhas. Tudo isso organizado em ordem crescente
    de classificação.

    Exemplos

    >>> imprime_quadro_medalhas([PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='AUS', ouro=1, prata=0, bronze=0, total=1), PaisMedalhas(pais='GBR', ouro=0, prata=1, bronze=0, total=1)])
    País    Ouro   Prata   Bronze   Total
    BEL        1       0        1       2
    AUS        1       0        0       1
    GBR        0       1        0       1

    >>> imprime_quadro_medalhas([PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='AUS', ouro=1, prata=0, bronze=0, total=1), 
    ... PaisMedalhas(pais='GBR', ouro=0, prata=1, bronze=0, total=1)])
    País    Ouro   Prata   Bronze   Total
    BEL        1       0        1       2
    AUS        1       0        0       1
    GBR        0       1        0       1

    >>> imprime_quadro_medalhas([PaisMedalhas(pais='BRA', ouro=1, prata=0, bronze=1, total=2), PaisMedalhas(pais='AUS', ouro=1, prata=0, bronze=0, total=1)])
    País    Ouro   Prata   Bronze   Total
    BRA        1       0        1       2
    AUS        1       0        0       1

    >>> imprime_quadro_medalhas([PaisMedalhas(pais='AUS', ouro=1, prata=1, bronze=0, total=2),PaisMedalhas(pais='BRA', ouro=1, prata=0, bronze=1, total=2)])
    País    Ouro   Prata   Bronze   Total
    AUS        1       1        0       2
    BRA        1       0        1       2

    >>> imprime_quadro_medalhas([PaisMedalhas(pais='AUS', ouro=1, prata=0, bronze=0, total=1), PaisMedalhas(pais='BRA', ouro=0, prata=1, bronze=1, total=2)])
    País    Ouro   Prata   Bronze   Total
    AUS        1       0        0       1
    BRA        0       1        1       2
    '''  
    print('País    Ouro   Prata   Bronze   Total')
    for a in lista:
        x = espacamento(a)
        print(a.pais, x.o*' ', a.ouro, x.p*' ', a.prata, x.b*' ', a.bronze, x.t*' ', a.total)



def espacamento(a: PaisMedalhas)-> Espacamento:
    '''
    Recebe *a*, tipo PaisMedalhaGenero. A função calcula o espaçamento 
    necessário para que a tabela fique alinhada, retornando desta forma 
    uma estrutura com o espaçamento entre os números de quantidade de medalha

    Exemplos

    >>> espacamento(PaisMedalhas(pais='BEL', ouro=1, prata=0, bronze=1, total=2))
    Espacamento(o=6, p=5, b=6, t=5)

    >>> espacamento(PaisMedalhas(pais='BEL', ouro=10, prata=0, bronze=1, total=11))
    Espacamento(o=5, p=5, b=6, t=4)

    >>> espacamento(PaisMedalhas(pais='BEL', ouro=10, prata=10, bronze=1, total=21))
    Espacamento(o=5, p=4, b=6, t=4)

    >>> espacamento(PaisMedalhas(pais='BEL', ouro=10, prata=10, bronze=10, total=30))
    Espacamento(o=5, p=4, b=5, t=4)

    >>> espacamento(PaisMedalhas(pais='BEL', ouro=10, prata=60, bronze=40, total=110))
    Espacamento(o=5, p=4, b=5, t=3)
    '''
    if len(str(a.ouro)) == 1:
        o = 6
    else:
        o = 5

    if len(str(a.prata)) == 1:
        p = 5
    else:
        p = 4

    if len(str(a.bronze)) == 1:
        b = 6
    else:
        b = 5

    if len(str(a.total)) == 1:
        t = 5
    elif len(str(a.total)) == 2:
        t = 4
    else: 
        t = 3 
    
    return Espacamento(o, p, b, t)



#PAÍSES EM QUE TODOS OS MEDALHISTAS SÃO DO MESMO GÊNERO
def computa_exibe_paises_1genero(tabela: list[PaisMedalhaGenero]):
    '''
    Recebe *tabela*, tipo lista. Identifica os países que possuem apenas 
    medalhistas de apenas um gênero.

    Exemplos

    >>> computa_exibe_paises_1genero([PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='ITA', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Bronze Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W'), PaisMedalhaGenero(pais='GBR', medalha='Silver Medal', genero='W')])
    Países em que apenas atletas de um só gênero ganharam medalhas:
    ['BEL', 'ITA', 'AUS', 'GBR']

    >>> computa_exibe_paises_1genero([PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='W')])
    Países em que apenas atletas de um só gênero ganharam medalhas:
    Nenhum país
    '''
    lst_1gen: list[str] = []
    i = 0
    paises_1genero(tabela, lst_1gen, i)
    imprime_paises_1genero(lst_1gen)



def paises_1genero(tabela: list[PaisMedalhaGenero], lst_1gen: list[str], i: int) -> None:
    '''
    Recebe as listas *tabela*, tipo PaisMedalhaGenero, *lst_1gen*, tipo string, eu valor *i*, tipo inteiro.
    A função adiciona os países, cujo quais seus medalhistas são todos do mesmo gênero, à lista lst_1gen, modificando a lista desta maneira.

    Exemplos

    >>> lst_1gen = []
    >>> paises_1genero([PaisMedalhaGenero(pais='ITA', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W'), PaisMedalhaGenero(pais='GBR', medalha='Silver Medal', genero='W')], lst_1gen, 0)
    >>> lst_1gen
    ['ITA', 'AUS', 'GBR']

    >>> lst_1gen = []
    >>> paises_1genero([PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='W'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='W')], lst_1gen,  0)
    >>> lst_1gen
    []

    >>> lst_1gen = []
    >>> paises_1genero([PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='BEL', medalha='Silver Medal', genero='W')], lst_1gen,  0)
    >>> lst_1gen
    []
    '''
    j = 0 
    adiciona1 = nao_existe(lst_1gen, tabela[i], j)

    if adiciona1:
        adiciona2 = se_adiciona(tabela, tabela[i], j)

    if adiciona1 and adiciona2:
        lst_1gen.append(tabela[i].pais)

    i = i + 1 
    if i < len(tabela):
        paises_1genero(tabela, lst_1gen, i)



def nao_existe(lst_1gen: list[str], medalhista: PaisMedalhaGenero, j: int) -> bool:
    '''
    Recebe *medalhista*, tipo PaisMedalhaGenero e recebe uma lista *lst_1gen*, tipo string e *j*, tipo inteiro. A função verifica se o
    o país de *medalhista* já está incluido na lista *lst_1gen*, caso esteja incluido, é retornado *adiciona1* como 
    True, caso contrário, como False

    Exemplos

    >>> nao_existe(['BEL', 'ITA', 'AUS', 'GBR'], PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), 0)
    False

    >>> nao_existe(['ITA', 'AUS', 'GBR'], PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), 0)
    True

    >>> nao_existe([], PaisMedalhaGenero(pais='BEL', medalha='Gold Medal', genero='M'), 0)
    True
    '''
    adiciona1 = True
    
    if lst_1gen == []:
        adiciona1 = True

    elif medalhista.pais == lst_1gen[j]:
        adiciona1 = False

    j = j + 1

    if adiciona1 and j < len(lst_1gen):
        adiciona1 = adiciona1 and nao_existe(lst_1gen, medalhista, j)  

    return adiciona1



def se_adiciona(tabela: list[PaisMedalhaGenero], medalhista: PaisMedalhaGenero, j: int) -> bool:  
    '''
    Recebe a lista *tabela*, tipo PaisMedalhaGenero, recebe *medalhista*, tipo PaisMedalhaGenero e recebe
    j, tipo inteiro. A função compara *medalhista* com cada elemento de *tabela*, caso a classe pais de 
    medalhista e de um elemento de tabela forem iguais e caso a classe genero de ambos forem diferentes, logo
    adiciona será igual a False, caso contrário será True. Portanto a função retorna *adiciona* tipo bool.

    Exemplos

    >>> se_adiciona([PaisMedalhaGenero(pais='BEL', medalha='Bronze Medal', genero='M'), PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W')], PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W'), 0)
    True
    >>> se_adiciona([PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='W'), PaisMedalhaGenero(pais='GBR', medalha='Silver Medal', genero='W')], PaisMedalhaGenero(pais='AUS', medalha='Gold Medal', genero='M'), 0)
    False
    >>> se_adiciona([PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='W'), PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='W')], PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'), 0)
    False
    >>> se_adiciona([PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'), PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero='M')], PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'), 0)
    True
    >>> se_adiciona([PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero=None), PaisMedalhaGenero(pais='BRA', medalha='Silver Medal', genero=None)], PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero='M'), 0)
    True
    >>> se_adiciona([PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero=None)], PaisMedalhaGenero(pais='BRA', medalha='Gold Medal', genero=None), 0)
    False
    '''
    adiciona = True

    if medalhista.genero == None:
        adiciona = False 
    
    elif adiciona:
        if tabela[j].genero == None:
            adiciona = True

        elif tabela[j].pais == medalhista.pais and tabela[j].genero != medalhista.genero:
            adiciona = False

        j = j + 1 
        if j <= len(tabela) -1: 
            adiciona = adiciona and se_adiciona(tabela, medalhista, j)

    return adiciona



def imprime_paises_1genero(lst_1gen: list[str]):
    '''
    Recebe *lst_1gen*, tipo list[str].
    A função imprime quais países tiveram apenas medalhistas de um único gênero

    Exemplos

    >>> imprime_paises_1genero(['BEL', 'ITA', 'AUS', 'GBR'])
    Países em que apenas atletas de um só gênero ganharam medalhas:
    ['BEL', 'ITA', 'AUS', 'GBR']

    >>> imprime_paises_1genero([])
    Países em que apenas atletas de um só gênero ganharam medalhas:
    Nenhum país
    '''

    print('Países em que apenas atletas de um só gênero ganharam medalhas:')

    if lst_1gen == []:
        print('Nenhum país')
    else:    
        print(lst_1gen)

if __name__ == '__main__':
    main()