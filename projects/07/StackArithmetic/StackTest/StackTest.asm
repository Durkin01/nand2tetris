@17
D=A
@0
A=M
M=D
@0
M=M+1
@17
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO0
D;JEQ
@0
A=M
A=A-1
M=0
@END0
0;JMP
(ISZERO0)
@0
A=M
A=A-1
M=-1
(END0)
@17
D=A
@0
A=M
M=D
@0
M=M+1
@16
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO1
D;JEQ
@0
A=M
A=A-1
M=0
@END1
0;JMP
(ISZERO1)
@0
A=M
A=A-1
M=-1
(END1)
@16
D=A
@0
A=M
M=D
@0
M=M+1
@17
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO2
D;JEQ
@0
A=M
A=A-1
M=0
@END2
0;JMP
(ISZERO2)
@0
A=M
A=A-1
M=-1
(END2)
@892
D=A
@0
A=M
M=D
@0
M=M+1
@891
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO3
D;JLT
@0
A=M
A=A-1
M=0
@END3
0;JMP
(ISZERO3)
@0
A=M
A=A-1
M=-1
(END3)
@891
D=A
@0
A=M
M=D
@0
M=M+1
@892
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO4
D;JLT
@0
A=M
A=A-1
M=0
@END4
0;JMP
(ISZERO4)
@0
A=M
A=A-1
M=-1
(END4)
@891
D=A
@0
A=M
M=D
@0
M=M+1
@891
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO5
D;JLT
@0
A=M
A=A-1
M=0
@END5
0;JMP
(ISZERO5)
@0
A=M
A=A-1
M=-1
(END5)
@32767
D=A
@0
A=M
M=D
@0
M=M+1
@32766
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO6
D;JGT
@0
A=M
A=A-1
M=0
@END6
0;JMP
(ISZERO6)
@0
A=M
A=A-1
M=-1
(END6)
@32766
D=A
@0
A=M
M=D
@0
M=M+1
@32767
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO7
D;JGT
@0
A=M
A=A-1
M=0
@END7
0;JMP
(ISZERO7)
@0
A=M
A=A-1
M=-1
(END7)
@32766
D=A
@0
A=M
M=D
@0
M=M+1
@32766
D=A
@0
A=M
M=D
@0
M=M+1
@0
AM=M-1
D=M
A=A-1
D=M-D
@ISZERO8
D;JGT
@0
A=M
A=A-1
M=0
@END8
0;JMP
(ISZERO8)
@0
A=M
A=A-1
M=-1
(END8)
@57
D=A
@0
A=M
M=D
@0
M=M+1
@31
D=A
@0
A=M
M=D
@0
M=M+1
@53
D=A
@0
A=M
M=D
@0
M=M+1
@0
A=M
A=A-1
D=M
A=A-1
M=D+M
D=A
@0
M=D+1
@112
D=A
@0
A=M
M=D
@0
M=M+1
@0
A=M
A=A-1
D=M
A=A-1
M=M-D
D=A
@0
M=D+1
@0
A=M
A=A-1
M=-M
@0
A=M
A=A-1
D=M
A=A-1
M=D&M
D=A
@0
M=D+1
@82
D=A
@0
A=M
M=D
@0
M=M+1
@0
A=M
A=A-1
D=M
A=A-1
M=D|M
D=A
@0
M=D+1
@0
A=M
A=A-1
M=!M
