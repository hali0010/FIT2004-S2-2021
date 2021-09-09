# Student Name: Haider Ali
# Student ID: 31371337 

# Task 1 Game Master

def count_encounters(target_difficulty,monster_list):
    monster_difficulties = [ j for i, j in monster_list]
    memo_monster = [[0] * (target_difficulty + 1) for x in range(len(monster_difficulties) + 1)] # memo for storing all the number of different sets of 'x' monsters for 0...target_difficulties

    for monsters in range(0,len(monster_difficulties)+1):
        memo_monster[monsters][0] = 1  # theres a way to get 0 difficulty (by choosing none of the monsters).
    
    for i in range(1, len(monster_difficulties) + 1): # the subproblem for this problem is that memo[monster][difficulty] = memo[monster -1][difficulty] + memo[monster][difficulty - prev difficulty](since we need to take the remaining amount into account as well)
        for j in range(1, target_difficulty + 1):
            if monster_difficulties[i - 1] > j:  # Cannot pick the highest coin:
                memo_monster[i][j] = memo_monster[i - 1][j] 
            else:  # Pick the highest coin:
                memo_monster[i][j] = memo_monster[i - 1][j] + memo_monster[i][j - monster_difficulties[i - 1]] 
    # function count_encounters runs in O(DM) where M is the number of monsters(length of monster_list) and D is the target difficulty
    # function count_encounters takes in 2 arguments. target_difficulty that is the total target difficulty to find and monster_list which is a list of tuples consisting of the type of monster and the difficulty of that monster
    return memo_monster[len(monster_difficulties)][target_difficulty] # count_encounters will return the number of different sets of monsters whose difficulties sum to target_difficulty

# Task 2 Greenhouse

def best_lamp_allocation(num_p , num_l,probs):
    memo_greenhouse = [[0 for i in range(num_l+1)] for j in range(num_p)]  # creates a new memo to store the probability of using a total of '0..num_l' number of lamps(add +1 since we are also including 0 lamps ) for 0..num_p number of plants
    for l in range(0,num_l+1):
        memo_greenhouse[0][l] = probs[0][l] # we need to populate the row[0] of the memo with the probability of using the first plant(plant[0]) since its the only one we can pick from plants 0..0 without taking into any previous plants using any number of lamps
    for plants in range(1,num_p):    # since we have already set the memo for plant0, we start to fill the memo from plant 1 upto num_p
        for lamps in range(0,num_l+1): # we need to find the optimum number of lamps for each plant
            if lamps>0: # the subproblem of this problem is that memo[plants][lamps] = max(probs[plant][lamps]*memo[plant-1][0],probs[plant][lamps-1]*memo[plant-1][1]...,probs[plant][lamps-l]*memo[plant-1][l], memo[plants][lamps-1])
                temp = [0]*(lamps+1) # creates a list for storing all the possible probabilities for a plant[i] when we assign it 'n'(lamps) number of lamps. Since we are considering 0 as well we need to add 1 to include the last lamp
                for l in range(0,lamps+1): # we need a way to calculate all the probabilities of probs[plant][lamps]*memo[plant-1][0],probs[plant][lamps-1]*memo[plant-1][1],probs[plant][lamps-2]*memo[plant-1][2]... upto probs[plant][lamps-l]*memo[plant-1][l]
                    temp[l]= probs[plants][lamps - l] * memo_greenhouse[plants -1][l] # we calculate the probabilites and store them into a temp list 
                maxP = max(temp) # we take the maximum probability from the list 
                maxP = max(memo_greenhouse[plants][lamps-1],maxP) # we compare the maximum probability of the list with the last maximum probability already calculated for 'plant'
                memo_greenhouse[plants][lamps] = maxP # we update the memo to include the new maximum probability for memo[plants][lamps]
            else: # this runs if we have no lamps to use i.e lamps = 0
                memo_greenhouse[plants][lamps] = probs[plants][lamps]*memo_greenhouse[plants -1][lamps] # sets the memo[plants][lamps] to probs[plants][lamps]*memo[plants -1][0] because we have 0 number of lamps available to use
    # function best_lamp_allocation runs in O(PL^2). where P is the number of plants(num_p) L is the number of lamps(num_l)
    # function best_lamp_allocation takes in 3 arguments. num_p where num_p is the total number of plants, num_l where num_l is the number of lamps we can use including 0 lamps, and 
    # probs that is a list of list containing all the probabilities such that probs[i][j] represents probability plant[i] will have when lamp[j] is used on it
    return memo_greenhouse[num_p-1][num_l] # best_lamp_allocation returns the maximum probability you can get when using num_l lamps for num_p plants


