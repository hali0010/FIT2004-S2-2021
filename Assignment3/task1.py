class Node:
    """
    The Node class for the Trie
    """

    def __init__(self, size=27):
        self.link = [None] * size

class Trie:
    def __init__(self, text):
        """
        Build a trie with strings in text list
        Precondition: Strings should not be empty
        Arguments:          text = List of strings
        Time complexity:    Best case = O(T) where T is the total number of characters of all the strings
                            Worst case = O(T) where T is the total number of characters of all the strings
        Space complexity:   O(T) where T is the total number of characters of all the strings
        Aux space complexity: None
        Return: None
        """
        self.root = Node() # create a root node for the trie

        # Insert each string in the text into the trie
        for word in text:
            current = self.root
            # Go through each character in the string and check if the node has the appropriate index value.
            # Make a new node if character not found and refer to it in the array (link)
            for char in word:
                index = ord(char) - 97 + 1  # terminal needs to be in index 0 so add 1
                if current.link[index] is not None: # the child exists. go to the child branch
                    current = current.link[index]                  
                else:
                    current.link[index] = Node() # creates a new child node at the current node if child node doesnt exist
                    current = current.link[index]
            index = 0
            # Make the terminal node. Traverse until None is found and make a node that signifies end of string
            if current.link[index] is not None:
                current = current.link[index]
            else:
                current.link[index] = Node()
                current = current.link[index]
                

