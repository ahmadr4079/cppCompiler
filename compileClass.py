from csvTokenGenerate import generateTokenCsvFile
from lexicalAnalysis import LexicalAnalysis
from fileScroller import FileScroller
from tokenList import TokenList
from syntaxAnalysis import SyntaxAnalysis

class Compile:
    def __init__(self,fileCode):
        file = FileScroller(fileCode)
        generateTokenCsvFile()
        self.lexicalObject = LexicalAnalysis(file)
        self.lexicalObject.switchState(0)
        self.tokenListObject = TokenList(self.lexicalObject.tokens)
        self.tokenListCompile()
        SyntaxAnalysis(self.tokenListObject)
        
    
    def tokenListCompile(self):
        print("the token that generate from your code")
        print("-"*80)
        self.tokenListObject.printTokenList()
        print("-"*80)
