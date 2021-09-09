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
    # function best_lamp_allocation runs in O(PL^2).
    # function best_lamp_allocation takes in 3 arguments. num_p where num_p is the total number of plants, num_l where num_l is the number of lamps we can use including 0 lamps, and 
    # probs that is a list of list containing all the probabilities such that probs[i][j] represents probability plant[i] will have when lamp[j] is used on it
    return memo_greenhouse[num_p-1][num_l] # best_lamp_allocation returns the maximum probability you can get when using num_l lamps for num_p plants





