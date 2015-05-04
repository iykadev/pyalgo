import sys

def isPrimeNum(num):
	for i in range(2, num):
		if (num % i) == 0:
			return False
	return True

def prime_numbers(lowNum, highNum):
	sys.stdout.write("Prime Numbers in range (%s,%s): " % (lowNum, highNum))
	for i in range(lowNum, highNum):
		if isPrimeNum(i):
			print(i, end=' ')

def prime_number_main():
	prime_numbers(2,100000)

prime_number_main()

"""
Prime Numbers in range (2,100000): 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89
97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239
241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419
421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601
607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797
99829 99833 99839 99859 99871 99877 99881 99901 99907 99923 99929 99961 99971 99989 99991 [Finished in 148.2s]
"""

# profiling result for 100.000 numbers

# profile: python -m profile prime_numbers.py

"""
          147967 function calls in 141.774 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    19185    0.031    0.000    0.031    0.000 :0(charmap_encode)
        1    0.000    0.000  141.774  141.774 :0(exec)
     9592    0.172    0.000    0.296    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(write)
    19185    0.094    0.000    0.125    0.000 cp857.py:18(encode)
        1    0.000    0.000  141.774  141.774 prime_numbers.py:1(<module>)
        1    0.000    0.000  141.774  141.774 prime_numbers.py:15(prime_number_m
ain)
    99998  141.259    0.001  141.259    0.001 prime_numbers.py:3(isPrimeNum)
        1    0.218    0.218  141.774  141.774 prime_numbers.py:9(prime_numbers)
        1    0.000    0.000  141.774  141.774 profile:0(<code object <module> at
 0x0181B430, file "prime_numbers.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""