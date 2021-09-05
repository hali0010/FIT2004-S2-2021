# Student Name: Haider Ali
# Student ID: 31371337 

# Task 1 Game Master
# count_aux has been modified from https://www.reddit.com/r/learnprogramming/comments/83vrpb/print_all_combination_of_coin_change_problem_i_am/
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


target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))
print(count_aux([1,2,3],5))