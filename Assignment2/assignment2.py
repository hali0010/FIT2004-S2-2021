# Student Name: Haider Ali
# Student ID: 31371337 

# Task 1 Game Master
# count_aux has been modified from https://www.reddit.com/r/learnprogramming/
def count_aux(monster_difficulties, goal):
    memo_monster_diff = [[monster_dif] for monster_dif in monster_difficulties] # a memo array to store the monster difficulties
    arr = [] # an empty array for helping with managing the memo array
    final_memo = []
    count = 0
    while memo_monster_diff:
        for existing_monster_difficulties in memo_monster_diff:
            sum_to_include_monster_diff = sum(existing_monster_difficulties) # adds the similiar difficulties together for example adds the difficulty of (2) and (3) along with the difficulty of (5)
            for monster_dif in monster_difficulties:
                if monster_dif >= existing_monster_difficulties[-1]:
                    if sum_to_include_monster_diff + monster_dif < goal:
                        arr.append(existing_monster_difficulties + [monster_dif])
                    elif sum_to_include_monster_diff + monster_dif == goal:
                        final_memo.append(existing_monster_difficulties + [monster_dif])
        memo_monster_diff = arr
        arr = []
    for i in range(0,len(final_memo)):
        count = count +1
    return count

def count_encounters(target_difficulty,monster_list):
    monster_difficulties = [ j for i, j in monster_list]
    return count_aux(monster_difficulties,target_difficulty)

# Task 2 Greenhouse

def best_lamp_allocation(num_p , num_l,probs):
    memo_greenhouse = [[0 for i in range(num_l+1)] for j in range(num_p)]
    lamp_left = num_l
    lamps_taken = 0
    for l in range(0,num_l+1):
        memo_greenhouse[0][l] = probs[0][l]
    for plants in range(1,num_p):    
        for lamps in range(0,num_l+1): # we need to find the optimum number of lamps for each plant
            lamp_left = num_l - lamps  # lamp_left is the number of lamps we can use
            max = probs[plants][lamps]*memo_greenhouse[plants-1][lamp_left]
            if (lamp_left>0):
               for l in range(lamp_left-1,-1,-1): # 1 -> 0 
                   temp = probs[plants][lamps]*memo_greenhouse[plants-1][l]  # 
                   if temp > max:
                       max = temp
                       lamps_taken =l
              # for the situations we cannot use any lamp for that plant

            memo_greenhouse[plants][lamps]= max
            print(memo_greenhouse)
    max = memo_greenhouse[num_p-1][0]
    for lamps in range(0,num_l+1):
        if(memo_greenhouse[num_p-1][lamps]>max):
            max = memo_greenhouse[num_p-1][lamps]
    return max
    
# test case 1    
# probs = [[0.92, 0.88, 0.07, 0.74, 0.83, 0.73, 0.85, 0.41, 0.94, 0.58, 0.17],
# [0.05, 0.42, 0.01, 0.53, 0.03, 0.13, 0.49, 0.64, 0.13, 0.78, 0.05],
# [0.68, 0.38, 0.86, 0.6, 0.53, 0.49, 0.89, 0.18, 0.69, 0.21, 0.3],
# [0.61, 0.85, 0.17, 0.78, 0.21, 0.05, 0.09, 0.7, 0.08, 0.86, 0.21],
# [0.72, 0.81, 0.12, 0.73, 0.45, 0.8, 0.3, 0.84, 0.89, 0.48, 0.33],
# [0.19, 0.33, 0.01, 0.54, 0.71, 0.56, 0.55, 0.28, 0.29, 0.43, 0.42],
# [0.36, 0.65, 0.38, 0.48, 0.05, 0.28, 0.45, 0.42, 0.49, 0.5, 0.97],
# [0.95, 0.05, 0.73, 0.91, 0.25, 0.16, 0.11, 0.67, 0.48, 0.48, 0.77],
# [0.96, 0.21, 0.19, 0.55, 0.04, 0.58, 0.91, 0.3, 0.92, 0.36, 0.48],
# [0.46, 0.6, 0.76, 0.91, 0.79, 0.92, 0.66, 0.28, 0.48, 0.32, 0.17]]
# num_l = 10
# num_p = 10

#solution
#allocation of lamps to plants: [0, 1, 0, 1, 0, 4, 1, 0, 0, 3] 
#best probability: 0.061589317090129915

# test case 2 

# probs = [[0.39, 0.53, 0.09, 0.13, 0.36, 0.91, 0.84, 0.14, 0.3, 0.23, 0.21],
#  [0.31, 0.49, 0.99, 0.13, 0.45, 0.7, 0.73, 0.22, 0.97, 0.89, 0.93],
#  [0.08, 0.73, 0.17, 0.24, 0.62, 0.69, 0.43, 0.31, 0.79, 0.73, 0.96],
#  [0.42, 0.1, 0.97, 0.27, 0.5, 0.84, 0.32, 0.53, 0.31, 0.22, 0.93],
#  [0.45, 0.51, 0.99, 0.86, 0.22, 0.62, 0.45, 0.47, 0.83, 0.88, 0.85],
#  [0.68, 0.35, 0.5, 0.06, 0.14, 0.88, 0.51, 0.84, 0.35, 0.12, 0.38],
#  [0.86, 0.64, 0.78, 0.17, 0.24, 0.69, 0.4, 0.72, 0.74, 0.14, 0.97],
#  [0.48, 0.02, 0.48, 0.09, 0.73, 0.37, 0.68, 0.34, 0.49, 0.28, 0.37],
#  [0.69, 0.25, 0.46, 0.2, 0.68, 0.73, 0.83, 0.26, 0.92, 0.74, 0.97],
#  [1.0, 0.57, 0.77, 0.55, 0.79, 0.54, 0.07, 0.89, 0.38, 0.55, 0.87]]
# num_l = 10
# num_p = 10

#solution
#allocation of lamps to plants: [1, 2, 1, 2, 2, 0, 0, 0, 0, 0] 
#best probability: 0.07124240062011918


# random small test cases :


# probs = [[0.5, 0.75, 0.25],[0.75,0.25,0.8]]
# num_p = 2
# num_l = 2
# probs = [[0.5, 0.5, 1],[0.25,0.1,0.75]]

# another test case 
# num_p = 3

# num_l = 4

# probs = [[0.84, 0.76, 0.42, 0.26, 0.51], [0.4, 0.78, 0.3, 0.48, 0.58], [0.91, 0.5, 0.28, 0.76, 0.62]]

# result: 0.596232

# Test case 2

num_p = 4

num_l = 3

probs = [[0.2,0.3,0.1,0.2], [0.7, 0.6, 0.4,0.3], [0.1,1,0.9,0.92], [0.6,0.5,0.2,0.8]]

# result: 0.288

print(best_lamp_allocation(num_p,num_l,probs))




