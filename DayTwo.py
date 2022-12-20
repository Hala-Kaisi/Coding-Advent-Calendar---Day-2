lines = open("D2_Input.txt").readlines()
opponent = 'A'
me = 'A'
roundScore = 0
totalScore = 0
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
strategy = {
    1: ['A', 'X', 'C', 3],                   # A for Rock, B for Paper, and C for Scissors
    2: ['A', 'Y', 'A', 4],                  
    3: ['A', 'Z', 'B' ,8],                   # 0 if you lost, 3 if the round was a draw, and 6 if you won
    4: ['B', 'X', 'A', 1],   
    5: ['B', 'Y', 'B', 5],
    6: ['B', 'Z', 'C', 9],
    7: ['C', 'X', 'B', 2],
    8: ['C', 'Y', 'C', 6],
    9: ['C', 'Z', 'A', 7],
}


for line in lines:
    opponent = line[0]
    me = line[2]
    
    for i in strategy:
        if opponent == strategy[i][0] and me == strategy[i][1]:
            roundScore += strategy[i][3]
            totalScore += roundScore
            roundScore = 0
            break
        
print('Total Score: ' + str(totalScore))
        
    
        