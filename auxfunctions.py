
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