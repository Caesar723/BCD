
def convert(iin):
    a=[]
    get=iin
    while get>0:
        get=int(get/10)
        a.append(get)
    bi=DB(iin)
    string=''

    for aa in range(0,len(a)):
        for ii in range(0,a[aa]):
            bi=(bin(int(bi,2)+int("0110"+("0000"*aa),2))[2:])
            #print(bi)
    ar = addO(bi)
    for iiii in bi:
        ar.append(iiii)
    for iiiii in range(0,len(ar)):
        if iiiii%4==0:
            string=string+" "
        string=string+ar[iiiii]
    print(string)
def addO(binary):

    array=[]
    if (4-len(binary)%4)!=4:
        for iii in range(0,4-len(binary)%4):
            array.append("0")
    return array
def DB(val):
    a=val
    arr=[]
    st=''
    while (a>=1):
        b=a%2
        a=a/2
        arr.append(str(int(b)))
    #print(arr)
    for i in range(0, len(arr)):
        st=st+arr[len(arr)-i-1]
    return st




def BD(binary):
    den=0
    for c in range(0,len(binary)):
        if(binary[len(binary)-c-1]=="1"):
            den=den+2**c
    #print(den)
    return den
def twescomplement(binary):
    string=""
    for cc in binary:
        if cc=="1":string=string+"0"
        else:string=string+"1"
    return DB(BD(string)+1)

def fromBCD(bi):
    Farr=addO(bi)
    for bb in bi:
        Farr.append(bb)
    decade=[]
    String=""
    char=""
    #print(Farr)
    for b in range(1,int((len(Farr)/4))+1):
        for bbb in range(0,(int((len(Farr)))-4*b)):
            String = String + Farr[bbb]
            #print(String)
            if (bbb+1)%4==0 and bbb!=0:
                char =char+str(BD(String))
                #print(char)
                String=""

        #print(int((len(Farr)))-4*b)
        decade.append(char)
        char = "0"
    com=twescomplement(bi)
    #print(decade)
    for bbbb in range(0,len(decade)):
        for bbbbb in range(0,int(decade[bbbb])):
            com = (bin(int(com, 2) + int("0110" + ("0000" * bbbb), 2))[2:])
    #print(complement(com))
    return twescomplement(com)
convert(398)
print(fromBCD("111001100"))
print(BD(fromBCD("1110011000")))