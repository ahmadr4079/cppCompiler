from style import Style
import re

class SyntaxAnalysis:

    def __init__(self,tokenList):
        self.tokenList = tokenList
        self.stmt()

    def match(self,tokenAttributeValue):
        if(self.tokenList.token.attributeValue) == tokenAttributeValue:
            print(Style.green('Line({})-Match '.format(self.tokenList.token.line))+'token ({} {} {}) '.format(self.tokenList.token,Style.green('with'),tokenAttributeValue))
            self.tokenList.nextToken()
        else:
            print(Style.red('Line({})-Syntax Error '.format(self.tokenList.token.line))+Style.reset('{} required.'.format(tokenAttributeValue)))

    def matchFactor(self,tokenName,tokenNameNeed=None):
        if(self.tokenList.token.tokenName) == tokenName:
            print(Style.green('Line({})-Pass '.format(self.tokenList.token.line))+Style.reset('token {}'.format(self.tokenList.token)))
            self.tokenList.nextToken()
        else:
            if(tokenNameNeed):
                print(Style.red('Line({})-Pass Error '.format(self.tokenList.token.line))+Style.reset('{} required.'.format(tokenNameNeed)))
            else:
                print(Style.red('Line({})-Pass Error '.format(self.tokenList.token.line))+Style.reset('{} required.'.format(tokenName)))

    def stmt(self):
        #grammer rule stmt --> eof
        if(self.tokenList.token.tokenName == 'eof'):
            return
        #grammer rule stmt --> if ( expr ) stmt
        if(self.tokenList.token.attributeValue == 'if'):
            self.match('if')
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            self.match('leftbracket')
            self.stmt()
            self.match('rightbracket')
            self.stmt()
        #grammer rule stmt --> while ( expr ) stmt
        elif(self.tokenList.token.attributeValue == 'while'):
            self.match('while')
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            self.stmt()
        #grammer rule stmt --> for ( optexpr; optexpr; optexpr ) stmt
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
        #grammer rule stmt --> { stmts } stmts
        elif(self.tokenList.token.attributeValue == 'leftbracket'):
            self.match('leftbracket')
            self.stmts()
            self.match('rightbracket')
            self.stmt()
        #grammer rule stmt --> # include < identifier .identifier? > stmt
        elif(self.tokenList.token.attributeValue == 'sharp'):
            self.match('sharp')
            self.match('include')
            self.match('LT')
            self.matchFactor('identifier')
            if(self.tokenList.token.tokenName == 'dot'):
                self.matchFactor('dot')
                self.matchFactor('identifier')
            self.match('GT')
            self.stmt()
        #grammer rule stmt --> do stmt while ( expr ); stmt
        elif(self.tokenList.token.attributeValue == 'do'):
            self.match('do')
            self.stmt()
            self.match('while')
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            self.match('semicolon')
            self.stmt()
        #grammer rule stmt --> type identifier ( params ) stmt
        #grammer rule stmt --> type identifier [ number ]; stmt
        #grammer rule stmt --> type identifier = expr; stmt
        elif(re.search('int|float|double',self.tokenList.token.attributeValue)):
            self.match(self.tokenList.token.attributeValue)
            self.matchFactor('identifier')
            if(self.tokenList.token.attributeValue == 'leftparantheses'):
                self.match('leftparantheses')
                self.params()
                self.match('rightparantheses')
                self.stmt()
            elif(self.tokenList.token.attributeValue == 'leftsqurebracket'):
                self.match('leftsqurebracket')
                self.matchFactor('number')
                self.match('rightsqurebracket')
                if(self.tokenList.token.attributeValue == 'EQ'):
                    self.match('EQ')
                    self.match('leftbracket')
                    self.arrayNumber()
                    self.match('rightbracket')
                    self.match('semicolon')
                    self.stmt()
                else:
                    self.match('semicolon')
                    self.stmt()
            elif(self.tokenList.token.attributeValue == 'EQ'):
                self.match('EQ')
                self.expr()
                self.match('semicolon')
                self.stmt()
            else:
                self.match('semicolon')
                self.stmt()
        #grammer rule stmt -->  void identifier ( params ) stmt
        elif(self.tokenList.token.attributeValue == 'void'):
            self.match('void')
            self.matchFactor('identifier')
            self.match('leftparantheses')
            self.params()
            self.match('rightparantheses')
            self.stmt()
        #grammer rule stmt --> return expr ; stmt
        elif(self.tokenList.token.attributeValue == 'return'):
            self.match('return')
            self.expr()
            self.match('semicolon')
            self.stmt()
        #grammer rule stmt --> identifier = expr ; stmt
        elif(self.tokenList.token.tokenName == 'identifier'):
            self.matchFactor('identifier')
            self.match('EQ')
            self.expr()
            self.match('semicolon')
            self.stmt()
        #grammer rule stmt --> cout coutState stmt
        elif(self.tokenList.token.attributeValue == 'cout'):
            self.match('cout')
            self.coutState()
            self.stmt()
        #grammer rule stmt --> cin cinState stmt
        elif(self.tokenList.token.attributeValue == 'cin'):
            self.match('cin')
            self.cinState()
            self.stmt()
        else:
            print(Style.red('Syntax Error'))

    def optexpr(self):
        self.expr()

    def stmts(self):
        self.stmt()
    #grammer rule params --> type identifier , params
    def params(self):
        if(re.search('int|float|double',self.tokenList.token.attributeValue)):
            self.match(self.tokenList.token.attributeValue)
            self.matchFactor('identifier')
            if(self.tokenList.token.attributeValue == 'comma'):
                self.match('comma')
            self.params()
        else:
            return 'OK'

    #grammer rule arrayNumber --> number , arrayNumber
    def arrayNumber(self):
        if(self.tokenList.token.tokenName == 'number'):
            self.matchFactor('number')
            self.match('comma')
            self.arrayNumber()
        else:
            return 'OK'

    #grammer rule coutState --> << expr coutState ;
    def coutState(self):
        if(self.tokenList.token.attributeValue == 'SHL'):
            self.match('SHL')
            self.expr()
            self.coutState()
            self.match('semicolon')
        else:
            return 'OK'
    #grammer rule cinState --> >> expr cinState ;
    def cinState(self):
        if(self.tokenList.token.attributeValue == 'SHR'):
            self.match('SHR')
            self.expr()
            self.cinState()
            self.match('semicolon')
        else:
            return 'OK'



    """state for increasing precedence
    A) = *= /= %= &= ^= |=
    I) ||
    J) &&
    K) |
    L) ^
    M) &
    B) == !=
    C) < <= > >=
    D) << >>
    E) + -
    F) * / %
    H) ++ --"""
    #grammer rule expr --> I expr_prime
    def expr(self):
        expr_state = self.I()
        if(expr_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.expr_prime()

    #grammer rule expr_prime --> = expr | epsilon
    def expr_prime(self):
        if(self.tokenList.token.attributeValue == 'EQ'):
            self.match('EQ')
            return self.expr()
        if(self.tokenList.token.attributeValue == 'ME'):
            self.match('ME')
            return self.expr()
        if(self.tokenList.token.attributeValue == 'DE'):
            self.match('DE')
            return self.expr()
        if(self.tokenList.token.attributeValue == 'moduloE'):
            self.match('moduloE')
            return self.expr()
        if(self.tokenList.token.attributeValue == 'ANDE'):
            self.match('ANDE')
            return self.expr()
        if(self.tokenList.token.attributeValue == 'bitwiseInsclusiveANDE'):
            self.match('bitwiseInsclusiveANDE')
            return self.expr()
        if(self.tokenList.token.attributeValue == 'ORE'):
            self.match('ORE')
            return self.expr()
        else:
            return 'OK'

    #grammer rule I --> J I_prime
    def I(self):
        I_state = self.J()
        if(I_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.I_prime()

    #grammer rule I_prime --> || I | epsilon
    def I_prime(self):
        if(self.tokenList.token.attributeValue == 'or'):
            self.match('or')
            return self.I()
        else:
            return 'OK'

    #grammer rule J --> K J_prime
    def J(self):
        J_state = self.K()
        if(J_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.J_prime()

    #grammer rule J_prime --> && J | epsilon
    def J_prime(self):
        if(self.tokenList.token.attributeValue == 'and'):
            self.match('and')
            return self.J()
        else:
            return 'OK'

    #grammer rule K --> L K_prime
    def K(self):
        K_state = self.L()
        if(K_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.K_prime()

    #grammer rule K_prime --> | K | epsilon
    def K_prime(self):
        if(self.tokenList.token.attributeValue == 'bitwiseOR'):
            self.match('bitwiseOR')
            return self.K()
        else:
            return 'OK'

    #grammer rule L --> M L_prime
    def L(self):
        L_state = self.M()
        if(L_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.L_prime()

    #grammer rule L_prime --> ^ L | epsilon
    def L_prime(self):
        if(self.tokenList.token.attributeValue == 'bitwiseInsclusiveAND'):
            self.match('bitwiseInsclusiveAND')
            return self.L()
        else:
            return 'OK'

    #grammer rule M --> B M_prime
    def M(self):
        M_state = self.B()
        if(M_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.M_prime()

    #grammer rule M_prime --> & M | epsilon
    def M_prime(self):
        if(self.tokenList.token.attributeValue == 'bitwiseAND'):
            self.match('bitwiseAND')
            return self.M()
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

    #grammer rule F --> H F_prime
    def F(self):
        F_state = self.H()
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
        elif(self.tokenList.token.attributeValue == 'modulo'):
            self.match('modulo')
            return self.F()
        else:
            return 'OK'

    #grammer rule H --> factor H_prime
    def H(self):
        H_state = self.factor()
        if(H_state == 'ERROR'):
            return 'ERROR'
        else:
            return self.H_prime()

    #grammer rule H_prime --> ++ H | -- H | epsilon
    def H_prime(self):
        if(self.tokenList.token.attributeValue == 'increment'):
            self.match('increment')
            return self.H()
        elif(self.tokenList.token.attributeValue == 'decrement'):
            self.match('decrement')
            return self.H()
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
        elif(self.tokenList.token.attributeValue == 'leftparantheses'):
            self.match('leftparantheses')
            self.expr()
            self.match('rightparantheses')
            return 'OK'
        else:
            return 'ERROR'
