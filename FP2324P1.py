def eh_territorio(t):
    '''
    Recebe um território com qualquer valor universal e devolve o valor boleano True se corresponder a um território e Falso se não corresponder
    '''
    if type(t)!=tuple or not(1<=len(t)<=26): #Verificar se o território é um tuplo e se o número de colunas está entre 1 e 26
        return False
    for i in range(len(t)):
        if type(t[i])!=tuple or len(t[0])!=len(t[i]) or not(1<=len(t[i])<=99):#Verificar se o número de linhas está entre 1 e 99
            return False
        for w in range(len(t[i])): #Verificar se todos os elementos são 1 ou 0
            if t[i][w]!=0 and t[i][w]!=1 or type(t[i][w])!=int:
                return False       
    return True


def obtem_ultima_intersecao(t):
    '''
    Recebe um território e devolve a interseção do mesmo
    '''
    num_colunas=len(t)-1 #Calcular o termo da coluna da última interseção
    num_linhas=len(t[0]) #Calcular o termo da linha da última interseção
    letras_alfabeto=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    arg=letras_alfabeto[num_colunas]
    return (arg,num_linhas)


def eh_intersecao(arg):
    '''
    Recebe um argumento do tipo universal e devolve o valor boleano True se o respetivo argumento corresponde a uma interseção e o valor boleano False caso contrário
    '''
    if type(arg)==tuple and len(arg)==2 and arg[0] in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z') and type(arg[1])==int and 0<arg[1]<100:
        return True #Verifica se o argumento é um tuplo com um letra no primeiro termo e um número inteiro entre 0 e 100 no segundo
    return False


def eh_intersecao_valida(t,i):
    '''
    Recebe um território e uma interseção e e devolve o valor boleano True se a interseção corresponde a uma interseção no território e o valor boleano False caso contrário
    '''
    num_colunas=len(t) #Calcular o número de colunas no território baseado no comprimento de t
    num_linhas=len(t[0]) #Calcular o número de linhas no território baseado no comprimento do primeiro valor de t, sabendo que todos os termos de t têm o mesmo comprimento
    alfabeto=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    termo=0 #Variável que vai ser usada para calcular o termo da letra no alfabeto
    while i[0]!=alfabeto[termo]: 
        termo+=1     #Pretende-se ir adicionando 1 valor à variável até determinar a posição da letra,que representa o eixo das colunas, no alfabeto 
    if termo<num_colunas and 0<i[1]<=num_linhas:
        return True
    return False


def eh_intersecao_livre(t,i):
    '''
    Recebe um território e uma interseção no território e devolve o valor boleano True se a interseção for livre e o valor boleano False caso contrário
    '''
    alfabeto=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    termo=0
    while i[0]!=alfabeto[termo]: 
        termo+=1     #Pretende-se ir adicionando 1 valor à variável até determinar a posição da letra,que representa o eixo das colunas, no alfabeto 
    if t[termo] and t[termo][i[1]-1]==0: #Averiguar se dentro da coluna correspondete à letra da interseção existe o valor 0, indicativo de interseção livre (-1 porque na interseção começa no 1 e não no 0)
        return True
    return False


def obtem_intersecoes_adjacentes(t,i):
    '''
    Recebe um território e uma interseção no território e devolve um tuplo constítuido pelas interseções adjacentes
    '''
    alfabeto=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    termo=0
    while i[0]!=alfabeto[termo]: 
        termo+=1     #Pretende-se ir adicionando 1 valor à variável até determinar a posição da letra,que representa o eixo das colunas, no alfabeto 
    num_adjacentes=[] #Ter uma lista com referência vazia para ir ser adicionado interseções adjacentes se existirem
    if 0<=termo-1:
        num_adjacentes.append((alfabeto[termo-1],i[1]))
    if i[1]+1<=len(t[0]):
        num_adjacentes.append((alfabeto[termo],i[1]+1))
    if termo+1<len(t):
        num_adjacentes.append((alfabeto[termo+1],i[1]))
    if 0<i[1]-1:
        num_adjacentes.append((alfabeto[termo],i[1]-1)) 
    return tuple(sorted(num_adjacentes,key=lambda num: num[1])) #Ordenar a lista, de acordo com o segundo elemento(número) e transformar-la em tuplo


