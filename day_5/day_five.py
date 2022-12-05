import pandas as pd
import numpy as np
from numpy import nan
import math

moves = pd.read_csv('D:/dev/advent_of_code/day_5/input.txt', 
                delimiter=' ', 
                names=['move', 'n_move', 'f', 'from', 't', 'to'],
                usecols=['n_move', 'from', 'to'])

crates = pd.read_csv('D:/dev/advent_of_code/day_5/crates.txt', delimiter=' ', header=None)

lists = []
for col in crates.columns:
    temp_list = []
    for val in range(len(crates[:][col])-1, -1, -1):
        if not pd.isna(crates[col][val]):
            temp_list.append(crates[col][val])
    lists.append(temp_list)

for i in range(len(moves)):
    n_moves = moves['n_move'][i]
    from_crate = moves['from'][i] - 1
    to_crate = moves['to'][i] - 1

    temp = []
    while n_moves > 0:
        popped = lists[from_crate].pop()
        temp.append(popped)
        n_moves -= 1
    
    for i in range(len(temp)):
        pop_temp = temp.pop()
        lists[to_crate].append(pop_temp)

for i, sublist in enumerate(lists):
    print(lists[i][-1])