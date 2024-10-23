from DictionaryBST import *


print("\n Welcome to Dictionary Application 3")
print("======================================\n")


# instantiate new BST database
dict = DictionaryBST()
# load dictionaries into BST
dict.load("english")
dict.load("french")
dict.load("spanish")

# spell checker
filename=input("Enter file name to spell check: ")
dict.spell_check(filename+".txt")
print()
