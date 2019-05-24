class FileScroller:
    def __init__(self,filename):
        self.fp = open(filename,'r')
    def nextChar(self):
        c = self.fp.read(1)
        if not c:
            return 'eof'
        else:
            return c
    def previousChar(self):
        self.fp.seek(self.fp.tell()-1)
    def closeFile(self):
        self.fp.close()