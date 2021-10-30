# student Name: Haider Ali
# student ID: 31371337
# this is my incomplete attempt at A4.
# reference : exampleGraphClass.py from the EdForums at https://edstem.org/au/courses/6067/discussion/619902
class WordGraph:
	def __init__(self, listOfWords):
		self.wordList = listOfWords # something to retain the original word list that is passed in
		self.num_vertices = len(listOfWords) # the number of words (vertices)
		self.adj_list = [[] for _ in range(len(listOfWords))] # adjacency list to store which word is connected to what word
		nc = len(listOfWords[0]) # the number of characters in each word
		for prev_words in range(0,(self.num_vertices)): # go through every word in the listOfWords
			for words in range (0,self.num_vertices): # compare with every other word
				char_found = 0
				if prev_words!=words: # skip the same word
					for char_in_each_word in range(0,nc):
						for char_in_prev_word in range(0,nc):
							if listOfWords[prev_words][char_in_prev_word] == listOfWords[words][char_in_each_word]: # checks each character of the word with words that have been passed
								char_found += 1
								break # breaks the loop to check for other characters
				if char_found >= 2:
					self.adj_list[prev_words].append(words) # makes a new edge for the word thats being added
	# Task 1 Word Ladder
	def best_start_word(self,target_words):
		arr = []
		for words in range(0,len(self.adj_list)):
			for targets in target_words:
				if targets in self.adj_list[words]:
					arr.append(words)
		if len(arr) == 0:
			return (-1)
		return arr[0]
	# best_start_word takes in one argument as a parameter. target_words is a list of the indices of the words that need to be checked.
	# best_start_word returns the index of the word in the initial wordlist which is at the center of the list of targets
	# This hasnt been completely implemented as I was having issues constructing my graph in python ;-; 
	# Time complexity of the given function is O(W*T) where W is the number of words in the graph and T is the number of targets in the list of target_words
		
				    