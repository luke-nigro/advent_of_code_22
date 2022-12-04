import pandas as pd
import string

#enumerate all letters
values = dict()
for index, letter in enumerate(string.ascii_letters):
   values[letter] = index + 1

#load input
df = pd.read_csv('D:/dev/advent_of_code/day_3/input.txt', names = ['ruck'])

sum_priorities, sum_badges = 0, 0

for sack in df.ruck:
    similar_item = ''.join(set(sack[0:len(sack)//2]) & set(sack[len(sack)//2:len(sack)]))
    sum_priorities += values[similar_item]

print('Sum total of priorities: {}'.format(sum_priorities))

for i in range(0, len(df)-2, 3):
    badge_id = ''.join(set(df['ruck'][i]) & set(df['ruck'][i+1]) & set(df['ruck'][i+2]))
    sum_badges += values[badge_id]

print('Sum total of all badges: {}'.format(sum_badges))