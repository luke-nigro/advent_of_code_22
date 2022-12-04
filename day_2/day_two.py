import pandas as pd

df = pd.read_csv('D:/dev/advent_of_code/day_2/input.txt', delimiter=' ', names=['opp', 'player'])

score = 0
for i in range(len(df)):
    if df['player'][i] =='X':
        if df['opp'][i] == 'A':
            score += 3
        elif df['opp'][i] == 'B':
            score += 1
        else:
            score += 2
    elif df['player'][i] =='Y':
        score += 3
        if df['opp'][i] == 'A':
            score += 1
        elif df['opp'][i] == 'B':
            score += 2
        else:
            score += 3
    else:
        score += 6
        if df['opp'][i] == 'A':
            score += 2
        elif df['opp'][i] == 'B':
            score += 3
        else:
            score += 1

print(score)