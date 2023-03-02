#IAS Implimentation using Python Language
def NumberToBinary(n):           #This is the function which is used to convert a number from decimal to binary in 12 bits
    if (n>=0):
        a="{0:b}".format(int(n))
        length=len(a)
        Address=""
        while(length<12):
            Address=Address+"0"
            length=length+1
        PosNumToBin=Address+a
        return PosNumToBin   #Here were are returning a 12 bit binary string of the number when the number is  positive in Two's Complement
    else:
        a="{0:b}".format(int(-n))
        c=len(a)+1
        d="{0:b}".format(int(pow(2,c)+n)) #Here findind the binary representation of a negative number by the property that in binary
        length=len(d)                     #number in the sum of for example 2 and -2 we ignore the overflow
        Address=""                        #So in a five bit system the representation of -2 and 14 is same 
        while(length<12):
            Address=Address+"1"
            length=length+1
        NegNumToBin=Address+d
        return NegNumToBin      #Returning a 12 bit binary string of the number when the number is negative
#This is a function in which it converts a number into a binary string in 40 bits
#We will be using this function when we write the values to the registers AC,MQ which store a 40 bit data
def NumberToBinary40(n):
    if (n>=0):                     #When the number is greater than n or equal to n we find by binary representation
        a="{0:b}".format(int(n))
        length=len(a)
        Address=""
        while(length<40):
            Address=Address+"0"
            length=length+1
        PosNumToBin=Address+a
        return PosNumToBin       #Returning a string when the number is positive and the string consists of 40 bit binary representation
    else:                           #of the number
        a="{0:b}".format(int(-n))
        c=len(a)+1
        d="{0:b}".format(int(pow(2,c)+n))
        length=len(d)
        Address=""
        while(length<40):
            Address=Address+"1"
            length=length+1
        NegNumToBin=Address+d
        return NegNumToBin     #Returning a string when the number is positive and the string consists of 40 bit binary representation
                                 #of the number
#Here we are making a function which converts a binary number into 80 bit of data .We will use this function in MUL M(X) when the most 
#significant 40 bits gets stored in AC and the 40 least significant bits gets stored in MQ
def NumberToBinary80(n):
    if (n>=0):
        a="{0:b}".format(int(n))
        length=len(a)
        Address=""
        while(length<80):
            Address=Address+"0"
            length=length+1
        PosNumToBin=Address+a
        return PosNumToBin       #Returning a binary string for the positive number in 80 bit
    else:
        a="{0:b}".format(int(-n))
        c=len(a)+1
        d="{0:b}".format(int(pow(2,c)+n))
        length=len(d)
        Address=""
        while(length<80):
            Address=Address+"1"
            length=length+1
        NegNumToBin=Address+d
        return NegNumToBin     #Returning a binary string for the negative number in 80 bit
#This is a function used to convert the binary string in two's complement to the integer value
def TwoComplimentToNumber(s):
    s1=s[1:]
    a=len(s)
    n=int(s1,2)
    if (s[0]=="1"):       #This is the condition when the binary string given is of a negative number
        n=n-pow(2,a-1)
    return n              #Here we are returning a number
#This is the function of the assembler which will return the opcode of the instructions used in
#the programs
def assembler(a):
    if a==('LOAD MQ'):              #For example the opcode of the LOAD MQ is 00001010 we will return the value in the form of string
        return ("00001010")         #This are the Assembly instructions we will be using in the the programs
    elif a==('LOAD MQ,M(X)'):       #LOAD MQ,LOAD MQ,M(X),MUL M(X) will be used to multiply any two numbers
       return ("00001001")          #LOAD M(X) will be used when we read from the memory and store in AC
    elif a==('STOR M(X)') :         #STOR M(X) will be used when we write in the memory 
       return ("00100001")          #ADD M(X) and SUB M(X) do the normal arthemetic operations
    elif a==('LOAD M(X)'):
       return ("00000001")
    elif a==('JUMP M(X,0:19)'):
       return "00001101"
    elif a==('JUMP M(X,20:39)'):
       return "00001110"
    elif a==('ADD M(X)'):
       return "00000101"
    elif a==('SUB M(X)'):
       return "00000110"
    elif a==('MUL M(X)'):
       return "00001011"
