
'''Funções Auxiliares:'''

def hamming_weight(a, b): 
    return (a^b).count(True)


'''Colocar os bits da palavra x na palavra codigo y'''

def setunParityBits(x,y):
    
    k=0
    for i in range(len(y)):
        if not ((i & (i-1) ==0)) and i!= 0:
            y[i] = x[k]
            k+=1
    return y


'''
Definir os parity bits. 
Eles são definidos de tal modo que o xor de todos os bits resulta do xor dos bits que tem 1  numa dada posiçao
Exemplo: H(7,4)
p1 = xor de todos os bits que estejam na posicao (**1)
p2 = xor de todos os bits que estejam na posicao (*1*)
p3 = xor de todos os bits que estejam na posicao (1**)
'''

# def setParityBits(y):
    
#     for i in range(1,len(y)):
    
#         value = 0
#         bit1=BitArray(int=i,length=len(y))
#         bit1_reversed = bit1[::-1]
#         position_1_bit_1 = list(bit1_reversed.findall('0b1')) # terá sempre apenas 1 posição
        
#         if (i & (i-1)==0):
            
#             for j in range(1+i,len(y)):
                
#                 if not (j & (j-1) == 0):
                    
#                     bit2=BitArray(int=j,length=len(y))
#                     bit2_reversed= bit2[::-1]
                    
#                     position_2_bit_2 = list(bit2_reversed.findall('0b1'))
                    
#                     for m in range(len(position_2_bit_2)):
#                         if position_1_bit_1[0] == position_2_bit_2[m]:
                            
#                             #print("computing XOR of",value,"with y[",j,"],",y[j])
                            
#                             value = value ^ y[j]
                            
#                              #print("which gives",value)
#             #print("So y[",i,"]=",value)
#             y[i] = value
#     return y.bin



def setParityBits(y):
    
    for i in range(1,len(y)):
        
        value = 0
        
        if (i & (i-1) == 0):
            
            for j in range(i+1,len(y)):
                #print("i=",i,"j=",j,"i&j==",i&j)
                if i & j == i:
                    #print("for the bit in position",i,"making the XOR between:", value, "and t[",j,"]=",y[j])
                    value = value ^ y[j]
                    #print("which is:",value)
            y[i] = value
    return y