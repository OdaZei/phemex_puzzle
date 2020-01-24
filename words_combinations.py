import bitcoin as b
from itertools import permutations 
solution = ""
partial=""
words = {
    "0":"XRP",
    "1":"ETH",
    "2":"BTC",
    "3":"PHEMEX",
}
string ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime=  "957496696762772407663"
word=""
//change to perm = permutations(words) , to get full dict permutations
perm = permutations(words,3)
//i--> print to get each permutation form
for i in perm:
    solution=""
    //each item in the permutation
    for j in i:
    //use it as dict keyword
        word=words[str(j)]
        partial=""
        //search for ascii numeriacal value
        for k in word:
            partial+= str(ord(k))
        solution+=partial
        print(word +" : "+partial)
    //prints solution as all partial ascii characters in each word
    print(solution)
    print("-"*64)
