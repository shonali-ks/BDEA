from random import getrandbits
from random import randint
import sys
def get_prime():
    n = getrandbits(12) + 3;
        if(is_prime(n)):
            return n
def is_prime_calc(num):
    return all(num % i for i in range(2, num))

def is_prime(num):
    return is_prime_calc(num)
q=get_prime()
def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def primitive_root(modulo):
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            return g
g = primitive_root(p)
private_a=23
private_b=13
public_a=pow(g, a_private) % p
public_b=pow(g,b_private) % p
key_a=pow(public_b, private_a) % p
key_b=pow(public_a, private_b) % p
