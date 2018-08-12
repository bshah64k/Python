# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%

def IsPalindrome(num):
###
### Checks whether input num is a palindrome - num is a positive integer
### Returns True or False
###
    pstr = str(num)
    i = 0
    j = len(pstr) - 1
    
    while (i <= j):
        
        if (pstr[i] != pstr[j]):
            return False
 
# Note  - we use two iterators - one going forward, one backwards        
        i += 1
        j -= 1
#  End of While loop - you drop out - you could use Else associated to While       
    return True

#%%
def LargestPalindrome(maxnum):
##
##  Returns largest Palindrome that is possible from product of 2 integers
##  up to maxnum   
## e.g. LargestPalindrom (25) -> 575 which is product of 25 * 23 and each
## of 25 and 23 are maxum 25 or less... 
## 

## Algorithm can be optimized more but you start with product of 
## i * j where both are maxnum, testing for palindrome and keep first 
## decrementing j, and if that fails, start again with i decremented by 1
## brute force of 2 while loops across p & q decrementing q, and then p    
        
    i = j = maxnum
    p = q= maxnum
    
    LPalindrome = 0
    maxi = 1
    
    while (i > maxi): 
        
        while (j > 1):
            
            prod = i*j
#            print(i, j, prod)
            if (IsPalindrome(prod)):
#                print ("largest palindrome is ",prod, i, j)
                if (LPalindrome < prod):
                    LPalindrome = prod
                    maxi = j
                    p = i
                    q = j
                break
            j -= 1
            
        i -= 1
        j = i
         
    if (LPalindrome != 0):
        print ("Largest Palindrome is ", LPalindrome, "and product of ", p, "and ",q) 
    else:
        print("No Palindones found")
    

#%%
def getprimes(lower, higher):
    
    #find all prime numbers between lower and higher numbers
    
    for i in range(lower, higher+1):
        
        for f in range(2, i): # for all f as factor of i - so upper lim is i
            
            if (i % f == 0):
                break
        else:
            #executed if for loop exits without break
            #found a prime as no factors
            print (i, "is a prime number")
            
            