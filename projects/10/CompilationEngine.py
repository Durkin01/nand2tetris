#!/usr/bin/env python3

# Compilation Engine
class CompilationEngine():

    def __init__(self,tokenizer,output):
        
        self.tk = tokenizer

        f = open(output + ".xml", "w")

        self.f = f
        self.f.write('<class>\n') 
        self.compileClass()
        self.f.write('</class>')

        f.close()

    def compileClass(self):
        f = self.f

        f.write('<keyword> class </keyword>\n')                           # '<keyword> class </keyword>\n' 
        self.tk.advance()
        identifier = self.tk.identifier()
        f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')   # <identifier> className </identifier> 
        self.tk.advance()
        f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')               # <symbol> { </symbol>
        self.tk.advance()
        while self.tk.tokenType() == "KEYWORD":
            if self.tk.keyWord() in ['STATIC','FIELD']:
                self.compileClassVarDec()
            else:
                self.compileSubroutineDec()
            self.tk.advance() 
        f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')               # <symbol> } </symbol>

    # keyword,[keyword,identifier],identifier,(symbol,identifier),symbol
    def compileClassVarDec(self): 
        f = self.f

        # <classVarDec>
        f.write('<classVarDec>\n')

        # keyword
        f.write(f'<keyword> {self.tk.keyWord().lower()} </keyword>\n')                           # '<keyword> {static,field} </keyword>\n' 

        # keyword or identifier
        self.tk.advance()
        brackets = self.tk.tokenType().lower()

        f.write(f'<{brackets}> {self.tk.identifier()} </{brackets}>\n')                           # '<keyword> {int,char,boolean,classname} </keyword>\n' 

        # identifier
        self.tk.advance()
        f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')                           # '<keyword> {int,char,boolean,classname} </keyword>\n' 

        # (symbol,identifier)* ----> LOOP
        self.tk.advance()
        while self.tk.symbol() == ',':
            f.write(f'<symbol> , </symbol>\n')
            self.tk.advance()
            f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')
            self.tk.advance()
        f.write('<symbol> ; </symbol>\n')

        # </classVarDec>
        f.write('</classVarDec>\n')

    # keyword,[keyword,identifier],identifier,symbol,parameterlist,symbol,subroutineBody
    def compileSubroutineDec(self):
        f = self.f
        f.write('<subroutineDec>\n')

        # keyword
        f.write(f'<keyword> {self.tk.keyWord().lower()} </keyword>\n')

        # keyword/identifier
        self.tk.advance()
        brackets = self.tk.tokenType().lower()
        f.write(f'<{brackets}> {self.tk.identifier()} </{brackets}>\n')

        # identifier
        self.tk.advance()
        f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

        # symbol
        self.tk.advance()
        f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
        
        # parameter List
        self.compileParameterList()

        # symbol
        f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')

        # subroutineBody
        self.compileSubroutineBody()

        f.write('</subroutineDec>\n')

    def compileParameterList(self):
        f = self.f
        f.write('<parameterList>\n')

        self.tk.advance()
        while self.tk.tokenType() in ['KEYWORD','IDENTIFIER']:

            # type
            brackets = self.tk.tokenType().lower()
            f.write(f'<{brackets}> {self.tk.identifier()} </{brackets}>\n')

            # varName
            self.tk.advance()
            f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

            self.tk.advance()
            # LOOP BELOW    
            while self.tk.symbol == ',':
                # symbol ','
                f.write(f'<symbol> , </symbol>\n')

                # type
                self.tk.advance()
                brackets = self.tk.tokenType().lower()
                f.write(f'<{brackets}> {self.tk.identifier()} </{brackets}>\n')

                # varName
                self.tk.advance()
                f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

                self.tk.advance()

        f.write('</parameterList>\n')

    # '{', varDec*, statements, '}'
    def compileSubroutineBody(self):
        f = self.f        
        f.write('<subroutineBody>\n')

        # '{'
        self.tk.advance()
        f.write('<symbol> { </symbol>\n')

        # varDec*       
        self.compileVarDec()

        # statements
        self.compileStatements()

        # '}' 
        f.write('<symbol> } </symbol>\n')

        f.write('</subroutineBody>\n')
        
    # 'var',identifier/keyword,identifier,(',',identifier)*,';'
    def compileVarDec(self):
        f = self.f
        f.write('<varDec>\n')

        # 'var'
        self.tk.advance()
        f.write(f'<keyword> var </keyword>\n')
    
        # identifier/keyword
        self.tk.advance()
        brackets = self.tk.tokenType().lower()
        f.write(f'<{brackets}> {self.tk.identifier()} </{brackets}>\n')
        
        # identifier
        self.tk.advance()
        f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

        # LOOP
        self.tk.advance()
        while self.tk.symbol() == ',':
            # ','
            f.write(f'<symbol> , </symbol>\n')

            # identifier
            self.tk.advance()
            f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

            self.tk.advance()

        # ';'
        self.tk.advance()
        f.write('<symbol> ; </symbol>\n')

        f.write('</varDec>\n')

    def compileStatements(self):
        f = self.f
        f.write('<statements>\n')

        while self.tk.symbol() in ['let','if','while','do','return']:
            symbol = self.tk.symbol()
            
            if symbol == 'let':
                self.compileLet()
            if symbol == 'if':
                self.compileIf()
            if symbol == 'while':
                self.compileWhile()
            if symbol == 'do':
                self.compileDo()
            if symbol == 'return':
                self.compileReturn()
    
        f.write('</statements>\n')

    # 'let',identifier, ('[' expression ']')? , '=', expression, ';'
    def compileLet(self):
        f = self.f

        # 'let'
        f.write('<letStatement>\n')
        f.write(f'<keyword> {self.tk.identifier()} </keyword>\n')

        # identifier
        self.tk.advance()
        f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

        # if '['
        self.tk.advance()
        if self.tk.symbol() == '[':
            f.write(f'<symbol> [ </symbol>\n')
            self.tk.advance()
            self.compileExpression()     
            # advance() here???
            f.write(f'<symbol> ] </symbol>\n')

        # '='
        self.tk.advance()
        f.write('<symbol> = </symbol>\n')

        # expression        
        self.compileExpression()

         # ';'
        self.tk.advance()
        f.write('<symbol> ; </symbol>\n')

        f.write('</letStatement>\n')

    def compileIf(self):
        f = self.f
        f.write('<ifStatement>\n')            

        # 'if'
        f.write(f'<keyword> {self.tk.identifier()} </keyword>\n')

        # '('
        self.tk.advance()
        f.write('<symbol> ( </symbol>\n')
        
        # expression
        self.tk.advance()
        self.compileExpression()

        # ')'
        self.tk.advance()
        f.write('<symbol> ) </symbol>\n')

        # '{'
        self.tk.advance()
        f.write('<symbol> { </symbol>\n')
        
        # statements 
        self.compileStatements()

        # '}'
        f.write('<symbol> } </symbol>\n')

        # if 'else'
        self.tk.advance()
        symbol = self.tk.symbol()
        if symbol == 'else':

            # 'else'
            self.tk.advance()
            f.write('<keyword> else </keyword>\n')

            # '{'
            self.tk.advance()
            f.write('<symbol> { </symbol>\n')

            # statements
            self.compileStatements()

            # '}'
            f.write('<symbol> } </symbol>\n')


        self.tk.advance()
        f.write('</ifStatement>\n')

    def compileWhile(self):
        f = self.f
        f.write('<whileStatement>\n')

        # 'while'
        f.write(f'<keyword> {self.tk.identifier} </keyword>\n')

        # '('
        self.tk.advance()
        f.write(f'<symbol> ( </symbol>\n')

        # expression                                
        self.tk.advance()
        self.compileExpression()

        # ')'
        self.tk.advance()
        f.write('<symbol> ) </symbol>\n')

        # '{'
        self.tk.advance()
        f.write('<symbol> { </symbol>\n')

        # statements
        self.compileStatements 

        # '}'
        f.write('<symbol> } </symbol>\n')

        self.tk.advance()
        f.write('</whileStatement>\n')

    def compileDo(self):
        f = self.f
        f.write('<doStatement>\n')

        # 'do'
        f.write(f'<keyword> {self.tk.identifier()} </keyword>\n')

        # subroutine call
        self.tk.advance()
        p1 = self.tk.identifier()
        self.tk.advance()
        p2 = self.tk.identifier()
        if p2 == '(':
            f.write(f'<identifier> {p1} </identifier>\n') 
            f.write(f'<symbol> {p2} </symbol>\n')
            # expressionList
            self.compileExpressionList()

            f.write(f'<symbol> ) </symbol>\n')
        else:
            # identifier
            f.write(f'<identifier> {p1} </identifier>\n')

            # '.'
            f.write(f'<symbol> {p2} </symbol>\n')

            # subroutine name
            self.tk.advance()
            f.write(f'<identifier> {self.tk.identifier()} </identifier>\n')

            # '('
            self.tk.advance()
            f.write(f'<symbol> ( </symbol>\n')

            # expressionList
            self.compileExpressionList()

            # ')'
            f.write(f'<symbol> ) </symbol>\n')

        f.write(f'<symbol> ; </symbol>\n')

        self.tk.advance()
        self.tk.advance()
        f.write('</doStatement>\n')

    def compileReturn(self):
        f = self.f
        f.write('<returnStatement>\n')
        f.write('<keyword> return </keyword>\n')
        self.tk.advance()
        if self.tk.symbol() != ";":
            self.compileExpression()

        f.write(f'<symbol> ; </symbol>\n')

        self.tk.advance()
        f.write('</returnStatement>\n')

    # advanced() CANNOT be used before entering
    def compileExpression(self):
        f = self.f

        f.write('<expression>\n')

        # term
        self.compileTerm()

        # LOOP if op
        self.tk.advance()
        if self.tk.symbol() in ['+','-','*','&','|','<','>','=','&lt;','&gt;','&quot;','&amp;']:
            
            # op
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')

            # term
            self.compileTerm()

        f.write('</expression>\n')

    # advance() NOT in; advance() OUT
    def compileTerm(self):
        f = self.f
        f.write('<term>\n')
        p1 = self.tk.symbol()
        p1_type = self.tk.tokenType()
        self.tk.savePeek()
        p2 = self.tk.returnPeek()
        p2_type = self.tk.typePeek()

        # integerConstant, stringConstant, keywordConstant, varName
        if p1_type in ["STRING_CONST","INT_CONST",'KEYWORD']:
            if p1_type == 'STRING_CONST':
                f.write(f'<stringConstant> {p1} </stringConstant>\n')
            elif p1_type == 'INT_CONST':
                f.write(f'<integerConstant> {p1} </integerConstant>\n')
            else:
                f.write(f'<{p1_type.lower()}> {p1} </{p1_type.lower()}>\n')
            
        # '('
        elif p1 == '(':
            f.write(f'<symbol> {p1} </symbol>\n')
            self.compileExpression()
        # unaryOp term
        elif p1 in ['-','~']:
            f.write(f'<symbol> {p1} </symbol>\n')
            self.compileTerm()
        
        # identifiers
        elif p2 == '[':
            f.write(f'<identifier> {p1} </integerConstant>\n')
            self.tk.advance()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
            self.compileExpression()
            self.tk.advance()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
        elif p2 == '(':
            f.write(f'<identifier> {p1} </identifier>\n') 
            self.tk.advance()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
            self.compileExpressionList()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
        elif p2 == '.':
            f.write(f'<identifier> {p1} </identifier>\n') 
            self.tk.advance()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
            f.write(f'<identifier> {p1} </identifier>\n') 
            self.tk.advance()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
            self.compileExpressionList()
            f.write(f'<symbol> {self.tk.symbol()} </symbol>\n')
        else:
            # varName
            f.write(f'<identifier> {p1} </identifier>\n') 

        f.write('</term>\n')

    # assumes advanced() not used BEFORE in; advanced() used BEFORE out
    def compileExpressionList(self):
        f = self.f
        self.tk.advance()

        f.write('<expressionList>\n')

        # expression
        if self.tk.symbol() == ',':
            self.compileExpression() 
            self.tk.advance()

        # if ','
        while self.tk.symbol() == ',':
            f.write(f'<symbol> , </symbol>\n')
            self.compileExpression() 
            self.tk.advance()

        f.write('</expressionList>\n')





