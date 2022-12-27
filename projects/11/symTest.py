import SymbolTable as sym

dic = sym.SymbolTable()
dic.define('x','int','FIELD')
dic.define('y','int','FIELD')
dic.define('pointCount','int','STATIC')
dic.define('this','Point','ARG')
dic.define('other','Point','ARG')
dic.define('dx','int','VAR')
dic.define('dy','int','VAR')
dic.varCount('FIELD')

print(dic.subScope)
print(dic.classScope)