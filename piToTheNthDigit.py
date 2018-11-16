from decimal import Decimal as Dec, getcontext as gc
from math import ceil as ceil

def PI(maxK=70, prec=1008, disp=1007): # parameter defaults chosen to gain 1000+ digits within a few seconds
    gc().prec = prec 
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK+1):
        M = (K**3 -16*K) * M // k**3
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp+1]) # drop few digits of precision for accuracy
    print("PI(maxK=%d iterations, gc().prec=%d, disp=%d digits) =\n%s" % (maxK, prec, disp, pi))
    return pi

repeat = 'y' 
while repeat == 'y':
    digits = int(input("How many digits of pi do you want? "))
    maxK = ceil(digits/14.18)
    disp = digits
    prec = digits + 2
    Pi = PI(maxK, prec, disp)
    repeat = input("Do you want to repeat? y/n: ")