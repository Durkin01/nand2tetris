

# VM Writer
class VMWriter():

    def __init__(self,output):
        self.output = output

    def writePush(self,segment,idx):
        self.output.write(f'push {segment} {idx}\n')

    def writePop(self,segment,idx):
        self.output.write(f'pop {segment} {idx}\n')

    def writeArithmetic(self,command):
        self.output.write(f'{command}\n')

    def writeLabel(self,label):
        self.output.write(f'label {label}\n')

    def writeGoTo(self,label):
        self.output.write(f'goto {label}\n')

    def writeIf(self,label):
        self.output.write(f'if-goto {label}\n')

    def writeCall(self,name,nArgs):
        self.output.write(f'call {name} {nArgs}\n')

    def writeFunction(name,nLocals):
        self.output.write(f'call {name} {nLocals}\n')

    def writeReturn(self):
        self.output.write("return\n")

    def close(self):
        self.output.close()
