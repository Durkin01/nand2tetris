@2
D=M
@1
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@4
M=D
@0
D=A
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@13
M=D
@4
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@1
D=A
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@13
M=D
@4
D=M
@1
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@2
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
M=M-1
A=M
D=M
@13
M=D
@2
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
(MAIN_LOOP_START)
@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JMP
@0
M=M-1
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
@4
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@4
D=M
@1
A=D+A
D=M
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
@0
M=M-1
A=M
D=M
@13
M=D
@4
D=M
@2
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@4
D=M
@0
A=M
M=D
@0
M=M+1
@1
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
@0
M=M-1
A=M
D=M
@4
M=D
@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@1
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
M=M-1
A=M
D=M
@13
M=D
@2
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)
@2
D=M
@1
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@4
M=D
@0
D=A
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@13
M=D
@4
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@1
D=A
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@13
M=D
@4
D=M
@1
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@2
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
M=M-1
A=M
D=M
@13
M=D
@2
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
(MAIN_LOOP_START)
@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JMP
@0
M=M-1
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
@4
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@4
D=M
@1
A=D+A
D=M
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
@0
M=M-1
A=M
D=M
@13
M=D
@4
D=M
@2
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@4
D=M
@0
A=M
M=D
@0
M=M+1
@1
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
@0
M=M-1
A=M
D=M
@4
M=D
@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
@1
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
M=M-1
A=M
D=M
@13
M=D
@2
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)
