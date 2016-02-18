import sys
import binascii

f = open(sys.argv[1], "rb")
fw = open("utf8encoder_out.txt", 'ab')
 
 

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
     
     
     
def str2bin(chain):
    return ''.join((bin(ord(c))[2:].zfill(8) for c in chain))


def getbit(n, i):
    if n & (1 << i) > 0:
        return "1"
    else:
        return "0"
 
deleteContent(fw)

print ("converting")
try:
    byte = f.read(2)
       
    mainstring=""
    while byte != "":
       
        y=binascii.hexlify(byte)
        x=str2bin(byte)
        z=int(x, 2)
        
        #print "ppp "+y+" ppp"+"  "+x
        
        UTFformat=""
        
        if int(y,16) <= 127:
            UTFformat="0vvvvvvv"
        elif int(y,16) <= 2047:
            UTFformat="110vvvvv10vvvvvv"
        elif int(y,16) <= 65535:
            UTFformat="1110vvvv10vvvvvv10vvvvvv"
    
    
        
        j=0
        str=""
        i=len(UTFformat)-1
        
        while i > -1:
            
            if UTFformat[i] == 'v':       
                str= str+getbit(z, j)
                j=j+1
            else:
                str=str+UTFformat[i];
            i=i-1   
        
        str=str[::-1]
        #print str
        
        
        
        
        
        if len(str) == 8:
           n=int(str,2)
           w=chr(n)
           fw.write(w)
         
        elif len(str) == 16:
           s1=str[0:8]
           n=int(s1,2)
           w=chr(n)
           fw.write(w)
           s1=str[8:16]
           n=int(s1,2)
           w=chr(n)
           fw.write(w)
           
        elif len(str) == 24:
           s1=str[0:8]
           n=int(s1,2)
           w=chr(n)
           fw.write(w)
           s1=str[8:16]
           n=int(s1,2)
           w=chr(n)
           fw.write(w)
           s1=str[16:]
           n=int(s1,2)
           w=chr(n)
           fw.write(w)
           
           
        byte = f.read(2)
   
finally:
    print ("End")
    f.close()
    
    
    
    
