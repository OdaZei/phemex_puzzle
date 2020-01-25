import pprint
import binascii
import mnemonic
import bip32utils
import bitcoin as b
from itertools import permutations 
solution = ""
match = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
partial=""
words = {
    "0":"BITCOIN",
    "1":"ETHEREUM",
    "2":"RIPPLE",
    "3":"PHEMEX"
}
string ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime="957496696762772407663"
word=""
def bip39(ss:str):
    mobj = mnemonic.Mnemonic("english")
    seed = bytes(ss,"utf-8")

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    for i in range(30):
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
                 if(priv_key["publickey"]==match):
                     print(priv_key)
                     print(("BINGO"+"\n")*64)
                
                 print(priv_key['path']+"\n"+priv_key['privatekey']+"\n"+"*"*64)
  
perm = permutations(words,4)
def search_index(st : str):
    for n in range(len(string)-1):
        if string[n] == st:
            return n      
for i in perm:
    solution=""
    for j in i:
        word=words[str(j)]
        partial=""
        for k in word:
            partial+= str(search_index(k))
        solution+=partial
        partial=""
    ss=str(prime+solution)
    print(bip39(ss))


