

class Token:
    def __init__(self,tokenName,attributeValue = None,tokenId = None):
        self.tokenId = tokenId
        self.tokenName = tokenName
        self.attributeValue = attributeValue
    def __repr__(self):
        return '<{},{},{}>'.format(self.tokenId,self.tokenName,self.attributeValue)