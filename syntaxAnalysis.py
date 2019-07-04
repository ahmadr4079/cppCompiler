class SyntaxAnalysis:
    def __init__(self,tokenList):
        self.tokenList = tokenList
        self.goal()
    def goal(self):
        self.tokenList.nextToken()
        if (self.expr() == 'ERROR' or self.tokenList.token.tokenName != 'eof'):
            print('error : unexpedted {}'.format(self.tokenList.token))
    def expr(self):
        if (self.term() == 'ERROR'):
            return 'ERROR'
        else:
            return self.expr_prime()
    def expr_prime(self):
        if(self.tokenList.token.attributeValue == 'addition'):
            print('expected {} token'.format(self.tokenList.token))
            self.tokenList.nextToken()
            return self.expr()
        elif(self.tokenList.token.attributeValue == 'subtraction'):
            print('expected {} token'.format(self.tokenList.token))
            self.tokenList.nextToken()
            return self.expr()
        else:
            return 'OK'
    def term(self):
        if (self.factor() == 'ERROR'):
            return 'ERROR'
        else:
            return 'OK'
    def term_prime(self):
        if(self.tokenList.token.attributeValue == 'multiplication'):
            print('expected {} token'.format(self.tokenList.token))
            self.tokenList.nextToken()
            return self.expr()
        elif(self.tokenList.token.attributeValue == 'division'):
            print('expected {} token'.format(self.tokenList.token))
            self.tokenList.nextToken()
            return self.expr()
        else:
            return 'OK'
    def factor(self):
        if(self.tokenList.token.tokenName == 'identifier'):
            print('expected {} token'.format(self.tokenList.token))
            self.tokenList.nextToken()
            return 'OK'
        elif(self.tokenList.token.tokenName == 'number'):
            print('expected {} token'.format(self.tokenList.token))
            self.tokenList.nextToken()
            return 'OK'
        else:
            return 'ERROR'
