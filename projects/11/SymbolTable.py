#!/usr/bin/env python3

# Jack Symbol Table
class SymbolTable():

    classScope = {}
    subScope = {} 
    countDict = {'STATIC':-1,'FIELD':-1,'VAR':-1,'ARG':-1}    

    def startSubroutine(self):
        self.subScope = {}
        self.countDict['ARG'] = 0
        self.countDict['VAR'] = 0

    def define(self,name,type,kind):

        if kind in ['STATIC','FIELD']:
            
            if name not in self.classScope:
                self.countDict[kind] += 1 

            self.classScope[name] = {'type':type,'kind':kind,'num':self.countDict[kind]} 

        else:
            if name not in self.subScope:
                self.countDict[kind] += 1 

            self.subScope[name] = {'type':type,'kind':kind,'num':self.countDict[kind]} 

    def varCount(self,kind):
        return self.countDict[kind]

    def kindOf(self,name):
        if name in self.classScope:
            return self.classScope[name]['kind']
        elif name in self.subScope:
            return name in self.subScope[name]['kind']
        else:
            return 'NONE'

    def typeOf(self,name):
        if name in self.classScope:
            return self.classScope[name]['type']
        elif name in self.subScope:
            return name in self.subScope[name]['type']

    def indexOf(self,name):
        if name in self.classScope:
            return self.classScope[name]['num']
        elif name in self.subScope:
            return name in self.subScope[name]['num']