#In this function the input is a instruction string and the output is the 40 bit binary number 
#In this function we use the function assembler and the function NumberToBinary which converts the Number to 12 bit binary
def I(Instruction):  
    count=0
    f=Instruction.split()                                      #It is splitting the given instruction in the list 
    if (len(f)==5 or len(f)==2):                               #If the length of the instruction is 5 or 2 then it must contain 'LOAD MQ' 
        if (Instruction=='LOAD MQ' and len(f)==2):             #If the instruction is "LOAD MQ" and the length of f is 2 
            return ("0000000000000000000000001010000000000000")#then there is single instruction so directly returning the 40 bit code
        elif (f[0]=="LOAD" and f[1]=="MQ"):                    #If the first instruction is "LOAD MQ" then finding out the the next instruction
            FI="00001010000000000000"                          #and returning the 40 bit code
            NI=f[2]+' '+f[3]
            NIopcode=assembler(NI)
            NIAddress=NumberToBinary(int(f[4]))
            return (FI+NIopcode+NIAddress)
        else:                                  #And the last case when the instruction "LOAD MQ" is in the last
            FI=f[0]+' '+f[1]                   #Finding the first instruction and returning the 40 bit code
            FIopcode=assembler(FI)
            FIAddress=NumberToBinary(int(f[2]))
            NI="00001010000000000000"
            return(FIopcode+FIAddress+NI)
                
    else:        
        for i in range (0,len(Instruction)):
            if (Instruction[i]==' '):                 #In this we are finding the index of the second space in the given instruction
                count=count+1                         #Finding the first instruction and after slicing storing in the variable
                if (count==2):                        #FirstInstruction and storing the left over instruction in Next
                    FirstInstruction=Instruction[0:i]
                    Next=Instruction[i+1:]
                    break
        a=Next.split(" ")                              #Spliting the next Instruction 
        if (len(a)==1 or len(a)==0):                   #If the length is 0 or 1 then there is only single Instruction so  
            NoFirstInstruction="00000000000000000000"  #the first 20 bits are 0's which is stored in NoFirstInstruction
            opcode2=assembler(FirstInstruction)
            Address2=NumberToBinary(int(a[0]))
            return(NoFirstInstruction+opcode2+Address2)
    
        else:
            NextInstruction=a[1]+' '+a[2]              #When there is more than one instuction i.e both left and right instruction
            opcode1=assembler(FirstInstruction)        #Finding the opcode of FirstInstruction using assembler function
            Address1=NumberToBinary(int(a[0]))         #Finding a 12 bit binary representation of the number
            opcode2=assembler(NextInstruction)         #The address of left instruction gets stored in a[0]
            Address2=NumberToBinary(int(a[3]))         #Finding opcode2 and address2 for the right instruction 
            return(opcode1+Address1+opcode2+Address2)
