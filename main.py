from fileScroller import FileScroller
from lexicalAnalysis import LexicalAnalysis

file = FileScroller('code.txt')
x = LexicalAnalysis(file)
x.switchState(0)
file.closeFile()