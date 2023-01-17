#!/usr/bin/env python3

# Jack Tokenizor
class JackTokenizer():

    keywordList = ['class','constructor','function','method','field','static','var','int','char','boolean','void','true','false','null','this','let','do','if','else','while','return']
    symbolList = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~',"&lt;,","&gt;","&quot;","&amp;"]

    # Constructor
    def __init__(self,file):
        
        self.tokenList = []
        self.currentToken = None
        self.tokenIdx = 0
        self.next = 0

        with open(file, 'r') as f:
            lines = f.readlines() 

        for line in lines:
            idx = None
            # print(line + 'hello')
            try:
                try:
                    idx = line.index('//')
                except:
                    try:
                        idx = line.index('/*')
                    except:
                        idx = line.index('*')
                        print(idx)
                        if not idx < 3:
                            idx = None
            except:
                pass
            if isinstance(idx,int):
                line = line[:idx]

            line = line.strip()

            quotation = False
            waitingToken = ''
            for c in line:

                # quotation commands
                if c == '"' and not quotation:
                    quotation = True
                    waitingToken += c
                elif c == '"' and quotation:
                    self.tokenList.append(waitingToken + c)
                    waitingToken = '' 
                    quotation = False
                elif quotation:
                    waitingToken += c

                # space commands
                elif c == ' ' and quotation:
                    waitingToken += c
                elif c == ' ' and not quotation:
                    if waitingToken != '':
                        self.tokenList.append(waitingToken)
                    waitingToken = ''

                # handles special symbols
                elif c in JackTokenizer.keywordList or c in JackTokenizer.symbolList:
                    if waitingToken != '' and waitingToken != ' ': 
                        self.tokenList.append(waitingToken)

                    if c == '"':
                        c = '&quot;'
                    elif c == '>':
                        c = '&gt;'
                    elif c == '<':
                        c = '&lt;'
                    elif c== '&':
                        c = '&amp;'

                    self.tokenList.append(c)
                    waitingToken = ''
                else:
                    if c != '' or c != ' ':
                        waitingToken += c

            if waitingToken != '':
                self.tokenList.append(waitingToken)

    def hasMoreTokens(self):
        try:
            self.tokenList[self.tokenIdx]
            return True
        except:
            return False

    def advance(self):
        self.tokenIdx += 1
        self.currentToken = self.tokenList[self.tokenIdx]        

    def tokenType(self,token=None):
        
        if token == None:
            token=self.currentToken

        if token[0] == '"':
            return "STRING_CONST"
        try:
            tk = int(token[0])
            return "INT_CONST"
        except:
            pass
        if token in self.keywordList:
            return "KEYWORD"
        if token in self.symbolList:
            return "SYMBOL"
        else:
            return "IDENTIFIER" 

    def keyWord(self):
        return self.currentToken.upper()

    def symbol(self):
        return self.currentToken 

    def identifier(self):
        return self.currentToken

    def intVal(self):
        return self.currentToken 

    def stringVal(self):
        return self.currentToken[1:-1] 
    
    def print(self):
        print(self.tokenList)
    
    def savePeek(self,n=1):
        self.next = self.tokenList[self.tokenIdx + n]
        
    def returnPeek(self):
        return self.next

    def peekNext(self,n=1):
        return self.tokenList(self.tokenIdx + n)

    def typePeek(self):
        return self.tokenType(self.next)