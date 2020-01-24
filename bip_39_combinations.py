import pprint
import binascii
import mnemonic
import bip32utils
from itertools import permutations 
solution = ""
match = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
partial=""
words = {
    "0":"BTC",
    "1":"ETH",
    "2":"XRP",
    "3":"PHEMEX"
}
#main problem??
string ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime="957496696762772407663"
word=""
def bip39(ss:str):
    mobj = mnemonic.Mnemonic("english")
    seed = bytes(ss,"utf-8")

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)
    return {
            'seed': seed,
            'bip32_root_key': bip32_root_key_obj.ExtendedKey(),
            'bip32_extended_private_key': bip32_child_key_obj.ExtendedKey(),
            'path': "m/44'/0'/0'/0",
            'addr': bip32_child_key_obj.Address(),
            'publickey': binascii.hexlify(bip32_child_key_obj.PublicKey()).decode(),
            'privatekey': bip32_child_key_obj.WalletImportFormat(),
            'coin': 'BTC'
            })
perm = permutations(words,3)
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


