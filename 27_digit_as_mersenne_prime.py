#Check childs of bip39 with seed as bytes of 21-digit prime and 27-digit Merssene prime
import itertools as it
import pprint
import binascii
import mnemonic
import bip32utils
import bitcoin as btc
primes=["618970019642690137449562111","957496696762772407663"]
match = "1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT"
actual_str=""
perm= it.permutations(primes)
def bip(seed_string:bytes):
    mobj = mnemonic.Mnemonic("english")
    seed = seed_string
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
        print(priv_key)
    if(priv_key["publickey"]==match):
        print(priv_key)
        print(("BINGO"+"\n")*64)
                
    print(priv_key['path']+"\n"+priv_key['privatekey']+"\n"+"*"*64)
for i in perm:
    for j in i:
        actual_str+=j
    print(bip(bytes(actual_str,"utf-8")))
    actual_str=""
        
#Nothingg
