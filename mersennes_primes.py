import sys

def mersennes_primes(i,l):
	for i in range(i,l):
		result = ((2**i)-1)
		print(result)

def mersennes_primes_main():
	mersennes_primes(2,130000)

mersennes_primes_main()

# for out to txt => python mersennes_primes.py > mersennes_primes.txt

# profiling result for (2^11140)-1

# profile: python -m profile mersennes_primes.py

"""
         55696 function calls in 8.767 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    22276    1.654    0.000    1.654    0.000 :0(charmap_encode)
        1    0.000    0.000    8.767    8.767 :0(exec)
    11138    6.412    0.001    8.112    0.001 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
    22276    0.047    0.000    1.700    0.000 cp857.py:18(encode)
        1    0.000    0.000    8.767    8.767 mersennes_primes.py:1(<module>)
        1    0.655    0.655    8.767    8.767 mersennes_primes.py:3(mersennes_pr
imes)
        1    0.000    0.000    8.767    8.767 mersennes_primes.py:8(mersennes_pr
imes_main)
        1    0.000    0.000    8.767    8.767 profile:0(<code object <module> at
 0x01DAB2A0, file "mersennes_primes.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""