def ordena_intersecoes(tup):
    '''
    Recebe um tuplo e ordena-o
    '''
    ordenado_letras=sorted(tup) #Ordena as interseções por letras
    return (tuple(sorted(ordenado_letras,key=lambda num: num[1]))) #A função gera um tuplo onde os tuplos de entrada estão ordenados de acordo com segundo elemento do tuplo(num[1])


def territorio_para_str(t):
    '''
    Recebe um território e devolve uma string com a representação gráfica correspondente
    '''
    alfabeto=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    if not eh_territorio(t):
        raise ValueError("territorio_para_str: argumento invalido") #Dá erro se o território não for válido
    colunas=len(t)
    linhas=len(t[0])
    if linhas<=9:
        desenho='  '
    else:
        desenho='  '
    for i in range(colunas): #Escreve as letras do alfabeto correspondente às colunas do território
        if linhas<=9:
            desenho+=(f' {alfabeto[i]}') 
        else:
            desenho+=(f' {alfabeto[i]}')
    for i in range(linhas): 
        if (linhas-i)<10: #Representa as interseções de território com X e com '.' se não existirem as mesmas
            desenho+=(f'\n {linhas-i} ')
            for a in range(colunas):
                if t[a][-(i+1)]==0:
                    desenho+=('. ')
                if t[a][-(i+1)]==1:
                    desenho+=('X ')
                if t[a][i]!=0 and t[a][i]!=1:
                    raise ValueError('territorio_para_str: argumento invalido')
            desenho+=(f' {linhas-i}')
        else:
            desenho+=(f'\n{linhas-i} ')
            for a in range(colunas):
                if t[a][-(i+1)]==0:
                    desenho+=('. ')
                if t[a][-(i+1)]==1:
                    desenho+=('X ')
                if t[a][i]!=0 and t[a][i]!=1:
                    raise ValueError('territorio_para_str: argumento invalido')
            desenho+=(f'{linhas-i}')
    if linhas<=9:
        desenho+='\n  '
    else:
        desenho+='\n  '
    for i in range(colunas): #Acaba a escrever as letras das colunas respetivas
        if linhas<=9:
            desenho+=(f' {alfabeto[i]}') 
        else:
            desenho+=(f' {alfabeto[i]}')
    return (desenho)


def obtem_cadeia(t,i):
    '''
    Recebe um território e uma interseção do mesmo e devolve todas as interseções da cadeia respetiva à interseção
    '''
    cadeia=[i]
    exemplo=[i]
    if not eh_territorio(t) or not isinstance(i, tuple) or len(i) != 2 or not eh_intersecao_valida(t, i):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    if eh_intersecao_livre(t,i)==True: #Se a interseção for livre
        while exemplo:
            novo_exemplo=exemplo.pop() #Criar uma variável que resulta do último elemento da lista "exemplo"
            num_adjacentes = obtem_intersecoes_adjacentes(t, novo_exemplo)  # "num_adjacentes" é uma variável que resulta da função do ex. 2.1.6 usando o terriório em questão e o elemento "novo_exemplo"

            for exemplo_adj in num_adjacentes:
                if eh_intersecao_livre(t,exemplo_adj) and (exemplo_adj not in cadeia): #Verificar se "exemplo_adj" é uma interseção livre e adicioná-la á cadeia se ainda não estiver lá
                    cadeia.append(exemplo_adj)
                    exemplo.append(exemplo_adj)
            cadeia_final=ordena_intersecoes(sorted(tuple(cadeia))) #Primeiro ordenar de acordo com as letras das colunas e depois através da função "ordena_intersecoes" do ex 2.1.7
    if eh_intersecao_livre(t,i)==False: #Se a interseção não for livre
        while exemplo:
            novo_exemplo=exemplo.pop()
            num_adjacentes = obtem_intersecoes_adjacentes(t, novo_exemplo)

            for exemplo_adj in num_adjacentes:
                if not eh_intersecao_livre(t,exemplo_adj) and (exemplo_adj not in cadeia):
                    cadeia.append(exemplo_adj)
                    exemplo.append(exemplo_adj)
            cadeia_final=ordena_intersecoes(sorted(tuple(cadeia)))
    return cadeia_final


