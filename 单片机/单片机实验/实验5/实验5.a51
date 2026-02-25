  ORG 0000H
	LJMP SE11
	ORG 0080H
            SE11:MOV SP,#53H
	mov p2,#0ffh
	MOV A,#43H
	MOV DPTR,#0FF20H
	MOVX @DPTR,A
	MOV 7EH,#01H
	MOV 7DH,#01H
	MOV 7CH,#01H
	MOV 7BH,#07H
	MOV 7AH,#05H
	MOV 79H,#00H            ;???????
            LO18:LCALL SSEE              ;???????
                               ;?????
            SSEE:SETB RS1                ;????
	MOV R5,#05H
            SSE2:MOV 30H,#20H
	MOV 31H,#7EH
	MOV R7,#06H
            SSE1:MOV A,30H
	CPL A      
	MOV DPTR,#0FF21H        ;???? 
	MOVX @DPTR,A
	MOV R0,31H
	MOV A,@R0
	MOV DPTR,#DDFF
	MOVC A,@A+DPTR          ;?????           
   MOV DPTR,#0FF22H        ;????
	MOVX @DPTR,A
	MOV A,30H
	RR A                    ;??
	MOV 30H,A
	DEC 31H
	MOV A,#0FFH           
	MOV DPTR,#0FF22H        ;???
	MOVX @DPTR,A
	DJNZ R7,SSE1            ;????????
	DJNZ R5,SSE2
	CLR RS1
	RET
            DDFF:DB 0C0H,0F9H,0A4H,0B0H,99H,92H,82H,0F8H,80H,90H
	DB 88H,83H,0C6H,0A1H,86H,8EH,0FFH,0CH,89H,0DEH
	END