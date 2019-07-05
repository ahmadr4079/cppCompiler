class TokenList:

    def __init__(self,list):
        self.list = list
        self.pointer = 0
        self.maxListIndex = len(list)
        self.token = list[0]

    def printTokenList(self):
        for item in self.list:
            print(item)

    def nextToken(self):
        self.pointer = self.pointer + 1
        if(self.pointer < self.maxListIndex):
            self.token = self.list[self.pointer]
            return self.token
