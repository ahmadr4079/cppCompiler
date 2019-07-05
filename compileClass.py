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
        self.showCode(fileCode=fileCode)
        self.tokenListCompile()
        SyntaxAnalysis(self.tokenListObject)


    def tokenListCompile(self):
        print("The token that generate from your code\n")
        self.tokenListObject.printTokenList()
        print("-"*80)

    def showCode(self,fileCode):
        file = open(fileCode,'r')
        print('Your code that written in {} :\n'.format(fileCode))
        print(file.read())
        print('-'*80)
