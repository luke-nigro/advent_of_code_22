import pandas as pd

df = pd.read_csv('D:/dev/advent_of_code/day_1/input.txt', header = None)

count = 0
for i in range(len(df)-1):
    if df[0][i] < df[0][i+1]:
        count+=1

print(count)

window_count = 0
for i in range(len(df)-3):
    window_one = df[0][i] + df[0][i+1] +df[0][i+2]
    window_two = df[0][i+1] + df[0][i+2] +df[0][i+3]

    if window_one < window_two:
        window_count += 1

print(window_count)