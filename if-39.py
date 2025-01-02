Grade = [['A',80],['B',70],['C',60],['D',50],['F',0]]
Score = int(input('Enter your score: '))
for i in range(len(Grade)):
    if(Score >= Grade[i][1]):
        print(Grade[i][0])
        break