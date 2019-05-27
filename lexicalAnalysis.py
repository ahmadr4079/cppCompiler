import re
import pandas as pd
from uuid import uuid1


class LexicalAnalysis:
    def __init__(self, file):
        self.fp = file

    # def for create switchState state
    def switchState(self, state, *argv):
        return getattr(self, 'state_' + str(state))(*argv)

    def state_0(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<eof>'")
        elif char == '<':
            return LexicalAnalysis.switchState(self, 1)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 5)
        elif char == '>':
            return LexicalAnalysis.switchState(self, 8)
        elif char == '+':
            return LexicalAnalysis.switchState(self, 11)
        elif char == '-':
            return LexicalAnalysis.switchState(self, 15)
        elif char == '*':
            return LexicalAnalysis.switchState(self, 19)
        elif char == '/':
            return LexicalAnalysis.switchState(self, 22)
        elif char == '%':
            return LexicalAnalysis.switchState(self, 25)
        elif char == '!':
            return LexicalAnalysis.switchState(self, 28)
        elif char == '&':
            return LexicalAnalysis.switchState(self, 31)
        elif char == '|':
            return LexicalAnalysis.switchState(self, 35)
        elif char == ',':
            return LexicalAnalysis.switchState(self, 39)
        elif char == '^':
            return LexicalAnalysis.switchState(self, 41)
        elif char == '~':
            return LexicalAnalysis.switchState(self, 44)
        elif char == ' ':
            return LexicalAnalysis.switchState(self, 48)
        elif char == ';':
            return LexicalAnalysis.switchState(self, 50)
        elif char == '(':
            return LexicalAnalysis.switchState(self, 52)
        elif char == ')':
            return LexicalAnalysis.switchState(self, 54)
        elif char == '{':
            return LexicalAnalysis.switchState(self, 56)
        elif char == '}':
            return LexicalAnalysis.switchState(self, 58)
        elif char == '\n':
            return LexicalAnalysis.switchState(self, 0)
        elif re.search('[A-Z]|[a-z]', char):
            return LexicalAnalysis.switchState(self, 60, char)

    def state_1(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,LT>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 2)
        elif char == '>':
            return LexicalAnalysis.switchState(self, 3)
        elif char == '<':
            return LexicalAnalysis.switchState(self, 46)
        else:
            return LexicalAnalysis.switchState(self, 4)

    def state_2(self):
        print("'<operator,LE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_3(self):
        print("'<operator,NE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_4(self):
        self.fp.previousChar()
        print("'<operator,LT>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_5(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,EQ>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 6)
        else:
            return LexicalAnalysis.switchState(self, 7)

    def state_6(self):
        print("'<operator,ET>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_7(self):
        self.fp.previousChar()
        print("'<operator,EQ>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_8(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,GT>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 9)
        elif char == '>':
            return LexicalAnalysis.switchState(self, 47)
        else:
            return LexicalAnalysis.switchState(self, 10)

    def state_9(self):
        print("'<operator,GE>''")
        return LexicalAnalysis.switchState(self, 0)

    def state_10(self):
        self.fp.previousChar()
        print("'<operator,GT>'")
        return LexicalAnalysis.switchState(self, 0)


    def state_11(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,addition>'")
            print("'<eof>'")
        elif char == '+':
            return LexicalAnalysis.switchState(self, 12)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 13)
        else:
            return LexicalAnalysis.switchState(self, 14)


    def state_12(self):
        print("'<operator,increment>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_13(self):
        print("'<operator,AE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_14(self):
        self.fp.previousChar()
        print("'<operator,addition>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_15(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,subtraction>'")
            print("'<eof>'")
        elif char == '-':
            return LexicalAnalysis.switchState(self, 16)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 17)
        else:
            return LexicalAnalysis.switchState(self, 18)

    def state_16(self):
        print("'<operator,decrement>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_17(self):
        print("'<operator,SE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_18(self):
        self.fp.previousChar()
        print("'<operator,subtraction>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_19(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,multiplication>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 20)
        else:
            return LexicalAnalysis.switchState(self, 21)

    def state_20(self):
        print("'<operator,ME>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_21(self):
        self.fp.previousChar()
        print("'<operator,multiplication>'")
        return LexicalAnalysis.switchState(self, 0)
    
    def state_22(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,division>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 23)
        else:
            return LexicalAnalysis.switchState(self, 24)

    def state_23(self):
        print("'<operator,DE>'")
        return LexicalAnalysis.switchState(self, 0)
    
    def state_24(self):
        self.fp.previousChar()
        print("'<operator,division>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_25(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,modulo>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 26)
        else:
            return LexicalAnalysis.switchState(self, 27)

    def state_26(self):
        print("'<operator,ME>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_27(self):
        self.fp.previousChar()
        print("'<operator,modulo>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_28(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,NOT>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 29)
        else:
            return LexicalAnalysis.switchState(self, 30)

    def state_29(self):
        print("'<operator,NET>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_30(self):
        self.fp.previousChar()
        print("'<operator,NOT>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_31(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,bitwiseAND>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 32)
        elif char == '&':
            return LexicalAnalysis.switchState(self, 33)
        else:
            return LexicalAnalysis.switchState(self, 34)

    def state_32(self):
        print("'<operator,ANDE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_33(self):
        print("'<operator,and>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_34(self):
        self.fp.previousChar()
        print("'<operator,bitwiseAND>'")
        return LexicalAnalysis.switchState(self, 0)
    
    def state_35(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,bitwiseInsclusiveOR>'")
            print("'<eof>'")
        elif char == '|':
            return LexicalAnalysis.switchState(self, 36)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 37)
        else:
            return LexicalAnalysis.switchState(self, 38)
    
    def state_36(self):
        print("'<operator,or>'")
        return LexicalAnalysis.switchState(self, 0)
    
    def state_37(self):
        print("'<operator,ORE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_38(self):
        self.fp.previousChar()
        print("'<operator,bitwiseInsclusiveOR>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_39(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,comma>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 40)

    def state_40(self):
        self.fp.previousChar()
        print("'<operator,comma>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_41(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,XOR>'")
            print("'<eof>'")
        elif char == '=':
            return LexicalAnalysis.switchState(self, 42)
        else:
            return LexicalAnalysis.switchState(self, 43)

    def state_42(self):
        print("'<operator,XORE>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_43(self):
        self.fp.previousChar()
        print("'<operator,XOR>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_44(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<operator,NOT~>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 45)

    def state_45(self):
        self.fp.previousChar()
        print("'<operator,NOT~>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_46(self):
        print("'<operator,SHL>'")
        return LexicalAnalysis.switchState(self, 0)
    
    def state_47(self):
        print("'<operator,SHR>'")
        return LexicalAnalysis.switchState(self, 0)

    def state_48(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<delim>'")
            print("'<eof>'")
        elif char == ' ':
            return LexicalAnalysis.switchState(self, 48)
        else:
            return LexicalAnalysis.switchState(self, 49)
    
    def state_49(self):
        print("'<delim>'")
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)
        
    def state_50(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<punctuation,semicolon>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 51)
    
    def state_51(self):
        print("'<punctuation,semicolon>'")
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_52(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<punctuation,leftparantheses>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 53)
            
    def state_53(self):
        print("'<punctuation,leftparantheses>'")
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_54(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<punctuation,rightparantheses>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 55)

    def state_55(self):
        print("'<punctuation,rightparantheses>'")
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0) 
    
    def state_56(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<punctuation,leftbracket>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 57)
    
    def state_57(self):
        print("'<punctuation,leftbracket>'")
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_58(self):
        char = self.fp.nextChar()
        if char == 'eof':
            print("'<punctuation,rightbracket>'")
            print("'<eof>'")
        else:
            return LexicalAnalysis.switchState(self, 59)

    def state_59(self):
        print("'<punctuation,rightbracket>'")
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    
    def checkToken(self):
        string = self.identifiers
        tokenDataFrame = pd.read_csv('token.csv', index_col=0)
        for item, value in tokenDataFrame.iterrows():
            if value['tokenName'] == 'keyword' and value['attributeValue'] == string:
                return value['id'], value['tokenName'], value['attributeValue']
        return None, None, None

    def addIdentifiers(self):
        string = self.identifiers
        tokenDataFrame = pd.read_csv('token.csv', index_col=0)
        tokenDataFrame = tokenDataFrame.append({'id': uuid1(),
                                                'tokenName': 'identifier',
                                                'attributeValue': string},
                                               ignore_index=True)
        tokenDataFrame.to_csv('token.csv')
        return True


    def state_60(self, *argv):
        if argv:
            self.identifiers = argv[0]
        char = self.fp.nextChar()
        if char == 'eof':
            tokenId, tokenName, tokenAttributeValue = LexicalAnalysis.checkToken(
                self)
            if tokenId:
                print("'<{},{}>'".format(tokenName, tokenAttributeValue))
            else:
                addTokenBool = LexicalAnalysis.addIdentifiers(self)
                if addTokenBool:
                    print("'<identifiers,{}>'".format(self.identifiers))
                else:
                    print('error to save token in token csv file')
            print("'<eof>'")
        elif re.search('[A-Z]|[a-z]|[0-9]', char):
            self.identifiers = self.identifiers + char
            return LexicalAnalysis.switchState(self, 60)
        else:
            return LexicalAnalysis.switchState(self, 61)
            

    def state_61(self):
        self.fp.previousChar()
        tokenId, tokenName, tokenAttributeValue = LexicalAnalysis.checkToken(
            self)
        if tokenId:
            print("'<{},{}>'".format(tokenName, tokenAttributeValue))
        else:
            addTokenBool = LexicalAnalysis.addIdentifiers(self)
            if addTokenBool:
                print("'<identifiers,{}>'".format(self.identifiers))
            else:
                print('error to save token in token csv file')
        return LexicalAnalysis.switchState(self, 0)


