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

    def matchFactor(self,tokenName,tokenNameNeed=None):
        if(self.tokenList.token.tokenName) == tokenName:
            print(Style.green('Pass ')+Style.reset('token {}'.format(self.tokenList.token)))
            self.tokenList.nextToken()
        else:
            if(tokenNameNeed):
                print(Style.red('Pass Error ')+Style.reset('{} required.'.format(tokenNameNeed)))
            else:
                print(Style.red('Pass Error ')+Style.reset('{} required.'.format(tokenName)))

    def stmt(self):
        if(self.tokenList.token.tokenName == 'eof'):
            return
        if(self.tokenList.token.attributeValue == 'if'):
            self.match('if')
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            self.stmt()
        elif(self.tokenList.token.attributeValue == 'while'):
            self.match('while')
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            self.stmt()
        elif(self.tokenList.token.attributeValue == 'for'):
            self.match('for')
            self.match('leftparantheses')
            self.optexpr()
            self.match('semicolon')
            self.optexpr()
            self.match('semicolon')
            self.optexpr()
            self.match('rightparantheses')
            self.stmt()
        elif(self.tokenList.token.attributeValue == 'leftbracket'):
            self.match('leftbracket')
            self.stmts()
            self.match('rightbracket')
        elif(self.tokenList.token.attributeValue == 'sharp'):
            self.match('sharp')
            self.matchFactor('keyword','include')
            self.match('LT')
            self.matchFactor('identifier')
            self.matchFactor('dot')
            self.matchFactor('identifier')
            self.match('GT')
            self.stmt()
        else:
            self.expr()
            self.match('semicolon')

    def optexpr(self):
        self.expr()

    def stmts(self):
        self.stmt()


    """state for increasing precedence from expr B ... F factor"""
    #grammer rule expr --> B expr_prime
    def expr(self):
        expr_state = self.B()
        if(expr_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.expr_prime()

    #grammer rule expr_prime --> = expr | epsilon
    def expr_prime(self):
        if(self.tokenList.token.attributeValue == 'EQ'):
            self.match('EQ')
            return self.expr()
        else:
            return 'OK'

    #grammer rule B --> C B_prime
    def B(self):
        B_state = self.C()
        if(B_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.B_prime()

    #grammer rule B_prime --> == B | != B | epsilon
    def B_prime(self):
        if(self.tokenList.token.attributeValue == 'ET'):
            self.match('ET')
            return self.B()
        elif(self.tokenList.token.attributeValue == 'NET'):
            self.match('NET')
            return self.B()
        else:
            return 'OK'


    #grammer rule C --> D C_prime
    def C(self):
        C_state = self.D()
        if(C_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.C_prime()

    #grammer rule C_prime --> < C | <= C | > C | >= C | epsilon
    def C_prime(self):
        if(self.tokenList.token.attributeValue == 'LT'):
            self.match('LT')
            return self.C()
        elif(self.tokenList.token.attributeValue == 'LE'):
            self.match('LE')
            return self.C()
        elif(self.tokenList.token.attributeValue == 'GT'):
            self.match('GT')
            return self.C()
        elif(self.tokenList.token.attributeValue == 'GE'):
            self.match('GE')
            return self.C()
        else:
            return 'OK'

    #grammer rule D --> E D_prime
    def D(self):
        D_state = self.E()
        if(D_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.D_prime()

    #grammer rule D_prime --> << D | >> D | epsilon
    def D_prime(self):
        if(self.tokenList.token.attributeValue == 'SHL'):
            self.match('SHL')
            return self.D()
        elif(self.tokenList.token.attributeValue == 'SHR'):
            self.match('SHR')
            return self.D()
        else:
            return 'OK'

    #grammer rule E --> F E_prime
    def E(self):
        E_state = self.F()
        if(E_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.E_prime()

    #grammer rule E_prime --> + E | - E | epsilon
    def E_prime(self):
        if(self.tokenList.token.attributeValue == 'addition'):
            self.match('addition')
            return self.E()
        elif(self.tokenList.token.attributeValue == 'subtraction'):
            self.match('subtraction')
            return self.E()
        else:
            return 'OK'

    #grammer rule F --> factor F_prime
    def F(self):
        F_state = self.factor()
        if(F_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.F_prime()

    #grammer rule F_prime --> * F | / F | epsilon
    def F_prime(self):
        if(self.tokenList.token.attributeValue == 'multiplication'):
            self.match('multiplication')
            return self.F()
        elif(self.tokenList.token.attributeValue == 'division'):
            self.match('division')
            return self.F()
        else:
            return 'OK'

    #grammer rule factor --> identifier | number | (expr)
    def factor(self):
        if(self.tokenList.token.tokenName == 'identifier'):
            self.matchFactor('identifier')
            return 'OK'
        elif(self.tokenList.token.tokenName == 'number'):
            self.matchFactor('number')
            return 'OK'
        elif(self.tokenList.token.tokenName == '('):
            self.match('(')
            self.expr()
            self.match(')')
            return 'OK'
        else:
            return 'ERROR'
