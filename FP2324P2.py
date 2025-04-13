#Construtor
def cria_intersecao(col,lin):
    #cria_intersecao: str × int → intersecao
    '''
    Recebe um caractere e um número inteiro que representam a coluna (col) e a linha (lin) e retorna a interseção correspondente
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(col)!=str or type(lin)!=int or col not in alfabeto or 1>=lin>=19:
        raise ValueError("cria_intersecao: argumentos invalidos")
    return (col,lin)

#Seletores
def obtem_col(i):
    #obtem_col: intersecao → str
    '''
    Retorna a coluna "col" da interseção "i"
    '''
    return i[0]
def obtem_lin(i):
    #obtem_lin: intersecao → int
    '''
    Retorna a linha "lin" da interseção "i"
    '''
    return i[1]

#Reconhecedor
def eh_intersecao(arg):
    #eh_intersecao: universal → booleano
    '''
    Retorna True se o argumento for um TAD interseção e False em caso contrário
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(arg)==tuple and len(arg)==2 and arg[0] in alfabeto and type(arg[1])==int and 0<arg[1]<20:
        return True
    return False

#Teste
def intersecoes_iguais(i1,i2):
    #intersecoes_iguais: universal × universal → booleano
    '''
    Retorna True somente se i1 e i2 são interseções idênticas e False em caso contrário
    '''
    return eh_intersecao(i1) and eh_intersecao(i2) and i2==i1

#Trasnformador
def intersecao_para_str(i):
    #intersecao_para_str : intersecao → str
    '''
    Retorna a string que representa o argumento, conforme exemplificado
    '''
    return str(i[0])+str(i[1])
def str_para_intersecao(s):
    #str_para_intersecao: str → intersecao
    '''
    Retorna a interseção representada pelo seu argumento
    '''
    digitos='1234567890'
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    arg_digitos=0
    arg_car=''
    for i in s:
        if i in digitos:
            arg_digitos=arg_digitos*10 + int(i)
        if i in alfabeto:
            arg_car+=i
    return (arg_car,arg_digitos)
