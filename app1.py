from DictionaryBST import *

print("\n Welcome to Dictionary Application 1")
print("======================================\n")

# instantiate new BST database
dict = DictionaryBST()

# load dictionaries into BST
while True:
    name=input("Enter dictionary name (english,french,spanish,short,tiny,etc.): ")
    if name =="": break
    dict.load(name) # add dictionary to the BST

# display some info
print("\nThe size of the BST is "+str(dict.getSize())+" with "+str(dict.getMaxLevel())+" level(s)")

if dict.getSize()<=50: # small size dictionary only
    # display BST in order 
    mylist=dict.extractInOrder() # this list of Word objects would be automatically sorted
    print("\nDisplay in order:")
    for w in mylist: print(w)
    
    # display some tree structures
    dict.show("word")
    dict.show("id")
    dict.show("index")
