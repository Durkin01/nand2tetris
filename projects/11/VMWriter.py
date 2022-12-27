

# VM Writer
class VMWriter():

    def __init__(self,output):
        pass

    def writePush(self,segment,idx):
        pass

    def writePop(self,segment,idx):
        pass

    def writeArithmetic(self,command):
        pass

    def writeLabel(self,label):
        pass

    def writeGoTo(self,label):
        pass

    def writeIf(self,label):
        pass

    def writeCall(self,name,nArgs):
        pass

    def writeFunction(name,nLocals):
        pass

    def writeReturn(self):
        pass

    def close(self):
        self.output.close()
