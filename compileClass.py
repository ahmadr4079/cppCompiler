from csvTokenGenerate import generateTokenCsvFile
from lexicalAnalysis import LexicalAnalysis
from fileScroller import FileScroller
from tokenList import TokenList
from syntaxAnalysis import SyntaxAnalysis
from style import Style

class Compile:
    def __init__(self,fileCode):
        file = FileScroller(fileCode)
        generateTokenCsvFile()
        self.lexicalObject = LexicalAnalysis(file)
        self.lexicalObject.switchState(0)
        self.tokenListObject = TokenList(self.lexicalObject.tokens)
        self.showCode(fileCode=fileCode)
        self.tokenListCompile()
        self.deleteDelimToken()
        print(Style.customHeader('Error and Pass Tokens during compile'))
        print('\n')
        SyntaxAnalysis(self.tokenListObject)


    def tokenListCompile(self):
        print(Style.customHeader("The token that generate from your code\n"))
        self.tokenListObject.printTokenList()
        print("-"*120)

    def showCode(self,fileCode):
        print('-'*120)
        print(Style.customHeader('Your Code\n'))
        file = open(fileCode,'r')
        for line,code in enumerate(file):
            print(Style.reset('{}) {}'.format(line+1,code)))
        print(Style.reset('-'*120))

    def deleteDelimToken(self):
        for item in self.tokenListObject.list:
            if item.tokenName == 'delim':
                self.tokenListObject.list.remove(item)
