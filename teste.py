from dataclasses import dataclass
@dataclass
class PaisMedalhas:
    pais: str
    ouro: int
    prata: int
    bronze: int
    total: int




from dataclasses import dataclass
@dataclass
class PaisGenero:
    pais: str
    genero: str 





def organiza_quadro_medalhas(tabela: list[list[str]]):
    '''
    Recebe o conteúdo da *tabela* e imprime um quadro de medalha
    '''
    pais_medalha: list[str] = []
    lista_estruturada: list[PaisMedalhas] = []
    i = 1
    
    for linha in range(1, len(tabela)):
            pais_medalha.append(tabela[linha][0])
            pais_medalha.append(tabela[linha][10])

    while i <= len(pais_medalha):
        G = 0 ; S = 0 ; B = 0
        j = 0 ; b = 0
                
        for b in pais_medalha:

            if pais_medalha[i] == b:
                if pais_medalha[j -1] == 'Gold Medal':
                    G = G + 1 
                elif pais_medalha[j -1] == 'Silver Medal':
                    S = S + 1 
                elif pais_medalha[j -1] == 'Bronze Medal': 
                    B = B + 1 
            j = j + 1

        p = 0
        adiciona = True 

        for a in lista_estruturada:
            if a == PaisMedalhas(pais_medalha[i], G, S, B, G + S + B):
                adiciona = False
                
        if adiciona == True:
            lista_estruturada.append(PaisMedalhas(pais_medalha[i], G, S, B,G + S + B))
        i = i + 2
              
    organiza_em_ordem(lista_estruturada)





def indice_maximo(lst: list[PaisMedalhas]) -> int:
    assert len(lst) != 0
    imax = 0
    for i in range(1, len(lst)):
        if lst[i].ouro == lst[imax].ouro and lst[i].prata == lst[imax].prata:
            if lst[i].bronze < lst[imax].bronze:
                imax = i
                
        if lst[i].ouro == lst[imax].ouro:
            if lst[i].prata < lst[imax].prata:
                imax = i
                
        if lst[i].ouro < lst[imax].ouro:
            imax = i
            

            
    return imax



def organiza_em_ordem(lista: list[int]):
    
    j = len(lista)
    while j>1:
        imax = indice_maximo(lista[:j])
        aux = lista[imax]
        lista[imax] = lista[j -1]
        lista[j -1] = aux
        j = j -1
        
    imprime_quadro_medalhas(lista)
o meu celular n carrega, cacete, porra, merda, caralho, fdp, não tenho, porra, meu irmao sumiu com o meu carregador
formato diferente de entrada, n funciona no meu celular, já dei, tadinho, tá no hospital



            
def imprime_quadro_medalhas(lista):
    print('País    Ouro   Prata   Bronze   Total')
    for a in lista:
        total = str(int(a.ouro) + int(a.prata) + int(a.bronze))
        print(a.pais,6*' ',a.ouro,5*' ',a.prata,6*' ',a.bronze,5*' ',str(total))




      
def identifica_pais_1genero(tabela: list[list[str]]):
    pais_genero: list[str] = []
    pais_unico_genero: list[str] = []
    
    for linha in range(1, len(tabela)):
        pais_genero.append(PaisGenero(tabela[linha][10],tabela[linha][4]))
                                
    for a in pais_genero:
        adiciona = True
        
        for b in pais_genero:
            if a.pais == b.pais and a.genero != b.genero:
                adiciona = False

        for d in pais_unico_genero:
            if a.pais == d:
                adiciona == False
                
        if adiciona == True:
            pais_unico_genero.append(a.pais)
            
    print(pais_unico_genero)
        
                            
