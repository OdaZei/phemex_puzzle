import bitcoin as b
prime=957496696762772407663
_27_digit_prime=[100001001101111111011101001,
100000109999990000011000001,
102030040005000006000000007,
102030040005000006000000007, #--->The smallest prime P formed from the concatenation of five consecutive tban numbers in the pattern {a, b, c, d, e, d, c, b, a}
111113333355555777779999929, #-->The only prime formed by inserting in ascending order, between the digits of a double-digit number n
121208284196421093429539251,
123456789012343210987654321,
135791113151719212325272931,#-->all odd numbers until 31 form a prime
149907114776274341482621993,
197352587024076973231046657,
211223227229233239241251257,
211233331113965338635107311,
213669322811313867625389733,
232222222222222222222222223,
234567234567345674567567677,
339341355381394398413415437,
390714505091666190505417093, #-->Double prime in base 10 and 2:10 100 001 100 110 001 000 000 111 100 001 100 011 000 111 011 100 011 000 110 000 111 100 000 010 001 100 110 000 101
397178329714159534771298317,#
599966117492747584686619009,#-->Smallest Carmichael number
618970017336847128235868159,#-->The number of positive integers between the 9th and 10th Mersenne primes is prime
618970019642690137449562111,#-->The smallest Mersenne prime containing all of the digits from 0 to 9
666666444488888888999999999, #-->The largest prime with each composite digit d repeated d times. 
742950290870000078092059247, #-->
766303535475945713821785251, #-->The first 27-digit prime to occur in the decimal expansion of e. Curiously, it is also an emirp
77777777777713131313131313, #-->Thirteen 7's followed by seven 13's is prime. "Lucky 7" and "Unlucky 13"
859935929762876868984659981,#---> The smallest non-trivial prime of the form n^13 + 13
897777777777777777777777689]
def dictionary():
    for i in _27_digit_prime:
        p=str(i)+str(prime)
        
        print(str(p)+" "+str(len(p))+b.privtoaddr(int(p))+"\n"+p[::-1]+" "+str(len(p))+" "+b.privtoaddr(int(p[::-1])))
        
dictionary()
