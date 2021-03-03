import random
import math
def xor(a, b, n):
    ans = "" 
    for i in range(n):  
        if (a[i] == b[i]):  
            ans += "0"
        else:  
            ans += "1"
    return ans 

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0' 
def decimalToBinary(n): 
    return bin(n).replace("0b", "")

def DNA_coding_encrypt(a,random_k):
    
    DNA_code={
    "00": "A",
    "01": "T",
    "10": "G",
    "11": "C"
      }
    n=len(a)
    DNA_CODED_STR=""
    for i in range(0,int(n),2):
        c=""
        c=str(xored_str[i:i+2])
        DNA_CODED_STR+=str(DNA_code.get(str(c)))
      
    KEY_COM={
        "AA": 0,
        "AT": 1,
        "AG": 2,
        "AC": 3,
        "TA": 4,
        "TT": 5,
        "TG": 6,
        "TC": 7,
        "GA": 8,
        "GT": 9,
        "GG": 10,
        "GC": 11,
        "CA": 12,
        "CT": 13,
        "CG": 14,
        "CC": 15
        }
    val=list(KEY_COM.values())
    KEY_BIN=[]
    for i in val:
        binary=str(decimalToBinary(i))
        x=len(binary)
        for j in range(0,4-x):
            binary="0"+binary
        KEY_BIN.append(binary)
    random.shuffle(KEY_BIN)


    EXP_STR=""
   
    for i in range(0,int(n/2),2):
        d=KEY_COM.get((DNA_CODED_STR[i:i+2]))
       
        EXP_STR+=str(KEY_BIN[d])
    return EXP_STR    


  



        


def start_encrypt(str1):
    n=len(text_to_bits(str1))
    wq=math.ceil( float(math.log(n)/math.log(2)))
    y=int((math.pow(2,wq)-n)/8)
    for i in range(0,y,1):
        str1+="%"
    res=text_to_bits(str1)
    n=len(res)
    z=8
    key=res[0:z]
    xored_str=""
    cr=math.pow(2,wq)
    while z<cr:
        ka=res[0:z]
        kb=res[z:2*z]
        xored=xor(ka,kb,z)
        xored_str+=xored
        z+=z
    random_k=random.randint(0,15)
    Encrypted_strn=DNA_coding_encrypt(xored_str,random_k)
    return Encrypted_strn
  