#The I function returns a 40 bit binary string which is corresponding to a given Instruction
#The function FetchAndDecoder decodes the instruction and performs the respective operations and store 
# them in the corresponing location        
def FetchAndDecoder(k):
        global AC         #We are globaling defining the Variables AC,MQ,MBR,PC so that it will not
        global MQ         #be lost in function calls.Finding the LHS and RHS Instruction and the 
        global MBR        #Opcode and the address of the LHS Instruction
        global PC         #Opcode is of 8 bits and address of 12 bits
        LHS=k[0:20]       #Converting the address into int             
        RHS=k[20:40]                
        LHSopcode=LHS[0:8]          
        LHSAddress=LHS[8:20]        
        BinaryToNumber=int(LHSAddress,2)
        #LOAD MQ,M(X)
        if (LHSopcode=="00001001"):                   #The opcode of LOAD MQ,M(X) is 00001001
            MBR=NumberToBinary40(M[BinaryToNumber])   #First the value in the memory location gets stored into MBR
            AC=0                                      #MBR contains the 40 bit binary string of the value in the memory location
            MQ=MBR                                    #AC has the garbage value assuming it to be 0
            print("MBR=",MBR)                         #The value from MBR goes to MQ
            print("MQ=",MQ)
        #MUL M(X) 
        elif (LHSopcode=="00001011"):                          #The opcode of MUL M(X) is 00001011
            Result=M[BinaryToNumber]*TwoComplimentToNumber(MQ) #Calculating the result by multipling two numbers              
            ResultBinary=NumberToBinary80(Result)              #Converting that into a 80 bit binary number 
            AC=ResultBinary[0:40]                              #40 most significant bits go into AC and 40 least significant bits
            MQ=ResultBinary[40:80]                             #go into MQ.MBR contains the 40 bit number
            MBR=NumberToBinary40(M[BinaryToNumber])
            print("AC=",AC)
            print("MBR=",MBR)
            print("MQ=",MQ)
        #LOAD MQ
        elif (LHSopcode=="00001010"):                    #The opcode of LOAD MQ is 00001010
            AC=MQ                                        #The value of MQ gets into AC
            print("MQ=",MQ)
            print("AC=",AC)
        #STOR M(X)
        elif (LHSopcode=="00100001"):                    #The opcode of STOR M(X) is 00100001
            M[BinaryToNumber]=TwoComplimentToNumber(AC)  #It stores the value of AC in the memory location
            print("AC=",AC)
            print(f'M[{BinaryToNumber}] = {AC}')
            print("MBR=",AC)
        #ADD M(X)
        elif (LHSopcode=="00000101"):                                                 #The opcode of ADD M(X) is 00000101
            MBR=NumberToBinary40(M[BinaryToNumber])                                   #The value from the memory location goes 
            AC=NumberToBinary40(TwoComplimentToNumber(AC)+TwoComplimentToNumber(MBR)) #into MBR
            print("MBR=",MBR)                                                         #AC=AC+MBR
            print("AC=",AC)
        #SUB M(X)
        elif (LHSopcode=="00000110"):                                                 #The opcode of SUB M(X) is 00000110
            MBR=NumberToBinary40(M[BinaryToNumber])                                   #The value from the memory location goes 
            AC=NumberToBinary40(TwoComplimentToNumber(AC)-TwoComplimentToNumber(MBR)) #into MBR
            print("MBR=",MBR)                                                         #AC=AC-MBR
            print("AC=",AC)
        #LOAD M(X)
        elif (LHSopcode=="00000001"):                          #The opcode of LOAD M(X) is 00000001 
            MBR=NumberToBinary40(M[BinaryToNumber])            #The value from the memory location gets stored in MBR
            AC=MBR                                             #From MBR it gets stored into AC
            print("MBR=",MBR)
            print("AC=",AC)
        if LHS!="00000000000000000000":                       #This is the case when there are both left and right instructions
            print("PC=",PC)                                   #Initially PC was defined as 1
            print("IR=",LHSopcode)
            print("IBR=",RHS)
            print("Left Instruction Completed")
            PC=PC+1                                          #Incrementing the value of PC
        print("-------------------------------------")       #Here the LEFT INSTRUCTION COMPLETES!!!!!!!
        RHSopcode=RHS[0:8]                   #Finding the opcode and address and the Binary to number of the address
        RHSaddress=RHS[8:20]                 #It was done using inbuild python function
        BinaryToNumber=int(RHSaddress,2)
        #LOAD MQ,M(X)
        if (RHSopcode=="00001001"):                    #The opcode of LOAD MQ,M(X) is 00001001    
            MBR=NumberToBinary40(M[BinaryToNumber])    #First the value in the memory location gets stored into MBR
            AC=0                                       #MBR contains the 40 bit binary string of the value in the memory location
            MQ=MBR                                     #AC has the garbage value assuming it to be 0
            print("MBR=",MBR)                          #The value from MBR goes to MQ
            print("MQ=",MQ)                            #MQ,MBR are 40 bit wide
        #MUL M(X) 
        elif (RHSopcode=="00001011"):                           #The opcode of MUL M(X) is 00001011
            Result=M[BinaryToNumber]*TwoComplimentToNumber(MQ)  #Calculating the result by multipling two numbers  
            ResultBinary=NumberToBinary80(Result)               #Converting that into a 80 bit binary number
            AC=ResultBinary[0:40]                               #40 most significant bits go into AC and 40 least significant bits
            MQ=ResultBinary[40:80]                              #go into MQ.MBR contains the 40 bit number
            MBR=NumberToBinary40(M[BinaryToNumber])
            print("AC=",AC)
            print("MBR=",MBR)
            print("MQ=",MQ)
        #LOAD MQ
        elif (RHSopcode=="00001010"):                  #The opcode of LOAD MQ is 00001010
            AC=MQ                                      #The value of MQ gets into AC     
            print("MQ=",MQ)                         
            print("AC=",AC)
        #STOR M(X)
        elif (RHSopcode=="00100001"):                   #The opcode of STOR M(X) is 00100001
            M[BinaryToNumber]=TwoComplimentToNumber(AC) #It stores the value of AC in the memory location
            print("AC=",AC)
            print(f'M[{BinaryToNumber}] = {AC}')
            print("MBR=",AC)
        #ADD M(X)
        elif (RHSopcode=="00000101"):                                                #The opcode of ADD M(X) is 00000101
            MBR=NumberToBinary40(M[BinaryToNumber])                                  #The value from the memory location goes
            AC=NumberToBinary40(TwoComplimentToNumber(AC)+TwoComplimentToNumber(MBR))#into MBR
            print("MBR=",MBR)                                                        #AC=AC+MBR
            print("AC=",AC)
        #SUB M(X)
        elif (RHSopcode=="00000110"):                                                #The opcode of SUB M(X) is 00000110
            MBR=NumberToBinary40(M[BinaryToNumber])                                  #The value from the memory location goes
            AC=NumberToBinary40(TwoComplimentToNumber(AC)-TwoComplimentToNumber(MBR))#into MBR
            print("MBR=",MBR)                                                        #AC=AC-MBR
            print("AC=",AC)
        #LOAD M(X)
        elif (RHSopcode=="00000001"):                                     #The opcode of LOAD M(X) is 00000001
            MBR=NumberToBinary40(M[BinaryToNumber])                       #The value from the memory location gets stored in MBR
            AC=MBR                                                        #From MBR it gets stored into AC
            print("MBR=",MBR)
            print("AC=",AC)
        print("PC=",PC)   
        print("IR=",RHSopcode)
        print("IBR=",RHS)
        if (LHS=="00000000000000000000"):                       #If there is only one instruction then now we are incrementing PC
            PC=PC+1                              
        print("<--------INSTRUCTION COMPLETED--------->")       #INSTRUCTION COMPLETED!!!!!