def obtem_vale(t,i):
    '''
    Recebe um território e uma interseção de território e devolve em tuplo todos os vales correspondentes à cadeia da respetiva interseção
    '''
    cadeia=[i]
    exemplo=[i]
    cadeia2=[]
    if not eh_territorio(t) or not isinstance(i, tuple) or len(i) != 2 or not eh_intersecao_valida(t, i) or eh_intersecao_livre(t,i):
        raise ValueError("obtem_vale: argumentos invalidos") #Verifica se o território e a interseção são válidos
    if eh_intersecao_livre(t,i)==False: #Com uma interseção não livre calcula-se a cadeia correspondente e retira-se um valor no qual calcula-se os adjacentes. Se o adjacente for livre e não repetido adiciona-se à cadeia de vales
        while exemplo:
            novo_exemplo=exemplo.pop()
            num_adjacentes = obtem_intersecoes_adjacentes(t, novo_exemplo)

            for exemplo_adj in num_adjacentes:
                if eh_intersecao_livre(t,exemplo_adj) and (exemplo_adj not in cadeia2):
                    cadeia2.append(exemplo_adj)
                if not eh_intersecao_livre(t,exemplo_adj) and (exemplo_adj not in cadeia):
                    cadeia.append(exemplo_adj)
                    exemplo.append(exemplo_adj)
            cadeia_final=ordena_intersecoes(sorted(tuple(cadeia2))) #Devolve uma cadeia com todos os vales da cadeia da interseção
    return cadeia_final


def verifica_conexao(t,i1,i2):
    '''
    Recebe um território e duas interseções e devolve o valor bolenao True se as duas interseções estão conectadas e o valor boleano False caso contrário
    '''
    if not eh_territorio(t) or not eh_intersecao_valida(t,i1) or not eh_intersecao_valida(t,i2):
        raise ValueError('verifica_conexao: argumentos invalidos') #Verifica se as interseções e o território são válidos
    lista1=obtem_cadeia(t,i1) #Calcula a cadeia da primeira interseção e devolve True se a segunda interseção pertencer a essa cadeia
    return i2 in lista1


def calcula_numero_montanhas(t):
    '''
    Recebe um território e devolve o número de interseções que são montanhas nesse mesmo território
    '''
    numero_montanhas=0
    if eh_territorio(t): #Se o território for válido calcula o numero de montanhas, representadas pelo número 1, que fazem parte do mesmo
        for i in range(len(t)):
            for num in t[i]:
                if num==1:
                    numero_montanhas+=1
    else:
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    return numero_montanhas


def calcula_numero_cadeias_montanhas(t):
    '''
    Recebe um território e devolve o número de cadeias presentes nesse mesmo território
    '''
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numero_cadeias=0
    cadeias=[]
    if not eh_territorio(t): #Verifica se o territótio é válido
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    for i in range(len(t)): #Verifica cada interseção e calcula a sua cadeia, de seguida adiciona essa cadeia a um contador se ainda não fizer parte do mesmo
        for w in range(len(t[0])):
            if t[i][w]==1 and t[i][w] not in cadeias:
                num_para_cadeias=obtem_cadeia(t,(alfabeto[i],w+1))
                if num_para_cadeias not in cadeias:
                    cadeias.append(num_para_cadeias)
                    numero_cadeias+=1
    return numero_cadeias


def calcula_tamanho_vales(t):
    '''
    Recebe um território e devolve o número total de vales diferentes que fazem parte desse território
    '''
    alfabeto={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    vales_totais=[]
    if not eh_territorio(t): #Verifica se o território é válido
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    for i in range(len(t)): #Verifica uma a uma cada interseção calculando os vales da cadeia correspondete e adiciona a uma lista os vales correspondestes se ainda não fizerem parte dessa lista
        for w in range(len(t[0])):
            if t[i][w]==1:
                vales=obtem_vale(t,(alfabeto[i],w+1))
                for z in range(len(vales)):
                    if vales[z] not in vales_totais:
                        vales_totais.append(vales[z])
    return len(vales_totais) #Devolve o número de elementos da lista com todos os vales