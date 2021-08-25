# Student Name: Haider Ali
# Student ID: 31371337 

import math

# Task 1 Game Master

# def min_coins(coins,V):
#     coins_needed = [math.inf] * (V+1)
#     coins_needed[0] = 0
#     for i in range(1,V+1):
#         if i>= min(coins):
#             best_so_far = math.inf
#         for c in coins:
#             if c<=i:
#                 best_so_far = min(best_so_far,1+coins_needed[i-c])
#         coins_needed[i] = best_so_far
#     return coins_needed[V]

def min_coins_TD(coins,V):
    coins_needed = [math.inf] * (V+1)
    output = min_coins_aux(coins,V,coins_needed)
    return output

def min_coins_aux(coins,V,coins_needed):
    if V ==0 :
        coins_needed[V] = 0
        return 0
    if coins_needed[V] == None:
        best_so_far = math.inf
        for c in coins:
            if c<=V:
                best_so_far = min(best_so_far,1+min_coins_aux(c,V-c,coins_needed))        
        coins_needed[V] = best_so_far

    return coins_needed[V]


def count_encounters(target_difficulty,monster_list):
    monster_difficulties = [ j for i, j in monster_list]
    best_outcomes = min_coins_TD(monster_difficulties,target_difficulty)
    max = best_outcomes[0]
    for i in range(1,len(best_outcomes)):
        if max < best_outcomes[i]:
            max = best_outcomes[i]
    return max


target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))