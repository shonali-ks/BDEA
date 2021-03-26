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
    str=""
    for i in range(0,len(bits),8):
        y=chr(int(bits[i:i+8],2))
        str+=y
    return str

   


def DNA_coding_decrypt(a,cea_list):
    Com_strn=""
    KEY_COM=[]
    for i in range(0,len(cea_list),4):
        r=""
        r=cea_list[i:i+4]
        KEY_COM.append(r)
    decr_li=["AA","AT","AG","AC","TA","TT","TG","TC","GA","GT","GG","GC","CA","CT","CG","CC"]
    res = {} 
    for key in KEY_COM: 
        for value in decr_li: 
            res[key] = value 
            decr_li.remove(value) 
            break 
   
    for i in range(0,len(a),4):
        d=str(res.get((a[i:i+4])))
        
        Com_strn+=d

    DNA_code={
        "A":"00",
        "T":"01",
        "G":"10",
        "C":"11"    
        }
    DNA_decoded_strn=""
    for i in Com_strn:

        DNA_decoded_strn+=str(DNA_code.get(str(i)))
    
    return DNA_decoded_strn    
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def power(x,y,n):
    temp = 0
    if (y == 0):
        return 1
    temp = power(x, int(y / 2),n)
    if (y % 2 == 0):
        return ((temp%n)*(temp%n))%n;
    else:
        return ((x%n)*(temp%n)*(temp%n))%n;
def decimalToBinary(n):
    return '{0:08b}'.format(n)
def start_decrypt(Encrypted_strn):
    kee=Encrypted_strn.split('/')
    e=text_from_bits(kee[0])
    c=kee[1]
    c_1=kee[2]
    c_2=kee[3]
    
    Encrypted_strn=kee[4]
    p =35089
    q =49031
    n = p * q
    phi = (p-1) * (q-1)
  
       
    d = modInverse(int(e),phi)
    
    be=""
    d_1=power(int(text_from_bits(c)),d,n)%n
    d_2=power(int(text_from_bits(c_1)),d,n)%n
    d_3=power(int(text_from_bits(c_2)),d,n)%n
    if(len(str(d_1))==8):
        d_1='0'+str(d_1)
    if(len(str(d_1))==7):
        d_1='00'+str(d_1)
    if(len(str(d_2))==8):
        d_2='0'+str(d_2)    
    if(len(str(d_2))==7):
        d_2='0'+str(d_2)
    if(len(str(d_3))==8):
        d_3='0'+str(d_3)    
    if(len(str(d_3))==7):
        d_3='0'+str(d_3)
    
   
    be+=(str(d_1)+(str(d_2)+str(d_3))) 
    
    ans="" 
    for i in range(0,len(be),3):
        ans+=str(decimalToBinary(int(be[i:i+3])))
    
    cea_list=""
    cea_list=ans[0:64]
    key=""
    key=ans[64:72]
    mess=""
    mess=Encrypted_strn
    z=8
    y=0
    
    Decrypt_Binary=DNA_coding_decrypt(mess,cea_list)
    while z<=len(Decrypt_Binary):
        kb=Decrypt_Binary[y:z]
        xored=xor(key,kb,len(key))
        key+=xored
        y=z
        z+=len(key)
    
    ans=text_from_bits(key)
    ans=ans.split('%') 
    return ans[0]

# syr="00110001001101010011000000110101001101110011010100110000001101010011010100110001/0011100000111000001100010011000000110011001100010011001000110111/00110001001101100011001100110111001110010011000100110111001110000011010000110011/001110010011010100110100001110000011010100110000001101010011000100111000/11110000111100001111001111111101010111001111000011111000100100011001101011110000111100111111001101010010111111010101011011111111111111101001101010010110111111010101110011110000111110001001011001101000111111111111111010011010100101101111110101011100111100001111001111110011010100101111110101010110100100011001001010010001100110101111000011110011111100110101001011111101010101101001000110010010100100011001101011110000111100111111001101010010111111010101011010010001100100101001000110011010111100001111001111111101010111001111000011111000100101100110100001010100010111110110001001100010010101000101111001011110010110000101100011110110010101000101111101100010011000100101010001011110010111100101100001011000111101100101010001011111011000100110001001010100010111100101111001011000010110001111011001010100010111110110001001100010010101000101111001011110010110000101100011110110010101000101111101100010011000100101010001011110010111100101100001011000111101100101010001011111011000100110001001010100010111100101111001011000"
# print(start_decrypt(syr))



