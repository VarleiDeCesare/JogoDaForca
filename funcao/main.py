import os 
def limpa():
    os.system('cls')
def linha():
    print('=-=-='*5)
def loop(palavrasecreta,letrasdescobertas,nome2,dica1,dica2,dica3,palavrasecreta1,nome):
    conterro =0
    contdica = 0
    print('=~~~JOGO DA FORCA~~~=')
    for i in range(0,len(palavrasecreta)):
        letrasdescobertas.append('*')
    acertou = False
    while acertou==False:
        opcao = int(input('\n [1]= JOGAR  //-/-//  [2]= DICA. '))
        if opcao==2:
            contdica= contdica+ 1
            if contdica==1:
                print('Dica1:',dica1)
            elif contdica==2:
                print('Dica2:', dica2)
            elif contdica==3:
                print('Dica3:',dica3)
            else:
                print("Não tem mais dicas...")
            opcao=1
        if opcao==1:
            letra = str(input('\nDigite uma letra: '.lower().strip()))
            for i in range(0,len(palavrasecreta)):
                if letra==palavrasecreta[i]:
                    letrasdescobertas[i]=letra
                print(letrasdescobertas[i],end=' ')
            if letra not in palavrasecreta:
                conterro +=1
                print("\nERRO: Você já errou", conterro,'vez')
            if conterro==5:
                historico = open('historico','a')
                historico.write('\nPalavra: {}, Desafiante {} e competidor PERDEDOR {}'.format(palavrasecreta1,nome,nome2))
                historico.close()
                print('\nVocê errou 5 vezes e perdeu o jogo') 
                break
            acertou=True
            for x in range(0,len(letrasdescobertas)):
                if letrasdescobertas[x]=='*':
                    acertou=False
            if '*' not in letrasdescobertas:
                historico = open('historico','a')
                historico.write('\nPalavra: {}, Desafiante {} e competidor VENCEDOR {}'.format(palavrasecreta1,nome,nome2))
                historico.close()
                print('\nParabéns você venceu o jogo!')
    return acertou
def play():
    limpa()
    linha()
    nome = str(input('Digite o nome do Desafiante: ')).strip().capitalize()
    nome2 = str(input('Digite o nome do Competidor: ')).strip().capitalize()
    linha()
    palavrasecreta1 = str(input('{}, Digite a palavra secreta: '.format(nome))).lower().strip()
    palavrasecreta = list(palavrasecreta1)
    letrasdescobertas = []
    linha()
    try:
        dica1 = str(input('Digite a dica1: ')).lower().strip()
        dica2 = str(input('Digite a dica2: ')).lower().strip()
        dica3 = str(input('Digite a dica3: ')).lower().strip()
    except:
        print('Valor não foi digitado ou foi digitado inválidamente.')
    limpa()
    linha()
    loop(palavrasecreta,letrasdescobertas,nome2,dica1,dica2,dica3,palavrasecreta1,nome)
    try:
        jogarnovamente = str(input('QUER JOGAR NOVAMENTE [S/N]')).lower().strip()
    except:
        print('Valor não foi digitado ou foi digitado inválidamente.')
    if jogarnovamente=='n':
        print('OBRIGADO POR JOGAR, VOLTE SEMPRE')
    elif jogarnovamente=='s':
        return play()
