def perfect_number(num):
	su = 0
	for i in range(1, num):
		if num % i == 0:
			su += i
	return su == num

def perfect_number_main(n):
	if perfect_number(n) == True:
		print("%s is perfect" % n)
	else:
		pass

for i in range(1,10000):
	perfect_number_main(i)

# profiling result for (2^n-1((2^n)-1))

# profile: python -m profile perfect_numbers.py

"""
         20022 function calls in 12.496 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        8    0.000    0.000    0.000    0.000 :0(charmap_encode)
        1    0.000    0.000   12.496   12.496 :0(exec)
        4    0.000    0.000    0.000    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        8    0.000    0.000    0.000    0.000 cp857.py:18(encode)
        1    0.047    0.047   12.496   12.496 perfect_numbers.py:1(<module>)
     9999   12.433    0.001   12.433    0.001 perfect_numbers.py:1(perfect_numbe
r)
     9999    0.016    0.000   12.449    0.001 perfect_numbers.py:8(perfect_numbe
r_main)
        1    0.000    0.000   12.496   12.496 profile:0(<code object <module> at
 0x01E0C2A0, file "perfect_numbers.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""