#MAIN CODE
M=[None]*1000
print("1----->Calculating n+n^2+n^3+m+m^2+m^3")                              #I am performing two functions n+n^2+n^3+m+m^2+m^3
print("2----->Finding the n element of the series T(n)=T(n-1)+T(n-2)+T(n-3)")#and a recursive function T(n)=T(n-1)+T(n-2)+T(n-3)
query=int(input())
if (query==1):
    M[0]=int(input())                    #In the first one i will be taking two inputs n and m and saving it in memory location
    M[1]=int(input())                    #and in the variables Num1 and Num2
    Num1=M[0]
    Num2=M[1]
else:
    M[0]=int(input())                   #In the second one i will be taking  three inputs which will be stored in M[0],M[1],M[2]
    M[1]=int(input())                   #I will take the input for the nth term of the series
    M[2]=int(input())
    Jumpcounter=int(input())
    Num1=M[0]
    Num2=M[1]
    Num3=M[3]
    Jump=Jumpcounter
PC=1                               #Initialising PC as 1
InstructionList=[]    
Instruction=input()
while(Instruction!="HALT"):      #Till the instruction is HALT which has a opcode=00000000 we store the 40 bit
    a=I(Instruction)             #in a list called InstructionList
    InstructionList.append(a)
    Instruction=input()
InstructionIndex=0               #Lets Initialise the Insr=truction Index as 0
while(InstructionIndex<len(InstructionList)):                                    #Till the instruction Index is less than length of
    if (InstructionList[InstructionIndex][20:28]=="00001101" and Jumpcounter>0): #Instruction List we have to use the for loop
        FetchAndDecoder(InstructionList[0])                                      #If we encounter the jump instruction and the JumpCounter
        Jumpcounter=Jumpcounter-1                                                #is greater than 0 we have to repeat the entire Instructions
        InstructionIndex=0                                                       #Set Then we maintain a JumpCounter to end the loop
    else:                                                                        #In the recursive Function I am performing The JUMP CONTER
        FetchAndDecoder(InstructionList[InstructionIndex])                       #is the nth element of the the series
    InstructionIndex=InstructionIndex+1
if (query==1):                                                                     
    print(f'The given numbers where {Num1} and {Num2}')
    print(f'The value of the operation was {M[6]}')
else:
    print(f'The given numbers where {Num1},{Num2} and {Num3}')
    print(f'The {Jump}th number of the series is {M[6]}')



        
       