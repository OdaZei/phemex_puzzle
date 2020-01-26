from itertools import permutations as prm
import base58 as b58
import bitcoin as btc
####################################################################################################################333
prime="957496696762772407663"
words =["First","21digit","prime","found","in","consecutive","digits","of","e","Bitcoin","Ripp1e","Ethereum","Phemex","Satoshi","Dorian","Nakamoto"]
number =[]
match = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
digit=[]
w=[]
pp=""
######################################################################################################################333
def add_prime_as_string():
    for i in digit:
        w.append(prime+i)
        w.append(i+prime)
def multiply_prime_as_integer():
    for i in digit:
        w.append(int(prime)*int(i))
def b58_encode():
    for i in words :
        decoded=b58.b58decode(i).hex()
        number.append(decoded)
def be_Ascii():
    global number
    number=[]
    decoded=""
    for word in words:
        for i  in word:
            decoded += str(ord(i))
            number.append(decoded)
        decoded=""
def permute():
    global pp
    perm = prm(number,2)
    for p in perm:
        for num in p:
            pp+=num
        xd=str(int(pp,16))
        if(len(xd)==27):
            digit.append(xd)
        pp=""
def add_prime_as_integer():
    global w
    w=[]
    for i in digit: 
        w.append(int(prime)+int(i))
def _get_wallet_sha256():
    for i in w:
        HEX=btc.encode_privkey(btc.sha256(str(i)),"hex")
        addr=btc.privtoaddr(HEX)
        if(addr==match):
            print(WIF)
        else:
           print(addr)

be_Ascii()
permute()
multiply_prime_as_integer()
_get_wallet_sha256()
add_prime_as_integer()
_get_wallet_sha256()
    

