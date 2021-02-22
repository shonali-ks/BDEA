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

   


def DNA_coding_decrypt(a,random_k):
    Com_strn=""

    KEY_COM={
        "0101":0,
        "0011":1,
        "0001":2,
        "0010":3,
        "0110":4,
        "1111":5,
        "0111":6,  
        "1001":7,
        "1010":8,
        "0100":9,
        "1000":10,
        "1100":11,
        "1110":12,
        "1011":13,
        "0000":14,
        "1101":15
        }

    decr_li=["AA","AT","AG","AC","TA","TT","TG","TC","GA","GT","GG","GC","CA","CT","CG","CC"]

    for i in range(0,len(a),4):
        d=int(KEY_COM.get((a[i:i+4])))
        # print(d)
        Com_strn+=str(decr_li[((d))])

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



        







def start_decrypt(Encrypted_strn):
    Decrypt_Binary=DNA_coding_decrypt(Encrypted_strn,random_k)
    z=8
    l=0
    while z<cr:
        ka=Decrypt_Binary[l:l+z] 
        xored=xor(ka,key,z)
        key+=xored
        l+=z
        z*=2
    ans=text_from_bits(key)
    return ans