organiza_quadro_medalhas([['medal_type','medal_code','medal_date','name','gender','discipline','event','event_type','url_event','code','country_code','country','country_long'],
["Gold Medal","1","2024-07-27","Remco EVENEPOEL","M","Cycling Road","Men's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--","1903136","BEL","Belgium","Belgium"],
["Silver Medal","2","2024-07-27","Filippo GANNA","M","Cycling Road","Men's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--","1923520","ITA","Italy","Italy"],
["Bronze Medal","3","2024-07-27","Wout van AERT","M","Cycling Road","Men's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--","1903147","BEL","Belgium","Belgium"],
["Gold Medal","1","2024-07-27","Grace BROWN","W","Cycling Road","Women's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/women-s-individual-time-trial/fnl-000100--","1940173","AUS","Australia","Australia"],
["Silver Medal","2","2024-07-27","Anna HENDERSON","W","Cycling Road","Women's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/women-s-individual-time-trial/fnl-000100--","1912525","GBR","Great Britain","Great Britain"],
["Bronze Medal","3","2024-07-27","Chloe DYGERT","W","Cycling Road","Women's Individual Time Trial","ATH","/en/paris-2024/results/cycling-road/women-s-individual-time-trial/fnl-000100--","1955079","USA","United States","United States of America"],
["Gold Medal","1","2024-07-27","China","W","Diving","Women's Synchronised 3m Springboard","TEAM","/en/paris-2024/results/diving/women-s-synchronised-3m-springboard/fnl-000100--","DIVW3MTEAM2-CHN01","CHN","China","People's Republic of China"],
["Silver Medal","2","2024-07-27","United States","W","Diving","Women's Synchronised 3m Springboard","TEAM","/en/paris-2024/results/diving/women-s-synchronised-3m-springboard/fnl-000100--","DIVW3MTEAM2-USA01","USA","United States","United States of America"],
["Bronze Medal","3","2024-07-27","Great Britain","W","Diving","Women's Synchronised 3m Springboard","TEAM","/en/paris-2024/results/diving/women-s-synchronised-3m-springboard/fnl-000100--","DIVW3MTEAM2-GBR01","GBR","Great Britain","Great Britain"],
["Gold Medal","1","2024-07-27","OH Sanguk","M","Fencing","Men's Sabre Individual","HATH","/en/paris-2024/results/fencing/men-s-sabre-individual/fnl-000100--","1927149","KOR","Korea","Republic of Korea"],
["Silver Medal","2","2024-07-27","Fares FERJANI","M","Fencing","Men's Sabre Individual","HATH","/en/paris-2024/results/fencing/men-s-sabre-individual/fnl-000100--","1937783","TUN","Tunisia","Tunisia"],
["Bronze Medal","3","2024-07-27","Luigi SAMELE","M","Fencing","Men's Sabre Individual","HATH","/en/paris-2024/results/fencing/men-s-sabre-individual/fnl-000200--","1924595","ITA","Italy","Italy"],
["Gold Medal","1","2024-07-27","KONG Man Wai Vivian","W","Fencing","Women's Épée Individual","HATH","/en/paris-2024/results/fencing/women-s-epee-individual/fnl-000100--","1963262","HKG","Hong Kong, China","Hong Kong, China"],
["Silver Medal","2","2024-07-27","Auriane MALLO-BRETON","W","Fencing","Women's Épée Individual","HATH","/en/paris-2024/results/fencing/women-s-epee-individual/fnl-000100--","1916183","FRA","France","France"],
["Bronze Medal","3","2024-07-27","Eszter MUHARI","W","Fencing","Women's Épée Individual","HATH","/en/paris-2024/results/fencing/women-s-epee-individual/fnl-000200--","1946375","HUN","Hungary","Hungary"],
["Gold Medal","1","2024-07-27","Yeldos SMETOV","M","Judo","Men -60 kg","HATH","/en/paris-2024/results/judo/men--60-kg/fnl-000100--","1935408","KAZ","Kazakhstan","Kazakhstan"],
["Silver Medal","2","2024-07-27","Luka MKHEIDZE","M","Judo","Men -60 kg","HATH","/en/paris-2024/results/judo/men--60-kg/fnl-000100--","1891304","FRA","France","France"],
["Bronze Medal","3","2024-07-27","NAGAYAMA Ryuju","M","Judo","Men -60 kg","HATH","/en/paris-2024/results/judo/men--60-kg/repf000100--","1896752","JPN","Japan","Japan"],
["Bronze Medal","3","2024-07-27","Francisco GARRIGOS","M","Judo","Men -60 kg","HATH","/en/paris-2024/results/judo/men--60-kg/repf000200--","1563544","ESP","Spain","Spain"],
["Gold Medal","1","2024-07-27","TSUNODA Natsumi","W","Judo","Women -48 kg","HATH","/en/paris-2024/results/judo/women--48-kg/fnl-000100--","1896735","JPN","Japan","Japan"],
["Silver Medal","2","2024-07-27","Baasankhuu BAVUUDORJ","W","Judo","Women -48 kg","HATH","/en/paris-2024/results/judo/women--48-kg/fnl-000100--","1914467","MGL","Mongolia","Mongolia"],
["Bronze Medal","3","2024-07-27","Shirine BOUKLI","W","Judo","Women -48 kg","HATH","/en/paris-2024/results/judo/women--48-kg/repf000100--","1891280","FRA","France","France"],
["Bronze Medal","3","2024-07-27","Tara BABULFATH","W","Judo","Women -48 kg","HATH","/en/paris-2024/results/judo/women--48-kg/repf000200--","1571911","SWE","Sweden","Sweden"],
["Gold Medal","1","2024-07-27","France","M","Rugby Sevens","Men","HTEAM","/en/paris-2024/results/rugby-sevens/men/fnl-000100--","RU7MTEAM7---FRA01","FRA","France","France"],
["Silver Medal","2","2024-07-27","Fiji","M","Rugby Sevens","Men","HTEAM","/en/paris-2024/results/rugby-sevens/men/fnl-000100--","RU7MTEAM7---FIJ01","FIJ","Fiji","Fiji"],
["Bronze Medal","3","2024-07-27","South Africa","M","Rugby Sevens","Men","HTEAM","/en/paris-2024/results/rugby-sevens/men/fnl-000200--","RU7MTEAM7---RSA01","RSA","South Africa","South Africa"],
["Gold Medal","1","2024-07-27","China 1","X","Shooting","10m Air Rifle Mixed Team","HTEAM","/en/paris-2024/results/shooting/10m-air-rifle-mixed-team/fnl-000100--","SHOXARMT----CHN01","CHN","China","People's Republic of China"],
["Silver Medal","2","2024-07-27","Korea 1","X","Shooting","10m Air Rifle Mixed Team","HTEAM","/en/paris-2024/results/shooting/10m-air-rifle-mixed-team/fnl-000100--","SHOXARMT----KOR01","KOR","Koreaa","Republic of Korea"]])

