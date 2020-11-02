from bitstring import BitArray,BitStream
import operator as op
from functools import reduce
from auxfunctions import hamming_weight,setunParityBits,setParityBits


def encode(r,s):
    
    k = 2**r-r-1
    n = 2**r-1
    
    print("Encoding message s=",s.bin,"for H(",n,",",k,"):")
    #Inicializar t
    
    t = BitArray(n+1) # Adicionar o bit t[0]
    
    '''Primeiro temos de popular t com os bits de s
    que são os bits que se encontram nas posições que NÃO são potências de 2 '''
    
    setunParityBits(s,t)
    
    #print("After setting unparity bits, t=",t.bin)
    
    '''Depois popular t nas posições que são potência de 2 de acordo com os testes de paridade'''
    
    setParityBits(t)
    
    #print("After setting parity bits, t=",t.bin)
    '''Se a soma de todos os bits 1 for ímpar, adicionar bit 1 na posição 0'''

    if sum(t) % 2 == 0:
        t[0] = 0
    else:
        t[0] = 1
        
    
    print("Message was successfully encoded!, t =",t.bin)
    
    return t


def decode(r,u,t):


    if hamming_weight(t,u) == 1: # Hamming distance is one, there was an error!

        wrong_bit=reduce(op.xor,list(u.findall('0b1')))

        print("The Hamming distance between u and t is 1, so there was an error in position:", wrong_bit, "\n")

        if u[wrong_bit] == 0:
        
            u[wrong_bit] = 1
        
        else:
            
            u[wrong_bit] = 0
            print("Correcting wrong bit...\n")
            print("Corrected! The original message was",u.bin,"\n")
        
    elif hamming_weight(t,u) == 0: # There was no error
        
        print("The Hamming distance is 0, noise didn't add any error! \n")
    
    else:
        print("The Hamming distance is greater than 1, we cannot decode message u correctly! \n")


'''
r numero de bits reduntantes
k numero de bits que serao codificados
n numero de bits depois de serem codificados

OK, a posição 0 de t vai ser uma posição auxiliar.

for r in range(3,10,1):
    print(r,2**r-1,2**r-r-1)

3 7 4
4 15 11
5 31 26
6 63 57
7 127 120
8 255 247
9 511 502
'''
