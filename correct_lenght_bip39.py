import pprint
import binascii
import mnemonic
import bip32utils
from itertools import permutations as pmt
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
perm = pmt(words)
def bip39(ss:str):
    mobj = mnemonic.Mnemonic("english")
    seed = bytes(ss,"utf-8")
    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    for i in range(10):
        bip32_child_key_obj = bip32_root_key_obj.ChildKey(44
                                                        + bip32utils.BIP32_HARDEN).ChildKey(0
                                                        + bip32utils.BIP32_HARDEN).ChildKey(0
                                                        + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(i)
        priv_key={
                    'seed': seed,
                    'bip32_root_key': bip32_root_key_obj.ExtendedKey(),
                    'bip32_extended_private_key': bip32_child_key_obj.ExtendedKey(),
                    'path': "m/44'/0'/0'/{}".format(i),
                    'addr': bip32_child_key_obj.Address(),
                    'publickey': binascii.hexlify(bip32_child_key_obj.PublicKey()).decode(),
                    'privatekey': bip32_child_key_obj.WalletImportFormat(),
                    'coin': 'BTC'
                    }
        if(priv_key["addr"]==match):
            print(priv_key)
            print(("BINGO"+"\n")*64)
                
        print(priv_key['path']+"\n"+priv_key['privatekey']+"\n"+"*"*64)
    
def find_base(solt:str):
    stt=""
    for i in solt:
        for j in base:
            if(i==j):
                stt+=str(base.find(j))
    if(len(stt)==partial):
        return  str(stt)

for i in perm:
    for j in i:
        word = words[j]
        solution+=word
    tt=find_base(solution)
    bip39(prime+tt)
    bip39(tt+prime)
    solution = ""

