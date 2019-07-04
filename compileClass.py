from csvTokenGenerate import generateTokenCsvFile
from lexicalAnalysis import LexicalAnalysis
from fileScroller import FileScroller
from tokenList import TokenList

class Compile:
    def __init__(self,fileCode):
        file = FileScroller(fileCode)
        generateTokenCsvFile()
        self.lexicalObject = LexicalAnalysis(file)
        self.lexicalObject.switchState(0)
        self.tokenListObject = TokenList(self.lexicalObject.tokens)
    
    def tokenListCompile(self):
        self.tokenListObject.printTokenList()
