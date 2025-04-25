def armague():
    pontos_player1=0
    pontos_player2=0
    informacoes=[[],[]]
    for x in range(len(informacoes)):
        for y in range(3):
            informacoes[x].append([float(x) for x in input().split()])
    #                      rodada
    
    #acrescimos baseados na combinacao de classes dos personagens
    # informacoes[player][rodada][stats]
    for _ in range(3):
        player1=informacoes[0][_]
        player2=informacoes[1][_]
        if player1[0]==1 and player2[0]==3:
            player1[2]*=1.3
        elif player2[0]==1 and player1[0]==3:
            player2[2]*=1.3
        elif player1[0]==3 and player2[0]==2:
            player1[1]*=1.25
        elif player2[0]==3 and player1[0]==2:
            player2[1]*=1.25
        elif player1[0]==2 and player2[0]==1:
            player1[1]*=1.15
            player1[2]*=1.15
        elif player2[0]==2 and player1[0]==1:
            player2[1]*=1.15
            player2[2]*=1.15
    
    # duelos
    for x in range(3):
        player1=informacoes[0][x]
        player2=informacoes[1][x]
        for y in range(2):
            if player1[2]<player2[2]:
                player2[2]-=player1[1]
                if player2[2]>0:
                    player1[2]-=player2[1]
            elif player2[2]<player1[2]:
                player1[2]-=player2[1]
                if player1[2]>0:
                    player2[2]-=player1[1]
            elif player1[2]==player2[2]:
                player2[2]-=player1[1]
                if player2[2]>0:
                    player1[2]-=player2[1]
        if player1[2]>player2[2]:
            pontos_player1+=1
        elif player2[2]>player1[2]:
            pontos_player2+=1
        elif player1[2]==player2[2]:
            if player1[1]>player2[1]:
                pontos_player1+=1
            elif player2[1]>player1[1]:
                pontos_player2+=1
    if pontos_player1>pontos_player2:
        print("jogador 1 ganhou!")
    elif pontos_player2>pontos_player1:
        print("jogador 2 ganhou!")

if __name__=='__main__':
    armague()
