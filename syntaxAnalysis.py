from style import Style

class SyntaxAnalysis:

    def __init__(self,tokenList):
        self.tokenList = tokenList
        self.stmt()

    def match(self,tokenAttributeValue):
        if(self.tokenList.token.attributeValue) == tokenAttributeValue:
            print(Style.green('Match ')+Style.reset('token {} - {}'.format(self.tokenList.token,tokenAttributeValue)))
            self.tokenList.nextToken()
        else:
            print(Style.red('Syntax Error ')+Style.reset('{} required.'.format(tokenAttributeValue)))

    def stmt(self):
        self.tokenList.nextToken()
        if(self.tokenList.token.tokenName == 'eof'):
            return
        if(self.tokenList.token.attributeValue == 'if'):
            self.match('if')
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            self.stmt()
        else:
            self.expr()
            self.match('semicolon')

    def expr(self):
        expr_state = self.term()
        if(expr_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.expr_prime()

    def expr_prime(self):
        if(self.tokenList.token.attributeValue == 'addition'):
            self.match('addition')
            return self.expr()
        elif(self.tokenList.token.attributeValue == 'subtraction'):
            self.match('subtraction')
            return self.expr()
        else:
            return 'OK'

    def term(self):
        term_state = self.factor()
        if(term_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.term_prime()

    def term_prime(self):
        if(self.tokenList.token.attributeValue == 'multiplication'):
            self.match('multiplication')
            return self.term()
        elif(self.tokenList.token.attributeValue == 'division'):
            self.match('division')
            return self.term()
        else:
            return 'OK'

    def factor(self):
        if(self.tokenList.token.tokenName == 'identifier'):
            print(Style.green('Pass ')+Style.reset('token {}'.format(self.tokenList.token)))
            self.tokenList.nextToken()
            return 'OK'
        elif(self.tokenList.token.tokenName == 'number'):
            print(Style.green('Pass ')+Style.reset('token {}'.format(self.tokenList.token)))
            self.tokenList.nextToken()
            return 'OK'
        else:
            return 'ERROR'
