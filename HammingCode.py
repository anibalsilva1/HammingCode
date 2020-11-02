from codingfunctions import encode,decode
from bitstring import BitArray


'''
r is the number of redundant bits
k is the number of bits in the original message
n is the number of bits of the encoded message


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

r = int(input("The number of redundant bits r is \n"))


message = input("Please insert the message of at least size k = {} that you want to send \n".format(2**r-r-1))


message = BitArray(bin=message)

t = encode(r,message)

u = input("What was the received message?\n")

u = BitArray(bin=u)

decode(r,u,t)