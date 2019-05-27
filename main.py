from fileScroller import FileScroller
from lexicalAnalysis import LexicalAnalysis
from csvTokenGenerate import generateTokenCsvFile
import sys

generateTokenCsvFile()

file = FileScroller('{}'.format(sys.argv[1]))
x = LexicalAnalysis(file)
x.switchState(0)
for item in x.tokens:
    print(item)
file.closeFile()