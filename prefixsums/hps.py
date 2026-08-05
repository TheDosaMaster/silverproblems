import sys
sys.stdin = open("hps.in","r")
sys.stdout = open("hps.out","w")
n = int(input())
games = list(str(input()) for _ in range(n))
score = [[0,0,0]]

for i in range(n):

    new = score[-1][:]
    if games[i] == "H":
        new[0] +=1
    elif games[i] == "P":
        new[1] += 1
    else:
        new[2] +=1
    score.append(new)

wins = 0
for i in range(n):
    preswitch = max(score[i][0],score[i][1],score[i][2])
    postswitch =max(score[n][0]-score[i][0],score[n][1]-score[i][1],score[n][2]-score[i][2])
    wins = max(wins,postswitch+preswitch)
print(wins)