#SAHIL GULATI
class Word:
    
    def __init__(self,word,id): # constructor
        self.__id=id
        self.__word=word

    def __str__(self):
        return str(self.__word)+"; "+str(len(self.__word))+ "; "+ self.__id
    
    # get methods to access the private members
    def getWord(self):
        return self.__word

    def getID(self):
        return self.__id
    
