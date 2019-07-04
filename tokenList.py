class TokenList:

    def __init__(self,list):
        self.list = list
        self.pointer = -1
        
    def printTokenList(self):
        for item in self.list:
            print(item)

    def nextToken(self):
        self.pointer = self.pointer + 1
        self.token = self.list[self.pointer]
        return self.token
        