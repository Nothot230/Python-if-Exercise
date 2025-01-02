Letter = [['A',80,100],['B',70,80],['C',60,70],['D',50,60],['F',0,50]]
Character = str(input("Enter Character: "))
for i in range(len(Letter)):
    if(Character == Letter[i][0]):
        print(Letter[i])