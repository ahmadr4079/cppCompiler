class SyntaxAnalysis:
    def __init__(self,tokenList):
        self.tokenList = tokenList
        self.goal()
    def goal(self):
        self.tokenList.nextToken()
        if (self.expr() == 'ERROR' or self.tokenList.token.attributeValue == 'eof'):
            print('unexpedted : {}'.format(self.tokenList.token))
            return 'ERROR'
    def expr(self):
        if (self.term() == 'ERROR'):
            return 'ERROR'
        else:
            return self.expr_prime()
    def expr_prime(self):
        if(self.tokenList.token.attributeValue == 'addition'):
            self.tokenList.nextToken()
            return self.expr()
        elif(self.tokenList.token.attributeValue == 'subtraction'):
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
            self.tokenList.nextToken()
            return self.expr()
        elif(self.tokenList.token.attributeValue == 'division'):
            self.tokenList.nextToken()
            return self.expr()
        else:
            return 'OK'
    def factor(self):
        if(self.tokenList.token.tokenName == 'identifier'):
            self.tokenList.nextToken()
            return 'OK'
        elif(self.tokenList.token.tokenName == 'number'):
            self.tokenList.nextToken()
            return 'OK'
        else:
            return 'ERROR'
