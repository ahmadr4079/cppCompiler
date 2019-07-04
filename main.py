from fileScroller import FileScroller
from lexicalAnalysis import LexicalAnalysis
from csvTokenGenerate import generateTokenCsvFile
from tokenList import TokenList
import sys

generateTokenCsvFile()

file = FileScroller('{}'.format(sys.argv[1]))
x = LexicalAnalysis(file)
x.switchState(0)
tokenList = TokenList(x.tokens)
tokenList.printTokenList()
file.closeFile()