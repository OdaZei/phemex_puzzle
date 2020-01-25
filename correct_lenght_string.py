"""
Outputs all permutations of words dictionary , with correct lenght (27-digits) + 21-prime
"""

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
    print((prime+tt)+"  "+str(len(tt+prime)))
    solution = ""
