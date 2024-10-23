#SAHIL GULATI
from Word import *

class Node:
    def __init__(self, items, index=0):
        self.items = items  #Store the Word object 
        self.index = index     
        self.left = None    #Left child
        self.right = None   #Right child

    
    def __str__(self):
        return str(self.items)
    
    
class DictionaryBST:
    def __init__(self):
        self.root = None    #Root node of the BST
        self.__size = 0     #Keeping track of number of nodes in the tree
        self.__max_level = 0       #keeping track of number of levels in the tree

    def load(self, filename):   
        dictionary_id = filename.split('.')[0]  # Extracting the dictionary name without extension(i.e txt)
        with open(f"{filename}.txt", "r",encoding='utf-8') as file:
            for word in file:
                self.insert(word.strip(), dictionary_id)    #Inserting every word into the BST

    def insert(self, word, dictionary_id):
        items = Word(word, dictionary_id)  # Create a Word object
        if self.root is None:
            self.root = Node(items)
            self.__size += 1    
            self.__max_level = 1    #Root is at level 1
        else:
            self.__recInsert(self.root, items, 0)    #Initiating recurssion 

    def __recInsert(self, current_node, items, current_level):
        if items.getWord() < current_node.items.getWord():  # Insert on the left if it's less than the current node's word
            if current_node.left is None:   
                current_level += 1  
                current_node.left = Node(items, 2 * current_node.index + 1)
                self.__size += 1
                if current_level > self.__max_level:
                    self.__max_level = current_level    #setting the max level
            else:
                self.__recInsert(current_node.left, items, current_level+1)
        else:   # Insert on the right if it's less than the current node's word
            if current_node.right is None:
                current_level += 1
                current_node.right = Node(items, 2 * current_node.index + 2)
                self.__size += 1
                if current_level > self.__max_level:
                    self.__max_level = current_level
            else:
                self.__recInsert(current_node.right, items, current_level+1)

    def getSize(self):
        return self.__size  #gives the number of nodes in the BST

    def getMaxLevel(self):
        return self.__max_level #fives the maximum levels of the BST

    def extractInOrder(self):
        result = []
        self.__inOrderTraversal(self.root, result)  #Sets up in order traversal of the BST 
        return result

    def __inOrderTraversal(self, node, result):
        if node:
            self.__inOrderTraversal(node.left, result)  #visiting the left subtree
            result.append(node.items)   # Displaying the current node 
            self.__inOrderTraversal(node.right, result) #visiting the right subtree

    def show(self, display_type):
        if display_type == 'word':
            print("The BSTree using type -word- looks like:")
            self.__showWord(self.root, 0)
        elif display_type == 'id':
            print("The BSTree using type -id- looks like:")
            self.__showID(self.root, 0)
        elif display_type == 'index':
            print("The BSTree using type -index- looks like:")
            self.__showIndex(self.root, 0)

    def __showWord(self, node, level):
        if node:
            self.__showWord(node.right, level + 1)
            print('  ' * 4 * level, node.items.getWord())   #Printing the word at the current node
            self.__showWord(node.left, level + 1)

    def __showID(self, node, level):
        if node:
            self.__showID(node.right, level + 1)
            print('  ' * 4 * level, node.items.getID()) #Printing the ID at the current noed
            self.__showID(node.left, level + 1)

    def __showIndex(self, node, level):
        if node:
            self.__showIndex(node.right, level + 1)
            print('  ' * 4 * level, node.index) #Printing the index at the current node
            self.__showIndex(node.left, level + 1)

    
    def search(self, data): #Searching for a word(data) in the BST
        current_node = self.root
        while current_node is not None:
            # Compare the search data with the current node's word
            if data == current_node.items.getWord():
                return current_node #If the word is found
            elif data < current_node.items.getWord():
                current_node = current_node.left    #Searching the left subtree
            else:
                current_node = current_node.right   #Searching the right subtree
        return None
    
    def spell_check(self, filename):
        punc = "’!()-[]{};:’\"\\,<>./?@#$%^&*_~’"   #Punctuations to remove

        with open(filename, 'r',encoding='utf-8') as file:
            for line in file:
                words = line.split()
                checked_words = []  #List to hold spell checked words
                line_ids = []   #List to hold their IDs

                for word in words:
                    # removing punctuation and converting to lowercase
                    clean_word = word.lower().lstrip(punc).rstrip(punc)
                    
                    # Search for the cleaned word in the dictionary
                    found_node = self.search(clean_word)
                    
                    if found_node:
                        # Word found: keep the original word and record its ID
                        checked_words.append(word)
                        line_ids.append(f"-{found_node.items.getID()}-")
                    else:
                        # Word not found: wrap the original word in parentheses and record 'no ID'
                        checked_words.append(f"({word})")
                        line_ids.append("-no ID-")
                
                # Print the checked line
                print(' '.join(checked_words))
                
                # Print the IDs line
                print(f"[{''.join(line_ids)}]")


