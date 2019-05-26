from fileScroller import FileScroller
from lexicalAnalysis import LexicalAnalysis
from csvTokenGenerate import generateTokenCsvFile

generateTokenCsvFile()

file = FileScroller('mainCode.txt')
x = LexicalAnalysis(file)
x.switchState(0)
file.closeFile()