import ecdsa
import binascii
import base58
import hashlib
from itertools import permutations as pmt
"//////////////////////////////////////////////////////////////////////////////////"
global filepath
global kk
"//////////////////////////////////////////////////////////////////////////////////"
solution = ""
match = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
partial=27
words = {
    "0":"BTC",
    "1":"ETH",
    "2":"XRP",
    "3":"Phemex"
}
prime="957496696762772407663"
base="abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"


"///////////////////////////////////////////////////////////////////////////////////////"
class GenAddressGivenInteger():
    def __init__(self,i):
        self.value = i
        self.integer = self.correct_lenght()
        self.private = self.get_PrivateKey()
        self.pubKey = self.get_PublicKey()

    def correct_lenght(self):
        """
        Adjust size of key to 32 bytes  lenght key
        eack key iis a combination of a permutation 
        in words dict order 
        """
        return int.to_bytes(self.value,32,"big")
        
    def rimped160(self,x):
        hash160 = hashlib.new('ripemd160')
        hash160.update(x)
        return hash160
    def get_PrivateKey(self):
        key = "00" + binascii.hexlify(self.integer).decode()
        sha256_one = hashlib.sha256(binascii.unhexlify(key)).hexdigest()
        sha256_two = hashlib.sha256(binascii.unhexlify(sha256_one)).hexdigest()
        WIF = base58.b58encode(binascii.unhexlify(key + sha256_two[:8]))
        return WIF.decode()
        
    def get_PublicKey(self):
        signed_key = ecdsa.SigningKey.from_string(self.integer,curve=ecdsa.SECP256k1)
        verifying_key = signed_key.get_verifying_key()
        public_key = "04" + binascii.hexlify(verifying_key.to_string()).decode()
        hash160 = self.rimped160(hashlib.sha256(binascii.unhexlify(public_key)).digest()).digest()
        public_addr_one = b"\x00" + hash160
        checksum = hashlib.sha256(hashlib.sha256(public_addr_one).digest()).digest()[:4]
        public_addr_two = base58.b58encode(public_addr_one + checksum)
        return public_addr_two.decode()

   
def find_base(solt:str):
    stt=""
    for i in solt:
        for j in base:
            if(i==j):
                stt+=str(base.find(j))
    if(len(stt)==partial):
        return  str(stt)
"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
perm = pmt(words)

for i in perm:
    for j in i:
        word = words[j]
        solution+=word
    tt=find_base(solution)
    addr_one = GenAddressGivenInteger(int(prime+tt))
    addr_two = GenAddressGivenInteger(int(tt+prime))
    if(addr_one.pubKey == match or addr_two.pubKey== match):
        print((addr_one.private +"   "+addr_two.private)*100)
        print(addr_one.pubKey + "  "+addr_two.pubKey)
        break
    solution = ""
    print(addr_one.pubKey + "  "+addr_two.pubKey+"\n"+"/"*80)
