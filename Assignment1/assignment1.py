import time
import random


# Task 1 Integer radix sort

def countSort(num_list, exp, b):  # Takes a number list, an exponent and base as parameters where num_list is the array, exp is the exponent and b s the base. Time complexity is O(n+b) where n is the number of elements in the list and
    # and b is the base. exp is the column for the digit we are sorting.
    number_of_items = len(num_list)  # the number of items in the list
    output = [0] * number_of_items  # the list that is used to sort the original list
    item_c = [0] * (
        b)  # the list that stores the count of that particular digit upto base (for example 0-9 for base 10)

    for items in range(0, number_of_items):  # complexity O(n)
        index = (num_list[items] / exp)
        item_c[int(index % b)] += 1

    for digit in range(1, b):  # Complexity O(b)
        item_c[digit] += item_c[digit - 1]

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

random.seed("FIT2004S22021")
data1 = [random.randint(0,2**25) for _ in range(2**15)]
data2 = [random.randint(0,2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1,23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]
y1 = base_timer(data1, bases1)
y2 = base_timer(data2, bases1)
y3 = base_timer(data1, bases2)
y4 = base_timer(data2, bases2)
print(y1)
print(y2)
print(y3)
print(y4)
nums = [43, 101, 22, 27, 5, 50, 15]
print(num_rad_sort(nums, 4))


