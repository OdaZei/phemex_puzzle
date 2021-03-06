"""
Outputs all permutations of words dictionary , with correct lenght (27-digits) + 21-prime
base="abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ" --> base string inspired on base58 string format--->
"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

NOTE THAT THERE ARE TWO POSSIBLE ANSWERS AS I GROUP THE 27-DIGIT NUMBER AS THE SOLUTION OF THE PERMUTATION , AND ADD(STRING ADDITION) THE 21-DIGIT PRIME
EXAMPLE:
21-DIGIT-PRIME + 27-DIGIT-PRIME OR 27-DIGIT-NUMBER + 21-DIGIT-PRIME
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