def obtem_intersecoes_adjacentes(i,l):
    #obtem_intersecoes_adjacentes: intersecao × intersecao → tuplo
    '''
    Retorna um tuplo contendo as interseções adjacentes à interseção 'i', seguindo a ordem de leitura em que 'l' corresponde à interseção superior direita do tabuleiro de Go
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    termo=0
    while i[0]!=alfabeto[termo]: 
        termo+=1
    num_adjacentes=[]
    if 0<=termo-1:
        num_adjacentes.append((alfabeto[termo-1],i[1]))
    if i[1]+1<=l[1]:
        num_adjacentes.append((alfabeto[termo],i[1]+1))
    if termo+1<l[1]:
        num_adjacentes.append((alfabeto[termo+1],i[1]))
    if 0<i[1]-1:
        num_adjacentes.append((alfabeto[termo],i[1]-1)) 
    return tuple(sorted(num_adjacentes,key=lambda num: num[1]))
def ordena_intersecoes(t):
    #ordena_intersecoes: tuplo → tuplo
    '''
    Retorna um tuplo de interseções com as mesmas interseções de 't', ordenadas de acordo com a ordem de leitura do tabuleiro de Go
    '''
    ordena_letras=sorted(t)
    return (tuple(sorted(ordena_letras,key=lambda num: num[1])))

##TAD pedra
#Construtor
def cria_pedra_branca():
    #cria_pedra_branca: {} → pedra
    '''
    Retorna uma pedra pertencente ao jogador branco
    '''
    return 1
def cria_pedra_preta():
    #cria_pedra_preta: {} → pedra
    '''
    Retorna uma pedra pertencente ao jogador preto
    '''
    return 2
def cria_pedra_neutra():
    #cria_pedra_neutra: {} → pedra
    '''
    Retorna uma pedra neutra
    '''
    return 0

#Reconhecedor
def eh_pedra(arg):
    #eh_pedra: universal → booleano
    '''
    Retorna True se o argumento for um TAD pedra e False caso contrário
    '''
    return arg==2 or arg==1 or arg==0
def eh_pedra_branca(p):
    #eh_pedra_branca: pedra → booleano
    '''
    Retorna True se a pedra 'p' pertencer ao jogador branco e False caso contrário
    '''
    return p==1
def eh_pedra_preta(p):
    #eh_pedra_preta: pedra → booleano
    '''
    Retorna True se a pedra 'p' pertencer ao jogador preto e False caso contrário
    '''
    return p==2

#Teste
def pedras_iguais(p1,p2):
    #pedras_iguais: universal × universal → booleano
    '''
    Retorna True somente se 'p1' e 'p2' forem pedras e forem iguais
    '''
    return p1==p2

#Transformador
def pedra_para_str(p):
    #pedra_para_str : pedra → str
    '''
    Devolve a cadeia de caracteres que representa o jogador dono da pedra, ou seja, 'O' para pedras do jogador branco, 'X' para pedras do jogador preto, ou '.' para pedras neutras
    '''
    if p==0:
        return '.'
    if p==1:
        return 'O'
    if p==2:
        return 'X'

def eh_pedra_jogador(p):
    #eh_pedra_jogador : pedra → booleano
    '''
    Retorna True se a pedra 'p' pertencer a um jogador (seja jogador branco ou jogador preto) e False caso contrário
    '''
    return p==2 or p==1

##TAD goban
#Construtor
def cria_goban_vazio(n):
    #cria_goban_vazio: int → goban
    '''
    O construtor cria um tabuleiro de Go de tamanho nxn sem interseções ocupadas. Ele verifica a validade do argumento n e gera um ValueError se o argumento n não for válido
    '''
    if n in (9,13,19):
        return list(list(0 for _ in range(n))for _ in range(n))
    raise ValueError('cria_goban_vazio: argumento invalido')
def cria_goban(n,ib,ip):
    #cria_goban: int × tuplo × tuplo → goban
    '''
    O construtor cria um tabuleiro de Go de tamanho n × n com as interseções especificadas pelos tuplos ib (ocupadas por pedras brancas) e ip (ocupadas por pedras pretas). Ele verifica a validade dos argumentos e gera um ValueError caso os argumentos não sejam válidos
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(n)!=int or type(ip)!=tuple or type(ib)!=tuple or not n in (9,13,19) or len(set(ib))!=len(ib) or len(set(ip))!=len(ip):
        raise ValueError('cria_goban: argumentos invalidos')
    goban=cria_goban_vazio(n)
    for w in ib:
        if type(w)==tuple:
            if w in ip or not eh_intersecao(w):
                raise ValueError('cria_goban: argumentos invalidos')
            termo=0
            while w[0]!=alfabeto[termo]:
                termo+=1
            goban[termo][w[1]-1]=1
        else:
            termo=0
            while ib[0]!=alfabeto[termo]:
                termo+=1
            goban[termo][ib[1]-1]=1
    for w in ip:
        if type(w)==tuple:
            if not eh_intersecao(w):
                raise ValueError('cria_goban: argumentos invalidos')
            termo=0
            while w[0]!=alfabeto[termo]:
                termo+=1
            goban[termo][w[1]-1]=2
        else:
            termo=0
            while ip[0]!=alfabeto[termo]:
                termo+=1
            goban[termo][ip[1]-1]=2
    return goban
def cria_copia_goban(t):
    #cria_copia_goban: goban → goban
    '''
    Cria a cópia de um goban
    '''
    if type(t)==list:
        copia=[]
        for elementos in t:
            copia.append(cria_copia_goban(elementos))
        return copia
    return t
#Seletores
def obtem_ultima_intersecao(g):
    #obtem_ultima_intersecao: goban → intersecao
    '''
    Devolve a interseção que corresponde ao canto superior direito do goban g
    '''
    if len(g)==9:
        return ('I',9)
    if len(g)==13:
        return ('M',13)
    if len(g)==19:
        return ('S',19)
