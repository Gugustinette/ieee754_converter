# ieee754_converter
Simple IEEE754 Convert in Python
One file for encoding, one file for decoding

In both files, you need to specify the total number of bytes, and number of bytes dedicated to exponent
These 2 values are in the first lines of each files, called "bytes_total" and "bytes_expo"

Encode file also needs you to specify the mode which will be used.
There are 2 modes :

  1 - Decimal Input, which takes a decimal number on run, int or float, no matter
  
  2 - Binary Input, which takes a binary number on run, either int or float, negative or positive,...
  
 All you need to do is to change the variable called "mode" to 1 or 2, depending on the mode you want to use.
 
 Decode file only has one mode, it just takes one IEEE754 binary on run
 
 Thanks.
 
 Augustin MERCIER "Gugustinette"
