# phemex_puzzle
My main idea is to use the Big Integer formed by "957496696762772407663" and a 27-digit number ,as the seed of a 
BIP-39 HD cold wallet.
The next step is the 27-digit number :
In the hits says is formed by some words from Satoshis portrait:
Each word is caged in a closed maze  except the "First 21-digit prime found in consecutive digits of e" expresion which leads out .
The list i understand is: BTC/Bitcoin , ETH/Ethereum,XRP/Ripple,Phemex.
so the words are pretty clear , i permuted them to get all combinations in words_combinations.py .
The next question is:How to transform them in a 27-digit number, without I/O?
Ive taked several approaches as :
Use of an encoding string of all posible letters and assign the position on the string as the integer.
Use Ascii encoding , leads to long string as lowercase values take a 3-digit number.


