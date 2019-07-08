import re
import pandas as pd
from uuid import uuid1
from tokenClass import Token


class LexicalAnalysis:
    def __init__(self, file):
        self.fp = file
        self.tokens = list()
        self.lineChar = 1

    # def for create switchState state
    def switchState(self, state, *argv):
        return getattr(self, 'state_' + str(state))(*argv)

    def state_0(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('eof',line=self.lineChar))
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
            self.lineChar = self.lineChar + 1
            return LexicalAnalysis.switchState(self, 0)
        elif char == '#':
            return LexicalAnalysis.switchState(self, 73)
        elif char == '.':
            return LexicalAnalysis.switchState(self, 75)
        elif char == '[':
            return LexicalAnalysis.switchState(self,77)
        elif char == ']':
            return LexicalAnalysis.switchState(self,79)
        elif re.search('[A-Z]|[a-z]', char):
            return LexicalAnalysis.switchState(self, 60, char)
        elif re.search('[0-9]',char):
            return LexicalAnalysis.switchState(self, 62, char)

    def state_1(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','LT',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 2)
        elif char == '>':
            return LexicalAnalysis.switchState(self, 3)
        elif char == '<':
            return LexicalAnalysis.switchState(self, 46)
        else:
            return LexicalAnalysis.switchState(self, 4)

    def state_2(self):
        self.tokens.append(Token('operator','LE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_3(self):
        self.tokens.append(Token('operator','NE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_4(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','LT',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_5(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','EQ',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 6)
        else:
            return LexicalAnalysis.switchState(self, 7)

    def state_6(self):
        self.tokens.append(Token('operator','ET',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_7(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','EQ',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_8(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','GT',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 9)
        elif char == '>':
            return LexicalAnalysis.switchState(self, 47)
        else:
            return LexicalAnalysis.switchState(self, 10)

    def state_9(self):
        self.tokens.append(Token('operator','GE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_10(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','GT',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)


    def state_11(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','addition',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '+':
            return LexicalAnalysis.switchState(self, 12)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 13)
        else:
            return LexicalAnalysis.switchState(self, 14)


    def state_12(self):
        self.tokens.append(Token('operator','increment',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_13(self):
        self.tokens.append(Token('operator','AE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_14(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','addition',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_15(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','subtraction',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '-':
            return LexicalAnalysis.switchState(self, 16)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 17)
        else:
            return LexicalAnalysis.switchState(self, 18)

    def state_16(self):
        self.tokens.append(Token('operator','decrement',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_17(self):
        self.tokens.append(Token('operator','SE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_18(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','subtraction',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_19(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','multiplication',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 20)
        else:
            return LexicalAnalysis.switchState(self, 21)

    def state_20(self):
        self.tokens.append(Token('operator','ME',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_21(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','multiplication',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_22(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','division',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 23)
        else:
            return LexicalAnalysis.switchState(self, 24)

    def state_23(self):
        self.tokens.append(Token('operator','DE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_24(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','division',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_25(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','modulo',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 26)
        else:
            return LexicalAnalysis.switchState(self, 27)

    def state_26(self):
        self.tokens.append(Token('operator','moduloE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_27(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','modulo',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_28(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','NOT',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 29)
        else:
            return LexicalAnalysis.switchState(self, 30)

    def state_29(self):
        self.tokens.append(Token('operator','NET',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_30(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','NOT',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_31(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','bitwiseAND',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 32)
        elif char == '&':
            return LexicalAnalysis.switchState(self, 33)
        else:
            return LexicalAnalysis.switchState(self, 34)

    def state_32(self):
        self.tokens.append(Token('operator','ANDE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_33(self):
        self.tokens.append(Token('operator','and',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_34(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','bitwiseAND',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_35(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','bitwiseOR',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '|':
            return LexicalAnalysis.switchState(self, 36)
        elif char == '=':
            return LexicalAnalysis.switchState(self, 37)
        else:
            return LexicalAnalysis.switchState(self, 38)

    def state_36(self):
        self.tokens.append(Token('operator','or',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_37(self):
        self.tokens.append(Token('operator','ORE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_38(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','bitwiseOR',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_39(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','comma',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 40)

    def state_40(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','comma',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_41(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','bitwiseInsclusiveAND',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '=':
            return LexicalAnalysis.switchState(self, 42)
        else:
            return LexicalAnalysis.switchState(self, 43)

    def state_42(self):
        self.tokens.append(Token('operator','bitwiseInsclusiveANDE',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_43(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','bitwiseInsclusiveAND',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_44(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','NOT~',line=self.lineChar))
            self.tokens.append(Token('eof'))
        else:
            return LexicalAnalysis.switchState(self, 45)

    def state_45(self):
        self.fp.previousChar()
        self.tokens.append(Token('operator','NOT~',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_46(self):
        self.tokens.append(Token('operator','SHL',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_47(self):
        self.tokens.append(Token('operator','SHR',line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_48(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('delim',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == ' ':
            return LexicalAnalysis.switchState(self, 48)
        else:
            return LexicalAnalysis.switchState(self, 49)

    def state_49(self):
        self.tokens.append(Token('delim',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_50(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','semicolon',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 51)

    def state_51(self):
        self.tokens.append(Token('punctuation','semicolon',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_52(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','leftparantheses',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 53)

    def state_53(self):
        self.tokens.append(Token('punctuation','leftparantheses',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_54(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','rightparantheses',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 55)

    def state_55(self):
        self.tokens.append(Token('punctuation','rightparantheses',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_56(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','leftbracket',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 57)

    def state_57(self):
        self.tokens.append(Token('punctuation','leftbracket',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_58(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','rightbracket',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 59)

    def state_59(self):
        self.tokens.append(Token('punctuation','rightbracket',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)


    def checkToken(self):
        string = self.identifiers
        tokenDataFrame = pd.read_csv('token.csv', index_col=0)
        for item, value in tokenDataFrame.iterrows():
            if value['attributeValue'] == string:
                return value['id'], value['tokenName'], value['attributeValue']
        return None, None, None

    def addIdentifiers(self):
        string = self.identifiers
        line = self.lineChar
        tokenDataFrame = pd.read_csv('token.csv', index_col=0)
        tokenId = uuid1()
        tokenDataFrame = tokenDataFrame.append({'id': tokenId,
                                                'tokenName': 'identifier',
                                                'attributeValue': string,
                                                'line':line},
                                               ignore_index=True)
        tokenDataFrame.to_csv('token.csv')
        return True,tokenId,'identifier',string


    def state_60(self, *argv):
        if argv:
            self.identifiers = argv[0]
        char = self.fp.nextChar()
        if char == 'eof':
            tokenId, tokenName, tokenAttributeValue = LexicalAnalysis.checkToken(
                self)
            if tokenId:
                self.tokens.append(Token(tokenName,tokenAttributeValue,tokenId,line=self.lineChar))
            else:
                addTokenBool,tokenId,tokenName,tokenAttributeValue = LexicalAnalysis.addIdentifiers(self)
                if addTokenBool:
                    self.tokens.append(Token(tokenName,tokenAttributeValue,tokenId,line=self.lineChar))
                else:
                    self.tokens.append('error to save token in token csv file')
            self.tokens.append(Token('eof',line=self.lineChar))
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
            self.tokens.append(Token(tokenName,tokenAttributeValue,tokenId,line=self.lineChar))
        else:
            addTokenBool,tokenId,tokenName,tokenAttributeValue = LexicalAnalysis.addIdentifiers(self)
            if addTokenBool:
                self.tokens.append(Token(tokenName,tokenAttributeValue,tokenId,line=self.lineChar))
            else:
                self.tokens.append('error to save token in token csv file')
        return LexicalAnalysis.switchState(self, 0)

    def state_62(self,*argv):
        if argv:
            self.number = argv[0]
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('number',self.number,line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif re.search('[0-9]',char):
            self.number = self.number + char
            return LexicalAnalysis.switchState(self,62)
        elif char == '.':
            self.number = self.number + char
            return LexicalAnalysis.switchState(self,64)
        elif char == 'E':
            self.number = self.number + char
            return LexicalAnalysis.switchState(self,66)
        else:
            return LexicalAnalysis.switchState(self,63)

    def state_63(self):
        self.fp.previousChar()
        self.tokens.append(Token('number',self.number,line=self.lineChar))
        return LexicalAnalysis.switchState(self, 0)

    def state_64(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('number',self.number,line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif re.search('[0-9]',char):
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 65)
        else:
            return LexicalAnalysis.switchState(self, 63)

    def state_65(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('number',self.number,line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif re.search('[0-9]',char):
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 65)
        elif char == 'E':
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 66)
        else:
            return LexicalAnalysis.switchState(self, 63)

    def state_66(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('number',self.number,line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif char == '+' or char == '-':
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 67)
        elif re.search('[0-9]',char):
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 68)
        else:
            return LexicalAnalysis.switchState(self, 63)

    def state_67(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('number',self.number,line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif re.search('[0-9]',char):
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 68)
        else:
            return LexicalAnalysis.switchState(self, 63)

    def state_68(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('number',self.number,line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        elif re.search('[0-9]',char):
            self.number = self.number + char
            return LexicalAnalysis.switchState(self, 68)
        else:
            return LexicalAnalysis.switchState(self, 63)

    def state_73(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('operator','sharp',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 74)

    def state_74(self):
        self.tokens.append(Token('operator','sharp',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_75(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('dot',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 76)

    def state_76(self):
        self.tokens.append(Token('dot',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_77(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','leftsqurebracket',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 78)

    def state_78(self):
        self.tokens.append(Token('punctuation','leftsqurebracket',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)

    def state_79(self):
        char = self.fp.nextChar()
        if char == 'eof':
            self.tokens.append(Token('punctuation','rightsqurebracket',line=self.lineChar))
            self.tokens.append(Token('eof',line=self.lineChar))
        else:
            return LexicalAnalysis.switchState(self, 80)

    def state_80(self):
        self.tokens.append(Token('punctuation','rightsqurebracket',line=self.lineChar))
        self.fp.previousChar()
        return LexicalAnalysis.switchState(self, 0)
