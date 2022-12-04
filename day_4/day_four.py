import pandas as pd

df = pd.read_csv('D:/dev/advent_of_code/day_4/input.txt', names = ['elf_one', 'elf_two'])

df['elf_one_min']  = [pos.split('-')[0] for pos in df['elf_one']]
df['elf_one_max']  = [pos.split('-')[1] for pos in df['elf_one']]
df['elf_two_min']  = [pos.split('-')[0] for pos in df['elf_two']]
df['elf_two_max']  = [pos.split('-')[1] for pos in df['elf_two']]

total_overlaps = 0
for i in range(len(df)):
    elf_one_min = int(df['elf_one_min'][i])
    elf_one_max = int(df['elf_one_max'][i])
    elf_two_min = int(df['elf_two_min'][i])
    elf_two_max = int(df['elf_two_max'][i])

    if elf_one_max >= elf_two_min and elf_two_max >= elf_one_min:
        print(df['elf_one'][i], df['elf_two'][i])
        total_overlaps += 1
    # elif elf_two_max >= elf_one_min:
    #     print(df['elf_one'][i], df['elf_two'][i])
    #     total_overlaps += 1

print(total_overlaps)