def obtem_pedra(g,i):
    #obtem_pedra: goban × intersecao → pedra
    '''
    Devolve a pedra na interseção i do goban g mas se a interseção não estiver ocupada, devolve uma pedra neutra
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    termo=0
    while i[0]!=alfabeto[termo]: 
        termo+=1
    return g[termo][i[1]-1]
def obtem_cadeia(g,i):
    #obtem_cadeia: goban × intersecao → tuplo
    '''
    Devolve o tuplo formado pelas interseções (em ordem de leitura) das pedras da mesma cor que formam a cadeia que passa pela interseção i
    '''
    cadeia=[i]
    exemplo=[i]
    if obtem_pedra(g,i)==1:
        while exemplo:
            novo_exemplo=exemplo.pop()
            num_adjacentes = obtem_intersecoes_adjacentes(novo_exemplo,obtem_ultima_intersecao(g))
            for exemplo_adj in num_adjacentes:
                if obtem_pedra(g,exemplo_adj)==1 and (exemplo_adj not in cadeia):
                    cadeia.append(exemplo_adj)
                    exemplo.append(exemplo_adj)
            cadeia_final=ordena_intersecoes(sorted(tuple(cadeia)))
    if obtem_pedra(g,i)==2:
        while exemplo:
            novo_exemplo=exemplo.pop()
            num_adjacentes = obtem_intersecoes_adjacentes(novo_exemplo,obtem_ultima_intersecao(g))

            for exemplo_adj in num_adjacentes:
                if obtem_pedra(g,exemplo_adj)==2 and (exemplo_adj not in cadeia):
                    cadeia.append(exemplo_adj)
                    exemplo.append(exemplo_adj)
            cadeia_final=ordena_intersecoes(sorted(tuple(cadeia)))
    if obtem_pedra(g,i)==0:
        while exemplo:
            novo_exemplo=exemplo.pop()
            num_adjacentes = obtem_intersecoes_adjacentes(novo_exemplo,obtem_ultima_intersecao(g))

            for exemplo_adj in num_adjacentes:
                if obtem_pedra(g,exemplo_adj)==0 and (exemplo_adj not in cadeia):
                    cadeia.append(exemplo_adj)
                    exemplo.append(exemplo_adj)
            cadeia_final=ordena_intersecoes(sorted(tuple(cadeia)))
    return cadeia_final

#Modificadores
def coloca_pedra(g,i,p):
    #coloca_pedra: goban × intersecao × pedra → goban
    '''
    Modifica destrutivamente o goban g, colocando a pedra do jogador p na interseção i, e devolve o próprio goban
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    termo=0
    while i[0]!=alfabeto[termo]:
        termo+=1 
    if eh_pedra_branca(p):
        g[termo][i[1]-1]=1
    if eh_pedra_preta(p):
        g[termo][i[1]-1]=2
    return g
def remove_pedra(g,i):
    #remove_pedra: goban × intersecao → goban
    '''
    Modifica destrutivamente o goban g, removendo a pedra da interseção i, e devolve o próprio goban
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    termo=0
    while i[0]!=alfabeto[termo]:
        termo+=1
    g[termo][i[1]-1]=0
    return g
def remove_cadeia(g,t):
    #remove_cadeia: goban × tuplo → goban
    '''
    Modifica destrutivamente o goban g, removendo as pedras nas interseções do tuplo t, e devolve o próprio goban
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in t:
        termo=0
        while i[0]!=alfabeto[termo]:
            termo+=1
        g[termo][i[1]-1]=0
    return g

#Reconhecedor
def eh_goban(arg):
    #eh_goban: universal → booleano
    '''
    Devolve True se o argumento for um TAD (Tipo Abstrato de Dados) goban e False caso contrário
    '''
    return len(arg) in (9,13,19) or len(arg[0]) in (9,13,19) and not all(isinstance(arg,tuple)and len(col)==len(arg[0]) and eh_intersecao(col) and all(lin in (0,1,2) for lin in col) for col in arg)
