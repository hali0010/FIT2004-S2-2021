#Student name: Haider Ali
#Student ID: 31371337
import time
import random


# Task 1 Integer radix sort

def countSort(num_list, exp, b):  # Takes a number list, an exponent and base as parameters where num_list is the array, exp is the exponent and b is the base. Time complexity is O(n+b) where n is the number of elements in the list and
    # and b is the base. exp is the column for the digit we are sorting.
    number_of_items = len(num_list)  # the number of items in the list
    output = [0] * number_of_items  # the list that is used to sort the original list
    item_c = [0] * (
        b)  # the list that stores the count of that particular digit upto base (for example 0-9 for base 10)

    for items in range(0, number_of_items):  # complexity O(n)
        index = (num_list[items] / exp) # calculates the digit to add to the count array
        item_c[int(index % b)] += 1 # increments the value of the occurences of that digit

    for digit in range(1, b):  # Complexity O(b)
        item_c[digit] += item_c[digit - 1] # adds the existing value of the previous count of digits to the newer digit count

    i = number_of_items - 1
    while i >= 0:  # complexity O(n)
        index = (num_list[i] / exp)
        output[item_c[int(index % b)] - 1] = num_list[i]
        item_c[int(index % b)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(num_list)):  # complexity O(n)
        num_list[i] = output[i]
    return num_list

# countSort takes 3 parameters as arguments which are: the list to sort, the exponent of the current digit being sorted and the base of the list


def num_rad_sort(num_list, b):  # takes a numerical list and base as parameters where num_list is the array and b is the base
    # time complexity is O((n+b)*log(M)) where n is the number of elements in the list and
    # b is the base and M is the maximum element in the list
    maximum = max(num_list)

    exp = 1  # sets the exponent to 1 for the rightmost first digit
    while maximum / exp > 0:  # complexity O(log(M))
        countSort(num_list, exp, b)  # passes num_list, exponent and base as arguments to countSort
        exp *= b  # moves to the next digit( towards the left ) (for example, goes from 2^1 to 2^2 if base is 2)

    return num_list


# Task 2 Timing bases
def base_timer(num_list,base_list):
    n = len(base_list)
    time_taken = [0] * n
    for i in range(0, n):
        time_start = time.time()
        num_rad_sort(num_list, base_list[i])
        time_stop = time.time()
        time_taken[i] = time_stop - time_start
    out = [(base_list[i], time_taken[i]) for i in range(0, n)]
    return out

# random.seed("FIT2004S22021")
# data1 = [random.randint(0,2**25) for _ in range(2**15)]
# data2 = [random.randint(0,2**25) for _ in range(2**16)]
# bases1 = [2**i for i in range(1,23)]
# bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]
# y1 = base_timer(data1, bases1)
# y2 = base_timer(data2, bases1)
# y3 = base_timer(data1, bases2)
# y4 = base_timer(data2, bases2)
# print(y1)
# print(y2)
# print(y3)
# print(y4)

# Task 3 Interest Groups
def countSort_letters(word_list, size, column, base, maximum_wlen):
    output = [0] * size
    character_count = [0] * (base + 1)
    minimum_base = ord('a')

    for words in word_list:
        character = ord(words[column]) - minimum_base if column < len(words) else 0
        if character == -65 : # checks if there is a space
            character = 27    # if there is a space then saved it as the last character
        character_count[character] += 1

    for letter in range(len(character_count) - 1):
        character_count[letter + 1] += character_count[letter]

    for words in reversed(word_list):
        character = ord(words[column]) - minimum_base if column < len(words) else 0
        if character == -65 : # checks if there is a space that needs to be added
            character = 27
        output[character_count[character] - 1] = words
        character_count[character] -= 1

    return output


def radixSort_letters(word_list):  # same complexity as numerical radix sort
    maximum_column = len(max(word_list, key=len,default=[" "]))  # finds out the max letters of words in the word list
    for column in range(maximum_column - 1, -1, -1):
        word_list = countSort_letters(word_list, len(word_list), column, 27, maximum_column)

    return word_list


def words_with_anagrams(list1, list2):  # takes list1 and list2 as parameters. list1 contains the words which we have to check and list2 is used to check for what anagarams can be made in word_list.
    checklist = [[]] * len(list2)   # new list for deconstructing list2 into characters
    list_to_store = [[]] * len(list1)  # new list to store the deconstructed words in list1
    output = [] * len(list1)  # list to output the result
    count = [0] * len(list1) # something nifty to store which words in list 1 have anagrams in list 2
    for i in range(0,len(list1)):
        list_to_store[i] = list(radixSort_letters(list1[i]))  # deconstructs each sorted word into its characters 
        #runs in O(nlog(M)) where n is the number of words in the list. M is the largest value of the character in alphabet among the words
    for i in range(0, len(list2)):
        checklist[i] = list(radixSort_letters(list2[i]))  # deconstructs each list2 word into its characters

    for i in range(0,len(list2)):
        for j in range(0, len(list1)):
            if list_to_store[j] == checklist[i]:  # checks for anagrams O(comp(length of longest word in list1 and list 2))
                count[j] = 1
    for j in range(0, len(list1)):
            if count[j] == 1:
                output += [list1[j]]
    return output

def interest_groups(data):  # takes data as parameters. contains the names and each distinct set of liked things 
    namelist = [ i for i, j in data ]  # the list that contains the names of the people
    list2 = [ j for i, j in data ]  # the list that contains the distinct set of liked things
#   sorted_names = radixSort_letters(list1)  # sorts namelist into alphabetical order
    checklist = [[]] * len(list2)   # new list for deconstructing set of liked things into characters
    list_to_store = [[]] * len(namelist)  # new list to store the deconstructed words in the names of people
    output = [[ ] * len(namelist)] * len(list2)  # list to output the result
    for i in range(0,len(namelist)):
        list_to_store[i] = list(radixSort_letters(namelist[i]))  # deconstructs each name into its characters
    for i in range(0, len(list2)):
        checklist[i] = list(radixSort_letters(list2[i]))  # deconstructs each distinct thing into its characters

    for i in range(0,len(list2)):
        for j in range(0, len(namelist)):
            if checklist[i] == list_to_store[j]:  # checks for anagarams
                output[i] = output[i]+[namelist[j]]  #adds the sorted word to the output list if anagaram is foun. runs in
                # O(nxw) where n is the number of elements in char_set_list and w is the number of words in word_list

    return output


data = [("nuka", ["birds", "napping"]),
("hadley", ["napping birds", "nash equilibria"]),
("yaffe", ["rainy evenings", "the colour red", "birds"]),
("laurie", ["napping", "birds"]),
("kamalani", ["birds", "rainy evenings", "the colour red"])]


print(interest_groups(data))