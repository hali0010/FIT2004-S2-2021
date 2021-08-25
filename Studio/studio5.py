import math
def min_coins(coins,V):
    coins_needed = [math.inf] * (V+1)
    coins_needed[0] = 0
    for i in range(1,V+1):
        if i>= min(coins):
            best_so_far = math.inf
        for c in coins:
            if c<=i:
                best_so_far = min(best_so_far,1+coins_needed[i-c])
        coins_needed[i] = best_so_far
    return coins_needed[V]

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