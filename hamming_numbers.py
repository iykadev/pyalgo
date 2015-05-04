import sys
sys.setrecursionlimit(10000)

def is_hamming_numbers(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		return is_hamming_numbers(x/2)
	if x % 3 == 0:
		return is_hamming_numbers(x/3)
	if x % 5 == 0:
		return is_hamming_numbers(x/5)
	return 0

def hamming_numbers(x):
	if x == 1:
		return 1
	hamming_numbers(x-1)
	if is_hamming_numbers(x) == True:
		print("%s" % x, end=' ')

def hamming_numbers_main():
	sys.stdout.write("Hamming Numbers: ")
	hamming_numbers(9830)

hamming_numbers_main()

# profiling result for 9830 numbers

# profile: python -m profile hamming_numbers.py

"""
         37722 function calls (10704 primitive calls) in 0.156 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      347    0.000    0.000    0.000    0.000 :0(charmap_encode)
        1    0.000    0.000    0.140    0.140 :0(exec)
      173    0.000    0.000    0.000    0.000 :0(print)
        1    0.016    0.016    0.016    0.016 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(setrecursionlimit)
        1    0.000    0.000    0.000    0.000 :0(write)
      347    0.000    0.000    0.000    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.140    0.140 hamming_numbers.py:1(<module>)
   9830/1    0.062    0.000    0.140    0.140 hamming_numbers.py:15(hamming_numb
ers)
        1    0.000    0.000    0.140    0.140 hamming_numbers.py:22(hamming_numb
ers_main)
27018/9829    0.078    0.000    0.078    0.000 hamming_numbers.py:4(is_hamming_n
umbers)
        1    0.000    0.000    0.156    0.156 profile:0(<code object <module> at
 0x0178C390, file "hamming_numbers.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""