# for w in range(0,10):
#     print(w)
#     for c in range(0,10):
#         print(" ")
#         print(w)
#         print(c)
#         for p_c in range(0,10):
#             if c == p_c:
#                 print(c)
#                 break
lst = [[1,2],[1,4],[1,2]]
target_words = [1,4]
arr = []
for words in range(0,len(lst)):
    for targets in target_words:
	    if targets in lst[words]:
		    arr.append(words)
    if len(arr) == 0:
        print(-1)
print(arr[1])