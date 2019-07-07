

class Token:
    def __init__(self,tokenName,attributeValue = None,tokenId = None,line=None):
        self.tokenId = tokenId
        self.tokenName = tokenName
        self.attributeValue = attributeValue
        self.line = line
    def __repr__(self):
        return '<{},{},{},{}>'.format(self.tokenId,self.tokenName,self.attributeValue,self.line)