def eh_intersecao_valida(g,i):
    #eh_intersecao_valida: goban × intersecao → booleano
    '''
    Devolve True se i for uma interseção válida dentro do goban g e False caso contrário
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    termo=0
    while i[0]!=alfabeto[termo]:
        termo+=1
    return eh_goban(g) and eh_intersecao(i) and len(g)>=i[1] and len(g[0])>=termo and g[termo][i[1]-1] in (0,1,2)

#Teste
def gobans_iguais(g1,g2):
    #gobans_iguais: universal × universal → booleano
    '''
    Devolve True somente se g1 e g2 forem gobans e forem iguais
    '''
    return eh_goban(g1) and eh_goban(g2) and g1==g2

#Transformador
def goban_para_str(g):
    #goban_para_str : goban → str
    '''
    Devolve a cadeia de caracteres que representa o goban, conforme exemplificado
    '''
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(g[0])<=9:
        desenho='  '
    else:
        desenho='  '
    for i in range(len(g)):
        if len(g[0])<=9:
            desenho+=(f' {alfabeto[i]}') 
        else:
            desenho+=(f' {alfabeto[i]}')
    for i in range(len(g[0])): 
        if (len(g[0])-i)<10:
            desenho+=(f'\n {len(g[0])-i} ')
            for a in range(len(g)):
                if g[a][-(i+1)]==0:
                    desenho+=('. ')
                if g[a][-(i+1)]==1:
                    desenho+=('O ')
                if g[a][-(i+1)]==2:
                    desenho+=('X ')
            desenho+=(f' {len(g[0])-i}')
        else:
            desenho+=(f'\n{len(g[0])-i} ')
            for a in range(len(g)):
                if g[a][-(i+1)]==0:
                    desenho+=('. ')
                if g[a][-(i+1)]==1:
                    desenho+=('O ')
                if g[a][-(i+1)]==1:
                    desenho+=('X ')
            desenho+=(f'{len(g[0])-i}')
    if len(g[0])<=9:
        desenho+='\n  '
    else:
        desenho+='\n  '
    for i in range(len(g)):
        if len(g[0])<=9:
            desenho+=(f' {alfabeto[i]}') 
        else:
            desenho+=(f' {alfabeto[i]}')
    return (desenho)

def obtem_territorios(g):
    #obtem_territorios: goban → tuplo
    '''
    Devolve o tuplo formado pelos tuplos com as interseções de cada território de g. A função retorna as interseções de cada território ordenadas na ordem de leitura do tabuleiro de Go e os territórios ordenados na ordem de leitura da primeira interseção do território
    '''
    lista_final = []
    alfabeto = 'ABCDEFGHIJKLMNOPQRS'
    for i in range(len(g)):
        for w in range(len(g[0])):
            if g[i][w] == 0 and (f'{alfabeto[i]}', w + 1) not in [intersecao for cadeia in lista_final for intersecao in cadeia]:
                lista = obtem_cadeia(g, (f'{alfabeto[i]}', w + 1))
                lista_final.append(lista)
    return tuple(ordena_intersecoes(cadeia) for cadeia in lista_final)
def obtem_adjacentes_diferentes(g,t):
    #obtem_adjacentes_diferentes: goban × tuplo → tuplo
    '''  
    Devolve o tuplo ordenado formado pelas interseções adjacentes às interseções do tuplo t livres, se as interseções do tuplo t estão ocupadas por pedras de jogador ou ocupadas por pedras de jogador, se as interseções do tuplo t estão livres
    '''
    lista=[]
    for elemento in t:
        for elemento2 in obtem_intersecoes_adjacentes(elemento,obtem_ultima_intersecao(g)):
            if not eh_pedra_jogador(obtem_pedra(g,elemento)) and eh_pedra_jogador(obtem_pedra(g,elemento2)) and elemento2 not in lista:
                lista.append(elemento2)
            if eh_pedra_jogador(obtem_pedra(g,elemento)) and not eh_pedra_jogador(obtem_pedra(g,elemento2)) and elemento2 not in lista:
                lista.append(elemento2)
    return ordena_intersecoes(lista)
def jogada(g,i,p):
    #jogada: goban × intersecao × pedra → goban
    '''
    Modifica destrutivamente o goban g, colocando a pedra do jogador p na interseção i e removendo todas as pedras do jogador contrário pertencentes a cadeias adjacentes a i sem liberdades, devolvendo o próprio goban
    '''
    for elementos in obtem_intersecoes_adjacentes(i,obtem_ultima_intersecao(coloca_pedra(g,i,p) )):
        if eh_pedra_preta(p) and obtem_adjacentes_diferentes(coloca_pedra(g,i,p),obtem_cadeia(g,elementos))==() and eh_pedra_branca(obtem_pedra(coloca_pedra(g,i,p),elementos)):
            remove_cadeia(g,obtem_cadeia(coloca_pedra(g,i,p),elementos))
        if eh_pedra_branca(p) and obtem_adjacentes_diferentes(coloca_pedra(g,i,p),obtem_cadeia(g,elementos))==() and eh_pedra_preta(obtem_pedra(coloca_pedra(g,i,p),elementos)):
            remove_cadeia(g,obtem_cadeia(coloca_pedra(g,i,p),elementos))
    return g
def obtem_pedras_jogadores(g):
    #obtem_pedras_jogadores: goban → tuplo
    '''
    Devolve um tuplo de dois inteiros que correspondem ao número de interseções ocupadas por pedras do jogador branco e preto, respectivamente
    '''
    contador_pretas=0
    contador_brancas=0
    for i in range(len(g)):
        for w in range(len(g[0])):
            if g[i][w]==1:
                contador_brancas+=1
            if g[i][w]==2:
                contador_pretas+=1
    return (contador_brancas,contador_pretas)
def calcula_pontos(g):
    #calcula_pontos: goban → tuple
    '''
    Recebe um goban e devolve um tuplo de dois inteiros com as pontuações dos jogadores branco e preto, respectivamente
    '''
    pontos_branco=0
    pontos_preto=0
    for territorios in obtem_territorios(g):
        if all(eh_pedra_branca(obtem_pedra(g,interseçao)) for interseçao in obtem_adjacentes_diferentes(g,territorios)) and obtem_adjacentes_diferentes(g,territorios)!=():
            pontos_branco+=len(territorios)
        if all(eh_pedra_preta(obtem_pedra(g,interseçao)) for interseçao in obtem_adjacentes_diferentes(g,territorios)) and obtem_adjacentes_diferentes(g,territorios)!=():
            pontos_preto+=len(territorios)
    pontos_branco+=obtem_pedras_jogadores(g)[0]
    pontos_preto+=obtem_pedras_jogadores(g)[1]
    return (pontos_branco,pontos_preto)
def eh_jogada_legal(g,i,p,l):
    #eh_jogada_legal: goban × intersecao × pedra × goban → booleano
    '''
    A função recebe um goban g, uma interseção i, uma pedra de jogador p e outro goban l, e devolve True se a jogada for legal ou False caso contrário, sem modificar g ou l
    '''
    copia=cria_copia_goban(g)
    if not eh_intersecao_valida(copia,i):
        return False
    jogada(copia,i,p)
    return not eh_pedra_jogador(obtem_pedra(g,i)) and obtem_adjacentes_diferentes(copia,obtem_cadeia(copia,i))!=() and not gobans_iguais(copia,l)
def turno_jogador(g,p,l):
    #turno_jogador: goban × pedra × goban → booleano
    '''
    Recebe um goban g, uma pedra de jogador p e outro goban l, e oferece ao jogador que joga com pedras p a opção de passar ou colocar uma pedra própria numa interseção. Se o jogador passar, a função devolve False sem modificar os argumentos. Caso contrário, a função devolve True e modifica destrutivamente o tabuleiro g de acordo com a jogada realizada
    '''
    x=None
    while x!='P':
        x=input("Escreva uma intersecao ou 'P' para passar [X]:")
        if x=='P':
            return False
        if eh_jogada_legal(g,str_para_intersecao(x),p,l):
            jogada(g,str_para_intersecao(x),p)
            if gobans_iguais(g,l):
                return False
            return True
        continue
def go(n,tb,tn):
    #go: int × tuple × tuple → booleano
    '''
    Recebe um inteiro correspondente à dimensão do tabuleiro e dois tuplos (potencialmente vazios) com a representação externa das interseções ocupadas por pedras brancas (tb) e pretas (tp) inicialmente e vai criar um jogo de Go
    '''
    if n not in (9,13,19) or type(tb)!=tuple or type(tn)!=tuple:
        raise ValueError('go: argumentos invalidos')
    g=cria_goban(n,tb,tn)
    l=cria_copia_goban(g)
    while turno_jogador(g,cria_pedra_branca(),l) and turno_jogador(g,cria_pedra_preta(),l):
        turno_jogador(g,cria_pedra_branca(),l)
        turno_jogador(g,cria_pedra_preta(),l)
        l=cria_copia_goban(g)
    if calcula_pontos(g)[0]>calcula_pontos(g)[1]:
        return True
    return False